![](./notebooks/img/ANDO-manga-manhwa-manhua.png)

# Proyecto de Machine Learning - EDA (Exploratory Data Analysis)

Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre el cómic asiático en la comunidad fansub hispanohablante y aplicar técnicas de Machine Learning para obtener información y conocimientos relevantes.

## Descripción del proyecto

El objetivo principal de este proyecto es analizar y explorar diferentes aspectos del cómic asiático, como los géneros, demografías, opiniones de la comunidad y evolución a lo largo del tiempo. Además, se implementarán varios modelos de Machine Learning para predecir variables de interés basadas en los datos recopilados. El proyecto consta de las siguientes etapas:

1. **Obtención de datos**: Se recopilaron datos utilizando técnicas de web scraping de la página [TuMangaOnline](https://lectortmo.com/) utilizando las bibliotecas Selenium y BeautifulSoup. Los datos obtenidos se almacenaron en la carpeta `data/raw`.

2. **Procesamiento y limpieza de datos**: Se llevó a cabo un proceso de limpieza y transformación de los datos obtenidos para eliminar duplicados, realizar el feature engineering y preparar los datos para su posterior análisis. Los datos procesados se guardaron en la carpeta `data/processed`.

3. **Análisis exploratorio de datos**: Se utilizó Python y diversas técnicas de análisis exploratorio de datos para examinar los datos obtenidos. Se realizaron gráficas y visualizaciones para representar la información de manera clara y comprensible. Se exploraron aspectos como la puntuación, valoraciones, géneros, demografías y subidas de capítulos. El análisis exploratorio se encuentra en el archivo Jupyter Notebook `notebooks/01_EDA.ipynb`.

4. **Entrenamiento de modelos de Machine Learning**: Se implementaron varios modelos de Machine Learning para predecir variables de interés basadas en los datos recopilados. Los modelos utilizados fueron RandomForestRegressor, LinearRegression con PolynomialFeatures y ElasticNet. Se realizaron los procesos de entrenamiento y validación de los modelos, y se guardaron los modelos entrenados y los conjuntos de datos de entrenamiento y prueba en la carpeta `models`.

5. **Evaluación de los modelos**: Se evaluaron los modelos utilizando métricas de evaluación adecuadas y se realizaron análisis e interpretaciones de las variables más relevantes. El proceso de evaluación de los modelos se encuentra en el archivo Jupyter Notebook `notebooks/03_Entrenamiento_Modelo.ipynb`.

## Estructura del proyecto

El proyecto se organiza en las siguientes carpetas y archivos:

- `data/`: Contiene los datos utilizados en el proyecto.
  - `raw/`: Contiene los datos en su formato original, sin procesar.
  - `processed/`: Almacena los datos procesados después de realizar las transformaciones necesarias.
  - `train/`: Contiene los datos de entrenamiento utilizados para entrenar los modelos.
  - `test/`: Almacena los datos de prueba utilizados para evaluar los modelos.

- `notebooks/`: Contiene los archivos Jupyter Notebook utilizados en cada etapa del proyecto, desde el análisis exploratorio de datos hasta el entrenamiento y evaluación de los modelos. Los notebooks se nombran y numeran adecuadamente según el orden de ejecución.



  - `01_EDA.ipynb`: Análisis exploratorio de datos.
  - `02_Preprocesamiento.ipynb`: Transformaciones y limpiezas, incluyendo el feature engineering.
  - `03_Entrenamiento_Modelo.ipynb`: Entrenamiento de modelos (RandomForestRegressor, LinearRegression con PolynomialFeatures y ElasticNet) junto con su hiperparametrización.
  - `04_Evaluacion_Modelo.ipynb`: Evaluación de los modelos (métricas de evaluación, interpretación de variables, etc.).

- `src/`: Contiene los archivos fuente de Python que implementan las funcionalidades clave del proyecto.
  - `data_processing.py`: Código para procesar los datos de la carpeta `data/raw` y guardar los datos procesados en la carpeta `data/processed`.
  - `model.py`: Código para entrenar y guardar los modelos entrenados utilizando los datos de la carpeta `data/processed`. También se guardan los conjuntos de datos de entrenamiento y prueba utilizados en el entrenamiento.
  - `evaluation.py`: Código para evaluar los modelos utilizando los datos de prueba de la carpeta `data/test` y generar métricas de evaluación.

- `models/`: Contiene los archivos relacionados con los modelos entrenados.
  - `trained_model.pkl`: Modelo entrenado guardado en formato pickle.
  - `model_config.yaml`: Archivo con la configuración del modelo (parámetros).

- `app/`: Contiene los archivos necesarios para el despliegue del modelo en Streamlit u otra plataforma similar.
  - `app.py`: Código para la aplicación web que utiliza el modelo entrenado (Streamlit, etc.).
  - `requirements.txt`: Especifica las dependencias del proyecto para poder ejecutar la aplicación.

- `docs/`: Contiene la documentación adicional relacionada con el proyecto, como las presentaciones u otros documentos relevantes.

- `README.md`: Portada del proyecto.

## Requisitos del sistema

- Python 3.x
- Bibliotecas de Python: Pandas, NumPy, Matplotlib, Scikit-learn, entre otras. Puedes instalar todas las bibliotecas necesarias ejecutando el siguiente comando: `pip install -r requirements.txt`.

## Instrucciones de uso

1. Clona este repositorio en tu máquina local utilizando el siguiente comando: `git clone [URL del repositorio]`.
2. Instala las bibliotecas de Python necesarias ejecutando el siguiente comando: `pip install -r requirements.txt`.
3. Ejecuta los notebooks Jupyter en el orden adecuado para reproducir los pasos del proyecto.
4. Utiliza los scripts en la carpeta `src` para procesar los datos, entrenar los modelos y evaluar su rendimiento.
5. Para desplegar la aplicación web con el modelo entrenado, ejecuta el archivo `app.py` en la carpeta `app`.


by ChatGPT
 
