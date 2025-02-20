def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Pls enter a number")