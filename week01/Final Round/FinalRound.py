def count_words(arr):
    return dict((i, arr.count(i)) for i in arr)

# print(count_words(["apple", "banana", "apple", "pie"]))


def nan_expand(times):
    nota = "Not a "
    not_aTimes = ""

    if times == 0:
        return ""

    if times < 0:
        return "Bad input"

    while times > 0:
        not_aTimes += nota
        times -= 1

    return not_aTimes + "NaN"

# print(nan_expand(2))


def iterations_of_nan_expand(expanded):
    if "NaN" not in expanded:
        return False

    return expanded.count("Not a")

# print(iterations_of_nan_expand('Not a'))


def group(something):
    tmp = []
    final = []
    tmp.append(something[0])
    for i in range(1, len(something)):
        if something[i] == something[i-1]:
            tmp.append(something[i])
            if i == len(something)-1:
                final.append(tmp)
        else:
            final.append(tmp)
            tmp = []
            tmp.append(something[i])
    return final


# print(group([1, 2, 1, 2, 3, 3]))
def max_consecutive(items):
    tmp_cnt = 0
    max_cnt = 0
    for i in range(0, len(items)-1):
        print(i)
        if items[i] == items[i+1]:
            tmp_cnt += 1
            
            if i+1 == len(items)-1:
                tmp_cnt += 1
        else:
            if tmp_cnt > max_cnt:
                max_cnt = tmp_cnt
                max_cnt += 1
            tmp_cnt = 0

    if tmp_cnt > max_cnt:
        max_cnt = tmp_cnt

    return max_cnt


# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def gas_stations(distance, tank_size, stations):
    stops = []
    last_st = 0
    for i in range(0, len(stations)):
        if stations[i] > distance:
            break
        if stations[i] - tank_size >= last_st:
            stops.append(stations[i-1])
            last_st = stations[i-1]
    stops.append(stations[len(stations)-1])
    return stops


    '''result = [0]
    stations.append(distance)

    for i in range(0, len(stations)-1):
        diff = stations[i+1] - stations[i]
        size = tank_size - (stations[i] - result[-1])

        if size < diff:
            result.append(stations[i])
            size = tank_size

    return result[1:]
'''
# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))


def sum_of_numbers(st):
    sum_num = 0
    tmp = 0
    cnt = 0
    for elem in st:
        if elem in '1234567890':
            if cnt > 0:
                tmp += elem
            else:
                tmp = elem
                cnt += 1
        else:
            sum_num += int(tmp)
            tmp = 0
            cnt = 0
    if st[len(st) - 1] in "1234567890":
        sum_num += int(tmp)
    return sum_num
# print(sum_of_numbers("ab125cd3"))


NUMBERS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}

'''
neznam zashto ne raboti za 'P' 


def message_to_numbers(messege):
    final = []
    last = 999
    for letter in messege:
        for key in NUMBERS:
            if letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                letter = letter.lower()
                final.append(1)

            if letter in NUMBERS[key]:
                print(letter)

                if last is key:
                    final.append(-1)

                for let_in_key in NUMBERS[key]:
                    print('let_in_key', let_in_key)
                    print('letter', letter)
                    if letter is let_in_key:
                        print('Yes')
                        final.append(key)
                        last = key
                        break
                    final.append(key)
    return final
'''


def symbol_to_list(letter):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:

        if letter in button:
            push_button = buttons.index(button) + 2
            press = button.index(letter) + 1
            return [push_button for i in range(press)]


def are_symbols_from_same_button(a, b):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:
        if a in button and b in button:

            return True

    return False


def message_to_numbers(message):
    sequence = []
    previous_symbol = ''

    for symbol in message:
        if symbol == ' ':
            sequence.append(0)
        else:
            if are_symbols_from_same_button(previous_symbol.lower(), symbol.lower()):
                sequence.append(-1)
            if symbol == symbol.upper():
                sequence.append(1)
                sequence += symbol_to_list(symbol.lower())
            else:
                sequence += symbol_to_list(symbol)
        previous_symbol = symbol

    return sequence


print(message_to_numbers("Ivo e Panda"))


def numbers_to_message(pressedSequence):

    pressed = group(pressedSequence)

    if pressedSequence[len(pressedSequence)-1] not in pressed[len(pressed)-1]:
        pressed.append([pressedSequence[len(pressedSequence)-1]])

    result = ""
    upper = False

    for combo in pressed:

        key = combo[0]
        count = len(combo)
        if key != -1:
            if key == 0:
                result += " "
                continue
            if key == 1:
                upper = True
                continue
            if upper:
                symbol = (
                    NUMBERS[key][(count - 1) % len(NUMBERS[key])]).upper()
                upper = False
            else:
                symbol = NUMBERS[key][(count - 1) % len(NUMBERS[key])]
            result += symbol

    return result

# print(numbers_to_message(
#     [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))

