# Import all python packages

import requests
from datetime import datetime
import sys

def param_validate(userinp):
    '''
    This function validates the parameter input for the function user_input as handling incosistent
    user-entered data is essential to ensure the proper/smooth functioning of a program

    Input(s):

        userinp (str): User input

    Output(s):
        
        str: userinp if user input is a string and contains "PM10"

        None: if anything else
    '''
    if len(userinp) < 1:
        
        print("Please specify a pollutant!")
        return None
    
    if isinstance(userinp,str) and userinp.upper() in ["PM10"]:
        
        return userinp
        
    else:

        print("Enter a valid input!")
        return None
    
def date_validate(startdateinp,enddateinp):
    '''
    This function validates the start and end date input for the function user_input as incosistent datetime formats will not query
    the API properly. Making sure that the dates are not more than 7 days apart and end date is later than the start date.

    Input(s):

        startdateinp (str): Start date input in YYYY-MM-DD format
        enddateinp (str): End date input in YYYY-MM-DD format

    Output(s):
        
        tuple: (formatted_startdate, formatted_enddate) if both the dates are of the appropriate YYYY-MM-DD format

        None: if anything else    
    '''
    try:

        start_date = datetime.strptime(startdateinp, "%Y-%m-%d")
        
        formatted_startdate = start_date.strftime("%Y-%m-%d")

    except:

        print("Incorrect start date format. Please use YYYY-MM-DD")
        return None
    
    try:

        end_date = datetime.strptime(enddateinp, "%Y-%m-%d")

        formatted_enddate = end_date.strftime("%Y-%m-%d")
    
    except:

        print("Incorrect end date format. Please use YYYY-MM-DD")
        return None
    
    if abs((end_date - start_date).days) <= 7 and end_date > start_date:
        
        return formatted_startdate, formatted_enddate
    
    else:

        print("The end date must be later than the start date and at least 7 days apart, or atleast 1 day apart.")
        return None

def measurements(formula, start, end, order_by="timestamp_measured", order_direction="asc", station="NL01494"):
    '''
    This function creates the final piece of the URL based on the input parameter/pollutant, and start and end date, to help make the final url
    that will be used to call the API. This function will help in essentially getting the pollutant measurements for
    a time range

    Input:
        formula (string): pollutant name
        start (string): start date
        end (string): end date

    Output:
        endpoint_included_url (string): url to create part of the query for api calling.
    '''
    endpoint_included_url = f'measurements?station_number={station}&formula={formula}&page=1&order_by={order_by}&order_direction={order_direction}&end={end}T09:00:00&start={start}T09:00:00'
    return endpoint_included_url


def user_input(base_url = 'https://api.luchtmeetnet.nl/open_api/'):
    '''
    This function asks the user for a parameter/pollutant, then invokes the input validation functions and if the user data
    is good, then it returns a complete URL needed for calling the API
    Input:
        base_url (string): base url

    Output:
        string: complete url for API querying
    '''
    parameter = input("Enter Parameter (Pollutant PM10 will only work for now): ")
    print()
    print("For simplicity sake, only station NL01494 is available")
    print()
    if param_validate(parameter) is not None:

        print("Enter date in the YYYY-MM-DD format")
        print()
        userstartdate_input = input("Enter which start date: ")
        print()
        userenddate_input = input("Enter which end date (Maximum 7 day range): ")

        if date_validate(userstartdate_input,userenddate_input) is not None:

            url = base_url + measurements(parameter.upper(), userstartdate_input, userenddate_input)
            return url
        
        else:

            return None
    
    else:
        
        return None

def call_api():
    '''
    Runs the user_input() function to make the URL for api calling and strips the time and pollutant values
    out of the json response, which is in the form of a dictionary in python. Prints the timestamp and its corresponding PM10
    value in a readable format.
    Input:
        No input

    Output:
        string: output text in the terminal
    '''
    call_user_input = user_input()

    if call_user_input is not None:

        r = requests.get(call_user_input)

        response = r.json()

        timestamps = [i['timestamp_measured'] for i in response['data']]

        values = [i['value'] for i in response['data']]

        print(f"{'Timestamp':<25} {'PM10 Value (µg/m³)':<15}")

        print("-" * 40)

        for timestamp, value in zip(timestamps, values):

            print(f"{timestamp:<25} {value:<15}")

    else:

        sys.exit()

if __name__ == "__main__":
    
    call_api()