 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD wait_for_db_and_start_server.sh .
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
