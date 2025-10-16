FROM alpine:latest

# Setup python
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN python3 -m venv venv && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ./venv/bin/python3 main.py --config /config.yml
