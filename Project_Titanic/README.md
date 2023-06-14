# **Titanic**

Buenas tardes, hoy vamos a realizar un estudio de un conjunto de datos pertenecientes a registros de pasajeros dentro del Titanic.

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

    Info: https://www.noaa.gov/gc-international-section/rms-titanic-history-and-significance#:~:text=The%20sinking%20of%20Titanic%20was,to%20improve%20safety%20of%20navigation%20.
    
    ## Primer vistazo
    
Se ha buscado información para entender a qué corresponde cada columna en las siguientes páginas:
* `URL`: https://github.com/awesomedata/awesome-public-datasets/issues/351
* `URL`: https://www.kaggle.com/c/titanic/data

Se nos presenta un dataset que contiene 891 filas y 12 columnas, siete de ellas son columnas con datos numéricos y, el resto, son columnas con dato objeto, o categóricas. Tras observar los datos que presentaban las columnas, se ha buscado información para poder entender bién a qué corresponde cada columna dentro de los datos.
* `PassengerId`: contine un identificador numérico para cada pasajero.
* `Survived`: Si hay un 0 es que no sobrevivieron y 1 es que sí.
* `Pclass`: La clase con la que viajaban los pasajeros. 1: 1ra clase, 2: 2nd clase y 3: 3ra clase.
* `Name`: El nombre de los pasajeros.
* `Sex`: El género de los pasajeros. Male: Masculino y Female: Femenino.
* `Age`: La edad de los pasajeros.
* `SibSp`: El número de hermanos o cónyuges a bordo.
* `Parch`: El número de padres o hijos a bordo.
* `Ticket`: El número de ticket del pasajero.
* `Fare`: La cuota que pagó el pasajero.
* `Cabin`: El número de cabina, si existe.
* `Embarked`: El puerto de embarcación. C: Cherbourg, Q: Queenstown y S: Southampton.

## Busco valores duplicados

Se ha comprobado que no existen duplicados dentro del conjunto de datos.

## Busco valores nulos

En los datos se observa que sólo hay tres columnas con valores nulos. En la columna ``Age`` tenemos un 19.87% de datos nulos, en la columna ``Cabin``, el porcentaje es de 77.1% y, finalmente, la columna ``Embarked`` tiene un 0.22%. A continuación, se procederá a tratar estos datos para evitar errores en posibles futuros cálculos o consideraciones. 
* Columna `Age`: Se ha hecho uso de la información proporcionada por la web rankia para determinar qué método sería el más adecuado para abordar el problema. Para rellenar aquellos valores nulos dentro de la columna primero se va a utilizar un histograma que ayudará a visaulizar si existe una distribución normal en los datos, de manera que si es afirmativo se usará la media de todos los datos y en caso de que la distribución de los datos sea sesgada, se utilizará la mediana.
* Columna `Cabin`: Tras las observaciones preliminares, se ha concluido que, en su mayoría, los camarotes sólo están asignados a los pasajeros de primera clase, no obstante, el resto de pasajeros también se alojaban en diferentes niveles del barco ya que era un viaje de larga duración. Para ello se ha hecho uso de la diferente información presente en wikipedia sobre las intalaciones del barco, para entender cómo estaban distribuidos los pasajeros y ser capaz de encontrar la moda en las variables según la clase, ya que con casi un 80% de valores nulos, sería imposible asignar un valor coherente mediante la información presente en el dataset.
* Columna `Embarked`: Para esta columna, ya que hay un porcentaje muy pequeño de datos nulos y dado que con seguridad los pasajeros han tenido que embarcar desde uno de los tres puertos disponibles, se va a hacer uso de la moda para asignar a esos valores el puerto de embarque más común entre pasajeros.

Info: https://www.rankia.com/diccionario/fondos-inversion/skewness

Info: https://es.wikipedia.org/wiki/Instalaciones_de_primera_clase_del_RMS_Titanic

