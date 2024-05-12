from faker import Faker
import csv
from random import randrange
import pandas as pd
import requests
import json

def html():
    fake = Faker()

    #fake.name()

    for i in range(0,10):
        print(i,fake.name())

    #random_age = round(random.uniform(18.0, 70.0), 1)

    with open('fakenames.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'Name','Age'])
        for n in range(1, 100):
            writer.writerow((n,fake.name(), randrange(18,70)))
            
    a = pd.read_csv("fakenames.csv") 
    # to save as html file 
    # named as "Table" 
    a.to_html("fakenames.html") 
    # assign it to a  
    # variable (string) 
    html_file = a.to_html()

if __name__ == "__main__":
    html()