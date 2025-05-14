FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./
COPY postcss.config.cjs ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npx", "vite", "--host", "0.0.0.0"]
