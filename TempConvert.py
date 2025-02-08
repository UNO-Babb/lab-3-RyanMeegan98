#TempConvert.py
#Name:Ryan Meegan
#Date:Feb 8 2025
#Assignment:F to C


def main():
  while True:
    try:
      tempF = float(input("Enter temperature in Fahrenheit: "))

      tempC = (5 / 9) * (tempF - 32)
      tempC = round(tempC, 1)

      print(f"{tempF}°F is {tempC}°C.")

      break

    except ValueError:
      print("Invalid input. Please enter a numeric temperature." )

  


if __name__ == '__main__':
  main()
