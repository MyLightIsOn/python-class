from openpyxl import Workbook


# Step 3 & Step 4 use the inputs from Step 1 to calculate required amounts
# Step 3: Calculate adjusted gross profit
def calculate_adjusted_profit(msrp, cost, type_code):
    gross_profit = msrp - cost
    if type_code == 1:  # import
        return gross_profit * (1 - 0.0175)
    return gross_profit

# Step 4: Calculate commission based on commission code
def calculate_commission(msrp, cost, type_code, commission_code):
    adjusted_profit = calculate_adjusted_profit(msrp, cost, type_code)
    if commission_code == "A":
        return adjusted_profit * 0.35
    elif commission_code == "B":
        return adjusted_profit * 0.25
    elif commission_code == "C":
        return adjusted_profit * 0.15
    return 0

# Step 2: Read the manifest file
def read_manifest(filename):
    cars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 5:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                car_name, msrp, cost, type_code, commission_code = parts
                msrp = float(msrp)
                cost = float(cost)
                type_code = int(type_code)
                commission_code = commission_code.upper()
                cars.append({
                    "name": car_name,
                    "msrp": msrp,
                    "cost": cost,
                    "type": type_code,
                    "commission_code": commission_code
                })
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return cars

# Step 5: Write car name and commission to Excel
def write_commissions_to_excel(car_list, filename="commission.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "commission"
    ws.append(["Car Name", "Commission Amount"])
    for car in car_list:
        name = car["name"]
        msrp = car["msrp"]
        cost = car["cost"]
        type_code = car["type"]
        commission_code = car["commission_code"]
        commission = calculate_commission(msrp, cost, type_code, commission_code)
        ws.append([name, round(commission, 2)])
    wb.save(filename)
    print(f"Commissions written to {filename}")

# Step 1: Add new cars to manifest
def update_manifest():
    while True:
        choice = input("Do you want to add a new car? Y/N ").strip().lower()
        if choice == "y":
            car_name = input('What is the name of the car? ').strip()
            msrp = float(input('What is the MSRP? ').strip())
            purchase_price = float(input('What is the purchase price? ').strip())
            type_code = int(input('Enter the type of car (0 = domestic, 1 = import): ').strip())
            commission_code = input('What is the commission code? (A, B, or C) ').strip().upper()

            with open("manifest.txt", "a") as file:
                file.write(f"{car_name} {msrp} {purchase_price} {type_code} {commission_code}\n")
        elif choice == "n":
            print("No new cars to add.")
            break
        else:
            print("Invalid input. Please enter Y or N.")

# Main program tying everything together
def main():
    update_manifest()
    cars = read_manifest("manifest.txt")
    if cars:
        write_commissions_to_excel(cars)

# Run the program
if __name__ == "__main__":
    main()
