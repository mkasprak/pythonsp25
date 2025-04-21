def multiples_of_five(n):
    for i in range(n):
        yield i * 5

# Example usage
result = list(multiples_of_five(10))
print(result)


#lambdas
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sort by age (index 1)
sorted_by_age = sorted(people, key=lambda person: person[1])
print(sorted_by_age)
# Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]


numbers = [1, 2, 3, 4, 5, 6]

# Keep evens
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# Output: [2, 4, 6]

# closure
def outer_func(x):                  # x is part of the enclosing scope
    def inner_func(y):
        return x + y                # x is remembered even after outer_func is done
    return inner_func

closure = outer_func(10)           # returns inner_func with x=10
print(closure(5))                  # calls inner_func(5), so x=10, y=5 ➜ 15


