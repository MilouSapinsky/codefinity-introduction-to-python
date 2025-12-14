meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheedar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

deli_dept = [meat, cheese, condiment]
print(f"Initial Deli list: ${deli_dept}")
# print(meat)

if "Ham" in meat and meat[2] < 100:
    meat[2] = 100
# print(meat)
    
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
# print(deli_dept)

deli_dept.remove(condiment)
# print(deli_dept)

deli_dept.sort()
print(f"Updated Deli List: ${deli_dept}")