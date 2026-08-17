FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install 

COPY . . 

EXPOSE 80

# VOLUME ["/app/feedback"]

CMD ["node" ,"--watch", "server.js"]