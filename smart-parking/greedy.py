# greedy.py

def allocate_parking_greedy(vehicles, slots):
    """
    Allocates parking slots using the Greedy Algorithm.
    Time Complexity: O(n * m) where n = vehicles, m = slots.
    Space Complexity: O(m).
    """
    allocations = []

    for vehicle in vehicles: # O(n) loop
        best_slot = None
        min_distance = float('inf')

        # Find nearest available slot: O(m) loop
        for slot in slots:
            if slot.is_available and slot.distance < min_distance:
                min_distance = slot.distance
                best_slot = slot
        
        # Local optimal choice made: Assign and mark occupied
        if best_slot:
            best_slot.is_available = False
            allocations.append({
                'Vehicle ID': vehicle.vehicle_id,
                'Assigned Slot': best_slot.slot_id,
                'Distance': best_slot.distance,
                'Status': 'Allocated'
            })
        else:
            allocations.append({
                'Vehicle ID': vehicle.vehicle_id,
                'Assigned Slot': 'N/A',
                'Distance': 'N/A',
                'Status': 'Parking Full'
            })
            
    return allocations