# Dog Breeds Data Processor

## Summary

This project retrieves a list of all dog breeds from the Dog API, inserts the data into an SQLite database, and creates a new table called `sub_breeds` which contains the main dog breed names and the count of their sub-breeds. The application is containerized using Docker.

## Prerequisites

- Docker
- Python 3.9

## How to Run and Validate


### 1. Build the Docker Image

```docker build -t dog-app .```

### 2. Run the Docker container

```docker run -d --name dog-container dog-app```

### 3. SSH into the Running Container

```docker exec -it dog-container /bin/bash```

### 4. Inspect the SQLite Database

```sqlite3 dogs.db```

### 5. Run Queries to validate output

``` sqlite> SELECT * FROM breeds; ```
``` sqlite> SELECT * FROM sub_breeds;```


## References:
- https://docs.python.org/3/library/sqlite3.html
- https://requests.readthedocs.io/en/latest/
- https://dog.ceo/dog-api/documentation/