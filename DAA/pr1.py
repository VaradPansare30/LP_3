n = 7

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("\nRecursive Fibonacci: ")
for i in range(n):
    print(fibonacci(i), end=" ")
