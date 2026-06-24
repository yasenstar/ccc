def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))

    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Category: {category}")

main()