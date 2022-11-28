FROM python
RUN pip install Faker
RUN pip install kafka-python
RUN mkdir /app
WORKDIR /app
COPY . /app
ENTRYPOINT ["python3","address_producer.py"]