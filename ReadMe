# weather-forecast

## This project is developed to predict the weather trend in 210 major US cities for the next 50 years  and find their match with current climate conditions.

### The best match is determined using the normalized temperature and percipitation residuals. 

![Sample](Boston_Massachusetts_2070.png?raw=true)

The yearly average temperature and percipiation of the city assigned by the user in the future are compared to the 2020 data of all 210 US cities (inlcuding the assigned city itself) and a residual is calculated for each parameter. The temperature and percipitation residuals are then normalized by their annual mean and then the average of the two is computed. One of the calculated residulas (temperature, percipitation) or the average of the two is used to determine the closest match: The city in 2020 with the smallest residual is selected as the matching city, i.e. the assigned city (by the user) in the future will have similar temperature and percipitation to the matching city in 2020.

**Available Files:**
1. Weather_Forecast_Development.ipynb: 
  -This notebook examines data (percipitation and temperature) from a sample city to determine the necessary actions and parameters required to read and process data; and develop a model to forecast trends.
  -The time series temperature and percipiation data for 210 US cities are downloaded from the [Carnegie Mellon University database](https://kilthub.cmu.edu/articles/dataset/Compiled_daily_temperature_and_precipitation_data_for_the_U_S_cities/7890488)
  -The notebook is segregated into 3 chapters:
    1. Chapter 1: Load and work with a sample dataset
       1. Load modules and libraries and set parameters
       2. Load city IDs and show a sample city
       3. Clean and Resample data
       4. Decompose yearly weather data into: 1-seasonal, 2-trend, and 3-residual components. 
       5. Find parameters for the forecast model: Seasonal ARIMA (SARIMA): (p, d, q)x(P, D, Q, m) 
       6. Create the model with the determined parameters 
       7. Forecast data using the model
      
    2. Chapter 2: Load all cities, fit model and predict data for 2020-2070  
       1. Define a function to load data, fit model and save results 
      
    3. Chapter 3: Take info from user and find the best match 
       1. Load saved forecast data
       2. Accept city, state and date from user 
       3. Find the best match
        
2. Weather-Forecast.ipynb:
  -This notebook is the standalone version of the chapter 3 of the weather_forecast_development.ipynb
    
3. city_info_recent_all.csv
  -Contains the information of the 210 US cities
    
4. usa-states-census-2014.shp and usa-states-census-2014.shx
    Shapefile shape format, contains the actual geometry data of the US states
    
5. forecast_2020_2070.h5
    Contains the predicted temperature and percipitation for 210 US cities from 2020 to 2070
    
6. US_map folder:
  -Contains the Shapefile shape format of the US states
  
7. us_cities_Temp_prcp folder:
  -Conatins the historical time series data of all 210 US cities
  
8. environment.yml and requirements.txt:
  -The environment files necessary to recreate the python environment (python 3.6)
    
**DISCLAIMER**
1. The forecasting model parameters are determined by analyzing a sample city data and may not be suitable for all 201 US cities. One could develop a model for each city individually.
2. Taking the average of the normalized residuals of the two parameters (temperature and percipitation) might not be the best approach to consider the effect of the both parameters.
3. As evident from the seasonal decomposition, the percipitation is less reliable to utilize in the forecast model. Therefore, I suggest using mainly the temperature.
4. Due to the small trend of the data, the model may not find a match other than the assigned city itself for the near future. 
5. Due to the low density of cities in the west and significant change of data between them, the model may not find a match other than the assigned city itself.
6. Due to the limitation of the data to the US main land, the model may not find a match other than the assigned city itself should it be close to the border (especially the southern border).
    
