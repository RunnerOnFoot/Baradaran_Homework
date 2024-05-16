def binomial_coefficient(n, m):
    if m == 0 or n == m:
        return 1
    else:
        return binomial_coefficient(n - 1, m) + binomial_coefficient(n - 1, m - 1)


# Calculate binomial coefficient for n=5, m=7
n = 7
m = 5
result = binomial_coefficient(n, m)
print(f"The binomial coefficient for n={n} and m={m} is {result}")
