import art
print(art.logo)

results = None

while True:
    if results is None:
        a = float(input("Enter first number:\n"))
    else:
        a = results
        print(f"Current result is: {a}")
    b = float(input("Enter second number:\n"))

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b


    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    op = input("Enter operator:\n+\n-\n*\n/\n")

    if op == "+":
        result = operations[op](a,b)
        print(result)
    elif op == "-":
        result = operations[op](a, b)
        print(result)
    elif op == "*":
        result = operations[op](a, b)
        print(result)
    elif op == "/":
        result = operations[op](a, b)
        print(result)

    results = result

    user_choice = input("Do you want to continue with the current result (yes) or start fresh (no)?:").lower()
    if user_choice == "yes":
        continue
    if user_choice == "no":
        print("\n"*100)
        continue
