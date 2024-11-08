# backend/Dockerfile
FROM python:3.9-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install -r requirements.txt

# Code kopieren
COPY . .

# Flask starten
EXPOSE 5000
CMD ["python", "app.py"]

