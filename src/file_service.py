import json
from abc import ABC, abstractmethod
from src.model import ParcelDataDict, UserDataDict, LockerDataDict, DeliverDataDict
from typing import override
import json


class FileReader[T](ABC):
    def read(self, filename: str) -> list[T]:
        with open(filename, 'r', encoding='utf8') as file:
            return json.load(file)


class UserJsonFileReader(FileReader[UserDataDict]):
    pass


class ParcelJsonFileReader(FileReader[ParcelDataDict]):
    pass


class LockerJsonFileReader(FileReader[LockerDataDict]):
    pass


class DeliverJsonFileReader(FileReader[DeliverDataDict]):
    pass


class FileWriter[T]:
    def write(self, filename: str, data: list[T]) -> None:
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class UserJsonFileWriter(FileWriter[UserDataDict]):
    pass


class ParcelJsonFileWriter(FileWriter[ParcelDataDict]):
    pass


class LockerJsonFileWriter(FileWriter[LockerDataDict]):
    pass


class DeliverJsonFileWriter(FileWriter[DeliverDataDict]):
    pass
