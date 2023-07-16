FROM python:latest

WORKDIR /app

COPY . /app	

RUN pip install fastapi uvicorn jsonmerge

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
