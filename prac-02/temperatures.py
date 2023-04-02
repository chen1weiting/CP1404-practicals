def Celsius_To_Fahrenheit(cTemp):
  fTemp = cTemp * 9.0 / 5 + 32
  return fTemp

def Fahrenheit_To_Celsius(fTemp):
  cTemp = 5 / 9 * (fTemp - 32)
  return cTemp


# Main

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
  if choice == "C":
    celsius = float(input("Celsius: "))
    fahrenheit = Celsius_To_Fahrenheit(celsius)
    print(f"Result: {fahrenheit:.2f} F")
  elif choice == "F":
    fahrenheit = float(input("Fahrenheit: "))
    celsius = Fahrenheit_To_Celsius(fahrenheit)
    print(f"Result: {celsius:.2f} C")
  else:
    print("Invalid option")
  print(MENU)
  choice = input(">>> ").upper()

print("Thank you.")