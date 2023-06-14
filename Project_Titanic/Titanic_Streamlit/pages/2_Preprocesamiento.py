#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from scipy.stats import skew
import re
import requests
from bs4 import BeautifulSoup
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

st.set_page_config(page_title='Preprocesamiento', page_icon='📐', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)

titanic = pd.read_csv(r"E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\datos\titanic.csv")

st.title('Preprocesamiento')

image1 = Image.open(r'E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\img\logo.png')
st.sidebar.image(image1)


#--------------------------------------Valores duplicados-------------------------------------#
st.markdown(
            """
            ## Búsqueda de valores duplicados
        """
        )

code0 = """
duplicates=titanic.duplicated()
num_duplicates=duplicates.sum()
if duplicates.any():
    print("Se han encontrado duplicados en el DataFrame.")
    print('Hay un total de', num_duplicates, 'valores duplicados en el DataFrame.')
else:
    print("No hay duplicados en el DataFrame.")
"""
st.code(code0,language='python')

duplicates=titanic.duplicated()
num_duplicates=duplicates.sum()
if duplicates.any():
    st.write("Se han encontrado duplicados en el DataFrame.")
    st.write('Hay un total de', num_duplicates, 'valores duplicados en el DataFrame.')
else:
    st.write("No hay duplicados en el DataFrame.")
#--------------------------------------Valores duplicados-------------------------------------#


#--------------------------------------Valores Nulos-------------------------------------#
st.markdown(
            """
            ## Búsqueda de valores nulos
        """
        )

code1 = """
for columna in titanic.columns:
    pct_null=(titanic[columna].isnull().sum()*100)/titanic.shape[0]
    if pct_null>float(0):
        print(f'El porcentaje de valores nulos en {columna} es del {round(pct_null,2)}%')
"""
st.code(code1,language='python')

for columna in titanic.columns:
    pct_null=(titanic[columna].isnull().sum()*100)/titanic.shape[0]
    if pct_null>float(0):
        st.write(f'El porcentaje de valores nulos en {columna} es del {round(pct_null,2)}%')

st.markdown(
                """
A continuación, se procederá a tratar estos datos para evitar errores en posibles futuros cálculos o consideraciones. 
* Columna `Age`: Se ha hecho uso de la información proporcionada por la web rankia para determinar qué método sería el más adecuado para abordar el problema. Para rellenar aquellos valores nulos dentro de la columna primero se va a utilizar un histograma que ayudará a visaulizar si existe una distribución normal en los datos, de manera que si es afirmativo se usará la media de todos los datos y en caso de que la distribución de los datos sea sesgada, se utilizará la mediana.
* Columna `Cabin`: Tras las observaciones preliminares, se ha concluido que, en su mayoría, los camarotes sólo están asignados a los pasajeros de primera clase, no obstante, el resto de pasajeros también se alojaban en diferentes niveles del barco ya que era un viaje de larga duración. Para ello se ha hecho uso de la diferente información presente en wikipedia sobre las intalaciones del barco, para entender cómo estaban distribuidos los pasajeros y ser capaz de encontrar la moda en las variables según la clase, ya que con casi un 80% de valores nulos, sería imposible asignar un valor coherente mediante la información presente en el dataset.
* Columna `Embarked`: Para esta columna, ya que hay un porcentaje muy pequeño de datos nulos y dado que con seguridad los pasajeros han tenido que embarcar desde uno de los tres puertos disponibles, se va a hacer uso de la moda para asignar a esos valores el puerto de embarque más común entre pasajeros.

Info: https://www.rankia.com/diccionario/fondos-inversion/skewness

Info: https://es.wikipedia.org/wiki/Instalaciones_de_primera_clase_del_RMS_Titanic

Info: https://es.wikipedia.org/wiki/Instalaciones_de_segunda_y_tercera_clase_del_RMS_Titanic#:~:text=Cabe%20comentar%20que%20en%20su,lo%20que%20los%20pasajeros%20pudieron

Info: https://es.wikipedia.org/wiki/Hundimiento_del_RMS_Titanic
            """
            )

