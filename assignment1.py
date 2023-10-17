import random

# Initialize a list with 10 zeros
elements = [0] * 10

# Add random numbers to the elements
for i in range(len(elements)):
    elements[i] += random.uniform(0, 1)  # Adds a random float between 0 and 1

# Print the elements with original and modified values
for i, element in enumerate(elements):
    original_value = 0  # Original value is always 0
    modified_value = element
    print(f"Element {i + 1}: Original={original_value}, Modified={modified_value}")
