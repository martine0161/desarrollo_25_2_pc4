.PHONY: setup run-local docker-build docker-run scan clean

setup:
	pip install -r app/requirements.txt
	pip install bandit pip-audit cyclonedx-bom

run-local:
	python app/main.py

docker-build:
	docker build -t local-sarif-factory -f docker/Dockerfile .

docker-run:
	docker run -p 5000:5000 local-sarif-factory

scan:
	cd scripts && bash full-scan.sh

clean:
	rm -rf evidence/*.json
	find . -type d -name __pycache__ -exec rm -rf {} +