# Deep Classifier Project

## Workflows:
1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update entity (namedtuple)
5. Update configuration
6. Update components
7. Update pipeline
8. Test run the staged pipeline
9. Run tox.ini for testing the package
10. Update dvc.yaml
11. Run "dvc repro" command for running all stages in pipeline

![img](https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/docs/images/Data%20Ingestion%402x%20(1).png)


STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/c17hawke/FSDS_NOV_deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=c17hawke \
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model

## Docker
docker run -i -dp {windows_port(HOST)}:{container_port} {image}