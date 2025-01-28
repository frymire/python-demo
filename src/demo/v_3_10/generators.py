from typing import Generator, Any


def count_up_to(max_value: int) -> Generator[int, Any, str]:  # Generator[YieldType, SendType, ReturnType]
    count = 1
    while count <= max_value:
        yield count
        count += 1
    return "Done!"


# The instantiated generator produces each subsequent value when calling next(),
# which happens automatically in a for loop.
count_generator = count_up_to(5)
for number in count_generator:
    print(number)

# If you want to get the return value, use a try catch block.
print("\nThis time, catch the return value.")
count_generator = count_up_to(3)
try:
    while True:
        number = next(count_generator)
        print(number)
except StopIteration as e:
    print(e.value)  # capture the generator return value


def square_received_values() -> Generator[int, int, None]:
    value = 1  # Initialize with some value
    try:
        while True:
            # Receive new value from send(), if None, continue with current value
            received = yield value**2
            if received is not None:
                value = received  # Update the value if something new is sent
    except GeneratorExit:
        print("Generator was closed.")


# Create the generator
squares = square_received_values()
print()

# Get the first value (initialize the generator)
print(next(squares))  # Should print 1 (1**2)

# Send a new value and get the next squared value
print(squares.send(3))  # Should print 9 (3**2)

# Send another value and get the next squared value
print(squares.send(5))  # Should print 25 (5**2)

# Continue without sending a new value
print(next(squares))  # Should print 25 again (5**2)

# Close the generator
squares.close()
