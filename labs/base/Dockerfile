FROM node:alpine-lts
WORKDIR /app
RUN yarn global add http-server
COPY public /app
CMD http-server -p 8080