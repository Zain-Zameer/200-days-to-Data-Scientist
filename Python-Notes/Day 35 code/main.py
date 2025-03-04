class MultiplyBy:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplier

    def __call__(self, numbers):
        return [num * self.factor for num in numbers]

# Create an instance and call it like a function
multiplier = MultiplyBy(10)
data = [1, 2, 3, 4, 5]
print(multiplier(data))  # Output: [10, 20, 30, 40, 50]
