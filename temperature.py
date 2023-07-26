#temperature convertor

unit = input("Is this temperature in Celsius or Fahrnheit (C/F):")
temp = float(input("Enter the temperature : "))
if unit == "C":
    temp = round((9 * temp)/5 + 32)
    print("The temperature in Fahrenheit is : ", temp, "Degree Fahrenheit")
elif unit == "F":
    temp = round((temp - 32)*5 / 9)
    print("The temperature is Celcius is : ", temp, "Degree Celcius")
else:
    print(unit,"is an invalid unit of temperature.")