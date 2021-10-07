"""Guitar Class tests"""

from Prac_06.Guitar import Guitar

CURRENT_YEAR = 2021


def main():
    name = "Fender Stratocaster"
    year = 1965
    cost = 22000

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2013, 2500.99)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 56, guitar.get_age()))

    print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 8, other_guitar.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))

    print("{} is_vintage() - Expected {}. Got {}".format(other_guitar.name, False, other_guitar.is_vintage()))


main()
