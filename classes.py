from typing import Union
# Student ID: W22063136
# Charles Laverick

class Bike():
    # Frame, fork, pedals, chains, gears, wheels, brakes, lights, seat, colour
    # Default Bike: Normal frame and forks with 2 pedals, fornt and rear brakes, 1 seat, two wheel, normal chain and gears, normal lights with front only
    def __init__(self, colour: str, pedals: str, brakes: str, lights: str, seat: str, gear: str, chain: str, wheel: str):
        self.set_bike_type("Standard")
        self.set_frame("Tubular Steel")
        self.set_fork("Tubular Steel")
        self.set_gears(gear)
        self.set_chain(chain)
        self.set_wheels(wheel)
        self.set_colour(colour)
        self.set_pedals(pedals)
        self.set_brakes(brakes)
        self.set_lights(lights)
        self.set_seat(seat)

        self.set_frame_count(1)
        self.set_fork_count(1)
        self.set_pedal_count(2)
        self.set_gear_count(1)
        self.set_chain_count(1)
        self.set_wheel_count(2)
        self.set_brake_count(2)
        self.set_light_count(2)
        self.set_seat_count(1)

    def set_frame_count(self, count: int) -> None:
        self.__frame_count = count

    def get_frame_count(self) -> str:
        return self.__frame_count

    def set_fork_count(self, count: int) -> None:
        self.__fork_count = count

    def get_fork_count(self) -> str:
        return self.__fork_count
    
    def set_pedal_count(self, count: int) -> None:
        self.__pedal_count = count

    def get_pedal_count(self) -> str:
        return self.__pedal_count
    
    def set_gear_count(self, count: int) -> None:
        self.__gear_count = count

    def get_gear_count(self) -> str:
        return self.__gear_count
    
    def set_chain_count(self, count: int) -> None:
        self.__chain_count = count

    def get_chain_count(self) -> str:
        return self.__chain_count
    
    def set_wheel_count(self, count: int) -> None:
        self.__wheel_count = count

    def get_wheel_count(self) -> str:
        return self.__wheel_count
    
    def set_brake_count(self, count: int) -> None:
        self.__brake_count = count

    def get_brake_count(self) -> str:
        return self.__brake_count
    
    def set_light_count(self, count: int) -> None:
        self.__light_count = count

    def get_light_count(self) -> str:
        return self.__light_count
    
    def set_seat_count(self, count: int) -> None:
        self.__seat_count = count

    def get_seat_count(self) -> str:
        return self.__seat_count

    def set_bike_type(self, type: str) -> None:
        self.__bike_type = type

    def get_bike_type(self) -> str:
        return self.__bike_type
    
    def set_frame(self, frame: str) -> None:
        self.__frame = frame

    def get_frame(self) -> str:
        return self.__frame

    def set_fork(self, fork: str) -> None:
        self.__fork = fork
    
    def get_fork(self) -> str:
        return self.__fork
    
    def set_gears(self, gears: str) -> None:
        self._gears = gears

    def get_gears(self) -> str:
        return self._gears
    
    def set_chain(self, chain: str) -> None:
        self._chain = chain

    def get_chain(self) -> str:
        return self._chain
    
    def set_wheels(self, wheels: str) -> None:
        self._wheels = wheels

    def get_wheels(self) -> str:
        return self._wheels
    
    def set_colour(self, colour: str) -> None:
        self._colour = colour

    def get_colour(self) -> str:
        return self._colour
    
    def set_pedals(self, pedals: str) -> None:
        self._pedals = pedals

    def get_pedals(self) -> str:
        return self._pedals
    
    def set_brakes(self, brakes: str) -> None:
        self._brakes = brakes

    def get_brakes(self) -> str:
        return self._brakes
    
    def set_lights(self, lights: str) -> None:
        self._lights = lights

    def get_lights(self) -> str:
        return self._lights
    
    def set_seat(self, seats: str) -> None:
        self._seats = seats

    def get_seat(self) -> str:
        return self._seats

    def __repr__(self):
        return f"Bike Type: {self.get_bike_type()}\nGears: {self.get_gears()}\nChain: {self.get_chain()}\nWheels: {self.get_wheels()}\nColour: {self.get_colour()}\nPedals: {self.get_pedals()}\nBrakes {self.get_brakes()}\nLights:{self.get_lights()}\nSeat: {self.get_seat()}"

class MountainBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.set_bike_type("Mountain Bike")
        self.set_frame_count(2)
        self.set_fork_count(2)

class RoadBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.set_bike_type("Road Bike")
        self.set_frame("Tubular Aluminium")
        self.set_fork("Tubular Aluminium")

class TrackBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.set_bike_type("Track Bike")
        self.set_frame("Carbon Fibre")
        self.set_fork("Carbon Fibre")
        self.set_brake_count(0)
        self.set_light_count(0)

class BMXBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.set_bike_type("BMX")
        self.set_brake_count(1)
        self.set_light_count(0)

class KidsBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.set_bike_type("Kids")
        self.set_frame_count(0.5)
        self.set_fork_count(0.5)


class Address():
    def __init__(self, address_line_1: str, address_line_2: str, city: str, postcode: str):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.postcode = postcode

    def __repr__(self):
        return f"Address Line 1: {self.address_line_1}\nAddress Line 2: {self.address_line_2}\nCity: {self.city}\nPostcode: {self.postcode}"

class Customer():
    __id = 0

    def __init__(self, name: str, email: str, phone_number: int, address: Address):
        self.set_id()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def set_id(self) -> None:
        Customer.__id += 1
        self.__id = Customer.__id

    def get_id(self) -> int:
        return self.__id

    def __repr__(self):
        return f"Customer: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\n{self.address}"

class Order():
    __id = 0

    def __init__(self, customer: Customer, bike: Union[Bike, MountainBike, RoadBike, TrackBike, BMXBike, KidsBike]):
        self.set_id()
        self.set_customer(customer)
        self.set_bike_order(bike)
    
    def set_customer(self, customer: Customer)-> None:
        self._customer = customer

    def get_customer(self) -> Customer:
        return self._customer
    
    def set_bike_order(self, bike_order: Union[Bike, MountainBike, RoadBike, TrackBike, BMXBike, KidsBike]) -> None:
        self._bike_order = bike_order

    def get_bike_order(self) -> Union[Bike, MountainBike, RoadBike, TrackBike, BMXBike, KidsBike]:
        return self._bike_order

    def set_id(self) -> None:
        Order.__id += 1
        self.__id = Order.__id

    def get_id(self) -> int:
        return self.__id

    def __repr__(self):
        return  f"Order Id: {self.get_id()}\nCustomer: {self.get_customer()}\nOrder: {self.get_bike_order()}"
