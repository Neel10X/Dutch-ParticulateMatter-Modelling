# Modelling and Predictions with Particulate Matter (PM10) in The Netherlands

**Name:** Neel Suri

**Student Number:** 5942004


## Project Description
[Luchtmeetnet](https://www.luchtmeetnet.nl/) is an initiative of the National Institute for Public Health (RIVM) to provide unvalidated measurement data for the Dutch air quality. Particulate Matter (PM10) refers to suspended particles in the air with maximum diameter of 0.01 millimeters (mm) or 10 (micrometers) μm. These particles can cause adverse health-affects if inhaled. In the Netherlands, the 24 hour limit value may not exceed [50 (μg/m<sup>3</sup>)](https://www.rivm.nl/bibliotheek/digitaaldepot/GTL_matthijsen.pdf) more than 35 times per year. Therefore, it is essential to monitor their concentrations/values in the air. The real-time or hourly data for PM10 will be used to predict/model dispersion of PM10 in the Dutch air using the Atmospheric Dispersion Model, or make heat maps of PM10 density using the different measurement stations in the Netherlands. Also possibly doing some simple statistical modelling like Linear Regression to check for trends. In the case that the API functionality is hard to establish or maintain, hourly weather data validated by the RIVM will be used instead. However, these steps are outside the scope of this project for the time being and full functionality will be established at a later time. Refer to **Project Methodology** for the scope of the project.

## Project Methodology
For the time being the project will start by creating basic functions that read user input data for which station they want PM10 data for (currently only station NL01494 in [Schiedam](https://www.luchtmeetnet.nl/meetpunten?station=NL01494&component=PM10)), and validate them to ensure that it can be used to call the API correctly using requests module. Then the test_main file will be used to test these functions.

## Packages/Libraries
- **Requests** - to query the API and process the json response
- **Datetime** - to handle datetime input from user
- **Pytest** - to create testing functions for the main python program
- **NumPy** - (will be implemented in the future)
- **Matplotlib** - (will be implemented in the future)
- **Folium** - (will be implemented in the future)

## Data Sources:
1. [RIVM Weather Data Website](https://www.luchtmeetnet.nl/informatie)
2. [Luchtmeetnet 2020 OpenAPI](https://api-docs.luchtmeetnet.nl/)
3. [Hourly Weather Data](https://data.rivm.nl/data/luchtmeetnet/Actueel-jaar/)
4. [Atmospheric Dispersion Modelling](https://github.com/pktparticle/gaussianPlume) (will be implemented in the future)

## Expected Outcomes 
Hourly real-time PM10 data for the given time-range (limited to page 1 of the API response). Future functionality - Modelling Particulate Matter (PM10) using the Atmospheric Dispersion Modeling to estimate dispersion of PM10 particles in the Netherlands, or making a heat map of the data for example.

### Example Input
```
Enter date in the YYYY-MM-DD format

Enter which start date: 2024-10-18

Enter which end date (Maximum 7 day range): 2024-10-19
```

### Example Output
```
Timestamp                 PM10 Value (µg/m³)
----------------------------------------
2024-10-18T09:00:00+00:00 16.9
2024-10-18T10:00:00+00:00 13.8
2024-10-18T11:00:00+00:00 14.3
2024-10-18T12:00:00+00:00 12.6
2024-10-18T13:00:00+00:00 13.3
2024-10-18T14:00:00+00:00 13.8
2024-10-18T15:00:00+00:00 10.9
2024-10-18T16:00:00+00:00 11.5
2024-10-18T17:00:00+00:00 12.7
2024-10-18T18:00:00+00:00 13.4
2024-10-18T19:00:00+00:00 14.0
2024-10-18T20:00:00+00:00 14.7
2024-10-18T21:00:00+00:00 16.4
2024-10-18T22:00:00+00:00 20.6
2024-10-18T23:00:00+00:00 16.7
2024-10-19T00:00:00+00:00 13.7
2024-10-19T01:00:00+00:00 13.7
2024-10-19T02:00:00+00:00 15.7
2024-10-19T03:00:00+00:00 18.8
2024-10-19T04:00:00+00:00 20.1
2024-10-19T05:00:00+00:00 18.7
2024-10-19T06:00:00+00:00 15.1
2024-10-19T07:00:00+00:00 20.3
2024-10-19T08:00:00+00:00 19.3
2024-10-19T09:00:00+00:00 20.5
```

## Project Files 
- **main.py** - The Python file with all the functions for this project.
- **test_main.py** - The Python file with all the testing functions
- **pyproject.toml** - The configuration file which contains the build system requirements for Python projects. Refer to the [Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/pyproject-toml/) webpage for more information. (file not available yet)

## Usage
Start by downloading the main.py file to your system or cloning the repository to your system. Run the main.py file from either your terminal or code editor. Enter your date range for PM10 data in **YYYY-MM-DD** format. You will get your PM10 data for each hour (from **09:00:00 to 23:00:00** for one day) for the specified range. **Ensure the date range is between 1 and 7 days**

**Please note the API requests have a rate limit of 100 requests every 5 minutes. For running the program individually that will not be a issue, however, be aware while using a script not to make too many requests, to avoid getting blacklisted**

To run the test_main.py file, type "pytest <directory>\test_main.py" in the terminal.