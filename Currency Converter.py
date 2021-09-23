#Creating simple currency converter

#Gather the parameter of interest
#Construct the URL and send a GET request to it
#For unsuccessful requests, print the error message
#For successful request: extract the relevant data and calculate the result
#Display the result to the user

import requests

base_url="https://api.exchangerate.host/"

date=input("Please enter the date (in format 'yyyy-mm-dd' or 'latest'): ")
base=input("Convert from (currency): ")
curr=input("Convert to (currency): ")
quantity=float(input(f'How much {base} you want to convert: '))

url=base_url + date + "?base=" + base + "&symbol=" +curr

response=requests.get(url)

if (response.ok==False):
    print(f'\nError {response.status_code}')
    print(response.json()['error'])
else:
    data=response.json()
    rate=data['rates'][curr]

    result=quantity * rate

    print(f'{quantity} {base} is equal to {result} {curr}, based upon exchange rates on {date}')
