# crispy-umbrella

## To start the application
`docker-compose up --build`

## To stop the application
`docker-compose down`

## To populate DB with dummy data
`python scripts/populate_db.py`

## To run app outside of docker
```poetry shell
poetry install --no-root
python device_info_gathering_service/manage.py migrate
python device_info_gathering_service/manage.py runserver
```