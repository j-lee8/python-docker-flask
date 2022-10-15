A basic Dockerized Flask app displaying all the SpaceX ships. This would serve as a suitable boilerplate.
## Building the image
Run the following command in the repo dir: ```docker build --tag spacex-flask-api .```

## Running the application
1. Run the following command: ```docker run --name spacex-flask-api -d -p 5000:5000 spacex-flask-api```
2. Go to ```http://127.0.0.1:5000``` to see it running