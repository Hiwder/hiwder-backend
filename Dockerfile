FROM python:3.8

WORKDIR /python-docker

RUN pip install flask gunicorn geopy firebase_admin

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]