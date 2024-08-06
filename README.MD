# Company Data Analysis

Este proyecto analiza datos de empleados de una compañía utilizando Python, pandas y matplotlib. Genera estadísticas descriptivas, correlaciones y visualizaciones gráficas.

## Requisitos

- Python 3.6 o superior
- pip

## Configuración del Entorno Virtual

Para mantener las dependencias del proyecto organizadas, se recomienda utilizar un entorno virtual.

1. Crea un entorno virtual:

```
python -m venv myenv
```

2. Activa el entorno virtual:

   - En Windows:

   ```
   myenv\Scripts\activate
   ```

   - En macOS/Linux:

   ```
   source myenv/bin/activate
   ```

## Instalación de Dependencias

Con el entorno virtual activado, instala las dependencias necesarias utilizando `pip`:

```
pip install pandas matplotlib mysqlclient
```

## Ejecución del Script

1. Asegúrate de tener un archivo CSV llamado `companydata.csv` en el mismo directorio que el script.

2. Ejecuta el script principal:

```
python main.py
```

## Descripción del Script

El script realiza las siguientes acciones:

1. Abre y lee los datos del archivo `companydata.csv`.
2. Conecta a una base de datos MySQL (aunque no realiza ninguna operación con la base de datos en este ejemplo).
3. Calcula estadísticas descriptivas para las columnas `performance_score` y `salary`.
4. Agrupa los datos por `department` y cuenta el número de empleados en cada departamento.
5. Calcula las correlaciones entre `years_with_company` y `performance_score`, y entre `salary` y `performance_score`.
6. Genera histogramas de `performance_score` para cada departamento.
7. Genera gráficos de dispersión de `years_with_company` vs. `performance_score` y de `salary` vs. `performance_score`.

## Visualizaciones Generadas

- Histogramas de `performance_score` para cada departamento.
- Gráfico de dispersión de `years_with_company` vs. `performance_score`.
- Gráfico de dispersión de `salary` vs. `performance_score`.