FROM python:3.8

COPY . /ernie
WORKDIR /ernie
RUN pip install -e .

CMD FLASK_APP=ernie flask run