from math import factorial


def sum_of_digits(n):
    sum_of = 0
    n = list(str(n))
    for i in range(0, len(n)):
        if ord(n[i]) >= 48 and ord(n[i]) <= 57:
            sum_of += int(n[i])

    return sum_of

# number = input('Number: ')
# print(sum_of_digits(number))


def to_digits(n):
    return [int(x) for x in str(n)]


# number = input('Number: ')
# print(to_digits(number))


def to_number(digits):
    result = 0
    counter = 0

    for digit in digits:
        for i in str(digit):
            counter += 1
        result = result * (10 ** counter) + digit
        counter = 0

    return result

# print(to_number([1, 2, 3]))


def fact_digits(n):
    numb = to_digits(n)
    final_n = 0
    for i in numb:
        final_n += factorial(i)
    return final_n

# umber = input('Number: ')
# print(fact_digits(number))


def fibonacci(n):
    result = []
    a, b = 1, 1
    cnt = 0
    while cnt < n:
        result.append(a)
        a, b = b, a + b
        cnt += 1

    return result


def fib_number(n):
    return to_number(fibonacci(n))

# number = int(input('Number: '))
# print(fib_number(number))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]

# inputed = input('Number: ')
# print(palindrome(inputed))


def count_vowels(str):
    result = 0

    for ch in str.lower():
        if ch in "aeiouy":
            result += 1

    return result

# inputed = input('Number: ')
# print(count_vowels("Python"))


def count_consonants(str):
    result = 0

    for ch in str.upper():
        if ch in "BCDFGHJKLMNPQRSTVWX":
            result += 1

    return result

# inputed = input('Number: ')
# print(count_consonants("Python"))


def char_histogram(string):
    # string = list(string)
    dict = {}
    l = list()

    for i in range(0, len(string)):
        cnt = 0
        for j in range(i, len(string)):
            if string[i] is string[j]:
                cnt += 1
        if string[i] not in l:
            l.append(string[i])
            dict.update({string[i]: cnt})



    '''for char in string:
        for i in range(0, len(string)):
            cnt = 0
            if char == string[i]:
                cnt += 1
            dict.update({char: cnt})
'''
    return dict

# print(char_histogram("Python!"))
# print(char_histogram("AAAAaaa!!!"))
