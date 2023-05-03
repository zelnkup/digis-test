build:
	docker-compose build

up:
	docker-compose up


test:
	docker-compose run --rm server sh -c "pytest"
