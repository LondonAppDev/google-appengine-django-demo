# Google App Engine Django Demo

Demo project of Django running on the Google App Engine.

## Setup

This project requires:

 1) Google Cloud Platform project and account
 2) Docker and Docker Compose
 3) [App Engine Admin API](https://console.cloud.google.com/apis/library/appengine.googleapis.com?project=londonappdev-test&folder&organizationId=26405936585) enabled for project

Also, to build or test locally, you will need a virtual environment with the requirements installed:

```
python -m venv env
pip install -r requirements.txt
```

## Usage

 1) Authenticate with Google Cloud Platform account (note, account credentials are stored in `creds/`, avoid sharing this directory with anyone)

```
docker-compose run --rm gcloud gcloud auth login
```

 2) Build static files

```
source env/bin/activate
python manage.py collectstatic --noinput
```

3) Deploy to App Engine

```
docker-compose run --rm gcloud gcloud app deploy --project <YOURPROJECT>
```

4) Browse (or view URL)

```
docker-compose run --rm gcloud gcloud app browse --project <YOURPROJECT>
```
