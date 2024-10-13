# Dutch-PM25-Modelling

Name: Neel Suri

Student Number: 5942004

Modelling and Predictions with Particulate Matter in The Netherlands

Project Description:
Luchtmeetnet is an initiative of the National Institute for Public Health (RIVM) to provide unvalidated measurement data for the Dutch air quality. If the project timeline allows for it, then real-time or hourly data for Particulate Matter (PM10) will be used to predict/model dispersion of PM10 in the Dutch air using the Atmospheric Dispersion Model, or make heat maps of PM10 density using the different measurement stations in the Netherlands. Also possibly doing some simple statistical modelling like Linear Regression to check for trends. 
In the case that the API functionality is hard to establish or maintain, hourly weather data validated by the RIVM will be used instead.

Project Methodology:
The project will start by creating basic functions that read user input data and validate them to ensure that it can be used to call the API
correctly using requests module. Once that has been established, then further analysis will follow...

Packages/Libraries: Matplotlib, Requests, Urllib, Folium, NumPy, Json, SSL 

Data Sources:
1. RIVM Weather Data Website: https://www.luchtmeetnet.nl/informatie
2. Luchtmeetnet 2020 OpenAPI: https://api-docs.luchtmeetnet.nl/
3. Hourly Weather Data: https://data.rivm.nl/data/luchtmeetnet/Actueel-jaar/
4. Atmospheric Dispersion Modelling: https://github.com/pktparticle/gaussianPlume

Expected Outcomes: Modelling Particulate Matter (PM10) using the Atmospheric Dispersion Modeling to estimate dispersion of PM particles in the Netherlands (in a broad perspective), or making a heat map
of the data for example.

Project Files: 
1. main.py - The python file with all the functions for this project.
2. gitignore - The file which specifies which files (in the local repository folder) to ignore while committing and pushing to Github.