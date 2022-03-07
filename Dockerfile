FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app
ADD ./ /app

RUN pip install -r requirements.txt
RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER  appuser

CMD [ "python", "main.py" ]