# main.py
from parking_system import ParkingSlot, Vehicle
from greedy import allocate_parking_greedy
from analysis import run_performance_test, print_academic_justification

def run_interactive_mode():
    print("\n--- 🛠️ Interactive Dynamic Allocation ---")
    
    # 1. Get the number of parking slots from the user
    num_slots = int(input("Enter the total number of parking slots: "))
    slots = []
    
    # 2. Get the distance (cost) for each individual slot
    print("\n--- Enter Distances ---")
    for i in range(1, num_slots + 1):
        distance = int(input(f"Enter distance for Slot S{i} (in meters): "))
        slots.append(ParkingSlot(f"S{i}", distance))
        
    # 3. Get the number of arriving vehicles
    num_vehicles = int(input("\nEnter the number of arriving vehicles: "))
    vehicles = [Vehicle(f"V{i}") for i in range(1, num_vehicles + 1)]
    
    # 4. Run the Greedy Algorithm
    print("\nProcessing Allocation...")
    allocations = allocate_parking_greedy(vehicles, slots)
    
    # 5. Print formatted output
    print("-" * 55)
    print(f"{'Vehicle ID':<15} | {'Assigned Slot':<15} | {'Distance':<10} | {'Status'}")
    print("-" * 55)
    for alloc in allocations:
        dist_str = f"{alloc['Distance']}m" if alloc['Distance'] != 'N/A' else 'N/A'
        print(f"{alloc['Vehicle ID']:<15} | {alloc['Assigned Slot']:<15} | {dist_str:<10} | {alloc['Status']}")
    print("-" * 55)


if __name__ == "__main__":
    print("🚗 SMART PARKING SLOT ALLOCATION SYSTEM 🚗")
    print("Team members \n \t -> Kamalesh K. | 703 \n \t -> Surenthar L. | 705 \n \t -> Palaniappan A L. | 305 \n ")
    
    # Run the interactive mode where you type the inputs
    run_interactive_mode()
    
    # Print the academic justification for your CO5/CO6 marks
    print_academic_justification()
    
    # Run the automated stress test (because typing 1000 slots manually is impossible!)
    print("--- Experimental Validation (Real-World Load) ---")
    run_performance_test(5, 10)     # Small load
    run_performance_test(50, 50)    # Medium load
    run_performance_test(1000, 500) # Stress test