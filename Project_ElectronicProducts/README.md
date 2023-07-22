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
* [Notebook con el código del análisis realizado](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_ElectronicProducts/Proyecto_Digital.ipynb)

## Preprocesamiento

* Búsqueda de valores duplicados.
* Búsqueda y eliminación de columnas con más de un `20% de datos nulos`.
* Creación de nuevas categorías en tipos de envío, disponibilidad de artículos, estado de productos, categorías, peso, tiendas y fuente de información, para agrupar los valores existentes y hacerlos más legibles.
* Cambio del tipo de dato en las columnas de fechas.
* Reordeno las columnas para que sea más fácil la visualización de los datos y me quedo con sólo aquellas columnas de interés.
* Había un `40% de datos nulos` en la columna tipo de envío por lo que se imputan los valores mediante un `Random Forest Classifier` (librería Scikit-Learn) con `accuracy: 84%`.
* Creo una nueva columna para analizar el precio medio de los artículos visitados.
* Hago que la divisa para todos los precios sea dólares (`USD`).

## Observaciones

* Proporción de artículos visitados en función de:
  * Categorías principales.
  * Tipos den envío.
  * Disponibilidad de artículos.
  * Estado de los artículos.
  * Artículos en rebajas.
* Marcas más populares en función de la categoría principal de cada artículo.
* Tiendas más visitadas.
* Distribución de los precios de los productos en función de las visitas realizadas.
* Distribución de los precios de los productos en función de:
  * Disponibilidad.
  * Estado.
  * Rebajas.
  * Envíos.
  * Tiendas.
* Precio medio de los artículos visitados en cada tienda en función de la fecha.

## A/B Testing y Análisis de Hipótesis

* Uso del `test Shapiro-Wilk` para determinar si la distribución de precios de productos visitados sigue una distribución normal.
* * A/B testing (`test Shapiro-Wilk` y `test U de Mann-Whitney`), para determinar:
  * Si la distribución de precios para aquellos artículos disponibles y los que sólo están disponibles por encargo es la misma.
  * Si los clientes buscan los mismos rangos de precios en artículos nuevos y usados.
  * Si los clientes buscan el mismo rango de precios para artículos rebajados y artículos sin descuento.
  * Si los clientes buscan el mismo rango de precio para envios estándar gratuitos y envíos con un mínimo de compra.
  * Si los clientes buscan el mismo rango de precios en las tiendas más visitadas, que serían Walmart y Bestbuy.
* Análisis de la estacionariedad de los precios de productos visitados mensualmente mediante `test Dickey-Fuller aumentada (ADF)` y `test Kwiatkowski–Phillips–Schmidt–Shin (KPSS)`

## Estudio de Serie Temporal

* Análisis de los precios medios de los productos visitados mensualmente desde 2014 a 2018.
* Imputo aquellos valores nulos con la media.
* Búsqueda de hiperparámetros óptimos para implementar el `modelo ARIMA` en base al menor `RMSE`.
* Hiperparámetros: (p=1, d=0, q=0). Menor RMSE: 191.729 (USD)
* Implemento `modelo Neural Prophet` para la predicción de valores futuros.
* Menor RMSE: 100 (USD), aproximadamente.

## Modelo de Clasificación

* Los datos utilizados son: el precio máximo y mínimo que ha podido tener el artículo, la disponibilidad, el estado, si tiene rebajas, el tipo de envío, categoría principal y categoría secundaria.
* Proporciona una tienda (Walmart, Bestbuy, Bhphotovideo o Ebay) que puede tener productos similares en base a las características que proporciona el cliente.
* Se tienen en cuenta valores atípicos.

### Extreme Gradient Boosting

[Enlace al modelo en Streamlit](https://electronicsmodels.streamlit.app/Pycaret_Extreme_Gradient_Boosting)

* Uso de la librería `pycaret`.
* Accuracy del `79%`.
* Se implementa el modelo en Streamlit.

### Gradient Boosting Classifier

[Enlace al modelo en Streamlit](https://electronicsmodels.streamlit.app/Gradient_Boostring_Classifier)

[Enlace al informe de Wandb](https://wandb.ai/alba-m-boga/project_digital4/reports/Modelo-de-clasificaci-n-de-tiendas--Vmlldzo0ODg2ODg4)

[Enlace a la búsqueda de parámetros mediante Wandb](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_ElectronicProducts/Project_digital_wandb.ipynb)

* Uso de la librería `Scikit-Learn` para determinar el modelo de clasificación que mejor se ajusta a los datos.
* Se utiliza la herramienta `Wandb` a través de una conexión API para la búsqueda de los parámetros más óptimos para implementar el modelo Gradient Boosting Classifier.
* Se obtienen los parámetros que proporcionan un accuracy del `78%` y se implementa el modelo.
* Se implementa el modelo en Streamlit.

### Red Neuronal

[Enlace al modelo en Streamlit](https://electronicsmodels.streamlit.app/Red_Neuronal)

[Enlace al código e implementación del modelo](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_ElectronicProducts/tensorflowdigital_class.ipynb)

* Uso de la librería `TensorFlow` para implementar una Red Neuronal.
* Se obtiene un accuracy final del `72%` y se implementa el modelo.
* Se implementa el modelo en Streamlit.

## Dashboard

[Enlace al dashboard en Streamlit](https://electronics.streamlit.app/Conclusiones)

[Enlace al dashboard en PowerBi](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_ElectronicProducts/productoselectronicos.pbix)

* Resumen de los datos analizados.
* Productos totales visitados.
* Filtrado por tienda, disponibilidad, estado, tipo de envío, descuentos y categorías principales.
* Marcas de los productos visitados en fución de las características.
* Precios de los productos visitados en función de la fecha de visita.

## Logos e imágenes

Logo: [vecteezy.com](https://www.vecteezy.com/)
Imágenes de la cabecera: [canva.com](https://www.canva.com/)
