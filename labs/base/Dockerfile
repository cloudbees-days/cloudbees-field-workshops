FROM node:lts-alpine
WORKDIR /app
RUN npm install --global http-server
COPY public /app
CMD http-server -p 8080