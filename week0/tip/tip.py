def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # removes the $ Symbol
    d = d.replace("$", "")

    # Converts the value to float
    dollars = round(float(d), 2)

    # Returns a float number
    return dollars

def percent_to_float(p):
    # removes the % symbol
    p = p.replace("%", "")

    # Converts the value to float and to decimal
    percent = float(p)/100

    # Returns a float number
    return percent


main()