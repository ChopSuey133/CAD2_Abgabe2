# frontend/Dockerfile
FROM node:16-alpine

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY package*.json ./
RUN npm install

# Kopieren des Codes und Erstellen der Anwendung
COPY . .
RUN npm run build

# App auf einem Webserver starten
EXPOSE 3000
CMD ["npx", "serve", "-s", "build"]
