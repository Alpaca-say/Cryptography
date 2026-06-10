import random

print("=" * 50)
print("PSEUDORANDOM SEQUENCE GENERATOR")
print("=" * 50)

# User enters a seed value
seed = int(input("Enter a seed value: "))

# Initialize the pseudorandom generator
random.seed(seed)

# Number of values to generate
n = int(input("How many random numbers do you want to generate? "))

print("\nGenerated Pseudorandom Sequence:")
print("-" * 35)

sequence = []

for i in range(n):
    number = random.randint(0, 100)
    sequence.append(number)
    print(f"Random Number {i+1}: {number}")

print("-" * 35)

# Display sequence statistics
print("\nSequence Summary")
print(f"Total Numbers Generated: {len(sequence)}")
print(f"Minimum Value: {min(sequence)}")
print(f"Maximum Value: {max(sequence)}")
print(f"Average Value: {sum(sequence)/len(sequence):.2f}")

print("\nNote:")
print("Using the same seed value will always")
print("produce the same pseudorandom sequence.")