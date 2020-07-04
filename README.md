# REST API Project
This is a basic REST API built with Python and Flask

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
