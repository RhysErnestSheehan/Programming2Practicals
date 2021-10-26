"""CP1404 Unreliable Car Test"""

from Prac_08.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Good car", 65, 100)
    bad_car = UnreliableCar("Bad car", 5, 64)

    for i in range(1, 5):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))


main()