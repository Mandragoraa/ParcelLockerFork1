import pytest
from typing import Type
from decimal import Decimal
from enum import Enum
from email_validator import EmailNotValidError
from src.validator import Validator, ParcelDataDictValidator, UserDataDictValidator, LockerDataDictValidator, \
    DeliverDataDictValidator
from src.model import CompartmentSize, UserDataDict, ParcelDataDict, DeliverDataDict, LockerDataDict


@pytest.mark.parametrize("value, expected", [
    (6, True),
    (-10, False),
])
def test_is_positive(value: int, expected: bool) -> None:
    assert Validator.is_positive(value) is expected


@pytest.mark.parametrize("value, enum_class, expected", [
    ('SMALL', CompartmentSize, False),
    ('small', CompartmentSize, True),
    ('eee', CompartmentSize, False),
    ('EEE', CompartmentSize, False),
])
def test_is_valid_value_of(value: str, enum_class: Type[Enum], expected: bool) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected


@pytest.mark.parametrize("email, expected", [
    ("test@gmail.com", True),
    ("user@gmail", False),
    ("user@.com", False),
    ("@gmail.com", False),
    ("user@gmail..com", False),
    ("user@domain.com.", False),

])
def test_is_valid_email(email: str, expected: bool) -> None:
    assert Validator.is_valid_email(email) == expected


@pytest.mark.parametrize("value, min_value, max_value, expected", [
    (10, 5, 15, True),
    (10, 20, 30, False),
    (10, 3, 9, False),

])
def test_validate_int_in_range(value: int, min_value: int, max_value: int, expected: bool) -> None:
    assert Validator.validate_int_in_range(value, min_value, max_value) == expected


@pytest.mark.parametrize("date1_str, date2_str, expected", [
    # Poprawne przypadki
    ("2025-02-10", "2025-02-09", False),  # date1 PO date2 -> False
    ("2025-02-10", "2025-02-10", False),  # daty identyczne -> False
    ("2025-02-09", "2025-02-10", True),  # date1 PRZED date2 -> True
    ("2024-12-31", "2025-01-01", True),  # koniec roku przed nowym rokiem -> True
    ("2023-06-15", "2025-01-01", True),  # duża różnica w latach -> True
    ("2024-02-28", "2024-02-29", True),  # rok przestępny -> True
    ("2024-02-29", "2024-03-01", True),  # 29 lutego przed marcem -> True
    ("2024-11-30", "2024-12-01", True),  # jeden dzień różnicy -> True
    ("2023-12-31", "2024-01-01", True),  # zmiana roku -> True
    ("2023-01-01", "2023-12-31", True),  # cały rok różnicy -> True

    # Błędne daty (oczekiwane False)
    ("2024-13-01", "2024-12-01", False),  # nieistniejący miesiąc
    ("2025-02-30", "2025-03-01", False),  # luty nie ma 30 dni
    ("invalid-date", "2024-12-01", False),  # całkiem błędna data
    ("2024-12-01", "invalid-date", False),  # druga data błędna
])
def test_validate_if_date_comes_after_date(date1_str: str, date2_str: str, expected: bool) -> None:
    assert Validator.validate_if_date_comes_after_date(date1_str, date2_str) == expected


@pytest.mark.parametrize("items, expected", [
    ({"a": 1, "b": 2, "c": 3}, True),  # Wszystkie wartości są dodatnie
    ({"x": -1, "y": 5, "z": 10}, False),  # Jedna wartość jest ujemna
    ({}, True),  # Pusty słownik powinien zwrócić True (brak wartości do sprawdzania)
    ({"m": 0, "n": 2, "o": 5}, False),  # Zero nie jest dodatnie
])
def test_are_positive(items: dict[str, int], expected: bool) -> None:
    assert Validator.are_positive(items) == expected


#
# @pytest.mark.parametrize("city, latitude, longitude, expected", [
#     ("New York", 40.7128, -74.0060, True),  # Poprawne dane dla Nowego Jorku
#     ("Los Angeles", 34.0522, -118.2437, True),  # Poprawne dane dla Los Angeles
#     ("Warsaw", 52.2298, 21.0122, True),  # Poprawne dane dla Warszawy
#     ("London", 51.5074, -0.1278, True),  # Poprawne dane dla Londynu
#     ("Fake City", 100.0000, 200.0000, False),  # Nieistniejące współrzędne
#     ("", 52.2298, 21.0122, False),  # Pusta nazwa miasta
#     ("Berlin", 91.0000, 21.0122, False),  # Szerokość geograficzna poza zakresem (-90,90)
#     ("Tokyo", 35.6895, -181.0000, False),
# ])
# def test_is_valid_city(city: str, latitude: float, longitude: float, expected: bool) -> None:
#     assert Validator.is_valid_city(city, latitude, longitude) == expected

@pytest.mark.parametrize("data, expected", [
    ({"height": 10, "weight": 10, "length": 10}, True),  # Wszystkie wartości dodatnie
    ({"height": 1, "weight": 1, "length": 1}, True),  # Minimalne poprawne wartości
    ({"height": 1000, "weight": 500, "length": 2000}, True),  # Duże wartości
    ({"height": -10, "weight": 10, "length": 10}, False),  # Ujemna wysokość
    ({"height": 10, "weight": -10, "length": 10}, False),  # Ujemna waga
    ({"height": 10, "weight": 10, "length": -10}, False),  # Ujemna długość
    ({"height": 0, "weight": 10, "length": 10}, False),  # Zero jako wysokość (nie jest dodatnie)
    ({"height": 10, "weight": 0, "length": 10}, False),  # Zero jako waga
    ({"height": 10, "weight": 10, "length": 0}, False),  # Zero jako długość
])
def test_parcel_data_dict_validator(data: ParcelDataDict, expected: bool) -> None:
    validator = ParcelDataDictValidator()
    assert validator.validate(data) == expected


@pytest.mark.parametrize("data, expected", [
    # Poprawne dane: poprawne e-maile i poprawna kolejność dat
    ({"receiver_email": "kasia@gmail.com", "sender_email": "sender@gmail.com", "sent_date": "2025-02-10",
      "delivery_date": "2025-02-12"}, True),
    # Niepoprawny e-mail odbiorcy
    ({"receiver_email": "invalid-email", "sender_email": "asia@example.com", "sent_date": "2025-02-10",
      "delivery_date": "2025-02-12"}, False),
    # Niepoprawny e-mail nadawcy
    ({"receiver_email": "jasia@example.com", "sender_email": "invalid-email", "sent_date": "2025-02-10",
      "delivery_date": "2025-02-12"}, False),
    ({"receiver_email": "aasdasft@gmail.com", "sender_email": "sender@gmail.com", "sent_date": "2025-02-10", "delivery_date": "2025-02-10"}, False),

])
def test_user_data_dict_validator(data: UserDataDict, expected: bool) -> None:
    validator = UserDataDictValidator()
    assert validator.validate(data) == expected
