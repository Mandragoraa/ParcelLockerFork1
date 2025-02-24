import pytest
from src.model import (
    Deliver,
    Locker,
    Parcel,
    User,
    CompartmentSize,
)


def test_parcel_to_dict(parcel1: Parcel):
    data = parcel1.to_dict()
    expected_data = {
        "parcel_id": "K13",
        "height": 10,
        "length": 2,
        "weight": 12
    }
    assert data == expected_data


def test_user_to_dict(user1: User):
    data = user1.to_dict()
    expected_data = {
        "parcel_id": "P1",
        "locker_id": "L12",
        "sender_email": "maria.koper@gmail.com",
        "receiver_email": "magda.gessler@gmail.com",
        "sent_date": "2025-01-20",
        "expected_delivery_date": "2025-01-22"
    }
    assert data == expected_data


def test_locker_to_dict(locker1: Locker):
    data = locker1.to_dict()
    expected_data = {
        "locker_id": "D44",
        "city": "Warszawa",
        "latitude": 52.2297,
        "longitude": 21.0122,
        "compartments": "small"
    }
    assert data == expected_data


def test_deliver_to_dict(deliver1: Deliver):
    data = deliver1.to_dict()
    expected_data = {
        "email": "john.doe@example.com",
        "name": "John",
        "surname": "Doe",
        "city": "Warszawa",
        "latitude": 52.2297,
        "longitude": 21.0122
    }
    assert data == expected_data