Info: https://es.wikipedia.org/wiki/Instalaciones_de_segunda_y_tercera_clase_del_RMS_Titanic#:~:text=Cabe%20comentar%20que%20en%20su,lo%20que%20los%20pasajeros%20pudieron

Info: https://es.wikipedia.org/wiki/Hundimiento_del_RMS_Titanic

#### Relleno valores nulos en Cabina a partir de la moda

Primero, se ha determinado que había 40 pasajeros de primera clase que no tenían camarote asignado, por ello, para abordar el problema, primero he observado los datos dentro de `Cabin`, descubriendo que estaba compuesto por una letra y números, después se ha creado una nueva columna, llamada `Level`, donde separo el nivel (la letra), del número de cabina, y finalmente, se hace la moda para asignar la cabina más común a los pasajeros de primera clase con datos faltantes. 

Seguidamente, para el caso de los pasajeros de segunda y tercera clase, se ha hecho uso de wikipedia para averiguar donde estaban la mayoría de pasajeros durante el viaje. En el caso de la segunda clase, la mayoría eran alojados en el nivel `E`, por lo que se ha tomado como la moda y se ha asignado a todas las variables faltantes. En el caso de los pasajeros de tercera clase, la mayoría eran alojados junto a los motores, por lo que se ha asignado el nivel `G` para designar el nivel donde se encontrarían durante el viaje.

Las tres modas obtenidas fueron los niveles `C`, `E` y `G`, para primera clase, segunda clase y tercera clase, respectivamente. De esta forma, evitamos tener que eliminar una columna de la cuál podríamos sacar información en un futuro, ya que con un porcentaje de casi el 80%, sin ningún tipo de información externa, no sería posible obtener los datos necesarios para establecer la moda de los niveles a partir de las clases.

#### Relleno valores nulos en Embarcación a partir de la moda

En la computación de los porcentajes de valores nulos, se obtuvo un 0.22% para esta columna. Por ello, se considera un valor muy bajo en comaparicón con el total de los datos, así que la asignación de la moda a las variables faltantes se consideraría óptimo, ya que no se espera que tenga un efecto desmesurado en la distribución de los valores según el puerto de embarque. Para este caso, se obtuvo que la moda, el puerto más común de embarque entre pasajeros, era ``Southampton``, el cuál se asignó a los faltantes.

#### Predicción de la Edad a partir de la media y algoritmo KNN

En el caso de la columna ``'Age'``, se ha determinado a través del coeficiente de Fisher-Pearson que la distribución es aproximadamente simétrica, con un valor de 0.4, por lo que se podría usar la media para rellenar aquellos valores nulos.

El porcentaje de valores nulos obtenido era de aproximadamente el 20%. Esto quiere decir que nos faltan valores para la columna edad de casi un cuarto de la población, por lo que al utilizar la media, los valores de la edad de los pasajeros van a dejar de estár repartidos a lo largo del rango de edades y se van a centrar en ella, no conservando así la distribución original. Dado que la columna no puede ser eliminada ya que los datos de las edades de los pasajeros continen información de gran interés, a la hora de realizar los análisis y que en la gráfica de distribución de edades se observa un número de población considerable en los extremos, que va desde los cero años de edad hasta los ochenta años de edad, se ha determinado que usar un método predictivo podría ayudar a conservar la distribución original, repartiendo las edades de una forma más uniforme y evitando la asignación de valores erróneos a los pasajeros. Es por ello que se ha dedicido implementar el algorítmo de K Nearest Neighbours, para poder aproximar de una manera más precisa el mayor número de datos. 

