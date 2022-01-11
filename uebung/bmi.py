# Calculate your Body-Mass-Index with Python
print("BMI - Calculator!")

weight_str = input("Please insert your weight (in kg): ")
height_str = input("Please insert your bodys height(in m): ")

weight = float(weight_str.replace(",", "."))
height = float(height_str.replace(",", "."))

bmi = weight / height ** 2

print("Your BMI is: " + str(round(bmi, 1)))