FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]