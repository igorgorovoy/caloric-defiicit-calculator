def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be either 'male' or 'female'")

def calculate_tdee(bmr, activity_level):
    activity_multiplier = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725,
        "extra_active": 1.9
    }
    return bmr * activity_multiplier.get(activity_level.lower(), 1.2)

def calculate_caloric_intake(tdee, deficit=500):
    return tdee - deficit

if __name__ == "__main__":
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    activity_level = input("Enter your activity level (sedentary/lightly_active/moderately_active/very_active/extra_active): ")

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    caloric_intake = calculate_caloric_intake(tdee)

    print(f"BMR: {bmr:.2f} kcal/day")
    print(f"TDEE: {tdee:.2f} kcal/day")
    print(f"Caloric Intake for Weight Loss: {caloric_intake:.2f} kcal/day")
