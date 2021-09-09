FROM python:latest
COPY . /app
WORKDIR /app
EXPOSE 8002
RUN pip install -r requirements.txt
CMD python app.py
