def number_sequence(start, end, step=1):
    current = start
    while current <= end:
        yield current
        current += step

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step value: "))

sequence_generator = number_sequence(start, end, step)

for number in sequence_generator:
    print(number)


def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1
# iterate over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)