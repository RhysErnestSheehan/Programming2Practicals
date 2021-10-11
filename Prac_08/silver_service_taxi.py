"""Silver Service Taxi Class"""

from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}"

    def get_fare(self):
        return self.flagfall
