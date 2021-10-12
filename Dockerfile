FROM python:3.8

COPY . /ernie
WORKDIR /ernie
RUN pip install -e .

ENV FLASK_APP ernie
CMD flask run