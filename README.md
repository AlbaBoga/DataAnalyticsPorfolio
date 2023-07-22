# Data Analytics Portfolio

Conjunto de proyectos realizados para la demostración de habilidades en Python, MATLAB, SQL, PowerBI, Streamlit y Machine Learning.

### Proyecto Productos de Electrónica y Precios

[Enlace a la sección](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/Project_ElectronicProducts)

* Programación en `Python`
* Análisis de los datos pertenecientes a la base de datos de productos de [Datafiniti](https://www.datafiniti.co/).
* Obtención de la muestra de los datos a través de [data.world](https://data.world/datafiniti/electronic-products-and-pricing-data).
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Implemento un modelo de `Random Forest Classifier` a través de la librería `Scikit-Learn` para imputar los datos faltantes en la columna de tipo de envío.
* Utilización de la librería `plotly` para la visualización de los datos.
* `A/B testing` para determinar si características influyen en el precio de productos.
* Análisis de los precios de los productos visitados mensualmente (`estudio de serie temporal`).
* Implemento `modelo ARIMA` con hiperparámetros óptimos.
* Uso de `modelo Neural Prophet` para la predicción de valores futuros.
* Modelos Machine Learning para clasificación (estimación de tienda en función de las características del producto que busca el cliente):
  * Modelo `Extreme Gradient Boosting` a través de la librería `Pycaret`.
  * Modelo `Gradient Boosting Classifier` a través de la librería `Scikit-Learn` y usando la herramienta `Wandb` para búsqueda de hiperparámetros óptimos.
  * Modelo `Red Neuronal` a través de la librería `TensorFlow`.
* Resumen de los datos analizados mediante un `dashboard en PowerBI`
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://electronics.streamlit.app/)


### Proyecto Titanic

[Enlace a la seccción](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/Project_Titanic)

* Programación en `Python`.
* Análisis de los datos pertenecientes a los pasajeros del Titanic.
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Utilización de un ``modelo KNN`` para predicción de las edades de los pasajeros faltantes.
* Utilización de la librería `plotly` para la visualización de los datos.
* Implementación de modelos de Machine Learning para clasificación y regresión.
* Uso de modelo Gradient Boosting Classifier a través de la librería ``Pycaret`` para predicción de supervivencia.
* Uso de modelo Gradient Boosting Classifier a través de la librería ``Scikit-Learn`` y estimación de parámetros óptimos a partir de Wandb para predicción de supervivencia.
* Implementación de modelo Gradient Boosting Regressor a través de la librería ``Pycaret`` para predicción de precio de billete.
* Uso de modelo MLPRegressor a través de la librería `Scikit-Learn` y estimación de parámetros óptimos a partir de Wandb para predicción de precio de billete.
* Implementación de modelo Neural Network a través de la librería ``TensorFlow`` para predicción de precio de billete.
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://alba-app-titanic.streamlit.app/)

### TFG Diseño de estimadores para abaratar la red de sensores de un edifico bioclimático

[Enlace a la seccción](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/TFG_Dise%C3%B1o_estimadores)

* Programación en `MATLAB`.
* Análisis de los datos registrados por los sensores de un edificio bioclimático.
* Definición y estudio de cada una de las variables que influyen en el cálculo del confort térmico de los usuarios.
* Análisis de Sensibilidad para determinar la influencia de las variables en el índice PMV.
* Eliminación de aquellos sensores de poca influencia.
* Determinación de dependencias matemáticas entre variables.
* Uso del `Filtro de Kalman` para la estimación del valor real de dichas variables.
* Optimización económica de la red de sensores tras la implementación del estimador.
* Conclusiones relevantes.

### Proyecto Airbnb Toronto

[Enlace a la sección](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/Project_AirbnbToronto)

* Programación en `Python`.
* Análisis de los datos pertenecientes a las ofertas de Airbnb Toronto, obtenido de la web [Inside Airbnb](http://insideairbnb.com/toronto)
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Utilización de la librería `plotly y folium` para la visualización de los datos.
* Uso de la librería `pycaret` y el modelo de regresión `huber` para la creación de un predictor que permita estimar el precio de futuras ofertas.
* Uso de la herramienta `Power BI` para crear un panel que permita resumir los datos más importantes.
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://airbnbtoronto.streamlit.app/)

### Proyecto Data Science 2023

[Enlace a la seccción](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/Project_DataScienceSalaries2023)

* Programación en `Python`.
* Análisis del conjunto de datos perteneciente a los diferentes empleos en el sector Data Science.
* Preprocesamiento de datos eliminando valores nulos, datos duplicados y agrupación de los diferentes trabajos en categorías.
* Utilización de la librería `plotly` para visualizar resultados.
* Creación de un ``modelo de regresión lineal`` para predecir futuras tendencias.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://alba-app-datascience.streamlit.app/)

### Technical Exercises

[Enlace a la seccción](https://github.com/AlbaBoga/DataAnalyticsPorfolio/tree/main/TechnicalExercises)

Ejercicios prácticos que permiten desarrollar y demostrar habilidades tanto en Python, PowerBI como en SQL.
