FROM node:latest

WORKDIR /app

COPY package.json . 
# this command runs when creating the image
RUN npm install 

COPY . . 

EXPOSE 80
# this command run when running the container
CMD ["node" ,"--watch" , "server.js"]

