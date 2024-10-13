# Import all python packages

import requests
import datetime
import sys

# Will be looked into in the future

'''def api_endpoints(parameter):
    
    This function determines which endpoint that needs to be used when the user calls the API

    For example: 1) If the user wants all the measuring station names, then the stations endpoint will be
    concatenated to the base url.
      
    2) the NO2 values for a day from one particular station would mean that the stations/{stationname}/measurements
    would be used

    Input:
        parameter: string

    Output:
        endpoint: string

    
    endpoints = ["component","components","organisations","stations",""]
    endpoint = endpoints[parameter]
    return endpoint'''


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
            return None
    '''
    if len(userinp) < 1:
        
        print("Incorrect input!")
        return None
    
    elif isinstance(userinp,str) and userinp in ["PM10"]:
        
        return userinp.upper()

    #elif isinstance(userinp,datetime):

        #return userinp

    else:
        
        print("Incorrect input!")
        return None
    
def station_measurements(param,order="formula",order_dir="asc",station="NL01494"):
    '''
    This function creates the final piece of the URL based on the input parameter/pollutant, to help make the final url
    that will be used to call the API. This function will help in essentially getting the pollutant measurements for
    a particular station 

    Input:
        param: string
        order: string
        station: string

    Output:
        endpoint_included_url: string
    '''
    endpoint_included_url = f'stations/{station}/measurements?page=1&order={order}&order_direction={order_dir}&formula={param}'
    return endpoint_included_url


def user_input(base_url = 'https://api.luchtmeetnet.nl/open_api/'):
    '''
    This function asks the user for a parameter/pollutant, then invokes the input validation functions and if the user data
    is good, then it returns a complete URL needed for calling the API
    Input:
        base_url: string

    Output:
        url: string
    '''
    parameter = input("Enter Parameter (Pollutant PM10 will only work for now): ")
    
    if input_validate(parameter) is not None:

        # print("Enter which time interval you need the data for")
        # time_range = input()
        url = base_url + station_measurements(parameter)
        return url
        # url = base_url + api_endpoints()
        # return url
    
    else:
        
        return None

def call_api():
    '''
    Input:
        No inputs, runs the user_input() function to make the URL for api calling

    Output:
        dictionary (API response)
    '''
    if user_input is not None:
        r = requests.get(user_input())
        return r.json()
    
    else:
        print("Hmm something went wrong...please try running the program again")
        sys.exit()

print(call_api())
# user_input()
# print(user_input())