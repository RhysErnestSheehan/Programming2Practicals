"""CP1404 Test file for silver service taxi class"""

from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Luxury Taxi", 75, 8)
    taxi.drive(30)
    print(taxi)
    print(taxi.get_fare())


main()