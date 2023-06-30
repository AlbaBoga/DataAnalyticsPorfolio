# **Titanic**

[Aplicación en Streamlit](https://alba-app-titanic.streamlit.app/)

Se va a realizar un estudio de un conjunto de datos pertenecientes a registros de pasajeros dentro del Titanic.

En este dataset utilizado durante el análisis se encuentran datos de gran relevancia relacionados con el hundimiento del Titanic. La creación de dicho barco fue de gran importancia en el siglo XX, ya que el trabajo de ingeniería realizado fue muy laborioso y suponía una conexión entre Inglaterra y Nueva York, siendo el barco de pasajeros más grande y lujoso de la historia. El Titanic albergó 2240 personas, entre tripulación y pasajeros, de los cuales murieron 1500. En este dataset, sólo hay constancia de 891 pasajeros, por lo que los diferentes descubrimientos van a ser en base a ellos, lo cuál supone 40% de las personas alojadas dentro del barco, perdiendo el 60% de la información restante. Para complementar la información dentro del dataset, se ha hecho uso de diferentes fuentes externas que han permitido llegar a conclusiones más acertadas en base a los datos obtenidos.

Procedimiento realizado:
- Primero se ha echado un primer vistazo a los datos.
- Seguidamente se ha realizado un trabajo de preprocesamiento de los datos donde se han buscado valores nulos, valores duplicados y, finalmente, se ha hecho una limpieza de las columnas pertinentes.
- Como tercer paso, se ha realizado una observación de los datos a través de diferentes gráficas, tablas y agrupaciones de datos.
- Finalmente, se han resumido las conclusiones más importantes en base a esas observaciones.

## *Índice*

* Importación de librerías
* Primer vistazo a los datos
* Búsqueda de valores duplicados
* Búsqueda de valores nulos
    - Relleno valores nulos en columna `Cabin`
    - Relleno valores nulos en columna `Embarked`
    - Relleno valores nulos en columna `Age`
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
