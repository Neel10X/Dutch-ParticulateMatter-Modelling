# Dutch-PM25-Modelling

Name: Neel Suri

Student Number: 5942004

Modeling and Predictions with Particulate Matter in The Netherlands

Project Description:
Luchtmeetnet is an initiative of the National Institute for Public Health (RIVM) to provide unvalidated measurement data for the Dutch air quality. I want to use real-time or hourly data to predict/model dispersion
of Particulate Matter in the Dutch air using the Atmospheric Dispersion Model, or make heat maps of PM density using the different measurement stations in the Netherlands. Also possibly doing some simple 
statistical modelling like Linear Regression to check for trends. In the case that the API functionality is hard to establish or maintain, I propose to use hourly weather data validated by the RIVM.

Packages/Libraries: Matplotlib, urllib, Folium, NumPy, json, ssl 

Data sources:
1. RIVM Weather Data Website: https://www.luchtmeetnet.nl/informatie
2. Luchtmeetnet 2020 OpenAPI: https://api-docs.luchtmeetnet.nl/
3. Hourly Weather Data: https://data.rivm.nl/data/luchtmeetnet/Actueel-jaar/
4. Atmospheric Dispersion Modelling: https://github.com/pktparticle/gaussianPlume

Expected Outcomes: Modelling Particulate Matter (10 or 2.5) using the Atmospheric Dispersion Modeling to estimate dispersion of PM particles in the Netherlands (in a broad perspective), or making a heat map
of the data for example.
