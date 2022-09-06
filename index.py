import json
import urllib.request
import random

fruits = ['apple', 'banana', 'cherry', 'avacado', 'blueberry']

baseURL = 'http://jsonplaceholder.typicode.com/posts/'


def create_recipe(arr):
    f = open('recipes.json', 'r+')
    file_data = json.load(f)
    for x in arr:
        content = urllib.request.urlopen(
            baseURL + str(random.randint(1, 10))).read()
        y = json.loads(content)
        recipe = {
            'title': x,
            'body': y['body']
        }
        file_data['recipes'].append(recipe)
        f.seek(0)
        json.dump(file_data, f, indent=4)
    f.close()


create_recipe(fruits)
