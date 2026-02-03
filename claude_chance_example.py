import random


def sum_of_100_rolls():
    """Roll a dice 100 times and return the sum"""
    return sum(random.randint(1, 6) for _ in range(100))


def iterations_to_reach_target(target=100):
    """Count how many iterations of 100 rolls it takes to reach the target sum"""
    total = 0
    iterations = 0

    while total < target:
        total += sum_of_100_rolls()
        iterations += 1

    return iterations, total


# Run it once
iterations, final_sum = iterations_to_reach_target(100)
print(f"It took {iterations} iteration(s) of 100 rolls to reach {final_sum}")