tab1,tab2,tab3=st.tabs(['Camarote','Puerto','Edad'])

with tab1:
    code3 = """
#Creo una nueva columna para obtener la moda, en pasajeros de primera clase
titanic['Level']=titanic['Cabin'].str.replace('[0-9]','',regex=True)
#Obtengo la moda
moda_cabin = titanic['Level'].mode().values[0]
print(f'La moda en pasajeros de primera clase es el nivel {moda_cabin}')
"""
    st.code(code3,language='python')
    titanic['Level']=titanic['Cabin'].str.replace('[0-9]','',regex=True)
    moda_cabin = titanic['Level'].mode().values[0]
    st.write(f'La moda en pasajeros de primera clase es el nivel {moda_cabin}')
    code4 = """
#Asigno la moda en primera clase
titanic.loc[(titanic['Pclass']==1) & (titanic['Cabin'].isnull()),'Cabin']=moda_cabin
titanic.loc[(titanic['Pclass']==1) & (titanic['Cabin']=='C'),'Level']=moda_cabin
#Asigno la moda en segunda clase
titanic.loc[(titanic['Pclass']==2) & (titanic['Cabin'].isnull()),'Cabin']='E'
titanic.loc[(titanic['Pclass']==2) & (titanic['Level'].isnull()),'Level']='E'
#Asigno la moda en tercera clase
titanic.loc[(titanic['Pclass']==3) & (titanic['Cabin'].isnull()),'Cabin']='G'
titanic.loc[(titanic['Pclass']==3) & (titanic['Level'].isnull()),'Level']='G'
"""
    st.code(code4,language='python')
    titanic.loc[(titanic['Pclass']==1) & (titanic['Cabin'].isnull()),'Cabin']=moda_cabin
    titanic.loc[(titanic['Pclass']==1) & (titanic['Cabin']=='C'),'Level']=moda_cabin
    titanic.loc[(titanic['Pclass']==2) & (titanic['Cabin'].isnull()),'Cabin']='E'
    titanic.loc[(titanic['Pclass']==2) & (titanic['Level'].isnull()),'Level']='E'
    titanic.loc[(titanic['Pclass']==3) & (titanic['Cabin'].isnull()),'Cabin']='G'
    titanic.loc[(titanic['Pclass']==3) & (titanic['Level'].isnull()),'Level']='G'
    st.markdown(
        """
Primero, se ha determinado que había 40 pasajeros de primera clase que no tenían camarote asignado, por ello, para abordar el problema, primero he observado los datos dentro de `Cabin`, descubriendo que estaba compuesto por una letra y números, después se ha creado una nueva columna, llamada `Level`, donde separo el nivel (la letra), del número de cabina, y finalmente, se hace la moda para asignar la cabina más común a los pasajeros de primera clase con datos faltantes. 

Seguidamente, para el caso de los pasajeros de segunda y tercera clase, se ha hecho uso de wikipedia para averiguar donde estaban la mayoría de pasajeros durante el viaje. En el caso de la segunda clase, la mayoría eran alojados en el nivel `E`, por lo que se ha tomado como la moda y se ha asignado a todas las variables faltantes. En el caso de los pasajeros de tercera clase, la mayoría eran alojados junto a los motores, por lo que se ha asignado el nivel `G` para designar el nivel donde se encontrarían durante el viaje.

Las tres modas obtenidas fueron los niveles `C`, `E` y `G`, para primera clase, segunda clase y tercera clase, respectivamente. De esta forma, evitamos tener que eliminar una columna de la cuál podríamos sacar información en un futuro, ya que con un porcentaje de casi el 80%, sin ningún tipo de información externa, no sería posible obtener los datos necesarios para establecer la moda de los niveles a partir de las clases.
        """
    )

