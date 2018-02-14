# Weather app

This app is using openweather map API to get weather information and output it on console

For this app to work is needed to have defined these enviroment variables:
- OPENWEATHER_API_KEY -> you can get this key by registering on the site openweathermap.org
- CITY_NAME -> city for which you want to get weather information

## Dockerfile

Dockerfile is for building docker image of this app from which you can run weather app container which will output weather data.

For building docker image run this command on host where you have docker installed.
```bash
docker build -t weather:dev .
```

For running created docker image as docker container, you need to run this command:
```bash
docker run --rm -e OPENWEATHER_API_KEY="your API key" -e CITY_NAME="Bratislava" weather:dev
```
