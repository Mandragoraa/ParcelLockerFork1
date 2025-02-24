from abc import abstractmethod, ABC
from src.model import ParcelDataDict, UserDataDict, LockerDataDict, DeliverDataDict
import re
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Type, override
from email_validator import validate_email, EmailNotValidError
import logging
from datetime import datetime
# from geopy.geocoders import Nominatim

logging.basicConfig(level=logging.INFO)


class Validator[T](ABC):

    @abstractmethod
    def validate(self, data: T) -> bool:
        pass

    @staticmethod
    def is_positive(data: int) -> bool:
        return data > 0

    @staticmethod
    def are_positive(items: dict[str, int | str]) -> bool:
        return all(value > 0 for value in items.values())
    @staticmethod
    def is_valid_value_of(value: str, enum_class: Type[Enum]) -> bool:
        return value in [item.value for item in enum_class]

    @staticmethod
    def is_valid_email(email: str) -> bool:
        try:
            validate_email(email, check_deliverability=True)
            return True
        except EmailNotValidError as e:
            logging.error(str(e))
            return False

    @staticmethod
    def validate_int_in_range(value: int, min_value: int, max_value: int) -> bool:
        return min_value <= value <= max_value

    @staticmethod
    def validate_if_date_comes_after_date(date1_str: str, date2_str: str) -> bool:
        datetime_format = "%Y-%m-%d"
        try:
            datetime1 = datetime.strptime(date1_str, datetime_format)
            datetime2 = datetime.strptime(date2_str, datetime_format)
            return datetime1 < datetime2
        except ValueError:
            return False

    # TODO TA METODA NIE DZIAŁA
    # @staticmethod
    # def is_valid_city(city: str, latitude: float, longitude: float) -> bool:
    #     try:
    #         geolocator = Nominatim(user_agent="parcel_locker_project_2")
    #         location = geolocator.reverse(f'{latitude},{longitude}')
    #         if location and 'address' in location.raw:
    #             address = location.raw['address']
    #             return address.get("city") == city or address.get("town") == city or address.get("village") == city
    #         return False
    #     except Exception as e:
    #         logging.error(str(e))
    #         return False


class ParcelDataDictValidator(Validator[ParcelDataDict]):

    @override
    def validate(self, data: ParcelDataDict) -> bool:
        return Validator.is_positive(data['height']) and Validator.is_positive(data['length']) and Validator.is_positive(data['weight'])


class UserDataDictValidator(Validator[UserDataDict]):

    @override
    def validate(self, data: UserDataDict) -> bool:
        return Validator.is_valid_email(data['receiver_email']) and Validator.is_valid_email(data['sender_email']) and Validator.validate_if_date_comes_after_date(data['sent_date'], data['delivery_date'])



class LockerDataDictValidator(Validator[LockerDataDict]):

    @override
    def validate(self, data: LockerDataDict) -> bool:
        return Validator.are_positive(data['compartments'])


class DeliverDataDictValidator(Validator[DeliverDataDict]):

    @override
    def validate(self, data: DeliverDataDict) -> bool:
        return Validator.is_valid_email(data['email'])
