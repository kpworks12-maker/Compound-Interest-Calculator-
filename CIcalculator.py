#compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("Enter a valid principle")

while rate <= 0:
    rate = float(input("Enter a rate: "))
    if rate <= 0:
        print("Enter a valid rate")

while time <= 0:
    time = float(input("Enter time: "))
    if time <= 0:
        print("Enter valid time")