# **Productos de Electrónica y Precios**

## Contenido

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
