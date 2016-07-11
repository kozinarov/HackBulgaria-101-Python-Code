import random
import json



class Car:

    def __init__(self, car, model, max_speed):
        self._car = car
        self._model = model
        self._max_speed = max_speed


class Driver:

    def __init__(self, name, car):
        self._name = name
        self._car = car
        self._crash_chance = 0
        self._points = 0


class Race:

    def __init__(self, list_of_drivers):
        self._list_of_drivers = list_of_drivers

    def str_drivers(self):
        return self._list_of_drivers

    def crash(self, crashed):
        for i in self._list_of_drivers:
            if i._crash_chance == crashed:
                return i

    def start_race(self): 
        list_crash_chance = random.sample(range(1, 10), len(self.str_drivers()))
        i = 0
        for racer in self._list_of_drivers:
            racer._crash_chance = list_crash_chance[i]
            i += 1
        crashed = max(list_crash_chance)
        self.calculate_points(list_crash_chance)
        return "{} has crashed".format(self.crash(crashed)._name)

    def give_point(self, list_crash_chance, crashed, data):
        point = 8
        for item in sorted(list_crash_chance):
                name = self.crash(item)._name
                if item == crashed:
                    if self.crash(item)._name in data:
                        data[name] = int(data[name]) + 0
                        print("{} - 0 point".format(name))
                        break
                    else:
                        data[self.crash(item)._name] = 0
                        print("{} - 0 point".format(name))
                        break
                if self.crash(item)._name in data:
                    data[name] = int(data[name]) + point
                    print("{} - {} points".format(name, point))
                else:
                    data[name] = point
                    print("{} - {} points".format(name, point))
                point -= 2

    def read_json(self):
        with open('points.json', 'r') as data:
            data = json.load(data)
        return data

    def write_json(self, data):
        with open('points.json', 'w') as f:
            json.dump(data, f)
        return data

    def calculate_points(self, list_crash_chance):
        crashed = max(list_crash_chance)
        data = self.read_json()
        self.give_point(list_crash_chance, crashed, data)
        self.write_json(data)
        return data

    def result(self):
        return "\nFinal results for this Championship : {}".format(self.read_json())


class Championship:

    def __init__(self, name, races_count):
        self._name = name
        self._races_count = races_count

    def print_score(self, count):
        print("\nRace #" + str(count))
        return "START"

    def top_3(self):
        top_3_list = []
        with open('points.json', 'r') as data:
            data = json.load(data)
        sorted_data = sorted(data[i] for i in data)
        limited_sorted_data = sorted_data[len(sorted_data)-3::]
        for i in limited_sorted_data:
            for name, score in data.items():
                if score == i:
                    top_3_list.append(name)
        return top_3_list

    def save_standing(self,race_name, self_race):
        dictionary = {}
        dictionary[race_name] = self_race.read_json()
        with open("standings.txt", "a") as data:
            data.write(str(dictionary))
        return ""

    def open_standings(self):
        with open("standings.txt", "r") as data:
            data = data.read()
        return data


class CLI:

    def __init__(self, race):
        self._race = race

    def hello_message(self):
        return "Hello Racer: "

    def command(self):
        return "Enter a command:"

    def top_3_message(self):
        return "THE TOP 3 ARE:"

    def start(self):
        print(self.hello_message())
        while True:
            print(self.command())
            console_input = input()
            try:
                text = console_input.split()
                command = text[0]
                if command == "exit":
                    break
                if command == "start":
                    race_name = text[1]
                    race_count = int(text[2])
                    if race_count > len(self._race._list_of_drivers):
                        raise Exception
                    championship = Championship(race_name, race_count)
                    print("Running {} races:".format(race_count))
                    count = 1
                    while count <= race_count:
                        print(championship.print_score(count))
                        print(self._race.start_race())
                        count += 1
                    print(self._race.result())
                    print(self.top_3_message())
                    print(championship.top_3())
                    print(championship.save_standing(race_name, self._race))
                if command == "standings":
                    print(championship.open_standings())
            except:
                print("Invalid comman!")


def main():
    

if __name__ == '__main__':
    main()
