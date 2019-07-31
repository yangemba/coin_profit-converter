FROM python:3.7.3

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip3 install -r requirements.txt
EXPOSE 9999

CMD [ "sleep", "2000" ]

