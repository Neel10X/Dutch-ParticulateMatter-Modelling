# Import all python packages

import pytest
import requests
from datetime import datetime
import sys
from main import param_validate, date_validate, measurements
# Define Test Functions

def test_param_validate():

    assert param_validate("PM10") == "PM10"          
    assert param_validate("pm10") == "pm10"          
    assert param_validate("") is None                 
    assert param_validate("PM25") is None

def test_date_validate():
    assert date_validate("2024-10-10", "2024-10-17") == ("2024-10-10", "2024-10-17")  
    assert date_validate("2024-10-10", "2024-10-18") is None                        
    assert date_validate("2024-10-18", "2024-10-10") is None                        
    assert date_validate("2024-10-10", "2024-10-11") == ("2024-10-10", "2024-10-11")
    assert date_validate("2024-10-10", "2024-10-10") == None 
    assert date_validate("date", "2024-10-02") is None
    assert date_validate("2024-10-10", "date") is None     

def test_measurements():
    
    expected_url = 'measurements?station_number=NL01494&formula=PM10&page=1&order_by=timestamp_measured&order_direction=asc&end=2024-10-17T09:00:00&start=2024-10-10T09:00:00'
    assert measurements("PM10", "2024-10-10", "2024-10-17") == expected_url 

def refactor_user_input(parameter, start_date, end_date, base_url='https://api.luchtmeetnet.nl/open_api/'):

    if param_validate(parameter) is not None:

        if date_validate(start_date,end_date) is not None:

            url = base_url + measurements(parameter.upper(), start_date, end_date)
            return url
        
        else:

            return None
    
    else:
        
        return None
    

def test_user_input():
    parameter = "PM10"
    start_date = "2024-10-10"
    end_date = "2024-10-17"
    url = refactor_user_input(parameter, start_date, end_date)
    expected_url = 'https://api.luchtmeetnet.nl/open_api/measurements?station_number=NL01494&formula=PM10&page=1&order_by=timestamp_measured&order_direction=asc&end=2024-10-17T09:00:00&start=2024-10-10T09:00:00'
    assert url == expected_url

    parameter = "PM10"
    start_date = "2024-10-10"
    end_date = "2024-10-18"
    url = refactor_user_input(parameter, start_date, end_date)
    assert url is None

def refactor_call_api(call_user_input):

    if call_user_input is not None:

        r = requests.get(call_user_input)

        return r.status_code

    else:

        sys.exit()

def test_call_api(): 

    call_user_input = 'https://api.luchtmeetnet.nl/open_api/measurements?station_number=NL01494&formula=PM10&page=1&order_by=timestamp_measured&order_direction=asc&end=2024-10-11T09:00:00&start=2024-10-10T09:00:00'

    assert refactor_call_api(call_user_input) == 200
