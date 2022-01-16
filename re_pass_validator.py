# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.
import re


def re_password_validator(password: str) -> bool:
    return bool(re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", password))


if __name__ == "__main__":
    print(re_password_validator("Ab1c2d3"))  # True
    print(re_password_validator("fjd3IR9"))  # False
    print(re_password_validator("Ab1c2d3E!"))  # False
