def get_numbers():
    # input-parsing helper
    return [int(i) for i in input("Enter your numbers: ").split()]


def even_numbers(nums):
    # list of all even numbers
    return [i for i in nums if i % 2 == 0]


def odd_numbers(nums):
    # TODO: return a list of all odd numbers
    return [i for i in nums if i % 2 != 0]


def count_above(nums, threshold):
    # how many numbers are > threshold
    return sum(1 for i in nums if i > threshold)


def sum_divisible_by(nums, x):
    # TODO: return the sum of numbers divisible by x
    return sum(i for i in nums if i % x == 0)

def analyze_numbers(nums, threshold, x):
    #TODO: call other functions to rest a final dictionary
    return {
        "evens": even_numbers(nums),
        "odds": odd_numbers(nums),
        "count_above": count_above(nums, threshold),
        "divisible_sum": sum_divisible_by(nums, x)
    }

# -------- main program  --------

numbers = get_numbers()

threshold = int(input("Enter a threshold: "))
divisor = int(input("Enter a divisor: "))

report = analyze_numbers(numbers, threshold, divisor)
print("=== Number Analysis Report ===")
print(f"Even numbers: {even_numbers(numbers)}")
print(f"Odd numbers: {odd_numbers(numbers)}")
print(f"Numbers above threshold ({threshold}): {report['count_above']}")
print(f"Sum of numbers divisible by {divisor}: {report['divisible_sum']}")
