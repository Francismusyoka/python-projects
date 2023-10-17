import random

# Set 10 elements to zero
elements = [0] * 10

# Add random numbers to the elements
for i in range(len(elements)):
    elements[i] += random.randint(1, 10)

# Print the elements with the original being the first and modified being second
print("Original elements:", elements[:len(elements) // 2])
print("Modified elements:", elements[len(elements) // 2:])
