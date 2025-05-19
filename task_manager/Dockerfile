FROM python:3.9-slim

RUN mkdir -p /var/app/flask_app
WORKDIR /var/app/flask_app

COPY requirements.txt /var/app/flask_app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /var/app/flask_app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]