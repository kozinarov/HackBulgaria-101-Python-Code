import datetime
from functools import wraps
import time


def accepts(*types):
    def function(func):
        def check_type(*func_types):
            count = 0
            while count < len(func_types):
                if isinstance(func_types[count], types[count]):
                    count += 1
                else:
                    return "TypeError: Argument {} of say_hello is not {}".\
                            format(count+1, types[count].__name__)
            return func(*func_types)
        return check_type
    return function


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

# print(say_hello(4))
# print(say_hello("Hacker"))


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

# print(deposit("RadoRado", 0))


def encrypt(num):
    def function(func):
        @wraps(func)
        def move_chars():
            alphabet = list("abcdefghijklmnopqrstuvwxyz")
            new_string = ''
            for elem in func().lower():
                if elem == ' ':
                    new_string += " "
                else:
                    new_string += alphabet[alphabet.index(elem) + num]
            return new_string
        return move_chars
    return function


def log(file_name):
    def function(func):
        @wraps(func)
        def save_to_file():
            with open(file_name, 'a') as f:
                date = datetime.datetime.now()
                f.write("{} was called at {}\n".format(func.__name__, date))
            return func()
        return save_to_file
    return function


@log("file.txt")
@encrypt(2)
def get_low():
    return "Get get get low"

# print(get_low())


def performance(file_name):
    def function(func):
        def get_time_execution():
            start_time = time.time()
            message = func()
            with open(file_name, 'a') as f:
                writings = "{} was called and took {} seconds to complete\n".\
                    format(func.__name__, time.time() - start_time)
                f.write(writings)
            return message
        return get_time_execution
    return function


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


print(something_heavy())
