mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root http://model:5005/artifacts \
    --host 0.0.0.0