with tab2:
    code3 = """
moda = titanic['Embarked'].mode().values[0]
titanic['Embarked'].fillna(moda, inplace=True)
print(f'El puerto del cuál más pasajeros han embarcado es {moda}')
"""
    st.code(code3,language='python')
    moda = titanic['Embarked'].mode().values[0]
    titanic['Embarked'].fillna(moda, inplace=True)
    st.write(f'El puerto del cuál más pasajeros han embarcado es {moda}')
    st.markdown(
        """
En la computación de los porcentajes de valores nulos, se obtuvo un 0.22% para esta columna. Por ello, se considera un valor muy bajo en comaparicón con el total de los datos, así que la asignación de la moda a las variables faltantes se consideraría óptimo, ya que no se espera que tenga un efecto desmesurado en la distribución de los valores según el puerto de embarque. Para este caso, se obtuvo que la moda, el puerto más común de embarque entre pasajeros, era ``Southampton``, el cuál se asignó a los faltantes.
        """
    )

with tab3:
    fig=px.histogram(x=titanic['Age'])
    fig.update_layout(height=500, width=500, title_text="Distribución de la Edad", 
                  xaxis=dict(title="Edad"), yaxis=dict(title="Número de pasajeros"), template='plotly_dark')
    st.plotly_chart(fig)
    st.write(f"Valor del coeficiente de Fisher-Pearson sobre la distribución de la columna 'Age': {skew(titanic['Age'],nan_policy='omit')}")
    
    st.markdown(
        """
En el caso de la columna ``'Age'``, se ha determinado a través del coeficiente de Fisher-Pearson que la distribución es aproximadamente simétrica, con un valor de 0.4, por lo que se podría usar la media para rellenar aquellos valores nulos.
"""
    )

    code4 = """
    #Implementación del algoritmo KNN
    #Normalización de Fare
    scaler = StandardScaler()
    titanic['Fare_Normalizado'] = scaler.fit_transform(titanic[['Fare']])

    # estas son las columnas que quieres como predictores para tu modelo
    columnas=['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare_Normalizado', 'Embarked',"Age"]
    # Aplicamos OneHotEncoder para codificar nuestras variables categóricas 
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    titanic_encoded = pd.DataFrame(encoder.fit_transform(titanic[columnas]))
    titanic_encoded.columns = encoder.get_feature_names_out(columnas)

    # Creamos dos dataframes basados en la presencia de Age
    titanic_encoded['Age'] = titanic['Age']
    titanic_with_age = titanic_encoded.dropna(subset=['Age']) 
    titanic_without_age = titanic_encoded[titanic_encoded['Age'].isna()].drop(columns='Age')
    
    # Dividimos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
    X_train, X_test, y_train, y_test = train_test_split(titanic_with_age.drop(columns='Age'), titanic_with_age['Age'], test_size=0.2, random_state=357)

    # Lista para almacenar los valores de MSE (Error Cuadrático Medio)
    mse = []

    # Rango de k para probar
    k_range = range(1, 7)

    for k in k_range:
        knn = KNeighborsRegressor(n_neighbors=k)

        # Realizamos la validación cruzada para obtener una medida más robusta del error
        scores = -cross_val_score(knn, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
        mse.append(scores.mean())
        print(f'scores = {scores}')
"""
    st.code(code4,language='python')

    #Normalización de Fare
    scaler = StandardScaler()
    titanic['Fare_Normalizado'] = scaler.fit_transform(titanic[['Fare']])

    # estas son las columnas que quieres como predictores para tu modelo
    columnas=['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare_Normalizado', 'Embarked',"Age"]
    # Aplicamos OneHotEncoder para codificar nuestras variables categóricas 
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    titanic_encoded = pd.DataFrame(encoder.fit_transform(titanic[columnas]))
    titanic_encoded.columns = encoder.get_feature_names_out(columnas)

    # Creamos dos dataframes basados en la presencia de Age
    titanic_encoded['Age'] = titanic['Age']
    titanic_with_age = titanic_encoded.dropna(subset=['Age']) 
    titanic_without_age = titanic_encoded[titanic_encoded['Age'].isna()].drop(columns='Age')
    
    # Dividimos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
    X_train, X_test, y_train, y_test = train_test_split(titanic_with_age.drop(columns='Age'), titanic_with_age['Age'], test_size=0.2, random_state=357)

    # Lista para almacenar los valores de MSE (Error Cuadrático Medio)
    mse = []

    # Rango de k para probar
    k_range = range(1, 7)

    st.write('Resultados del error cuadrático medio:')
    for k in k_range:
        knn = KNeighborsRegressor(n_neighbors=k)

        # Realizamos la validación cruzada para obtener una medida más robusta del error
        scores = -cross_val_score(knn, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
        mse.append(scores.mean())
        st.write(f'scores = {scores}')
        
    
    # Graficamos los valores 
    fig1 = px.line(x=k_range, y=mse, template="plotly_dark")

    fig1.update_layout(
    title='Regla del codo para determinar el valor óptimo de k',
    xaxis=dict(title='k'),
    yaxis=dict(title='MSE')
    )
    st.plotly_chart(fig1)

    code5 = """
    # Determinar el mejor valor de k
    best_k = k_range[mse.index(min(mse))]
    print(f'Mejor número K: {best_k}')
"""
    st.code(code5,language='python')

    # Determinar el mejor valor de k
    best_k = k_range[mse.index(min(mse))]
    st.write(f'Mejor número K: {best_k}')

    code6 = """
    # Creamos el modelo KNN con el mejor valor de k
    knn = KNeighborsRegressor(n_neighbors=best_k)

    # Ajustamos el modelo a los datos sin valores nulos
    knn.fit(X_train, y_train)

    # Imputamos los valores faltantes en la columna 'Age'
    imputed_ages = knn.predict(titanic_without_age)
    titanic.loc[titanic['Age'].isna(), 'Age'] = imputed_ages
"""
    st.code(code6,language='python')

    # Creamos el modelo KNN con el mejor valor de k
    knn = KNeighborsRegressor(n_neighbors=best_k)

    # Ajustamos el modelo a los datos sin valores nulos
    knn.fit(X_train, y_train)

    # Imputamos los valores faltantes en la columna 'Age'
    imputed_ages = knn.predict(titanic_without_age)
    titanic.loc[titanic['Age'].isna(), 'Age'] = imputed_ages

    st.markdown(
        """
El porcentaje de valores nulos obtenido era de aproximadamente el 20%. Esto quiere decir que nos faltan valores para la columna edad de casi un cuarto de la población, por lo que al utilizar la media, los valores de la edad de los pasajeros van a dejar de estár repartidos a lo largo del rango de edades y se van a centrar en ella, no conservando así la distribución original. Dado que la columna no puede ser eliminada ya que los datos de las edades de los pasajeros continen información de gran interés, a la hora de realizar los análisis y que en la gráfica de distribución de edades se observa un número de población considerable en los extremos, que va desde los cero años de edad hasta los ochenta años de edad, se ha determinado que usar un método predictivo podría ayudar a conservar la distribución original, repartiendo las edades de una forma más uniforme y evitando la asignación de valores erróneos a los pasajeros. Es por ello que se ha dedicido implementar el algorítmo de K Nearest Neighbours, para poder aproximar de una manera más precisa el mayor número de datos. 

Para su implementación, se siguen los siguientes pasos:
* Normalizamos la columna `Fare` para centrar su media en cero y su desviación estándar en 1, de manera que no pueda introducir datos erróneos.
* Se hace uso de la función ``OneHotEncoder`` en las columnas ``Survived``, ``Pclass``, ``SibSp``, ``Parch``, ``Fare`` y ``Embarked``. Esta función crea categorías en base a los valores únicos dentro de las columnas y determina la presencia de dichas categorías dentro de los datos mediante un codificado binario.
* A partir de los datos codificados se crean dos dataframe distintos, uno que va a guardar los datos que no contienen valores nulos en la edad y otro, donde se van a guardar todas aquellas filas que tenían valores nulos en esa columna.
* Seguidamente, se hace un entrenamiento del modelo, en el que el 80% de los datos dentro del dataframe con las edades no nulas es usado para predecir el 20% restante.
* Una vez se ha entrenado el conjunto de datos, se procede a determinar el número de vecinos, es decir el número de conjunto de datos necesarios para ser capaces de aproximar los valores nulos. Para ello se hace uso del error cuadrático medio, que nos proporciona la media del error que hay entre los datos reales y los estimados.
* En la gráfica se puede observar que el número de vecinos que produce el menor error cuadrático medio es 3, por lo que ese es el valor que se usará para predecir los valores de las edades.
* Finalmente, una vez entrenados los datos, se utilizan para predecir las edades dentro del dataframe creado atneriormente con sólo las filas que contenían los datos faltantes y se procede a sustituir esos valores nulos por los valores predichos dentro del dataframe original.
        """
    )
#--------------------------------------Valores Nulos-------------------------------------#


#--------------------------------------Limpieza columnas-------------------------------------#
st.markdown(
            """
            ## Limpieza de columnas
        """
        )

st.markdown(
            """
Cambios que se van a realizar en las columnas:
* Columna `Age`: Se va a cambiar el tipo de dato a integer, ya que la edad es una variable discreta.
* Columna `Sex`: Los géneros de los pasajeros están escritos en minúscula, por lo que se va a poner la primera letra en mayúsculas.
* Columna `Name`: Se ha decidido separar el nombre en dos columnas, una que contiene los nombres completos de casados o solteros de los pasajeros, y otro que contiene los nombres de pila de aquellas mujeres casadas, de manera que se facilita la visualización. Una de las columnas ha pasado a llamarse `MarriedName` y la otra `FullName`.
* Columna `Level`: Se van a limpiar los datos para que sólo aparezca un valor ya que en muchos, se repite el mismo nivel.
* Finalmente, como se han creado columnas nuevas, se han reorganizado las mismas para facilitar la visualización.
        """
        )

st.write(titanic.head())

code2 = """
#Cambio el tipo de dato
titanic['Age']=titanic['Age'].astype(int)

#Primera letra en mayúsculas.
titanic['Sex']=titanic['Sex'].str.title()

#Creo a partir de la columna 'Name', 'MarriedName' y 'FullName'
titanic['MarriedName']=titanic['Name'].str.split('[(]',regex=True).str[0]
titanic['FemaleName']=titanic['Name'].str.split('[,|(|)]',regex=True).str[2]
titanic['FullName']=titanic['FemaleName'].combine_first(titanic['MarriedName'])
titanic.drop(columns=['FemaleName','Name'],inplace=True)

#Elimino los duplicados dentro de una misma fila en 'Level'
titanic['Level']=titanic['Level'].str.split(' ').str[0]

#Reordeno las columnas
titanic=titanic[['PassengerId', 'Survived', 'Pclass', 'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin','Level', 'Embarked']]
"""
st.code(code2,language='python')

titanic['Age']=titanic['Age'].astype(int)


titanic['Sex']=titanic['Sex'].str.title()


titanic['MarriedName']=titanic['Name'].str.split('[(]',regex=True).str[0]
titanic['FemaleName']=titanic['Name'].str.split('[,|(|)]',regex=True).str[2]
titanic['FullName']=titanic['FemaleName'].combine_first(titanic['MarriedName'])
titanic.drop(columns=['FemaleName','Name'],inplace=True)


titanic['Level']=titanic['Level'].str.split(' ').str[0]

titanic=titanic[['PassengerId', 'Survived', 'Pclass', 'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin','Level', 'Embarked']]

st.write(titanic.head())
#--------------------------------------Limpieza columnas-------------------------------------#