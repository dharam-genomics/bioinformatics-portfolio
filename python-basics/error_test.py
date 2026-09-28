class MyError(Exception):
    pass


def check_value(value):
    if value < 0:
        raise MyError("Value cannot be negative")

    return value

try:
    print(check_value(10))
    print(check_value(-5))
except MyError as error:
    print("Error handled:", error)
