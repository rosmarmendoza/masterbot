# Install dependencies
RUN pip install pipenv
COPY Pipfile* /
RUN pipenv lock --requirements > requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev
RUN pip install -r requirements.txt
# Copy sources files
WORKDIR /code
COPY . .
# Default port
ARG ARG_DEFAULT_PORT=8000
EXPOSE $ARG_DEFAULT_PORT
ENV DEFAULT_PORT=${ARG_DEFAULT_PORT}
# Install migrations
RUN python manage.py migrate
# Run server
ENTRYPOINT python manage.py runserver 0.0.0.0:${DEFAULT_PORT}