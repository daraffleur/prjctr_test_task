# prjctr_test_task

## API Server (Stage 1, Stage 2)

### Description

API Server for the trained model from Stage1. The API contains one endpoint for prediction.

### Requirements

- Python >= 3.9
- FastAPI
- Pip for Python package and environment management.

## Start

1. To build and up api container, execute `docker-compose up -d --build`

2. Execute `docker-compose ps` and check if `api` container is in `running` STATUS. 
   If so, check PORTS column and copy the host\port value (e.g. `127.0.0.1:54289`), then open it in the browser.

3. Enjoy testing! 
   