Para su implementación, se siguen los siguientes pasos:
* Normalizamos la columna `Fare` para centrar su media en cero y su desviación estándar en 1, de manera que no pueda introducir datos erróneos.
* Se hace uso de la función ``OneHotEncoder`` en las columnas ``Survived``, ``Pclass``, ``SibSp``, ``Parch``, ``Fare`` y ``Embarked``. Esta función crea categorías en base a los valores únicos dentro de las columnas y determina la presencia de dichas categorías dentro de los datos mediante un codificado binario.
* A partir de los datos codificados se crean dos dataframe distintos, uno que va a guardar los datos que no contienen valores nulos en la edad y otro, donde se van a guardar todas aquellas filas que tenían valores nulos en esa columna.
* Seguidamente, se hace un entrenamiento del modelo, en el que el 80% de los datos dentro del dataframe con las edades no nulas es usado para predecir el 20% restante.
* Una vez se ha entrenado el conjunto de datos, se procede a determinar el número de vecinos, es decir el número de conjunto de datos necesarios para ser capaces de aproximar los valores nulos. Para ello se hace uso del error cuadrático medio, que nos proporciona la media del error que hay entre los datos reales y los estimados.
* En la gráfica se puede observar que el número de vecinos que produce el menor error cuadrático medio es 3, por lo que ese es el valor que se usará para predecir los valores de las edades.
* Finalmente, una vez entrenados los datos, se utilizan para predecir las edades dentro del dataframe creado atneriormente con sólo las filas que contenían los datos faltantes y se procede a sustituir esos valores nulos por los valores predichos dentro del dataframe original.

## Limpieza de columnas

Cambios que se van a realizar en las columnas:
* Columna `Age`: Se va a cambiar el tipo de dato a integer, ya que la edad es una variable discreta.
* Columna `Sex`: Los géneros de los pasajeros están escritos en minúscula, por lo que se va a poner la primera letra en mayúsculas.
* Columna `Name`: Se ha decidido separar el nombre en dos columnas, una que contiene los nombres completos de casados o solteros de los pasajeros, y otro que contiene los nombres de pila de aquellas mujeres casadas, de manera que se facilita la visualización. Una de las columnas ha pasado a llamarse `MarriedName` y la otra `FullName`.
* Columna `Level`: Se van a limpiar los datos para que sólo aparezca un valor ya que en muchos, se repite el mismo nivel.
* Finalmente, como se han creado columnas nuevas, se han reorganizado las mismas para facilitar la visualización.

## Observaciones en los datos

#### Observaciones preliminares de los datos numéricos

Se utiliza la función ``.describe()`` en los datos numéricos del dataset para ver el número total de datos, la media, la desviación estándar, el máximo, el mínimo y los cuartiles.

De estos datos se observa que la edad mínima es 0 años, indicando la presencia de recién nacidos dentro del barco. La edad máxima era de 80 años, lo cuál nos dice que había personas de todas las edades a bordo. Y, por último, la mediana es de 28 años y la media es de casi 30 años, por lo que la cercanía entre ambas indicaría simetría en la distribución de los datos de edad.

En esta tabla también podemos extraer información relevante de la columna Fare, en la cuál se puede observar una diferencia muy grande entre la mediana, la media y el valor máximo pagado por billete. Esta distribución desigual de los datos indica que los pasajeros de primera clase pagaron una cantidad muy alta en comparación con el resto de pasajeros, lo cuál también puede suponer la presencia de valores atípicos dentro de la distribución.

#### Distribución de la edad dentro del barco

Procedimiento:
* Primero, se ha realizado un histograma que refleja el número de pasajeros en función de la edad.
* En la siguiente gráfica, se ha obtenido el número de personas por edad, divididas según la clase, grácias a una gráfica de dispersión.
* Para determinar datos de interés entre las diferentes clases y la esperanza de vida de la época, se ha hecho uso de páginas externas que han permitido una mejor comprensión de los datos.

