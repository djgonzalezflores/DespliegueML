FROM python:3.5

ADD requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000

ADD ./ /src/

WORKDIR /src
