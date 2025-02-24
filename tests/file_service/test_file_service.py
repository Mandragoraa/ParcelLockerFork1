import json
import os
import pytest
from src.file_service import (
    DeliverJsonFileReader,
    LockerJsonFileReader,
    ParcelJsonFileReader,
    UserJsonFileReader,
    DeliverJsonFileWriter,
    LockerJsonFileWriter,
    ParcelJsonFileWriter,
    UserJsonFileWriter,
)
from src.model import DeliverDataDict, LockerDataDict, ParcelDataDict, UserDataDict


def test_read_parcels(parcels_file: str, parcels_data: list[ParcelDataDict]) -> None:
    reader = ParcelJsonFileReader()
    parcels = reader.read(parcels_file)
    assert parcels == parcels_data


def test_read_delivers(delivers_file: str, delivers_data: list[DeliverDataDict]) -> None:
    reader = DeliverJsonFileReader()
    delivers = reader.read(delivers_file)
    assert delivers == delivers_data


def test_read_lockers(lockers_file: str, lockers_data: list[LockerDataDict]) -> None:
    reader = LockerJsonFileReader()
    lockers = reader.read(lockers_file)
    assert lockers == lockers_data


def test_read_users(users_file: str, users_data: list[UserDataDict]) -> None:
    reader = UserJsonFileReader()
    users = reader.read(users_file)
    assert users == users_data


def test_write_parcels(tmpdir, parcels_data: list[ParcelDataDict]) -> None:
    writer = ParcelJsonFileWriter()
    file_path = os.path.join(tmpdir, "test_parcels.json")
    writer.write(file_path, parcels_data)

    with open(file_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == parcels_data
