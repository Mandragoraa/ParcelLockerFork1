import pytest
from src.model import (
    Deliver,
    Locker,
    Parcel,
    User,
    CompartmentSize,
)


@pytest.fixture
def user1() -> User:
    return User(parcel_id="P1", locker_id="L12", sender_email="maria.koper@gmail.com",
                receiver_email="magda.gessler@gmail.com", sent_date="2025-01-20", expected_delivery_date="2025-01-22")


@pytest.fixture
def user2() -> User:
    return User(parcel_id="P2", locker_id="L15", sender_email="john.doe@example.com",
                receiver_email="jane.doe@example.com", sent_date="2025-01-21", expected_delivery_date="2025-01-23")


@pytest.fixture
def user3() -> User:
    return User(parcel_id="P3", locker_id="L18", sender_email="anna.smith@example.com",
                receiver_email="mark.jones@example.com", sent_date="2025-01-19", expected_delivery_date="2025-01-24")


@pytest.fixture
def users(user1, user2, user3) -> list[User]:
    return [user1, user2, user3]


@pytest.fixture
def parcel1() -> Parcel:
    return Parcel(parcel_id="K13", height=10, length=2, weight=12)


@pytest.fixture
def parcel2() -> Parcel:
    return Parcel(parcel_id="M24", height=15, length=5, weight=8)


@pytest.fixture
def parcel3() -> Parcel:
    return Parcel(parcel_id="P37", height=8, length=3, weight=20)


@pytest.fixture
def parcels(parcel1, parcel2, parcel3) -> list[Parcel]:
    return [parcel1, parcel2, parcel3]


@pytest.fixture
def locker1() -> Locker:
    return Locker(locker_id="D44", city="Warszawa", latitude=52.2297, longitude=21.0122,
                  compartments=CompartmentSize.SMALL)


@pytest.fixture
def locker2() -> Locker:
    return Locker(locker_id="A12", city="Kraków", latitude=50.0647, longitude=19.9450,
                  compartments=CompartmentSize.MEDIUM)


@pytest.fixture
def locker3() -> Locker:
    return Locker(locker_id="Z99", city="Gdańsk", latitude=54.3520, longitude=18.6466,
                  compartments=CompartmentSize.LARGE)


@pytest.fixture
def lockers(locker1, locker2, locker3) -> list[Locker]:
    return [locker1, locker2, locker3]


@pytest.fixture
def deliver1() -> Deliver:
    return Deliver(
        email="john.doe@example.com",
        name="John",
        surname="Doe",
        city="Warszawa",
        latitude=52.2297,
        longitude=21.0122
    )


@pytest.fixture
def deliver2() -> Deliver:
    return Deliver(
        email="anna.smith@example.com",
        name="Anna",
        surname="Smith",
        city="Kraków",
        latitude=50.0647,
        longitude=19.9450
    )


@pytest.fixture
def deliver3() -> Deliver:
    return Deliver(
        email="maria.kowalska@example.com",
        name="Maria",
        surname="Kowalska",
        city="Gdańsk",
        latitude=54.3520,
        longitude=18.6466
    )


@pytest.fixture
def delivers(deliver1, deliver2, deliver3) -> list[Deliver]:
    return [deliver1, deliver2, deliver3]
