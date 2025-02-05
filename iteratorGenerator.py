# Ödev 5
# EvenNumbers Iterator
class EvenNumbers:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

even_iterator = EvenNumbers(20)
for num in even_iterator:
    print(num, end=" ")

# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end=" ")

