install:
	poetry install

lint:
	poetry run flake8

test:
	coverage run manage.py test -v 2
	coverage report
	coverage xml

runserver:
	poetry run python3 manage.py runserver

runshell:
	poetry run python3 manage.py shell

build:
	poetry build

publish: build
	poetry publish -r $(REPO) -u $(USER) -p $(PASSWORD)


