import random
from collections import Counter
import time
import numpy as np

def naive_shuffle(cards):
    for i in range(len(cards)):
        n = random.randint(0, len(cards)-1)
        cards[i], cards[n] = cards[n], cards[i]

def fisher_yates_shuffle(cards):
    for i in range(len(cards)-1, 0, -1):
        n = random.randint(0, i)
        cards[i], cards[n] = cards[n], cards[i]

def count_combinations(shuffle_func):
    counts = Counter()
    start_time = time.time()
    for _ in range(1000000):
        cards = [1, 2, 3, 4]
        shuffle_func(cards)
        counts[tuple(cards)] += 1
    end_time = time.time()
    duration = end_time - start_time
    return counts,  duration
    
def calculate_std_deviation(counts):
    frequencies = list(counts.values())
    std_deviation = np.std(frequencies)
    return std_deviation
    
def print_counts(counts):
    for combination, count in counts.items():
        print(f"{list(combination)}: {count}")

print("Naive algorithm:")
naive_counts, naive_time = count_combinations(naive_shuffle)
print_counts(naive_counts)
print("Time taken:", naive_time)
naive_std_deviation = calculate_std_deviation(naive_counts)
print("Standard deviation:", naive_std_deviation)

print("Fisher–Yates shuffle:")
fy_counts, fy_time = count_combinations(fisher_yates_shuffle)
print_counts(fy_counts)
print("Time taken:", fy_time)
fy_std_deviation = calculate_std_deviation(fy_counts)
print("Standard deviatio:", fy_std_deviation)

