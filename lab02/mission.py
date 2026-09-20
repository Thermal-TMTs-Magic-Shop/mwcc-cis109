name = input("Enter your agent name: ")
age = int(input("Enter your age: "))
years = int(input("How many years have you been training?: "))
color = input("Enter your favorite color: ")
gadget = int(input("How many gadgets are you carrying?: "))
minutes = int(input("How many minutes do you have? "))

training_percentage = (years / age) * 100
gadget_density = gadget / years
mission_seconds = minutes * 60
mission_time_remaining = minutes - 7
mission_code = f"{name.upper()}-{color.upper()}-{age}"
is_adult = age >=18
has_many_gadgets = gadget >= 5
has_training_experience = years > 0

print("====================================")
print("SECRET MISSION BRIEFING")
print("====================================")
print()
print(f"Agent: {name}")
print(f"Mission Code: {mission_code}")
print()
print(f"Age: {age}")
print(f"Training: {years} years")
print(f"Training Percentage: {training_percentage:.2f}%")
print()
print(f"gadgets: {gadget}")
print(f"Gadget Density: {gadget_density:.2f} per training year")
print()
print(f"mission time: {minutes} minutes")
print(f"mission time remaining: {mission_time_remaining} minutes")
print(f"mission time in seconds: {mission_seconds} seconds")
print()
print(f"Adult Agent: {is_adult}")
print(f"Many Gadgets: {has_many_gadgets}")
print(f"Training Experience: {has_training_experience}")
print()
print("====================================")
print("GOOD LUCK, AGENT!")
print("====================================")