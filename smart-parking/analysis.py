# analysis.py
import time
from parking_system import ParkingSlot, Vehicle
from greedy import allocate_parking_greedy

def run_performance_test(num_vehicles, num_slots):
    """Validates real-world applicability through stress testing."""
    import random
    vehicles = [Vehicle(f"V{i}") for i in range(1, num_vehicles + 1)]
    slots = [ParkingSlot(f"S{i}", random.randint(5, 100)) for i in range(1, num_slots + 1)]
    
    start_time = time.perf_counter()
    allocate_parking_greedy(vehicles, slots)
    end_time = time.perf_counter()
    
    exec_time = (end_time - start_time) * 1000
    print(f"Test: {num_vehicles} Vehicles, {num_slots} Slots | Exec Time: {exec_time:.4f} ms")

def print_academic_justification():
    print("\n--- COMPLEXITY ANALYSIS & PARADIGM JUSTIFICATION ---")
    print("1. Greedy Algorithm (Implemented):")
    print("   - Time Complexity: O(n * m)")
    print("   - Space Complexity: O(m)")
    print("   - Justification: Fast, real-time assignment making immediate local optimal choices.")
    print("\n2. Graph Matching (Hungarian Method - Theoretical):")
    print("   - Time Complexity: O(n^3)")
    print("   - Space Complexity: O(n^2)")
    print("   - Justification: Evaluates all combinations for a global optimal solution, but computational cost is too high for dynamic arrival.")
    print("----------------------------------------------------\n")