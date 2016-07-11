
from collections import deque
import sys
import json


class Panda:

    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender.lower() == 'male'

    def isFemale(self):
        return self.__gender.lower() == 'female'

    def __str__(self):
        return '{} - {} - {}'.format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return 'Panda({}, {}, {})'.format(self.__name, self.__email, self.__gender)

    def __eq__(self, other):
        return self.__repr__() == other

    def __hash__(self):
        return hash(self.__str__())

    def mail_is_valid(self):
        return '@' in self.get_email() and self.get_email()[-8:] == 'mail.com'


class PandaSocialNetwork:
    def __init__(self):
        self.graph = {}

    def add_panda(self, panda):
        self.graph[panda] = []

    def has_friend(self, panda):
        return panda in self.graph

    def make_friends(self, panda1, panda2):
        if panda1 not in self.graph:
            self.graph[panda1] = []

        if panda2 not in self.graph:
            self.graph[panda2] = []

        self.graph[panda1].append(panda2)
        self.graph[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.graph[panda2] and panda2 in self.graph[panda1]

    def friends_of(self, panda):
        if panda not in self.graph:
            return False

        return self.graph[panda]

    def bfs(self, start, end):
        visited = []
        queue = deque()
        level_queue = deque()

        visited.append(start)
        queue.append(start)
        level_queue.append(0)

        while len(queue) != 0:
            node = queue.popleft()
            level = level_queue.popleft()

            if node == end:
                return level

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    level_queue.append(level + 1)
        return -1

    def connection_level(self, panda1, panda2):
        if self.are_friends(panda1, panda2) is True:
            return 1
        else:
            return self.bfs(panda1, panda2)

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) > 0

    def read_json(self):
        filename = sys.argv[1]
        with open(filename, 'r') as i:
            self.graph = json.load(i)

    def save_json(self):
        filename = sys.argv[1]
        with open(filename, 'r') as i:
            json.dump(self.graph, i)


'''
a = Panda('sdfg', "asd@dfgmail.com", 'male')
b = Panda('iuyj', "oiu@degmail.com", 'female')
c = Panda('vbn', "lkn@qwvmail.com", 'male')
d = Panda('er', "ern@ermail.com", 'male')
e = Panda('gt', "gt@utvmail.com", 'female')
f = Panda('por', "po@rwvmail.com", 'male')
network = SocialNetwork()
network.add_panda(a)
network.add_panda(b)
network.add_panda(c)
network.add_panda(d)
network.add_panda(e)
network.add_panda(f)
network.make_friends(a, c)
network.make_friends(c, e)
network.make_friends(a, b)
network.make_friends(a, d)
network.make_friends(e, d)
network.make_friends(e, f)
print(network.connection_level(a, e))
print(network.are_connected(a, e))
'''

network =  SocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)

print(network.connection_level(ivo, rado))  # True
print(network.connection_level(ivo, tony))  # True
