FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

RUN pip install poetry

COPY poetry.toml poetry.lock ./

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

