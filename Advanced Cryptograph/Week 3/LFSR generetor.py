def lfsr(seed, taps, length):
    """
    seed: Initial binary state as a list (e.g., [1,0,1,1])
    taps: Positions used for feedback (e.g., [0, 3])
    length: Number of bits to generate
    """
    
    register = seed.copy()
    output_sequence = []

    for _ in range(length):
        output_bit = register[-1]  # Output is the last bit
        output_sequence.append(output_bit)

        # XOR tapped bits to generate feedback
        feedback = 0
        for tap in taps:
            feedback ^= register[tap]

        # Shift right and insert feedback bit at the beginning
        register = [feedback] + register[:-1]

    return output_sequence


# Example Usage
seed = [1, 0, 1, 1]      # Initial state
taps = [0, 3]            # Feedback taps
length = 20              # Number of bits to generate

sequence = lfsr(seed, taps, length)

print("Initial Seed:", seed)
print("Generated Sequence:")
print(''.join(map(str, sequence)))