FROM node:lts-alpine as build-stage
WORKDIR /frontend
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /frontend/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


# docker build -t indicator-frontend .
# docker run -it -p 8080:80 --rm --name indicator-frontend-1 indicator-frontend
