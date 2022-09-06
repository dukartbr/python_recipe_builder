import json
import random
import requests

fruits = ['apple', 'banana', 'cherry', 'avacado', 'blueberry']

base_url = 'http://jsonplaceholder.typicode.com/posts/'


def create_recipe(ingredients):
    with open('recipes.json', 'r') as file:
        file_data = json.load(file)
        for ingredient in ingredients:
                content_response = requests.get(f"{base_url}{random.randint(1, 10)}")   
                content = content_response.json()
                recipe = {
                    'title': ingredient,
                    'body': content['body']
                }
                file_data['recipes'].append(recipe)
    with open('recipes.json', "w") as fd:
        json.dump(file_data, fd, indent=4)


create_recipe(fruits)
