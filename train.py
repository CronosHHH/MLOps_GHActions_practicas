import os
import argparse
import mlflow
import azure.ai.ml.automl as automl
from azure.ai.ml import MLClient, Input, load_job
from azure.identity import DefaultAzureCredential
from azure.ai.ml.constants import AssetTypes

def main():
    # 1. Configurar la autenticación con Azure ML usando variables de entorno
    mlclient = MLClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
        resource_group_name=os.getenv("AZURE_RESOURCE_GROUP"),
        workspace_name=os.getenv("AZURE_WORKSPACE_NAME")
    )

    print(" Autenticado con éxito en Azure ML Studio")

    # 2. Definir la entrada de datos (referencia al dataset registrado)
    my_training_data_input = Input(
        type=AssetTypes.MLTABLE,
        path="azureml:diabetes-dataset:1"
    )

    # 3. Configurar el experimento de AutoML para clasificación
    job = automl.classification(
        experiment_name="diabetes-automl_future_pipeline",
        training_data=my_training_data_input,
        target_column_name="target",
        compute="cpu-cluster",
        primary_metric="accuracy"
    )

    # Configurar límites del job
    job.set_limits(
        timeout_minutes=60,
        trial_timeout_minutes=20,
        max_trials=5,
        enable_early_termination=True,
    )

    # 4. Lanzar el job en Azure ML
    print("Enviando el job de AutoML a Azure...")
    returned_job = mlclient.jobs.create_or_update(job)
    
    print(f" Job AutoML iniciado: {returned_job.name}")
    print(f"📌 Sigue el progreso en Azure ML Studio → Jobs → {returned_job.name}")
    print(f"📊 Estado actual del job: {returned_job.status}")

if __name__ == "__main__":
    main()