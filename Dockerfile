FROM python:3.12

WORKDIR /app

RUN pip install requests
RUN pip install inquirer

COPY . src/app