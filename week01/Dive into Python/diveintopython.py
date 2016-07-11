import copy


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def to_digits(n):
    return [int(x) for x in str(n)]


def is_number_balanced(n):
    print(n)
    digits = to_digits(n)
    middle_len = len(digits) // 2

    left_digits = digits[0:middle_len]

    if len(digits) % 2 == 0:
        right_digits = digits[middle_len:]
    else:
        right_digits = digits[middle_len + 1:]

    print(left_digits)
    print(right_digits)

    return sum(left_digits) == sum(right_digits)
    


# number = input("Number: ")
# print(is_number_balanced(number))


def is_increasing(seq):

    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False

    return True

# print(is_increasing([1, 2, 3, 4, 5]))


def is_decreasing(seq):

    for i in range(0, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
    return True

# print(is_decreasing([100, 50, 120]))


def get_largest_palindrome(n):
    n -= 1
    while n >= 0:
        if palindrome(n):
            break
        n -= 1
    return n

# print(get_largest_palindrom(994687))


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    a = str(a)
    b = str(b)
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    len_a = len(a)
    cnt = 0

    for elem_a in a:
        for elem_b in b:
            if elem_a == elem_b:
                cnt += 1

    return len_a == cnt


# print(is_anagram("BRADE", "BeaRD"))


def birthday_ranges(birthdays, ranges):
    result = []

    for rang in ranges:
        counter = 0

        for day in birthdays:
            if day >= rang[0] and day <= rang[1]:
                counter += 1

        result.append(counter)

    return result

# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def sum_matrix(m):
    num = 0
    for i in m:
        for j in i:
            num = num + int(j)
    return num

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def prime_numbers(n):

    all_numbers = [x for x in range(2, n + 1)]

    for i in range(2, n + 1):
        not_prime = [x for x in range(i * 2, n + 1, i)]
        all_numbers = set(all_numbers) - set(not_prime)

    return sorted(list(all_numbers))


# number = input("Number: ")
# print(prime_numbers(number))

# da napisha matrix bombing 


def is_transversal(transversal, family):

    for members in family:

        result = []

        for person in members:
            if person in transversal:
                result.append(person)

        if len(result) == 0:
            return False

    return True

#print(is_transversal([2, 3, 6], [[1, 2], [4, 5, 6], [3, 4]]))

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def is_in(m, coord):
    if coord[0] < 0 or coord[0] >= len(m):
        return False

    if coord[1] < 0 or coord[1] >= len(m[0]):
        return False

    return True


def bomb(m, coord):
    if not is_in(m, coord):
        return m

    target_value = m[coord[0]][coord[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (coord[dx] + position[dx], coord[dy] + position[dy])

        if is_in(m, position):
            position_value = m[position[dx]][position[dy]]
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result

