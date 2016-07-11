import requests

codes = requests.get("http://astral.hacksoft.io/api/airline/")

json_code = codes.json()

names = requests.get("http://data.okfn.org/data/core/country-list/r/data.json")

json_name = names.json()


def how_maney_airlines(country):
    counter = 0
    code = ""
    for elem in json_name:
        if elem['Name'] == country:
            print("hahaha")
            code = elem["Code"]
    for elem in json_code:
        if elem["country_code"] == code:
            counter += 1
    return counter

print(how_maney_airlines("Bulgaria"))
