# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


def bmi(weight: float, height: float) -> str:
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


def bmi_calc_one_liner(weight: float, height: float) -> str:
    return (
        "Underweight"
        if (weight / (height ** 2)) <= 18.5
        else "Normal"
        if (weight / (height ** 2)) <= 25.0
        else "Overweight"
        if (weight / (height ** 2)) <= 30.0
        else "Obese"
    )


if __name__ == "__main__":
    print(bmi_calc_one_liner(80, 1.80))
    print(bmi_calc_one_liner(68, 1.68))
    print(bmi_calc_one_liner(90, 1.80))
