from math import e, pi, cos, sin, pow, exp

# Part 1
radius = 5  # in centimeters
volume = (4/3)*pi*radius**3  # in cubic centimeters
print(f"The volume of a sphere with radius {radius} centimeters is {volume:.3f} centimeters^3")

# Part 2
x = 42.555555555
pythagorean_identity = cos(x)**2 + sin(x)**2
print(f"""Is the Pythagorean Identity True for {x}?
{"Yes" if pythagorean_identity == 1 else "No"} the Pythagorean Identity was {pythagorean_identity}""")

# Part 3
euler_number_squared = e**2
print(f"Euler's Number Squared via the exponentiation operator: {euler_number_squared:>.32f}")
euler_number_squared = pow(e, 2)
print(f"Euler's Number Squared via math.pow: {euler_number_squared:>53.32f}")
euler_number_squared = exp(2)
print(f"Euler's Number Squared via math.exp: {euler_number_squared:>53.32f}")

