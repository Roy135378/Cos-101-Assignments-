G = 6.674e-11        # gravitational constant
GRAVITY = 9.8        # m/s²
LIGHT_SPEED = 3e8    # m/s


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def gravitational_force():
    m1 = get_number("Enter first mass (in Kg): ")
    m2 = get_number("Enter second mass (in Kg): ")
    r = get_number("Enter distance between them (in meters): ")
    if r == 0:
        print("Distance cannot be zero.")
    else:
        print("Gravitational Force =", G * m1 * m2 / r ** 2, "N")


def capacitor_charge():
    capacitance = get_number("Enter capacitance (in F): ")
    voltage = get_number("Enter voltage (in V): ")
    print("Charge =", capacitance * voltage, "C")


def fluid_pressure():
    density = get_number("Enter fluid density (in Kg/m³): ")
    height = get_number("Enter depth/height (in meters): ")
    print("Fluid Pressure =", density * GRAVITY * height, "Pa")


def refractive_index():
    v = get_number("Enter speed of light in the medium (in m/s): ")
    if v == 0:
        print("Speed cannot be zero.")
    else:
        print("Refractive Index =", LIGHT_SPEED / v)


def wavelength():
    speed = get_number("Enter wave speed (in m/s): ")
    frequency = get_number("Enter frequency (in Hz): ")
    if frequency == 0:
        print("Frequency cannot be zero.")
    else:
        print("Wavelength =", speed / frequency, "m")


operations = {
    "A": gravitational_force,
    "B": capacitor_charge,
    "C": fluid_pressure,
    "D": refractive_index,
    "E": wavelength,
}


def show_menu():
    print("\nSelect a Physics formula")
    print("A. Gravitational Force (F = G * m1 * m2 / r²)")
    print("B. Charge on a Capacitor (Q = C * V)")
    print("C. Fluid Pressure (P = ρ * g * h)")
    print("D. Refractive Index (n = c / v)")
    print("E. Wavelength (λ = v / f)")


while True:
    show_menu()
    user_choice = input("Enter a letter A-E: ").strip().upper()

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid choice. Please choose from A to E.")
        continue

    again = input("\nDo you want to run another operation? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
