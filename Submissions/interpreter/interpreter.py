def main():
    x,y,z = input("Enter the expression : ").split()
    x = float(x)
    z = float(z)
    match y:
        case "+":
            print(f"{(x + z):.1f}")
        case "-":
            print(f"{(x - z):.1f}")
        case "*":
            print(f"{(x * z):.1f}")
        case "/":
            print(f"{(x / z):.1f}")
        case _:
            pass
main()

