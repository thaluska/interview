FROM python:2

ADD weather_app.py /

RUN pip install pyowm

ARG APIKEY
ARG CITY

ENV OPENWEATHER_API_KEY=$APIKEY
ENV CITY_NAME=$CITY

CMD ["python", "./weather_app.py"]
