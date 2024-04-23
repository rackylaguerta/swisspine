FROM python:3.9.19-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 4004

ENV FLASK_APP=app.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "4004"]
