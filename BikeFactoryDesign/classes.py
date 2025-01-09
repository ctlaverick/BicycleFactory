from typing import Union

class Bike():
    # Frame, fork, pedals, chains, gears, wheels, brakes, lights, seat, colour
    # Default Bike: Normal frame and forks with 2 pedals, fornt and rear brakes, 1 seat, two wheel, normal chain and gears, normal lights with front only
    def __init__(self, colour: str, pedals: str, brakes: str, lights: str, seat: str, gear: str, chain: str, wheel: str):
        self.bike_type = "Standard"
        self.frame = "Tubular Steel"
        self.fork = "Tubular Steel"
        self.gears = gear
        self.chain = chain
        self.wheels = wheel
        self.colour = colour
        self.pedals = pedals
        self.brakes = brakes
        self.lights = lights
        self.seat = seat

        self.frame_count = 1
        self.fork_count = 1
        self.pedal_count = 2
        self.gear_count = 1
        self.chain_count = 1
        self.wheel_count = 2
        self.brake_count = 2
        self.light_count = 2
        self.seat_count = 1


class MountainBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.bike_type = "Mountain Bike"
        self.frame_count = 2
        self.fork_count = 2

class RoadBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.bike_type = "Road Bike"
        self.frame = "Tubular Aluminium"
        self.fork = "Tubular Aluminium"

class TrackBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.bike_type = "Track Bike"
        self.frame = "Carbon Fibre"
        self.fork = "Carbon Fibre"
        self.brake_count = 0
        self.light_count = 0

class BMXBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.bike_type = "BMX"
        self.brake_count = 1
        self.light_count = 0

class KidsBike(Bike):
    def __init__(self, colour, pedals, brakes, lights, seat, gear, chain, wheel):
        super().__init__(colour, pedals, brakes, lights, seat, gear, chain, wheel)
        self.bike_type = "Kids"
        self.frame_count = 0.5
        self.fork_count = 0.5


class Address():
    def __init__(self, address_line_1: str, address_line_2: str, city: str, postcode: str):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.postcode = postcode

    def __repr__(self):
        return f"Address Line 1: {self.address_line_1}\nAddress Line 2: {self.address_line_2}\nCity: {self.city}\nPostcode: {self.postcode}"

class Customer():
    id = 0
    def __init__(self, name: str, email: str, phone_number: int, address: Address):
        Customer.id += 1
        self.id = Customer.id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"Customer: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\n{self.address}"

class Order():
    id = 0

    def __init__(self, customer: Customer, bike: Union[Bike, MountainBike, RoadBike, TrackBike, BMXBike, KidsBike]):
        Order.id += 1
        self.id = Order.id
        self.customer = customer
        self.bike_order = bike

    def __repr__(self):
        return  f"Order Id: {self.id}\nCustomer: {self.customer}\nOrder: {self.bike_order}"
