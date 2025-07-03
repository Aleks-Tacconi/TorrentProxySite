FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl build-essential git gnupg \
 && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
 && apt-get install -y nodejs \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

COPY .env /app/.env
COPY backend /app/backend
COPY client /app/client

WORKDIR /app/client
RUN npm install
RUN npm install -g webtorrent-cli

EXPOSE 5173
EXPOSE 5000

WORKDIR /app
ENV PYTHONPATH=/app
CMD sh -c "poetry run python backend/main.py & cd client && npm run dev -- --host"
