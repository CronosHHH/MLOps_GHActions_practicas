Para implementar automáticamente:

Empaquetar y registrar el modelo

Guardar la salida del modelo y registrarlo en el área de trabajo.
- Especificar si es MLflow o modelo personalizado.
- Con MLflow → implementación sin código.
- Habilitar registro automático con mlflow.autolog().
- El modelo se almacena en la salida del trabajo o en un almacén de datos de Azure ML.
- Crear un punto de conexión e implementar el modelo

El endpoint es una URL HTTPS a la que la app web envía datos y recibe predicciones.
- El endpoint permanece igual aunque se actualice el modelo → la app web no necesita cambios.
- Usar la CLI de Azure ML (v2) para crear y desplegar.
- Probar el modelo implementado

Probar antes de integrar el endpoint con la app web o de migrar todo el tráfico.
- Se puede probar manualmente o automatizar la prueba con Acciones de GitHub.
- Asegurar que las pruebas solo se ejecuten cuando el despliegue se haya completado correctamente (puede tardar).