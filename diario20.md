### Enunciado

terminado el modelo de clasificacion de diabetes

quieren escalar el proyecto para ello:
vamos a 
- automatizar el PROCESO DE ENTRENAMIENTO & EVALUACIÓN
    - para DISTINTOS SEGMENTOS DE DATOS (población)

para ello usaremos Github Actions.

La automatización:

1. GH actions Desencadena un Entrenamiento en AzureML
    - crear entidad de servicio (nosotros no podemos pq el azure es el de la ugr)
    - almacenaremos credenciales en SECRETOS de GH
    - crear un workflow en GH actions que desencadene el entrenamiento en AzureML


> **En Azure Portal:**
> - Abriste tu Managed Identity: `mi-devops-conexion`
> - Fuiste a **Settings** de la Identidad creada → **Federated credentials**
> - Clickeaste **Add credential** y rellenaste:
>   - Escenario: GitHub Actions
>   - Organización: CronosHHH -> Tu usuario de GitHub
>   - Repositorio: MLOps_GHActions_practicas
>   - Entidad: Rama
>   - Rama: prod

Luego extraímos los valores necesarios de tu Managed Identity: 

AZURE_CLIENT_ID
AZURE_TENANT_ID
AZURE_SUBSCRIPTION_ID
AZURE_RESOURCE_GROUP
AZURE_WORKSPACE_NAME

añadimos AZURE_CLIENT_SECRET si usamos un Service Principal (SP) en lugar de una Managed Identity.

para encontrar el workspace selecciona el recurso (resource group) y busca el nombre del workspace que busques, en mi caso "ml-project-demo".


Creamos 5 secretos en GitHub para almacenar estas credenciales de forma segura.

---

Workflow con pull request (PR):

Creas Rama para trabajar en ella:
```bash
# Te aseguras de estar actualizado y creas una nueva rama
git checkout main
git pull
git checkout -b feature/nuevo-job-azure

# Haces cambios en tu código y creas un commit
git add src/job.yml
git commit -m "feat: añade configuración de entrenamiento para Azure ML"

# Subes la rama a GitHub
git push origin feature/nuevo-job-azure
```

Entras a la web de tu repositorio en GitHub y verás un botón amarillo que dice "Compare & pull request".
Al pulsar en él, configuras la petición:
- Base (Destino): "main" o la rama que quieras que reciba los cambios, en mi caso "prod"
- Compare (Origen): feature/nuevo-job-azure
- Título y descripción: ...

