FROM python:3.8.7-buster

RUN apt-get update && apt-get upgrade -y

WORKDIR /app/

COPY requirements/app.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ .

ENV FLASK_APP=main.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
