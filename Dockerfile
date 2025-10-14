FROM python:3.14-slim

# Upgrade pip and system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends gcc && \
	pip install --upgrade pip && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY datasets ./datasets
COPY rest-api .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
