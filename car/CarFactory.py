from datetime import date
from Car import Car
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import Battery, SpindlerBattery, NubbinBattery


from battery.Battery import Battery


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
    