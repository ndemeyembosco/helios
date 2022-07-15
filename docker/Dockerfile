#syntax=docker/dockerfile:1
FROM jupyter/minimal-notebook:ubuntu-20.04 as Helios 

# docker build -t ideas-uo .

# The base image has changed the active user to jovyan
USER root
RUN apt-get update && apt-get install -y libmysqlclient-dev gcc

# Install ideas-uo
WORKDIR /home/jovyan/work
COPY . /home/jovyan/work

# && pip install -e .. && chown -R jovyan ..

# Return to original notebook user
# USER jovyan

FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

USER root 
COPY --from=Helios / /

WORKDIR /code 

COPY requirements.txt /code/

RUN pip install -r requirements.txt 

COPY ./ code/


ARG PROJECT_NAME 

ENV project_name=${PROJECT_NAME}

CMD /bin/bash 