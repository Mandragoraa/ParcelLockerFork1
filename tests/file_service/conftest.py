from src.model import UserDataDict, ParcelDataDict, LockerDataDict, DeliverDataDict
import pytest
import os
import json


@pytest.fixture
def parcels_data() -> list[ParcelDataDict]:
    return [
        {"parcel_id": "P50", "height": 100, "weight": 120, "length": 200},
        {"parcel_id": "P50", "height": 100, "weight": 120, "length": 200}
    ]


@pytest.fixture
def delivers_data() -> list[DeliverDataDict]:
    return [
        {
            "email": "lena.adamowicz@gmail.com",
            "name": "Lena",
            "surname": "Adamowicz",
            "city": "San Francisco",
            "latitude": 40.71,
            "longitude": -73.96
        },
        {
            "email": "oliver.brown@example.com",
            "name": "Oliver",
            "surname": "Brown",
            "city": "Berlin",
            "latitude": 52.52,
            "longitude": 13.405
        }
    ]

@pytest.fixture()
def users_data() -> list[UserDataDict]:
    return [
        {
            "parcel_id": "P4",
            "locker_id": "L20",
            "sender_email": "emily.clark@example.com",
            "receiver_email": "jack.davis@example.com",
            "sent_date": "2025-01-22",
            "expected_delivery_date": "2025-01-25"
        },
        {
            "parcel_id": "P5",
            "locker_id": "L25",
            "sender_email": "lucas.miller@example.com",
            "receiver_email": "sophie.wilson@example.com",
            "sent_date": "2025-01-23",
            "expected_delivery_date": "2025-01-27"
        }
    ]


@pytest.fixture
def lockers_data() -> list[LockerDataDict]:
    return [
        {
            "locker_id": "B12",
            "city": "Łódź",
            "latitude": 51.7592,
            "longitude": 19.4560,
            "compartments": "medium"
        },
        {
            "locker_id": "C34",
            "city": "Wrocław",
            "latitude": 51.1079,
            "longitude": 17.0385,
            "compartments": "large"
        }
    ]



@pytest.fixture
def parcels_file(tmpdir, parcels_data: list[ParcelDataDict]) -> str:
    file_path = os.path.join(tmpdir, "test_parcels.json")
    with open(file_path, "w") as file:
        json.dump(parcels_data, file)
    return file_path

@pytest.fixture
def delivers_file(tmpdir, delivers_data: list[DeliverDataDict]) -> str:
    file_path = os.path.join(tmpdir, "test_delivers.json")
    with open(file_path, "w") as file:
        json.dump(delivers_data, file)
    return file_path

@pytest.fixture
def lockers_file(tmpdir, lockers_data: list[LockerDataDict]) -> str:
    file_path = os.path.join(tmpdir, "test_lockers.json")
    with open(file_path, "w") as file:
        json.dump(lockers_data, file)
    return file_path

@pytest.fixture
def users_file(tmpdir, users_data: list[UserDataDict]) -> str:
    file_path = os.path.join(tmpdir, "test_users.json")
    with open(file_path, "w") as file:
        json.dump(users_data, file)
    return file_path
