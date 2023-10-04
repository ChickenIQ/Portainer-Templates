FROM python:slim

WORKDIR /app

COPY . /app	

RUN apt install python3-distutils

RUN pip install fastapi fastapi-cache2 uvicorn jsonmerge 

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
