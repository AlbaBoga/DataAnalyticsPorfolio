# **Titanic**

### Contenido

* Programación en `Python`.
* Análisis de los datos pertenecientes a los pasajeros del Titanic.
* Preprocesamiento de los datos, buscando valores nulos, valores duplicados y limpieza de columnas pertinentes.
* Utilización de un ``modelo KNN`` para predicción de las edades de los pasajeros faltantes.
* Utilización de la librería `plotly` para la visualización de los datos.
* Implementación de modelos de Machine Learning para clasificación y regresión.
* Uso de modelo Gradient Boosting Classifier a través de la librería Pycaret para predicción de supervivencia.
* Uso de modelo Gradient Boosting Classifier a través de la librería Scikit-Learn y estimación de parámetros óptimos a partir de Wandb para predicción de supervivencia.
* Implementación de modelo Gradient Boosting Regressor a través de la librería Pycaret para predicción de precio de billete.
* Implementación de modelo Neural Network a través de la librería Scikit-Learn para predicción de precio de billete.
* Conclusiones de los datos.
* Utilización de la herramienta `Streamlit` para la visualización y explicación de los datos.
* [Enlace a la aplicación](https://alba-app-titanic.streamlit.app/)

## *Índice*

* Importación de librerías
* Primer vistazo a los datos
* Búsqueda de valores duplicados
* Búsqueda de valores nulos
    - Relleno valores nulos en columna `Cabin`
    - Relleno valores nulos en columna `Embarked`
    - Relleno valores nulos en columna `Age, (regresión KNN)` 
    - Comprobación
* Limpieza de columnas
    - Observación preliminar de los datos
    - Tratamiento columna `Age`
    - Tratamiento columna `Sex`
    - Tratamiento columna `Name`
    - Tratamiento dataframe
* Observaciones
    - Observaciones preliminares de los datos numéricos
    - Distribución de la edad dentro del barco
    - Distribución del precio del billete
    - Porcentaje de pasajeros según la clase
    - Distribución por precio del billete, clase y nivel del barco
    - Pasajeros que embarcaron según el género
    - Número de pasajeros en función de su edad
    - Proporción de pasajeros según su título
    - Fallecidos vs Supervivientes
    - Pasajeros que viajaron solos vs acompañados
    - Correlaciones entre variables
