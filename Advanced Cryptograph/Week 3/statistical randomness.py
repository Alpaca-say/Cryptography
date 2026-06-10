import random
import math
from collections import Counter

# Generate a random binary sequence
def generate_sequence(n=1000):
    return [random.randint(0, 1) for _ in range(n)]

# Frequency (Monobit) Test
def frequency_test(seq):
    n = len(seq)
    s = sum([1 if bit == 1 else -1 for bit in seq])
    test_stat = abs(s) / math.sqrt(n)
    p_value = math.erfc(test_stat / math.sqrt(2))
    return p_value

# Runs Test
def runs_test(seq):
    n = len(seq)
    pi = sum(seq) / n
    if abs(pi - 0.5) > (2 / math.sqrt(n)):
        return 0.0  # Fail due to imbalance
    runs = 1 + sum([1 for i in range(1, n) if seq[i] != seq[i-1]])
    expected_runs = 2 * n * pi * (1 - pi)
    z = abs(runs - expected_runs) / (2 * math.sqrt(2 * n) * pi * (1 - pi))
    p_value = math.erfc(z / math.sqrt(2))
    return p_value

# Chi-Square Test (for uniformity of bits)
def chi_square_test(seq):
    counts = Counter(seq)
    n = len(seq)
    expected = n / 2
    chi_square = sum([(counts[b] - expected) ** 2 / expected for b in [0, 1]])
    # Degrees of freedom = 1
    p_value = math.exp(-chi_square / 2)
    return p_value

# Demo
if __name__ == "__main__":
    seq = generate_sequence(1000)
    print("Frequency Test p-value:", frequency_test(seq))
    print("Runs Test p-value:", runs_test(seq))
    print("Chi-Square Test p-value:", chi_square_test(seq))

