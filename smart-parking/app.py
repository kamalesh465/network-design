import tkinter as tk
from tkinter import messagebox
import time

# Greedy Algorithm Logic
def allocate_parking_greedy(vehicles, slots):
    allocations = []
    
    for vehicle in vehicles:
        best_slot = None
        min_distance = float('inf')

        # Find the nearest available slot
        for slot in slots:
            if slot['is_available'] and slot['distance'] < min_distance:
                min_distance = slot['distance']
                best_slot = slot

        # Allocate if a slot was found
        if best_slot:
            best_slot['is_available'] = False
            allocations.append((vehicle, best_slot['id'], best_slot['distance'], "Allocated"))
        else:
            allocations.append((vehicle, "N/A", "N/A", "Parking Full"))
            
    return allocations

# Process input and generate output
def run_allocation():
    try:
        # Get vehicle count
        num_vehicles = int(entry_vehicles.get())
        if num_vehicles <= 0:
            raise ValueError("Number of vehicles must be greater than 0")

        # Get slot details
        slot_lines = text_slots.get("1.0", tk.END).strip().split("\n")
        slots = []
        
        for line in slot_lines:
            if not line.strip(): 
                continue
                
            parts = line.split()
            if len(parts) != 2:
                raise ValueError("Each slot line must be: SlotID Distance (e.g., S1 5)")
            
            slot_id, dist = parts[0], int(parts[1])
            slots.append({'id': slot_id, 'distance': dist, 'is_available': True})

        # Generate vehicle IDs
        vehicles = [f"V{i+1}" for i in range(num_vehicles)]

        # Run algorithm and measure performance
        start_time = time.perf_counter()
        allocations = allocate_parking_greedy(vehicles, slots)
        end_time = time.perf_counter()

        exec_time = (end_time - start_time) * 1000

        # Display Results
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "-" * 55 + "\n")
        result_text.insert(tk.END, f"{'Vehicle ID':<15} | {'Assigned Slot':<15} | {'Distance':<10} | {'Status'}\n")
        result_text.insert(tk.END, "-" * 55 + "\n")

        for v, s, d, stat in allocations:
            dist_str = f"{d}m" if d != "N/A" else "N/A"
            result_text.insert(tk.END, f"{v:<15} | {s:<15} | {dist_str:<10} | {stat}\n")
        
        result_text.insert(tk.END, "-" * 55 + "\n")
        
        # Display Complexity Metrics for CO5/CO6
        result_text.insert(tk.END, f"\n⏱️ Execution Time: {exec_time:.4f} ms\n")
        result_text.insert(tk.END, "📊 Time Complexity: O(n × m)\n")
        result_text.insert(tk.END, "💾 Space Complexity: O(m)\n")
        result_text.insert(tk.END, "✅ Method: Greedy Approach (Immediate Local Optimal Choice)\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window Setup
root = tk.Tk()
root.title("Smart Parking System - Greedy Algorithm")
root.geometry("600x650")

# Academic Titles
tk.Label(root, text="🚗 Smart Parking Slot Allocation System", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Team members \n \t -> Kamalesh K. | 703 \n \t -> Surenthar L. | 705 \n \t -> Palaniappan A L. | 305 \nGovt. College of Technology, Coimbatore", font=("Arial", 10, "italic"), fg="gray").pack()

tk.Frame(root, height=2, bd=1, relief="sunken", width=500).pack(pady=10)

# Input: Number of vehicles
tk.Label(root, text="Number of Arriving Vehicles:", font=("Arial", 10, "bold")).pack()
entry_vehicles = tk.Entry(root, justify="center")
entry_vehicles.insert(0, "4")  # Default Case Study value
entry_vehicles.pack(pady=5)

# Input: Parking Slots
tk.Label(root, text="Enter Parking Slots Configuration:\n(Format: SlotID Distance)", font=("Arial", 10, "bold")).pack(pady=5)
text_slots = tk.Text(root, height=6, width=25, font=("Courier", 10))
# Pre-fill with your specific Case Study Data
text_slots.insert(tk.END, "S1 5\nS2 10\nS3 15\nS4 20")
text_slots.pack()

# Action Button
tk.Button(root, text="Allocate Slots (Run Greedy Algorithm)", command=run_allocation, bg="#0052cc", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=15)

# Output Console
tk.Label(root, text="System Output:", font=("Arial", 10, "bold")).pack()
result_text = tk.Text(root, height=12, width=65, font=("Courier", 10), bg="#f4f4f4")
result_text.pack(pady=5)

# Run app
root.mainloop()