PYTHON ?= python3
.PHONY: test run docker
test:
	$(PYTHON) -m pytest -q
run:
	PYTHONPATH=src $(PYTHON) -m uvicorn aik8sops.main:app --reload --port 8080
docker:
	docker build -t ai-kubernetes-operations-platform:local .
