from django import forms
from django.forms import ModelForm

import json
import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-key': "fc10ca2471msh1436e5004570dd2p152fdfjsn953b9a54ea03",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

area=response.json()
area1=(area['response'])
location = []
for every_country in area1 :
    location.append((every_country, every_country.upper()))
a= [('a','A'),('b','B'),('c','C'),('d','D'),['e','E']]

class CountryForm(forms.Form):
    # country = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Input Country "}),  )
    country = forms.CharField(label='which conuntry', widget=forms.Select(choices=location)  )