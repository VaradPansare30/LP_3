
n = 3

weight = [2, 3, 4]
profit = [12, 20, 30]

W = 5

# Sort items by profit/weight ratio
items = []

for i in range(n):
    items.append((weight[i], profit[i], i + 1))

items.sort(key=lambda x: x[1] / x[0], reverse=True)

weight = [x[0] for x in items]
profit = [x[1] for x in items]
item_no = [x[2] for x in items]

max_profit = 0
best_items = []


# Calculate upper bound
def bound(i, w, p):

    total = p

    while i < n and w + weight[i] <= W:
        w = w + weight[i]
        total = total + profit[i]
        i = i + 1

    if i < n:
        total = total + (W - w) * profit[i] / weight[i]

    return total


# Branch and Bound
def knapsack(i, w, p, selected):

    global max_profit, best_items

    if p > max_profit:
        max_profit = p
        best_items = selected[:]

    if i == n:
        return

    if bound(i, w, p) <= max_profit:
        return

    # Take current item
    if w + weight[i] <= W:
        knapsack(i + 1, w + weight[i],
                 p + profit[i], selected + [item_no[i]])

    # Don't take current item
    knapsack(i + 1, w, p, selected)


knapsack(0, 0, 0, [])

print("Maximum Profit:", max_profit)
print("Selected Items:", best_items)
