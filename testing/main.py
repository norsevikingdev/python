def calculate(num1, num2):
    try:
        return (num1 + int(num2))
    except ValueError as err:
        return err
