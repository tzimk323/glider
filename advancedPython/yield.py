# In Python, the yield keyword is used in the context of generator functions
# to create iterable sequences. Generator functions allow you to define a
# function that can yield values one at a time, and these values can be
# iterated over without generating the entire sequence in memory. T
# This is especially useful for working with large datasets or infinite sequences.


#GENERATOR
# o generator mporei na exei apeira mesa den thelw na ta treksw ola, ousiastika kanw mia for, to next to katalavainei to yield
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage:
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))



# def process_large_file(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line.strip()
#
# # Usage:
# for line in process_large_file('large_data.txt'):
#     # Process each line
#     print(line)