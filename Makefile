install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest --cov=page_loader tests/ --cov-report xml

runserver:
	poetry run python3 manage.py runserver

runshell:
	poetry run python3 manage.py shell

build:
	poetry build

publish: build
	poetry publish -r $(REPO) -u $(USER) -p $(PASSWORD)


