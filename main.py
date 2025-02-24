from src.file_service import (
    UserJsonFileReader,
    ParcelJsonFileReader,
    LockerJsonFileReader,
    DeliverJsonFileReader,
    UserJsonFileWriter,
    ParcelJsonFileWriter,
    LockerJsonFileWriter,
    DeliverJsonFileWriter,
)
from src.validator import Validator
from src.model import CompartmentSize
from enum import Enum


def main() -> None:
    # print(Validator.is_valid_city("Warsaw", 52.2297, 21.0122))
    # print(Validator.is_valid_city("Berlin", 52.2297, 21.0122))
    print(Validator.validate_if_date_comes_after_date("2025-02-09", "2025-02-08"))
    print(Validator.validate_if_date_comes_after_date("2025-02-07", "2025-02-08"))
    print(Validator.validate_int_in_range(4, 2, 5))
    print(Validator.validate_int_in_range(44, 2, 5))
    # print(Validator.is_valid_email("kaja.rabka@gmail.com"))
    # print(Validator.is_valid_email("kaja.rabka@gmail..com"))
    # print(Validator.is_positive(12))
    # print(Validator.is_valid_value_of("small", CompartmentSize))
    # print(Validator.is_valid_value_of("SMALL", CompartmentSize))
    # parcels = [
    #     {"parcel_id": "P50", "height": 100, "weight": 120, "length": 200},
    #     {"parcel_id": "P51", "height": 80, "weight": 90, "length": 150}
    # ]
    #
    # parcel_json_file_writer = ParcelJsonFileWriter()
    # parcel_json_file_writer.write('temp_parcels.json', parcels)
    #
    # delivers = [
    #     {
    #         "email": "lena.adamowicz@gmail.com",
    #         "name": "Lena",
    #         "surname": "Adamowicz",
    #         "city": "San Francisco",
    #         "latitude": 40.71,
    #         "longitude": -73.96
    #     },
    #     {
    #         "email": "oliver.brown@example.com",
    #         "name": "Oliver",
    #         "surname": "Brown",
    #         "city": "Berlin",
    #         "latitude": 52.52,
    #         "longitude": 13.405
    #     }
    # ]
    # deliver_json_file_writer = DeliverJsonFileWriter()
    # deliver_json_file_writer.write('temp_delivers.json', delivers)
    #
    # users = [
    #     {
    #         "parcel_id": "P4",
    #         "locker_id": "L20",
    #         "sender_email": "emily.clark@example.com",
    #         "receiver_email": "jack.davis@example.com",
    #         "sent_date": "2025-01-22",
    #         "expected_delivery_date": "2025-01-25"
    #     },
    #     {
    #         "parcel_id": "P5",
    #         "locker_id": "L25",
    #         "sender_email": "lucas.miller@example.com",
    #         "receiver_email": "sophie.wilson@example.com",
    #         "sent_date": "2025-01-23",
    #         "expected_delivery_date": "2025-01-27"
    #     }
    # ]
    # user_json_file_writer = UserJsonFileWriter()
    # user_json_file_writer.write('temp_users.json', users)
    #
    # lockers = [
    #     {
    #         "locker_id": "B12",
    #         "city": "Łódź",
    #         "latitude": 51.7592,
    #         "longitude": 19.4560,
    #         "compartments": "medium"
    #     },
    #     {
    #         "locker_id": "C34",
    #         "city": "Wrocław",
    #         "latitude": 51.1079,
    #         "longitude": 17.0385,
    #         "compartments": "large"
    #     }
    # ]
    # locker_json_file_writer = LockerJsonFileWriter()
    # locker_json_file_writer.write('temp_lockers.json', lockers)


# user_json_file_reader = UserJsonFileReader()
# users = (user_json_file_reader.read('./data/users.json'))
# for user in users:
#     print(user)
#
# parcel_json_file_reader = ParcelJsonFileReader()
# parcels = (parcel_json_file_reader.read('./data/parcels.json'))
# for parcel in parcels:
#     print(parcel)
#
# #   todo czy któreś z tych file readerów nazwać repository?
# locker_json_file_reader = LockerJsonFileReader()
# lockers = (locker_json_file_reader.read('./data/lockers.json'))
# for locker in lockers:
#     print(locker)
#
# deliver_json_file_reader = DeliverJsonFileReader()
# delivers = (deliver_json_file_reader.read('./data/delivers.json'))
# for deliver in delivers:
#     print(deliver)


if __name__ == '__main__':
    main()
