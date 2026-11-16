print("Select a Physics formula")
print("A. Gravitational Force ( F = G * m1 * m2 / r²)")
print("B. Charge on a Capacitor ( Q = C * V)")
print("C. Fluid Pressure ( P = ρ * g * h)")
print("D. Refractive Index ( n = c / v)")
print("E. Wavelength ( λ = v / f)")

user_choice = input("Enter a letter A-E: ").upper()

if user_choice == "A":
    G = 6.674e-11
    m1 = float(input("Enter first mass (in Kg): "))
    m2 = float(input("Enter second mass (in Kg): "))
    r = float(input("Enter distance between them (in meters): "))
    if r == 0:
        print("Distance cannot be zero.")
    else:
        force = G * m1 * m2 / r ** 2
        print("Gravitational Force =", force, "N")

elif user_choice == "B":
    capacitance = float(input("Enter capacitance (in F): "))
    voltage = float(input("Enter voltage (in V): "))
    charge = capacitance * voltage
    print("Charge =", charge, "C")

elif user_choice == "C":
    density = float(input("Enter fluid density (in Kg/m³): "))
    height = float(input("Enter depth/height (in meters): "))
    g = 9.8
    pressure = density * g * height
    print("Fluid Pressure =", pressure, "Pa")

elif user_choice == "D":
    c = 3e8
    v = float(input("Enter speed of light in the medium (in m/s): "))
    if v == 0:
        print("Speed cannot be zero.")
    else:
        n = c / v
        print("Refractive Index =", n)

elif user_choice == "E":
    speed = float(input("Enter wave speed (in m/s): "))
    frequency = float(input("Enter frequency (in Hz): "))
    if frequency == 0:
        print("Frequency cannot be zero.")
    else:
        wavelength = speed / frequency
        print("Wavelength =", wavelength, "m")

else:
    print("Invalid choice. Please choose from A to E.")