En la gráfica se puede ver que el mayor número de pasajeros se encuentran entre las edades que van de 18 a 35 años, siendo las edades más comunes entre pasajeros las que van de 24 a 25 años. Si se compara esta gráfica con la obtenida en el apartado de valores nulos, veremos que se ha conseguido mantener la distribución de edades en su mayoría, sin cambios significativos. Debido a que el porcentaje de valores nulos era casi del 20%, se previó que iba a tener un impacto considerable sobre la distribución de los datos, por lo que se optó por el algoritmo KNN, lo cuál permitiría encontrar relaciones entre los datos y obtener unas edades más ajustadas, impactando lo menos posible dicha distribución.
Seguidamente, se observa la distribución de las edades por clase dentro del barco. Se puede ver que la mayoría de pasajeros entre 19 y 38 años pertenecían a tercera clase. Si nos fijamos en los extremos, la mayoría de niños e infantes pertenecían a la tercera clase, mientras que por encima de 42 años, hay un mayor número de pasajeros en primera clase. Por otro lado, los pasajeros de segunda clase se distribuyen de una forma más uniforme a lo largo del rango de edades.

La esperanza de vida en Inglaterra alrededor de 1912 estaba situada en 52 años para los hombres y 55 años para las mujeres, esto puede implicar, en apoyo de los datos mostrados en la gráfica que la vida pausada de la gente de clase alta de la época les permitían vivir muchos más años y tener mucha más actividad de ocio, en comparación con la gente de clase baja, expuesta a más enfermedades, trabajos laboriosos y que viajaban por necesidad, ya sea por encontrar una vida mejor o por la búsqueda de un trabajo.

Info: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/articles/howhaslifeexpectancychangedovertime/2015-09-09

Info: https://localhistories.org/life-in-1912/

#### Distribución del precio del billete

Procedimiento:
* En la gráfica se ha realizado un histograma que refleja el precio del billete y cuántas personas pagaron por él.

En la gráfica se puede ver que la mayoría de pasajeros pagaron entre 5 y 15 libras por billete, lo cuál asocia este precio a los pasajeros de tercera clase, mientras que aquellos pasajeros en primera clase, cuyo porcentaje será menor, pagarían precios mucho más altos en función del nivel de camarote en el que se encontrasen, dando lugar a valores que pueden ser reconocidos como valores atípicos, como en el caso del valor máximo.

#### Porcentaje de pasajeros según la clase

Procedimiento:
* Se ha utilizado un gráfico circular para ver el porcentaje de pasajeros dentro de cada clase.

En esta gráfica se confirma que la mayoría de pasajeros estaban alojados en tercera clase, lo cuál explica por qué la distribución del precio de los billetes está sesgada hacia precios más bajos. Por otro lado, se puede apreciar que hay casi un 4% más de pasajeros en primera clase que en segunda clase, lo cuál se puede asociar a la libertad que tenía la clase alta, gracias a su economía, para realizar viajes de ocio, en comparación con la clase media.

#### Distribución por precio del billete, clase y nivel del barco

Procedimiento:
* Se han dividido los precios del billete en 10 grupos de precio.
* Estos se han utilizado para agrupar la clase de los pasajeros y los niveles en función de los mismos, obteniendo una tabla y sólo visualizando aquellos donde el número de pasajeros es mayor que cero.
* A través de un procedimiento de WebScrapping se ha conseguido una tabla donde se listan los diferentes camarotes de lujo dentro del barco.
* Se ha utilizado una web externa para entender mejor la distribución de los camarotes por clases y por niveles dentro del barco.

En la tabla se puede comprobar que los niveles que alojaban más gente eran los niveles ``C``, ``E`` y ``G``, los cuales se tomaron como la moda en apartados anteriores, lo cuál también ha influído en la distribución de pasajeros por niveles. Los precios más altos estaban reservados para los niveles ``C`` y ``B``, donde se encontraban las cabinas más lujosas del barco, listadas en la tabla dataframe_camarotes. Para los demás niveles, los rangos de precios varían e,igualmente, el número de personas que pagaron por ellos. Se observa que diferentes niveles estaban están también en diferentes clases, lo cuál se debe a que según el nivel, también podías encontrar habitaciones de primera, segunda o tercera clase. Para primera clase, los camarotes iban de los niveles ``A`` a ``E``. Para la segunda clase, los camarotes ofrecidos iban de los niveles ``B`` a ``F``. Mientras que para la tercera clase, sus habitaciones iban de los niveles ``D`` a ``G``. De esta manera, la diferencia de precios que hay entre niveles hace referencia a las diferentes habitaciones que había por clase y por nivel. Finalmente, también se encuentra un valor atípico en los niveles, el nivel ``T``, en el cual sólo hay constancia de que una persona pagó por él y no se han podido encontrar más referencias acerca de él.

