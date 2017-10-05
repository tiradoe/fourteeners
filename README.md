## Fourteeners

This repo contains the Dockerized version of fourteeners.  Once this code is production ready it will replace the current project.

Setup:

1. Install Docker: https://www.docker.com/ and Docker Compose: https://docs.docker.com/compose/install/
2. Rename .env_example to .env and update the fields as needed
   - You can generate a Django secret key here: https://www.miniwebtool.com/django-secret-key-generator/
   - Get a weather api key here: https://home.openweathermap.org/users/sign_up
3. From within the project's directory run:
    docker-compose up -d

That should be enough to get the site running at 0.0.0.0:8000 though it may take a few seconds.  Any pages requiring a database query
will fail until a django migration has been performed on the container.  Script for that incoming.
