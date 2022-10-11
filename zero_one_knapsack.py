"""The knapsack problem"""

# Imagine that you are a thief who enters a museum but you have a big problem, you just have a backpack but there are many more things than you can carry, so you must determine which items you can carry and they will give you the highest possible value.

# For this problem we know that we cannot split the items, so our first approximation will be to evaluate the items.


def knapsack(capacity, weights, values, n) -> int:

    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(capacity, weights, values, n - 1)

    return max(
        values[n - 1] + knapsack(capacity - weights[n - 1],
                                 weights, values, n - 1),
        knapsack(capacity, weights, values, n - 1))


def run():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)

    result = knapsack(capacity, weights, values, n)
    print(result)


if __name__ == '__main__':
    run()