from abc import ABC, abstractmethod


class Battery:
    def __init__(self, capacity_kwh: float):
        self.capacity_kwh = capacity_kwh
        self.charge_level = capacity_kwh

    def charge(self, amount: float):
        self.charge_level = min(self.capacity_kwh, self.charge_level + amount)


class FuelTank:
    def __init__(self, capacity_liters: float):
        self.capacity_liters = capacity_liters
        self.fuel_level = capacity_liters

    def refuel(self, amount: float):
        self.fuel_level = min(self.capacity_liters, self.fuel_level + amount)


class Car(ABC):
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def range(self):
        pass


class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int, battery_capacity: float):
        super().__init__(brand, model, year)
        self.battery = Battery(battery_capacity)

    def range(self):
        return self.battery.charge_level

    def charge(self, amount: float):
        self.battery.charge(amount)


class PetrolCar(Car):
    def __init__(self, brand: str, model: str, year: int, tank_capacity: float):
        super().__init__(brand, model, year)
        self.fuel_tank = FuelTank(tank_capacity)

    def range(self):
        return self.fuel_tank.fuel_level

    def refuel(self, amount: float):
        self.fuel_tank.refuel(amount)


if __name__ == "__main__":
    ev = ElectricCar("Tesla", "Model 3", 2023, 75.0)
    car = PetrolCar("Toyota", "Corolla", 2022, 50.0)

    print(f"{ev.brand} {ev.model} - aktualny stan: {ev.range()} kWh")
    ev.charge(10.0)
    print(f"Po próbie ładowania: {ev.range()} kWh")

    print(f"{car.brand} {car.model} - aktualny stan: {car.range()} litrów")
    car.refuel(15.0)
    print(f"Po tankowaniu: {car.range()} litrów")
