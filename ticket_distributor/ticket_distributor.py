from typing import Iterable
from Crypto.Hash import keccak


class TicketDistributor:
    def __init__(self, min_ticket: int, max_ticket: int, parameter: str):
        self.min_ticket = min_ticket
        self.max_ticket = max_ticket
        self.parameter = parameter

    def distribute(self, students: Iterable[str]) -> list[int]:
        return [self.distribute_ticket(student) for student in students]

    def distribute_ticket(self, student: str) -> int:
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update((student + self.parameter).encode())
        hash_value = int.from_bytes(keccak_hash.digest(), byteorder='big')
        return self._int_to_ticket(hash_value)

    def _int_to_ticket(self, ticket: int) -> int:
        return ticket % (self.max_ticket - self.min_ticket + 1) + self.min_ticket
