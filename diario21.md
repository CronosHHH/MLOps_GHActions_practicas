Problema:
en la misma empresa de investigacion de enfermedades, vamos a buscar, en la misma app, tener:
- MAS MODELOS, PARA DISTINTAS ENFERMEDADES

Ademas en el proyecto buscaremos tener:
- **un entorno seguro de experimentación**, donde experimentar con los modelos
- **punto de conexión al que se llamará desde la aplicación web**, para llamar a los modelos que tienen buenos resultados para asegurarnos que se pueden integrar en la app

Los distintos entorno que se usaran al final serán:
- **Desarrollo**, para la experimentación.
- **Ensayo**, para pruebas.
- **Producción**, para implementar el modelo en el punto de conexión de producción.

CADA ENTORNO TENDRÁ UN AREA DE TRABAJO (workspace) DEDICADA
- Mejor control de acceso y seguridad
- rol específico para cada entorno

Para trabajar con entornos, querrá:

- Crear entornos en el repositorio de GitHub.
- Almacenar las credenciales en cada área de trabajo de Azure Machine - - Learning como secreto de entorno en GitHub.
- Agregar revisores necesarios a entornos para la aprobación controlada.
Usar entornos en los flujos de trabajo de Acciones de GitHub.

La arquitectura incluye:

- **Configuración**: cree todos los recursos necesarios de Azure para la solución.
- **Desarrollo de modelos** (bucle interno): explore y procese los datos para entrenar y evaluar el modelo.
- **Integración continua**: empaquetar y registrar el modelo.
- **Implementación de modelos** (bucle externo): implemente el modelo.
- **Implementación continua**: pruebe el modelo y promueva al entorno de producción.
- **Supervisión**: supervise el rendimiento del modelo y del punto de conexión.

- El entorno de desarrollo se usa para el bucle interno:
    - Los científicos de datos entrenan el modelo.
    - El modelo se empaqueta y registra.

- El entorno de ensayo se usa para parte del bucle externo:
    - Pruebe el código y el modelo con linting y pruebas unitarias.
    - Implemente el modelo para probar el punto de conexión.

- El entorno de producción se usa para otra parte del bucle externo:
    - Implemente el modelo en el punto de conexión de producción. El punto de conexión de producción se integra con la aplicación web.
    - Supervise el rendimiento del modelo y del punto de conexión para desencadenar el reentrenamiento cuando sea necesario.

---

Añadir los entornos en el gh
- se crean en environments en setting del repo
- y pones el JSON para AZURE_CREDENTIALS

en el .yaml sera algo asi:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: produccion
      url: https://ml.workspace.azure.com  # opcional
    steps:
      - name: Login to Azure
        uses: azure/login@v2
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      # ...
```



