FROM python:3.9-slim

RUN pip install --upgrade pip
RUN apt-get -y update

COPY requirements.txt /ip-info/requirements.txt
RUN pip install -r /ip-info/requirements.txt

COPY main.py /ip-info/main.py
EXPOSE 8080

WORKDIR /ip-info
CMD ["python", "main.py"]