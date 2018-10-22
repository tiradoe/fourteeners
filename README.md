## Fourteeners

This repo contains the Dockerized version of fourteeners.

Setup:

1. Install Docker: https://www.docker.com/ and Docker Compose: https://docs.docker.com/compose/install/
2. Rename .env_example to .env and update the fields as needed.
   - You can generate a Django secret key here: https://www.miniwebtool.com/django-secret-key-generator/
   - Get a weather api key here: https://home.openweathermap.org/users/sign_up
3. Make sure the password in your .env file matches the one in the fourteeners/settings.py file
4. From within the project's directory run:
    docker-compose up -d

That should be enough to get the site running in your browser at localhost:8000 though it may take a few seconds.  After that,
you'll need to run the database migrations and load the fixtures so that the list of mountains can display.
I plan on having this automated in the future, but for now it needs to be run in the container.

Running the migrations:

1. Enter the running container:
    - Run this command from the main project directory: docker exec -ti fourteeners bash
2. Once inside, run these commands for the migrations:
    - python manage.py makemigrations
    - python manage.py migrate
3. Now load the mountain data from a fixture:
    - python manage.py loaddata apps/mountains/fixtures/mountains.json


That's it!  You should now be able to use the app by pointing your browser to localhost:8000
