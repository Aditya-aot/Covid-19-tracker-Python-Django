from django.shortcuts import render
from .forms import CountryForm

import json
import requests
# Create your views here.
def home(request) :
    user_input="india"
    form = CountryForm()
    if request.method == 'POST' :
        form = CountryForm(request.POST , request.FILES)
        if form.is_valid() :
            user_input = form.cleaned_data['country']


    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country": user_input, }
    headers = {
             'x-rapidapi-key': "fc10ca2471msh1436e5004570dd2p152fdfjsn953b9a54ea03",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    quotes = response.json()


            # ('------------AREA---------------------')
    continent=( quotes['response'][0]['continent'])
    country =( quotes['response'][0]['country'])
    population=( quotes['response'][0]['population'])

    # ('------------CASE-------------------')
    new_cases = ( quotes['response'][0]['cases']['new'])
    active_cases = ( quotes['response'][0]['cases']['active'])
    critical_cases = ( quotes['response'][0]['cases']['critical'])
    recovered_cases = ( quotes['response'][0]['cases']['recovered'])
    case_1M_pop = ( quotes['response'][0]['cases']['1M_pop'])
    total_cases = ( quotes['response'][0]['cases']['total'])

    #('------------DEATHS-------------------')
    new_deaths = ( quotes['response'][0]['deaths']['new'])
    deaths_1M_pop = ( quotes['response'][0]['deaths']['1M_pop'])
    total_deaths = ( quotes['response'][0]['deaths']['total'])

    # ('------------TESTS--------------------')
    test_1M_pop = (quotes['response'][0]['tests']['1M_pop'])
    total = (quotes['response'][0]['tests']['total'])

    # ('------------LAST UPDATE---------------')
    days = (quotes['response'][0]['day'])
    time = (quotes['response'][0]['time'])

    context = { 'form' : form ,
                'quotes' : quotes ,
                'population' :population ,
                'continent' : continent ,
                'country' : country ,
             
                'new_cases' : new_cases,
                'active_cases' : active_cases,
                'critical_cases' : critical_cases,
                'recovered_cases': recovered_cases,
                'case_1M_pop' : case_1M_pop,
                'total_cases' : total_cases,

                'new_deaths' : new_deaths ,
                'deaths_1M_pop': deaths_1M_pop ,
                'total_deaths':  total_deaths ,

                'test_1M_pop':  test_1M_pop,
                'total': total ,

                'days' : days ,
                'time' : time ,
                   }
    return render(request, 'covid_19/home.html', context)
    