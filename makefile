install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	pylint src
test:
	pytest 

