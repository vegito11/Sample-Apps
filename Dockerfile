# alpine in Docker terminolgy means very compact that is small in size 
# so this is smallest image available for node you can also use node:6.14 or node:9.1 etc
FROM node:alpine

WORKDIR /usr/app

# Sometime when change only in our code file not in package.json . We have to install all packages once 
# again for next build we can use cache for this so first copy package.json then npm install 
# as package.json will not be modified npm install will be used from cache 
COPY ./package.json ./

RUN npm install

# copy all file from build directory to container
COPY ./ ./


CMD ["npm","start"]