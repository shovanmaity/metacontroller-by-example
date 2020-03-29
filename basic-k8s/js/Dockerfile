FROM node:10

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY sync.js sync.js

EXPOSE 8080
CMD [ "node", "sync.js" ]
