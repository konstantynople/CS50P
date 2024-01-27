expression = input("Expression: ")
x, y, z = expression.split()

if y == "+":
    print(f"{int(x)+int(z):.1f}")
elif y == "-":
    print(f"{int(x)-int(z):.1f}")
elif y == "*":
    print(f"{int(x)*int(z):.1f}")
elif y == "/":
    print(f"{int(x)/int(z):.1f}")
else:
    print("Nonsense!")
