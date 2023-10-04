FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . /app	

RUN pip install fastapi fastapi-cache2 uvicorn jsonmerge 

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
