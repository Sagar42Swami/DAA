# Function to get the maximum value for given weight capacity
def fractional_knapsack(values, weights, capacity):
    n = len(values)

    # Step 1: Calculate value-to-weight ratio for each item
    ratio = []
    for i in range(n):
        ratio.append((values[i] / weights[i], values[i], weights[i]))

    # Step 2: Sort items by ratio in descending order
    ratio.sort(reverse=True)

    total_value = 0.0  # Resultant total value
    remaining_capacity = capacity

    print("\nItem\tValue\tWeight\tFraction")
    print("-----------------------------------")

    # Step 3: Pick items greedily
    for r, value, weight in ratio:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
            print(f"{r:.2f}\t{value}\t{weight}\t1.00")
        else:
            # Take fractional part
            fraction = remaining_capacity / weight
            total_value += value * fraction
            print(f"{r:.2f}\t{value}\t{weight}\t{fraction:.2f}")
            remaining_capacity = 0

    return total_value


# Driver Code
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print("Fractional Knapsack Problem using Greedy Method")
    max_value = fractional_knapsack(values, weights, capacity)
    print("\nMaximum value in Knapsack =", max_value)
