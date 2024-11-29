x, y, z = input("Expression : ").split()
x = int(x)
z = int(z)
match y:
    case "+":
        print(f"{x+z:.1f}")
    case "-":
        print(f"{x-z:.1f}")
    case "*":
        print(f"{x*z:.1f}")
    case "/":
        print(f"{x/z:.1f}")
    case _:
        print(f'You can only use math operator instead of "{y}".')
