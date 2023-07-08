# **Titanic**

## Contenido

* Programación en `Python`.
* Análisis de los datos pertenecientes a los pasajeros del Titanic.
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Utilización de un ``modelo KNN`` para predicción de las edades de los pasajeros faltantes.
* Utilización de la librería `plotly` para la visualización de los datos.
* Implementación de modelos de Machine Learning para clasificación y regresión.
* Uso de modelo Gradient Boosting Classifier a través de la librería ``Pycaret`` para predicción de supervivencia.
* Uso de modelo Gradient Boosting Classifier a través de la librería ``Scikit-Learn`` y estimación de parámetros óptimos a partir de Wandb para predicción de supervivencia.
* Implementación de modelo Gradient Boosting Regressor a través de la librería ``Pycaret`` para predicción de precio de billete.
* Implementación de modelo Neural Network a través de la librería ``TensorFlow`` para predicción de precio de billete.
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://alba-app-titanic.streamlit.app/)

## Preprocesamiento

* Búsqueda y eliminación de valores duplicados.
* Búsqueda de valores nulos:
  * Imputación de valores nulos en columna `Cabin` a través de la moda.
  * Imputación de valores nulos en columna `Embarked` a través de la moda.
  * Imputación de valores nulos en columna `Age` a través de regresión mediante K Nearest Neighbours.
* Limpieza de columnas:
  * Observación preliminar de los datos.
  * Tratamiento columna `Age`.
  * Tratamiento columna `Sex`.
  * Tratamiento columna `Name`.
  * Tratamiento dataframe.

## Observaciones

* Observaciones preliminares de los datos numéricos
* Distribución de la edad dentro del barco
* Distribución del precio del billete
* Porcentaje de pasajeros según la clase
* Distribución por precio del billete, clase y nivel del barco
* Pasajeros que embarcaron según el género
* Número de pasajeros en función de su edad
* Proporción de pasajeros según su título
* Fallecidos vs Supervivientes
* Pasajeros que viajaron solos vs acompañados
* Correlaciones entre variables

## Modelo de Clasificación

[Enlace al modelo en Streamlit](https://titanicmodels.streamlit.app/Classification)

[Enlace al informe de Wandb](https://wandb.ai/alba-m-boga/Project_Titanic/reports/Predictor-de-Supervivencia--Vmlldzo0ODA1NTE3)

[Enlace a búsqueda de parámetros mediante Wandb](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_Titanic/Project_Titanic_wandb.ipynb)

* Los datos utilizados son: la clase del pasajero, el sexo, la edad, los acompañantes, el nivel del barco donde se alojaban y el puerto de embarque.
* Se utiliza la librería de `pycaret` y los modelos de clasificación para estimar si dado un pasajero, sobrevivió o no durante el hundimiento del Titanic.
* Se utiliza el modelo de clasificación Gradient Boosting Classifier y se implementa el modelo.
* Se obtiene un accuracy del ``84%``.
* Se utiliza la librería ``Scikit-Learn`` para determinar el modelo de clasificación que mejor se ajusta a los datos.
* También se hace uso de la herramienta ``GridSearchCV`` para la búsqueda de parámetros.
* Se obtiene un accuracy del ``87%`` para los modelos Gradient Boosting Classifier y XGB Classifier.
* Se utiliza la herramienta ``Wandb`` a través de una conexión API para la búsqueda de los parámetros más óptimos para implementar el modelo Gradient Boosting Classifier.
* Se obtienen los parámetros que proporcionan un accuracy del ``89%`` y se implementa el modelo.
* Para Streamlit se ha implementado este último modelo.

## Modelo de Regresión

[Enlace al modelo en Streamlit](https://titanicmodels.streamlit.app/Regression)

[Enlace a la implementación de Neural Network](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_Titanic/tensorflowtitanic_reg.ipynb)

* Los datos utilizados son: la clase del pasajero, el sexo, la edad, los acompañantes, el nivel del barco donde se alojaban y el puerto de embarque.
* Se utiliza la librería de `pycaret` y los modelos de regresión para estimar el precio del billete de los pasajeros.
* Se utiliza el modelo de clasificación Gradient Boosting Regressor y se implementa el modelo.
* Se obtiene un RMSE de ``24.4 (pounds)``.
* Se utiliza la librería ``Scikit-Learn`` para determinar el modelo de regresión que mejor se ajusta a los datos.
* Se obtiene un RMSE de ``16.52 (pounds)`` para el modelo Neural Network, y sólo considerado sólo aquellos valores atípicos cuyo z-score < 4.
* Se implementa un modelo Neural Network a través de la librería ``TensorFlow``, teniendo en cuenta valores atípicos.
* Se obtiene un RMSE final de ``50 (pounds)`` y se implementa el modelo.
* En `Streamlit` se ha implementado el modelo de Pycaret ya que producía el menor error.

