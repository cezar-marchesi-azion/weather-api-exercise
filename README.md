# weather-api-exercise
A flask application to retrieve data from the Open Weather API

By passing the name of a city it will return the data in json format.
#
### Endpoints

```
temperature/<city_name>
```
Will return the following information about the queried city:

Field | Content | 
--- | --- | 
min | Minimum temperature in degrees Celsius. |
max | Maximum temperature in degrees Celsius. | 
avg | Average temperature in degrees Celsius. | 
feels_like | Feels like temperature in degrees Celsius. | 
city_name | Queried city's name. | 
country | Queried city's country code in the ISO 3166-1 alpha 3 format. | 

```
temperature/max=<max_number>
```
Will return a list of the cached temperatures for up to the latest
max_number queried cities. If a max_number is not provided, it will use the default value informed in the environment variable, as explained below.

#

## Usage

To use the application you will need your own api key provided by the Open Weather API. You can get it [here](https://home.openweathermap.org/api_keys).

You will need a .env file. There is a .env_example file in the project that has all the environment variables, just fill up the blanks and rename it to .env.
```
# API key from the Open Weather API
WEATHER_APPID=

# Time for the cache to expire in seconds. Defaults to 300 (5 minutes) if not filled.
CACHE_TTL=

# Max number of cities that will be retrived from the /temperature/max endpoint. It defaults to 5 cities if not filled.
DEFAULT_MAX_NUMBER=
```

With the .env file ready just build and run the Dockerfile. The Dockerfile is exposing the port 7007.


