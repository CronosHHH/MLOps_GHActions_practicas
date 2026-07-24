import argparse
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # 1. Configurar argumentos de entrada
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=False, help="Ruta al dataset si viene de Azure ML")
    parser.add_argument("--n_estimators", type=int, default=100, help="Número de árboles")
    parser.add_argument("--max_depth", type=int, default=6, help="Profundidad máxima")
    args = parser.parse_args()

    # 2. Habilitar autologging de MLflow (Azure ML captura métricas automáticamente)
    mlflow.autolog()

    # 3. Cargar el dataset de Diabetes de sklearn
    print("Cargando el dataset de diabetes...")
    diabetes = load_diabetes(as_frame=True)
    X = diabetes.data
    y = diabetes.target

    # Dividir datos en Train / Test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Entrenar el modelo
    print(f"Entrenando RandomForestRegressor (n_estimators={args.n_estimators}, max_depth={args.max_depth})...")
    model = RandomForestRegressor(
        n_estimators=args.n_estimators, 
        max_depth=args.max_depth, 
        random_state=42
    )
    model.fit(X_train, y_train)

    # 5. Evaluar
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"Resultados -> MSE: {mse:.4f} | R2: {r2:.4f}")

if __name__ == "__main__":
    main()