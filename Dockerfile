FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

CMD ["uvicorn", "config.asgi:application", "--reload"], "--host", "0.0.0.0", "--port", "8000"