Info: https://rmstitanic1912.weebly.com/the-levels-of-the-titanic.html

#### Pasajeros que embarcaron según el género

Procedimiento:
* Se han agrupado los pasajeros por género y se muestran junto al total de pasajeros.
* Se han dividido los pasajeros agrupados por género según la clase.
* Se han dividido los pasajeros agrupados por género según el puerto de embarque.

De las gráficas mostradas se pueden sacar los siguientes datos significativos:
* El ``65%`` de pasajeros eran de género masculino.
* La tercera clase era la que más pasajeros albergaba, con un ``55%`` de la población total.
* Finalmente, el puerto más popular entre los pasajeros era Southampton, desde el cuál embarcaron más del ``72%`` de los pasajeros.

#### Número de pasajeros en función de su edad

Procedimiento:
* Se ha creado una columna nueva que se llama ``Pasajero``.
* Dentro de esa columna van a estar presentes tres variables categóricas: ``Niño``, ``Adulto`` y ``Persona Mayor``.
* El primer rango es para menores de ``18 años``.
* El segundo rango es para pasajeros entre ``18 y 60 años``
* El tercer rango es para pasajeros mayores de ``60 años``.
* Se representa en una gráfica el número de pasajeros que había dentro de esos rangos de edades.

La mayor parte de los pasajeros, es decir, más del ``80%`` se encontraban dentro del rango de edad de entre ``18`` y ``60`` años. Por otro lado, menos del ``15%`` estaban comprendidos dentro del rango de edad de menores de ``18`` años y el resto, eran mayores de ``60`` años.

#### Proporción de pasajeros según su título

Procedimiento:
* Se ha creado una nueva columna llamada `Título`.
* Esta columna recoje los títulos de los pasajeros, presentes en el nombre, justo después del apellido.
* Se ha creado una gráfica donde se representa el número de pasajeros que tenían los títulos encontrados.
* En la segunda gráfica se han distribuído los títulos segun los diferentes niveles del barco.

De las siguientes gráficas se han podido observar los siguientes datos:
* Más de un ``58%`` de los títulos pertenecientes a los pasajeros del barco eran Mr.
* Había un mayor porcentaje de ``mujeres solteras`` en el barco, que poseían el título Miss.
* Algunos de los títulos minoritarios presentes en la gráfica, hacen referencia a gente de ``primera clase``.
* La mayoría de estos títulos minoritarios se alojaban en el nivel `B` y `C`, donde se encontraban las cabinas de lujo del barco.

#### Muertos vs Supervivientes

Procedimiento:
* Se ha creado una nueva columna llamada `Estado`.
* Esta columna contiene variables categóricas que se corresponden con `Fallecido` si en la columna ``Survived`` hay un 0 y ``Sobrevivió``, si hay un 1.
* Se ha representado el porcentaje de pasajeros que sobrevivió y falleció en el barco.
* Se ha representado el pocentaje de fallecidos según las diferentes clases dentro del barco.
* Se ha representado el porcentaje de fallecidos según el género de los pasajeros.
* Se ha representado el porcentaje de fallecidos según el rango de edades.

De las siguientes gráficas se ha podido observar los siguientes datos:
* Un ``62%`` de los pasajeros fallecieron.
* Sólo el ``42%`` de ellos pertenecían a tercera clase, mientras que los pasajeros con un ``mayor porcentaje de superviviencia`` eran de primera clase.
* Un ``52%`` de pasajeros fallecidos con respecto al total eran hombres, mientras que el ``mayor porcentaje de supervivencia`` correspondió a las mujeres.
* Dentro del rango de mayores de 60, fallecieron ``19 personas`` de 26 pasajeros en total..
* Más de un ``6% de los fallecidos`` estaban dentro del rango de edad de menores de 18 años, lo cuál equivale a 54 pasajeros de 121 pasajeros considerados en ese rango.

