# REST API Project
This is a basic REST API built with Python and Flask

## Docker

Build the image:

```docker build -t edarioq/rest-api .```

Run the container

```docker run -p 8888:5000 edarioq/rest-api```

OR run Docker Compose

```docker-compose build```

```docker-compose up```

To get into the container's shell, use:

```docker exec -it <container> bash```
