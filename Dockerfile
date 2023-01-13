FROM python:3.9.16-alpine3.16
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY prod-new.py /app/
CMD [ "python" , "prod-new.py"]