#### Pasajeros que viajaron solos vs acompañados

Procedimiento:
* Se ha creado una columna nueva llamada `Acompañamiento`, para determinar si los pasajeros viajaban o no con familia.
* Si `SibSp` y `Parch` es cero, se ha determinado que los pasajeros viajaban solos, mientras que si alguna de esas variables eran mayores que cero, viajaban con familia.
* Se ha representado el porcentaje de pasajeros en función de si viajaban solos o no.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por aquellos que fallecieron o sobrevivieron.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por género.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por clase.

De las siguientes gráficas se ha podido observar:
* Un ``60%`` de los pasajeros que viajaban en Titanic no estaban acompañados por su familia.
* De ellos, el ``42%`` falleció.
* De los pasajeros que viajaban con familia, la mitad consiguió sobrevivir y la otra falleció.
* Más de la mitad de pasajeros que viajaban en familia eran mujeres.
* Sólo un ``14%`` de las mujeres sobre los pasajeros totales viajaban solas.

#### Correlaciones entre variables

Procedimiento:
* Se han codificado las variables categóricas del DataFrame mediante ``LabelEncoder()``, para obtener las correlaciones entre variables.
* Se ha hecho uso de un mapa de calor para representar dichas correlaciones.

Correlaciones significativas entre variables:
* Hay una correlación significativa de `` 0.95 `` entre la clase de los pasajeros y el nivel del barco donde se alojaban.
* Hay una correlación significativa de `` 0.55 `` entre la clase de los pasajeros, el nivel del barco donde se alojaban y el precio pagado por el billete.
* Hay una correlación significativa de `` 0.55 `` entre el género y la supervivencia de los pasajeros.
* Para el resto de variables parece no haber una relación significativa lineal entre ellas.

## Conclusiones

#### Principales hallazgos

* Gracias a la utilización de fuentes externas, se pudo conservar la columna `Cabin`, para posterior análisis.
* A pesar de la incertidumbre dentro de la columna `Age`, el uso de un modelo predictivo permitió obtener los datos faltantes sin modificar la distribución de las variables.
* Los valores atípicos dentro de la columna `Fare`, que se correspondían con los precios más caros de los billetes, hacían referencia a los pasajeros que se alojaban en los camarotes más lujosos del barco.
* La mayoría de pasajeros en tercera clase eran adultos de entre ``19 y 38 años``, mientras que la mayoría de pasajeros entre ``42 y 80 años``, eran de primera clase, lo cuál hace referencia a la disparidad de recursos entre las clases.
* La mayoría de pasajeros pagaron entre ``5 y 15 libras`` por sus billetes, mientras que lo máximo pagado fue ``512 libras``.
* El ``65%`` de los pasajeros era de género masculino y sólo sobrevivió el ``13%`` de ellos, es decir, ``116 personas de 891 pasajeros``.
* De las mujeres sólo falleció un ``9%``, es decir, ``80 personas de 891 pasajeros``.
* El ``mayor porcentaje de supervivencia`` se correspondía con los pasajeros de género fememnino y la primera clase, mientras que ``el menor``, con la tercera clase y los de género masculino.

#### Posibles aplicaciones

El análisis realizado permite vislumbrar la distribución de pasajeros según su clase económica, lo cuál puede ser de interés a la hora de estudiar los diferentes roles en Inglaterra durante el siglo XX y como éstos impactaron en la supervivencia de ciertos pasajeros.

#### Análisis futuros

De la información obtenida, se observa una clara disparidad entre clases, lo cuál fue clave para la supervivencia de los pasajeros y es un área que se podría seguir estudiando en análisis futuros.
