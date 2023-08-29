FROM python:3.9-slim
WORKDIR /quotes
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "quotes.py"]
    