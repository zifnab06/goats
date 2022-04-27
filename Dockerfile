FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD gunicorn app:app -b 0.0.0.0:8080 -w 9 --max-requests 1000 --max-requests-jitter 500
