# CRUD-Rest-API
CRUD Rest API in Python using Flask, Postgres, Docker

**How to test this api locally:**

- First download the assigment file by downloading it as a zip file or cloning it.
- Then you should download [Docker](https://www.docker.com/) to build and run the images in a container.
- Then you can open cmd(preferably windows powershell if you're using windows) or just terminal.
- Now cd to the file your just downloaded.
- Type `docker compose up -d flask_db` to run the container.
- Use `docker ps -a` to check the status of the image.
- Then download [Table Plus](https://tableplus.com/download) which is a tool to test the connection of postgreSQL connection.
- Click on the plus button and choose PostgreSQL , now fill Host with `localhost` , Port with `5432` and (User,Password,Database) with `postgres`
- Now click on test then connect.
- Then let's build the image by typing `docker compose build` in the terminal , or we can just type `docker compose up --build flask_app` to build and run.
- We can now visit `http://localhost:8000/persons` in any browser to check if it's working.
- Now you should download [Postman](https://www.postman.com/downloads/) to try and test the API.
- You can test first by choosing which method you want to use then typing `http://localhost:8000/persons` in the url then pressing send.
- Finally you can Create, Read, Update, Delete person objects in this api!
