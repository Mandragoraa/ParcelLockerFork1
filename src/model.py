from enum import Enum
from dataclasses import dataclass
from decimal import Decimal

ParcelDataDict = dict[str, str | int]
UserDataDict = dict[str, str]
LockerDataDict = dict[str, str | float | Enum]
DeliverDataDict = dict[str, str | float]


class CompartmentSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


@dataclass(frozen=True)
class Parcel:
    parcel_id: str
    height: int
    length: int
    weight: int

    def to_dict(self) -> ParcelDataDict:
        return {
            "parcel_id": self.parcel_id,
            "height": self.height,
            "length": self.length,
            "weight": self.weight,
        }


@dataclass(frozen=True)
class User:
    parcel_id: str
    locker_id: str
    sender_email: str
    receiver_email: str
    sent_date: str
    expected_delivery_date: str

    #Add str do datime converter function

    def to_dict(self) -> UserDataDict:
        return {
            "parcel_id": self.parcel_id,
            "locker_id": self.locker_id,
            "sender_email": self.sender_email,
            "receiver_email": self.receiver_email,
            "sent_date": self.sent_date,
            "expected_delivery_date": self.expected_delivery_date,
        }


@dataclass(frozen=True)
class Locker:
    locker_id: str
    city: str
    latitude: float
    longitude: float
    compartments: CompartmentSize

    def to_dict(self) -> LockerDataDict:
        return {
            "locker_id": self.locker_id,
            "city": self.city,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "compartments": self.compartments.value,
        }


@dataclass(frozen=True)
class Deliver:
    email: str
    name: str
    surname: str
    city: str
    latitude: float
    longitude: float

    def to_dict(self) -> DeliverDataDict:
        return {
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "city": self.city,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
