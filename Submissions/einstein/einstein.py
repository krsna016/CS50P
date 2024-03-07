def main():
    mass = int(input("Enter the mass(in kgs) : "))
    e = energy(mass)
    print(e)

def energy(mass):
    # Speed of Light
    c = 300000000 # meters per second
    e = mass*(c**2)
    return e

main()
