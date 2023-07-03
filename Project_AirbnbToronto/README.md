# Proyecto Airbnb Toronto

## Contenido

* Programación en `Python`.
* Análisis de los datos pertenecientes a las ofertas de Airbnb Toronto, obtenido de la web [Inside Airbnb](http://insideairbnb.com/toronto)
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Utilización de la librería `plotly y folium` para la visualización de los datos.
* Uso de la librería `pycaret` y el modelo de regresión `huber` para la creación de un predictor que permita estimar el precio de futuras ofertas.
* Uso de la herramienta `Power BI` para crear un panel que permita resumir los datos más importantes.
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://airbnbtoronto.streamlit.app/)

## Preprocesamiento

* No se encontraron valores duplicados.
* No se encontraron valores nulos dentro de los datos a analizar.
* Se encontraron valores nulos en las reviews, pero como no todo el mundo deja reviews y para trabajar con datos reales, no se hizo ningún tipo de tratamiento.
* Las ofertas estaban distribuidas en 140 barrios diferentes, por lo que se agruparon en zonas para facilitar la visualización de resultados.

## Análisis de los datos

* Se utilizó la librería `plotly` para visualizar resultados.
* Se utilizó la librería `folium` para situar y visualizar en un mapa la situación de las ofertas.
* En `análisis de ofertas` se estudiaron las diferentes ofertas existentes por zona, barrio, por tipo de habitación, propiedad y por número máximo de personas.
* En `regulaciones del gobierno` se estudiaron los posibles infringimientos en base a las normas establecidas por el gobierno de Toronto.
* En `evaluación de turismo` se analiza el precio de las ofertas, las reseñas y la atención de los anfitriones, por zonas, para dos acompañantes, que son las ofertas mayoritarias.
* Se utiliza `NPS` (Net Promoter Score) para evaluar la satisfacción de los clientes.

## Predictor

* [Enlace al predictor de ofertas](https://predictorairbnb.streamlit.app/)
* Se utiliza la librería `pycaret` y los modelos de regresión para estimar cuál ofrece la mejor predicción del precio diario de las ofertas.
* Se utiliza el modelo de regresión `huber` y se implementa el modelo.
* Se utilizan como parámetros el tipo de habitación, el número de personas, el número de noches mínimas, la disponibilidad de la oferta con un año de antelación, el tipo de alquiler, si tiene licencia disponible, la zona y el barrio.

## Resumen de los datos

* [Enlace al dashboard](https://airbnbtoronto.streamlit.app/Conclusiones)
* [Enlace al archivo de Power BI](https://github.com/AlbaBoga/DataAnalyticsPorfolio/blob/main/Project_AirbnbToronto/AIRBNBTORONTO.pbix)
* Se utiliza `Power BI` para resumir los datos más relevantes.
* Se muestra:
  * Número de anfitriones.
  * Media de precio diario y media de huéspedes dependiendo de la zona y el barrio.
  * Número de ofertas por zona y barrio.
  * Media de noches mínimas requeridas por las ofertas, dividido por zona y barrio.
  * Los diferentes tipos de habitaciones en los que se clasifican las ofertas.
