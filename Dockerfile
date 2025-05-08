from python:3.11-slim

WORKDIR /university_api

#set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ['uvicorn', "app.main:app", "--host", "0.0.0.0", "--port", "8080"]