#ApproxPi.py
#Name:Ryan Meegan
#Date:Feb 8 2025
#Assignment:AproxiPi
import math
import time

def approximate_pi(precision):
  approx_pi = 0
  denominator = 1
  sign = 1
  iterations = 0

  while abs(approx_pi - math.pi) > 10**(-precision) and iterations <10_000_000:
    approx_pi += (4 / denominator) * sign
    sign *= -1
    denominator += 2
    iterations += 1

    if iterations % 100_000 == 0:
      print(f"Still Running... Iterations: {iterations}, Pi: {approx_pi}")

  return approx_pi, iterations

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision = int(input("How many decimal points to compute (0 - 10): "))

  if precision < 0 or precision > 10:
    print(" Invalid input. Please enter a number between 0 and 10.")
    return

  start = time.time()

  #calculate pi using the approximation technique
  approx_pi, iterations = approximate_pi(precision)

  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start

  print(f"Pi: {approx_pi:.{precision}f}")
  print(f"Calculated in {elapsedTime:.6f} seconds.")
  print(f"Total iterations: {iterations}")



if __name__ == '__main__':
  main()
