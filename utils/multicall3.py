from contextlib import suppress
from dataclasses import dataclass
from typing import Any

from eth_abi.abi import decode
from web3 import AsyncWeb3
from web3.contract.async_contract import AsyncContractFunction

from config import MULTICALL3_ABI


@dataclass
class Call:
    fn: AsyncContractFunction
    allow_failure: bool


class Multicall3:
    def __init__(self, w3: AsyncWeb3, multicall_address: str):
        self.w3 = w3
        self.address = multicall_address
        self.contract = self.w3.eth.contract(
            address=self.address,
            abi=MULTICALL3_ABI,
        )

    async def aggregate3(self, *calls: AsyncContractFunction | Call):
        aggregated_calls: list[tuple[str, bool, Any]] = []
        outputs_types: list[list[Any]] = []
        for call in calls:
            if isinstance(call, AsyncContractFunction):
                aggregated_calls.append(
                    (
                        call.address,
                        True,  # allow failure by default
                        call._encode_transaction_data(),  # pyright: ignore[reportPrivateUsage]
                    )
                )
                output_types: list[str] = []
                for output in call.abi["outputs"]:
                    output_types.append(output["type"])
                outputs_types.append(output_types)

            if isinstance(call, Call):
                aggregated_calls.append(
                    (
                        call.fn.address,
                        call.allow_failure,
                        call.fn._encode_transaction_data(),  # pyright: ignore[reportPrivateUsage]
                    )
                )
                output_types: list[str] = []
                for output in call.fn.abi["outputs"]:
                    output_types.append(output["type"])
                outputs_types.append(output_types)

        outputs = await self.contract.functions.aggregate3(
            calls=aggregated_calls
        ).call()

        results: list[None | Any] = []
        for i, result in enumerate(outputs):
            output_types = outputs_types[i]
            success = result[0]
            if not success:
                results.append(None)
                continue
            call_output = result[1]
            decoded = None
            with suppress(Exception):
                decoded = decode(output_types, call_output)
                if len(decoded) == 1:
                    decoded = decoded[0]
            results.append(decoded)

        return results