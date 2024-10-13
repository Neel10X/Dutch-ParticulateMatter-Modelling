# Import all python packages

import requests
import datetime

def api_endpoints(parameter):
    '''
    This function determines which endpoint that needs to be used when the user calls the API

    For example: 1) If the user wants all the measuring station names, then the stations endpoint will be
    contatenated to the base url.
      
    2) the NO2 values for a day from one particular station would mean that the stations/{stationname}/measurements
    would be used

    Input:
        parameter: string

    Output:
        endpoint: string

    '''
    endpoints = ["component","components","organisations","stations",""]
    endpoint = endpoints[parameter]
    return endpoint


def input_validate(userinp):
   '''
    This function validates the user input for the function user_input as handling incosistent
    user-entered data is essential to ensure the proper/smooth functioning of a program

    Input:
        userinp: string

    Output:
        
        If user input valid:
            userinp: string

        Else:
            break the while loop and return to the top of the user_input function
    '''
#    while True:
       
#        if type(user_input)

def user_input(base_url = 'https://api.luchtmeetnet.nl/open_api'):
    '''
    '''
    print("Enter which data you need ")
    parameter = input("Enter Parameter:")


    print("Enter which time interval you need the data for")
    # time_range =

    url = base_url + api_endpoints()
    return url


def call_api():
    '''Define the API url reading function
    '''
    r = requests.get(user_input())
    print(r.json())


endpoint = 'components'
