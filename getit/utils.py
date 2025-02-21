import json
import os

def load_data(filename):
    data = f'static/data/{filename}'
    with open(data,'r') as data:
        return json.load(data)

def load_template(filename):
    template = f'crudapp/templates/{filename}'
    with open(template, 'r') as template:
        return template.read()
    
def add_note(data, filename):
    with open(f'static/data/{filename}', 'w') as file:
        json.dump(data, file)