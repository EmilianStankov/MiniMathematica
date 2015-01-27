from mathematica import MiniMathematica


instructions = """
Enter a (valid) mathematical expression using the following syntax:
- For the trigonometric functions:
    sin(n) where 'n' is the number you want the sine of.
    cos(n), where 'n' is the number you want the cosine of.
    tg(n), where 'n' is the number you want the tangent of.
    cotg(n), where 'n' is the number you want the cotangent of.
- For roots:
    sqrt(n), where 'n' is the number you want the square root of.
    nthrt(k, n), where 'k' is the number you want the 'n'-th root of.
- For powers:
    pow(k, n), where 'k' is the number you want the 'n'-th power of.
- For logarithms:
    log(k, n), where 'k' is the base and 'n' the number you want the logarithm of.

Example:
    Enter an expression you would like to be calculated.
    > 5 + sin(pi) / pow(2, 10) - log(e, pow(e, sqrt(4)))
    The result is: 3.0
"""
if __name__ == "__main__":
    print("Type in \'exit\' to exit at any time.")
    print("You can also type in \'help\' for instructions\n")
    while True:
        try:
            print("Enter an expression you would like to be calculated.")
            expression = input("> ")
            if expression == "exit":
                break
            elif expression == "help":
                print(instructions)
            else:
                result = MiniMathematica().calculate(expression)
                print("The result is: {0}\n".format(result))
        except ValueError:
            print("This is not a valid input, try again!\n")
