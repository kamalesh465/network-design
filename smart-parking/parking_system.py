# parking_system.py

class ParkingSlot:
    def __init__(self, slot_id, distance):
        self.slot_id = slot_id
        self.distance = distance
        self.is_available = True

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id