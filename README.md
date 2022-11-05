# Sample API Serving a Tensorflow Model

## Setup
- `docker-compose up -d` will build and run the container
- `docker-compose logs -f` will follow log output
- Once the log output has stopped and the application is running, navigate to http://localhost:8000/docs. There is an API endpoint for using a Tensorflow model to run image classification on an uploaded image. Upload an image to see the response.
- This project can be modified and extended to fit your usecase. For example, you can load a different Keras model, load your own pre-trained model (see https://www.tensorflow.org/tutorials/keras/save_and_load#save_the_entire_model), or load multiple models and set up multiple FastAPI endpoints for your models.

## Notes
- The main.py and app.py files are mounted into the container in the docker-compose.yml. This allows any changes made during development to be picked up by the Uvicorn server.
- main.py contains ONLY the Web API logic
- model.py contains all the logic for loading a tensorflow model and running inference on an uploaded image. Try it out!
