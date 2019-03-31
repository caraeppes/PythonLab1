# Sum of Even Terms of Fibonacci Sequence < 4,000,000


def is_even(num):
    return num % 2 == 0


def get_even_terms():
    term1 = 0
    term2 = 1
    evens = []
    while term2 <= 4000000:
        sumOfTerms = term1 + term2
        if is_even(term2):
            evens.append(term2)
        term1 = term2
        term2 = sumOfTerms
    return evens


def sum_of_even_terms():
    sumOfEvens = 0
    evens = get_even_terms()
    for even in evens:
        sumOfEvens += even
    return sumOfEvens


# print(is_even(4))  # true
# print(is_even(3))  # false
# print(get_even_terms()) # [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]

print("The sum of the even terms of the Fibonacci sequence whose values are less than 4000000 is %d."
     % sum_of_even_terms())
