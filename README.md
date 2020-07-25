# REST API Project
This is a starter project with a basic REST API built with Docker, Flask, and PostgreSQL. Use this to build your own REST API.

## Docker

Build the services
```
docker-compose build
```

Start the services
```
docker-compose up
```

To get into the container's shell, use:
```
docker exec -it <container> bash
```

To get into the Postgres shell, use:
```
docker exec -it <db-container> psql -U postgres
```
