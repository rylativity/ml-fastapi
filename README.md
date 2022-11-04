# Sample API Serving a Tensorflow Model

## Setup
- `docker-compose up -d`
- `docker-compose logs -f` (to follow log output)

## Notes
- The main.py and app.py files are mounted into the container in the docker-compose.yml. This allows any changes made during development to be picked up by the Uvicorn server.
- model.py contains all the logic for loading a tensorflow model and running inference
- main.py contains ONLY the API logic