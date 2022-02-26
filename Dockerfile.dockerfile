FROM python:3.8-slim-buster
WORKDIR /code
RUN pip3 install Flask
COPY  Score.txt /Score.txt
COPY  Utils.py ./
COPY templates ./
COPY MainScores.py ./
CMD [ "python3", "MainScores.py" ]