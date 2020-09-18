FROM node:12.13-alpine
WORKDIR /app
RUN yarn global add http-server
COPY docs /app
CMD http-server