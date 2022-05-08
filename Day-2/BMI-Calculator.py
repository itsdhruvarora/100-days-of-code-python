print("Body Mass Calculator\n\n\n")

height = float((input("Please Enter Your Height (In m): ")))
weight = float(((input("Please Enter Your Weight (In kg): "))))

BMI = float((weight))/float((height**2))
bmi_as_int = round(float((BMI)))

print(bmi_as_int)