#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code is a calculator for two numbers


def calc_process(num1, symbol, num2):
    # Calculates the answers given the symbol given
    if symbol == "+":
        answer = num1 + num2
    elif symbol == "-":
        answer = num1 - num2
    elif symbol == "*":
        answer = num1 * num2
    elif symbol == "/":
        answer = num1 / num2
    elif symbol == "%":
        answer = num1 % num2
    return answer


def main():
    # Get user input
    user_num1 = input("Please pick a number! ")
    user_symbol = input("Please pick a math symbol (+,-,/, *) ")

    # Ensures the user symbol is a valid math operator
    if (
        (user_symbol == "+")
        or (user_symbol == "/")
        or (user_symbol == "%")
        or (user_symbol == "*")
        or (user_symbol == "-")
    ):

        user_num2 = input("Please pick another number! ")

        # Try catch for the two numbers
        try:
            num1_float = float(user_num1)
            try:
                num2_float = float(user_num2)

                # Checks for undefined cases (dividing by zero)
                if (num2_float == 0) and (user_symbol == "/" or "%"):
                    print("You cannot divide or modulo by zero!")

                # If it is valid the function is called and printed
                else:
                    answer = calc_process(num1_float, user_symbol, num2_float)
                    print(num1_float, user_symbol, num2_float, "=", answer)

            # If they cant be converted this happen
            except ValueError:
                print(user_num2, " is not a valid float!")
        except ValueError:
            print(user_num1, " is not a valid float!")
    else:
        print("Please enter a valid symbol!")


if __name__ == "__main__":
    main()
