def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratio = []

    # Calculate ratios
    for i in range(n):
        ratio.append((values[i] / weights[i], i))

    # Sort in descending order
    ratio.sort(reverse=True)

    fractions = [0.0] * n
    total_value = 0

    # Select items
    for r, i in ratio:
        if capacity >= weights[i]:
            fractions[i] = 1.0
            capacity -= weights[i]
            total_value += values[i]
        else:
            fractions[i] = capacity / weights[i]
            total_value += values[i] * fractions[i]
            capacity = 0
            break

    print("Fractions of items selected:")
    for i in range(n):
        print("Item", i+1, ":", fractions[i])

    print("\nMaximum value =", total_value)


# Driver code
values = [60, 30, 50]
weights = [20, 10, 25]
capacity = 50

fractional_knapsack(values, weights, capacity)
