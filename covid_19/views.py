from django.shortcuts import render
from .forms import CountryForm

import threading
import json
from json import dumps
import requests
# Create your views here.
url2 = "https://coronavirus-map.p.rapidapi.com/v1/summary/latest"

headers = {
        'x-rapidapi-key': "",
        'x-rapidapi-host': "coronavirus-map.p.rapidapi.com"
        }

response2 = requests.request("GET", url2, headers=headers)
all_data=(response2.json())




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
             'x-rapidapi-key': "",
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


# [
    a=all_data['data']['regions']
    topcon=[]
    topnum=[]  
    n=0
    for i in a:    
        n=n+1
        if n<6 :
            querystring3 = {"country":i,}
            
            response3 = requests.request("GET", url, headers=headers, params=querystring3)
            quotes3 =response3.json()

            a=quotes3['response'][0]['country']
            b=quotes3['response'][0]['cases']['total']

            topcon.append(a)
            topnum.append(b)
    topcon2=dumps(topcon)
    topnum2=dumps(topnum)        

# ]




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
                'topcon' : topcon2,
                'topnum' : topnum2 ,
                   }
    return render(request, 'covid_19/home.html', context)



    
def top_country(request) :    
    form = CountryForm()

    a=all_data['data']['regions']
    topcon=[]
    topnum=[]  
    n=0

  
    for i in a:    
        n=n+1
        if n<6 :
            url3 = "https://covid-193.p.rapidapi.com/statistics"
            querystring3 = {"country":i,}
            headers = {
                    'x-rapidapi-key': "fc10ca2471msh1436e5004570dd2p152fdfjsn953b9a54ea03",
                    'x-rapidapi-host': "covid-193.p.rapidapi.com"
            }
            response3 = requests.request("GET", url3, headers=headers, params=querystring3)
            quotes3 =response3.json()

            a=quotes3['response'][0]['country']
            b=quotes3['response'][0]['cases']['total']

            topcon.append(a)
            topnum.append(b)
    topcon2=dumps(topcon)
    topnum2=dumps(topnum) 

    context = { 'form':form ,
                'topcon' : topcon2,
                'topnum' : topnum2 ,
                   }

    return render(request, 'covid_19/top_country.html' , context)

def start(request) :    

    form = CountryForm()

    a=all_data['data']['regions']
    topcon=[]
    topnum=[]  
    top_country("http://127.0.0.1:8000")
    context = { 'form':form ,
                'topcon' : topcon,
                'topnum' : topnum ,
                   }
    return render(request, 'covid_19/top_country.html' , context)    