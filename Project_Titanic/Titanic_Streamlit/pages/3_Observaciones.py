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



st.set_page_config(page_title='Observaciones', page_icon='🔬', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

titanic = pd.read_csv(r"E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\data\preprocesado.csv")

st.title('Observaciones')

image1 = Image.open(r'E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\img\logo.png')
st.sidebar.image(image1)



#--------------Observaciones preliminares de datos numéricos--------------#
st.markdown(
            """
            ## Observaciones preliminares de datos numéricos
        """
        )
st.markdown(
            """
Se utiliza la función ``.describe()`` en los datos numéricos del dataset para ver el número total de datos, la media, la desviación estándar, el máximo, el mínimo y los cuartiles.
        """
        )
st.write(titanic.describe().T)
st.markdown(
            """
De estos datos se observa que la edad mínima es 0 años, indicando la presencia de recién nacidos dentro del barco. La edad máxima era de 80 años, lo cuál nos dice que había personas de todas las edades a bordo. Y, por último, la mediana es de 28 años y la media es de casi 30 años, por lo que la cercanía entre ambas indicaría simetría en la distribución de los datos de edad.

En esta tabla también podemos extraer información relevante de la columna Fare, en la cuál se puede observar una diferencia muy grande entre la mediana, la media y el valor máximo pagado por billete. Esta distribución desigual de los datos indica que los pasajeros de primera clase pagaron una cantidad muy alta en comparación con el resto de pasajeros, lo cuál también puede suponer la presencia de valores atípicos dentro de la distribución.
        """
        )
#--------------Observaciones preliminares de datos numéricos--------------#



#--------------Distribución de la edad en el barco--------------#
st.markdown(
            """
            ## Distribución de la edad en el barco
        """
        )
st.markdown(
            """
Procedimiento:
* Primero, se ha realizado un histograma que refleja el número de pasajeros en función de la edad.
* En la siguiente gráfica, se ha obtenido el número de personas por edad, divididas según la clase, grácias a una gráfica de dispersión.
* Para determinar datos de interés entre las diferentes clases y la esperanza de vida de la época, se ha hecho uso de páginas externas que han permitido una mejor comprensión de los datos.
        """
        )
col1,col2 =st.columns(2)
with col1:
    fig=px.histogram(x=titanic['Age'])
    fig.update_layout(height=500, width=500, title_text="Distribución de la Edad", 
                  xaxis=dict(title="Edad"), yaxis=dict(title="Número de pasajeros"), template='plotly_dark')
    st.plotly_chart(fig)
    st.markdown(
            """
En la gráfica se puede ver que el mayor número de pasajeros se encuentran entre las edades que van de 18 a 35 años, siendo las edades más comunes entre pasajeros las que van de 24 a 25 años. Si se compara esta gráfica con la obtenida en el apartado de valores nulos, veremos que se ha conseguido mantener la distribución de edades en su mayoría, sin cambios significativos. Debido a que el porcentaje de valores nulos era casi del 20%, se previó que iba a tener un impacto considerable sobre la distribución de los datos, por lo que se optó por el algoritmo KNN, lo cuál permitiría encontrar relaciones entre los datos y obtener unas edades más ajustadas, impactando lo menos posible dicha distribución.

        """
        )

with col2:
    edad_clases=titanic.groupby('Pclass')['Age'].value_counts().reset_index()
    edad_clases.columns=['Pclass','Age', 'count']
    fig1 = px.strip(edad_clases, x="Age", y="count", template="plotly_dark", color='Pclass')

    fig1.update_layout(
    title='Distribución de edades por clase',
    xaxis=dict(title='Edad'),
    yaxis=dict(title='Número de pasajeros')
)

    st.plotly_chart(fig1)

    st.markdown(
            """
Seguidamente, se observa la distribución de las edades por clase dentro del barco. Se puede ver que la mayoría de pasajeros entre 19 y 38 años pertenecían a tercera clase. Si nos fijamos en los extremos, la mayoría de niños e infantes pertenecían a la tercera clase, mientras que por encima de 42 años, hay un mayor número de pasajeros en primera clase. Por otro lado, los pasajeros de segunda clase se distribuyen de una forma más uniforme a lo largo del rango de edades.

La esperanza de vida en Inglaterra alrededor de 1912 estaba situada en 52 años para los hombres y 55 años para las mujeres, esto puede implicar, en apoyo de los datos mostrados en la gráfica que la vida pausada de la gente de clase alta de la época les permitían vivir muchos más años y tener mucha más actividad de ocio, en comparación con la gente de clase baja, expuesta a más enfermedades, trabajos laboriosos y que viajaban por necesidad, ya sea por encontrar una vida mejor o por la búsqueda de un trabajo.

Info: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/articles/howhaslifeexpectancychangedovertime/2015-09-09

Info: https://localhistories.org/life-in-1912/
        """
        )
#--------------Distribución de la edad en el barco--------------#



#--------------Distribución precio de billete--------------#
st.markdown(
            """
            ## Distribución precio de billete
        """
        )
st.markdown(
            """
Procedimiento:
* En la gráfica se ha realizado un histograma que refleja el precio del billete y cuántas personas pagaron por él.
        """
        )
fig2=px.histogram(x=titanic['Fare'])
fig2.update_layout(height=500, width=500, title_text="Distribución del precio del billete", 
                  xaxis=dict(title="Precio"), yaxis=dict(title="Número de pasajeros que han pagado"), template='plotly_dark')
st.plotly_chart(fig2)
st.markdown(
            """
En la gráfica se puede ver que la mayoría de pasajeros pagaron entre 5 y 15 libras por billete, lo cuál asocia este precio a los pasajeros de tercera clase, mientras que aquellos pasajeros en primera clase, cuyo porcentaje será menor, pagarían precios mucho más altos en función del nivel de camarote en el que se encontrasen, dando lugar a valores que pueden ser reconocidos como valores atípicos, como en el caso del valor máximo.
        """
        )
#--------------Distribución precio de billete--------------#



#--------------Porcentaje de pasajeros según la clase--------------#
st.markdown(
            """
            ## Porcentaje de pasajeros según la clase
        """
        )
st.markdown(
            """
Procedimiento:
* Se ha utilizado un gráfico circular para ver el porcentaje de pasajeros dentro de cada clase.
        """
        )
pct_pasajeros_1 = (len(titanic[titanic['Pclass']==1])*100)/titanic.shape[0]
pct_pasajeros_2 = (len(titanic[titanic['Pclass']==2])*100)/titanic.shape[0]
pct_pasajeros_3 = (len(titanic[titanic['Pclass']==3])*100)/titanic.shape[0]

fig3 = px.pie(labels=['Primera Clase','Segunda Clase', 'Tercera Clase'], 
             values=[pct_pasajeros_1,pct_pasajeros_2,pct_pasajeros_3],
             names=['Primera Clase','Segunda Clase', 'Tercera Clase'],
             color=['Primera Clase','Segunda Clase', 'Tercera Clase'],
             template='plotly_dark')

fig3.update_layout(
    title='Porcentaje de pasajeros dentro de cada clase')

st.plotly_chart(fig3)
st.markdown(
            """
En esta gráfica se confirma que la mayoría de pasajeros estaban alojados en tercera clase, lo cuál explica por qué la distribución del precio de los billetes está sesgada hacia precios más bajos. Por otro lado, se puede apreciar que hay casi un 4% más de pasajeros en primera clase que en segunda clase, lo cuál se puede asociar a la libertad que tenía la clase alta, gracias a su economía, para realizar viajes de ocio, en comparación con la clase media.
        """
        )
#--------------Porcentaje de pasajeros según la clase--------------#



#--------------Porcentaje de pasajeros según la clase--------------#
st.markdown(
            """
            ## Distribución por precio de billete, clase y nivel del barco
        """
        )
st.markdown(
            """
Procedimiento:
* Se han dividido los precios del billete en 10 grupos de precio.
* Estos se han utilizado para agrupar la clase de los pasajeros y los niveles en función de los mismos, obteniendo una tabla y sólo visualizando aquellos donde el número de pasajeros es mayor que cero.
* A través de un procedimiento de WebScrapping se ha conseguido una tabla donde se listan los diferentes camarotes de lujo dentro del barco.
* Se ha utilizado una web externa para entender mejor la distribución de los camarotes por clases y por niveles dentro del barco.
        """
        )
col1,col2 =st.columns(2)
with col1:
    rango_precios=pd.cut(titanic['Fare'], 10)
    distribucion=titanic.groupby(rango_precios)[['Pclass','Level']].value_counts().reset_index()
    st.write(distribucion[distribucion['count']>0].reset_index())

with col2:
    enlace = "https://es.wikipedia.org/wiki/Instalaciones_de_primera_clase_del_RMS_Titanic"
    texto_web = requests.get(enlace).text
    sopa = BeautifulSoup(texto_web, 'html5')
    sopa.prettify()
    camarote_lujo = sopa.find_all('table', class_= 'wikitable')
    camarotes = camarote_lujo[0]
    dataframe_camarotes = pd.read_html(str(camarotes),header=0)[0]
    st.write(dataframe_camarotes)

st.markdown(
            """
En la tabla se puede comprobar que los niveles que alojaban más gente eran los niveles ``C``, ``E`` y ``G``, los cuales se tomaron como la moda en apartados anteriores, lo cuál también ha influído en la distribución de pasajeros por niveles. Los precios más altos estaban reservados para los niveles ``C`` y ``B``, donde se encontraban las cabinas más lujosas del barco, listadas en la tabla dataframe_camarotes. Para los demás niveles, los rangos de precios varían e,igualmente, el número de personas que pagaron por ellos. Se observa que diferentes niveles estaban están también en diferentes clases, lo cuál se debe a que según el nivel, también podías encontrar habitaciones de primera, segunda o tercera clase. Para primera clase, los camarotes iban de los niveles ``A`` a ``E``. Para la segunda clase, los camarotes ofrecidos iban de los niveles ``B`` a ``F``. Mientras que para la tercera clase, sus habitaciones iban de los niveles ``D`` a ``G``. De esta manera, la diferencia de precios que hay entre niveles hace referencia a las diferentes habitaciones que había por clase y por nivel. Finalmente, también se encuentra un valor atípico en los niveles, el nivel ``T``, en el cual sólo hay constancia de que una persona pagó por él y no se han podido encontrar más referencias acerca de él.

Info: https://rmstitanic1912.weebly.com/the-levels-of-the-titanic.html
        """
        )
#--------------Porcentaje de pasajeros según la clase--------------#



#--------------Pasajeros que embarcaron según el género--------------#
st.markdown(
            """
            ## Pasajeros que embarcaron según el género
        """
        )
st.markdown(
            """
Procedimiento:
* Se han agrupado los pasajeros por género y se muestran junto al total de pasajeros.
* Se han dividido los pasajeros agrupados por género según la clase.
* Se han dividido los pasajeros agrupados por género según el puerto de embarque.
        """
        )
col1,col2 =st.columns(2)
with col1:
    genero=titanic.groupby('Sex')['Sex'].value_counts().reset_index()
    genero.loc[2,['Sex','count']]=['Total',titanic['Sex'].count()]
    fig4=px.histogram(genero, x="Sex", y="count", color="Sex",labels={'Sex':'Género','count':'Número de Pasajeros'})
    fig4.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig4)

with col2:
    clase_genero=titanic.groupby('Sex')['Pclass'].value_counts().reset_index()
    total_clase=titanic.groupby('Pclass')['Pclass'].value_counts().reset_index()
    clase_genero.loc[6,['Sex','Pclass','count']]=['Total',1,total_clase.loc[0,'count']]
    clase_genero.loc[7,['Sex','Pclass','count']]=['Total',2,total_clase.loc[1,'count']]
    clase_genero.loc[8,['Sex','Pclass','count']]=['Total',3,total_clase.loc[2,'count']]

    fig5=px.histogram(clase_genero, x="Pclass", y="count", color="Sex", nbins=3, barmode='group',labels={'Pclass':'Clase', 'count':'Número de Pasajeros'})

    fig5.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig5)

col3,col4,col5 =st.columns(3)
with col4:
    puerto_genero=titanic.groupby('Sex')['Embarked'].value_counts().reset_index()
    total_puerto=titanic.groupby('Embarked')['Embarked'].count()
    puerto_genero.loc[6,['Sex','Embarked','count']]=['Total','S',total_puerto.iloc[2]]
    puerto_genero.loc[7,['Sex','Embarked','count']]=['Total','C',total_puerto.iloc[0]]
    puerto_genero.loc[8,['Sex','Embarked','count']]=['Total','Q',total_puerto.iloc[1]]
    fig6=px.histogram(puerto_genero, x="Embarked", y="count", color="Sex", 
                  labels= {'Embarked': 'Puerto','count':'Número de Pasajeros'}, nbins=3, barmode='group',template='plotly_dark')
    fig6.update_layout(height=500, width=800, title_text="Distribución de pasajeros")
    st.plotly_chart(fig6)

st.markdown(
            """
De las gráficas mostradas se pueden sacar los siguientes datos significativos:
* El ``65%`` de pasajeros eran de género masculino.
* La tercera clase era la que más pasajeros albergaba, con un ``55%`` de la población total.
* Finalmente, el puerto más popular entre los pasajeros era Southampton, desde el cuál embarcaron más del ``72%`` de los pasajeros.
        """
        )
#--------------Pasajeros que embarcaron según el género--------------#



#--------------Número de pasajeros en función de la edad--------------#
st.markdown(
            """
            ## Número de pasajeros en función de la edad
        """
        )
st.markdown(
            """
Procedimiento:
* Se ha creado una columna nueva que se llama ``Pasajero``.
* Dentro de esa columna van a estar presentes tres variables categóricas: ``Niño``, ``Adulto`` y ``Persona Mayor``.
* El primer rango es para menores de ``18 años``.
* El segundo rango es para pasajeros entre ``18 y 60 años``
* El tercer rango es para pasajeros mayores de ``60 años``.
* Se representa en una gráfica el número de pasajeros que había dentro de esos rangos de edades.
        """
        )
code = """
titanic['Pasajero']=None
titanic['Pasajero'].loc[titanic['Age']<18]='Niño/a'
titanic['Pasajero'].loc[(titanic['Age']>=18)&(titanic['Age']<60)]='Adulto/a'
titanic['Pasajero'].loc[titanic['Age']>=60]='Persona Mayor'
"""
st.code(code,language='python')

titanic['Pasajero']=None
titanic['Pasajero'].loc[titanic['Age']<18]='Niño/a'
titanic['Pasajero'].loc[(titanic['Age']>=18)&(titanic['Age']<60)]='Adulto/a'
titanic['Pasajero'].loc[titanic['Age']>=60]='Persona Mayor'

pasajeros=titanic.groupby('Pasajero')['Pasajero'].value_counts().reset_index()
fig7=px.histogram(pasajeros, x="Pasajero", y="count", color="Pasajero",labels={'Pasajero':'Rango de Edad','count':'Número de Pasajeros'})
fig7.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')

st.plotly_chart(fig7)

st.markdown(
            """
La mayor parte de los pasajeros, es decir, más del ``80%`` se encontraban dentro del rango de edad de entre ``18`` y ``60`` años. Por otro lado, menos del ``15%`` estaban comprendidos dentro del rango de edad de menores de ``18`` años y el resto, eran mayores de ``60`` años.
        """
        )
#--------------Número de pasajeros en función de la edad--------------#



#--------------Proporción de pasajeros según su título--------------#
st.markdown(
            """
            ## Proporción de pasajeros según su título
        """
        )
st.markdown(
            """
Procedimiento:
* Se ha creado una nueva columna llamada `Título`.
* Esta columna recoje los títulos de los pasajeros, presentes en el nombre, justo después del apellido.
* Se ha creado una gráfica donde se representa el número de pasajeros que tenían los títulos encontrados.
* En la segunda gráfica se han distribuído los títulos segun los diferentes niveles del barco.
        """
        )
code = """
titanic['Título']=titanic['MarriedName'].str.split('[,|.]', regex=True).str[1]
titanic=titanic[['PassengerId', 'Survived', 'Pclass','Pasajero','Título', 'MarriedName', 'FullName', 'Sex',
       'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Level', 'Embarked']]
"""
st.code(code,language='python')

titanic['Título']=titanic['MarriedName'].str.split('[,|.]', regex=True).str[1]
titanic=titanic[['PassengerId', 'Survived', 'Pclass','Pasajero','Título', 'MarriedName', 'FullName', 'Sex',
       'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Level', 'Embarked']]

col1,col2 =st.columns(2)
with col1:
    titulos=titanic.groupby('Título')['Título'].value_counts()
    titulos_pct=pd.DataFrame(titulos.apply(lambda x:(x*100)/titulos.sum())).reset_index()
    fig8=px.histogram(titulos_pct, x="Título", y="count", color="Título",labels={'Título':'Título del pasajero','count':'Número de Pasajeros'})
    fig8.update_layout(height=650, width=800, title_text="Distribución de pasajeros por títulos", 
                  template='plotly_dark')
    st.plotly_chart(fig8)

with col2:
    titulos_level=titanic.groupby('Level')['Título'].value_counts()
    titulos_level_pct=pd.DataFrame(titulos_level.apply(lambda x:(x*100)/titulos_level.sum())).reset_index()
    fig9=px.histogram(titulos_level_pct, x="count", y="Level", color="Título", labels={'Level':'Nivel del barco','count':'Porcentaje de Pasajeros'},barmode='group',orientation='h')
    fig9.update_layout(height=1000, width=1200, title_text="Distribución de pasajeros por títulos y nivel", 
                  template='plotly_dark')
    st.plotly_chart(fig9)

st.markdown(
            """
De las siguientes gráficas se han podido observar los siguientes datos:
* Más de un ``58%`` de los títulos pertenecientes a los pasajeros del barco eran Mr.
* Había un mayor porcentaje de ``mujeres solteras`` en el barco, que poseían el título Miss.
* Algunos de los títulos minoritarios presentes en la gráfica, hacen referencia a gente de ``primera clase``.
* La mayoría de estos títulos minoritarios se alojaban en el nivel `B` y `C`, donde se encontraban las cabinas de lujo del barco.
        """
        )

#--------------Proporción de pasajeros según su título--------------#



#--------------Fallecidos vs Supervivientes--------------#
st.markdown(
            """
            ## Fallecidos vs Supervivientes
        """
        )
st.markdown(
            """
Procedimiento:
* Se ha creado una nueva columna llamada `Estado`.
* Esta columna contiene variables categóricas que se corresponden con `Fallecido` si en la columna ``Survived`` hay un 0 y ``Sobrevivió``, si hay un 1.
* Se ha representado el porcentaje de pasajeros que sobrevivió y falleció en el barco.
* Se ha representado el pocentaje de fallecidos según las diferentes clases dentro del barco.
* Se ha representado el porcentaje de fallecidos según el género de los pasajeros.
* Se ha representado el porcentaje de fallecidos según el rango de edades.
        """
        )
code = """
titanic['Estado']=None
titanic['Estado'].loc[titanic['Survived']==0]='Fallecido/a'
titanic['Estado'].loc[titanic['Survived']==1]='Sobrevivió'
titanic=titanic[['PassengerId', 'Survived','Estado', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
       'Fare', 'Cabin', 'Level', 'Embarked']]
"""
st.code(code,language='python')

titanic['Estado']=None
titanic['Estado'].loc[titanic['Survived']==0]='Fallecido/a'
titanic['Estado'].loc[titanic['Survived']==1]='Sobrevivió'
titanic=titanic[['PassengerId', 'Survived','Estado', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
       'Fare', 'Cabin', 'Level', 'Embarked']]


col1,col2 =st.columns(2)
with col1:
    bajas=titanic.groupby('Estado')['Estado'].value_counts()
    bajas_pct=pd.DataFrame(bajas.apply(lambda x:(x*100)/bajas.sum())).reset_index()
    fig10=px.histogram(bajas_pct, x="Estado", y="count", color="Estado",labels={'Estado':'Estado de los pasajeros tras Titanic','count':'Porcentaje de Pasajeros'})
    fig10.update_layout(height=650, width=800, title_text="Distribución del estado de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig10)

with col2:
    bajas_clases=titanic.groupby('Pclass')['Estado'].value_counts()
    bajas_clases_pct=pd.DataFrame(bajas_clases.apply(lambda x:(x*100)/bajas_clases.sum())).reset_index()
    fig11=px.histogram(bajas_clases_pct, x="Estado", y="count", color="Pclass",labels={'Estado':'Estado de los pasajeros tras Titanic','count':'Porcentaje de Pasajeros'},barmode='group')
    fig11.update_layout(height=650, width=800, title_text="Distribución del estado de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig11)

col3,col4 =st.columns(2)
with col3:
    estado_genero=titanic.groupby('Sex')['Estado'].value_counts()
    estado_genero_pct=pd.DataFrame(estado_genero.apply(lambda x:(x*100)/estado_genero.sum())).reset_index()
    fig12=px.histogram(estado_genero_pct, x="Sex", y="count", color="Estado", labels={'Sex':'Género del Pasajero','count':'Porcentaje de Pasajeros'},barmode='group',orientation='v')
    fig12.update_layout(height=500, width=800, title_text="Distribución de pasajeros por estado y género", 
                  template='plotly_dark')
    st.plotly_chart(fig12)

with col4:
    estado_pasajero=titanic.groupby('Pasajero')['Estado'].value_counts()
    estado_pasajero_pct=pd.DataFrame(estado_pasajero.apply(lambda x:(x*100)/estado_pasajero.sum())).reset_index()
    fig13=px.histogram(estado_pasajero_pct, x="Pasajero", y="count", color="Estado", labels={'Sex':'Género del Pasajero','count':'Porcentaje de Pasajeros'},barmode='group',orientation='v')
    fig13.update_layout(height=500, width=800, title_text="Distribución de pasajeros por estado y género", 
                  template='plotly_dark')
    st.plotly_chart(fig13)

st.markdown(
            """
De las siguientes gráficas se ha podido observar los siguientes datos:
* Un ``62%`` de los pasajeros fallecieron.
* Sólo el ``42%`` de ellos pertenecían a tercera clase, mientras que los pasajeros con un ``mayor porcentaje de superviviencia`` eran de primera clase.
* Un ``52%`` de pasajeros fallecidos con respecto al total eran hombres, mientras que el ``mayor porcentaje de supervivencia`` correspondió a las mujeres.
* Dentro del rango de mayores de 60, fallecieron ``19 personas`` de 26 pasajeros en total..
* Más de un ``6% de los fallecidos`` estaban dentro del rango de edad de menores de 18 años, lo cuál equivale a 54 pasajeros de 121 pasajeros considerados en ese rango.
    """
        )
#--------------Fallecidos vs Supervivientes--------------#



#--------------Pasajeros que vaiajron solos vs acompañados--------------#
st.markdown(
            """
            ## Pasajeros que viajaron solos vs acompañados
        """
        )
st.markdown(
            """
Procedimiento:
* Se ha creado una columna nueva llamada `Acompañamiento`, para determinar si los pasajeros viajaban o no con familia.
* Si `SibSp` y `Parch` es cero, se ha determinado que los pasajeros viajaban solos, mientras que si alguna de esas variables eran mayores que cero, viajaban con familia.
* Se ha representado el porcentaje de pasajeros en función de si viajaban solos o no.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por aquellos que fallecieron o sobrevivieron.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por género.
* Se ha representado el porcentaje de pasajeros acompañados, agrupados por clase.
        """
        )
code = """
titanic['Acompañamiento']=None
titanic['Acompañamiento'].loc[(titanic['SibSp']==0)&(titanic['Parch']==0)]='Viaja Solo/a'
titanic['Acompañamiento'].loc[(titanic['SibSp']>0)|(titanic['Parch']>0)]='Viaja Acompañado/a'
titanic=titanic[['PassengerId', 'Survived','Estado', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch', 'Acompañamiento', 'Ticket',
       'Fare', 'Cabin', 'Level', 'Embarked']]
"""
st.code(code,language='python')

titanic['Acompañamiento']=None
titanic['Acompañamiento'].loc[(titanic['SibSp']==0)&(titanic['Parch']==0)]='Viaja Solo/a'
titanic['Acompañamiento'].loc[(titanic['SibSp']>0)|(titanic['Parch']>0)]='Viaja Acompañado/a'
titanic=titanic[['PassengerId', 'Survived','Estado', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch', 'Acompañamiento', 'Ticket',
       'Fare', 'Cabin', 'Level', 'Embarked']]


col1,col2 =st.columns(2)
with col1:
    familias=titanic.groupby('Acompañamiento')['Acompañamiento'].value_counts()
    familias_pct=pd.DataFrame(familias.apply(lambda x:(x*100)/familias.sum())).reset_index()
    fig14=px.histogram(familias_pct, x="Acompañamiento", y="count", color="Acompañamiento",labels={'Acompañamiento':'Pasajeros que viajaron solos o acompañados','count':'Porcentaje de Pasajeros'})
    fig14.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig14)

with col2:
    estado_familias=titanic.groupby('Estado')['Acompañamiento'].value_counts()
    estado_familias_pct=pd.DataFrame(estado_familias.apply(lambda x:(x*100)/estado_familias.sum())).reset_index()
    fig15=px.histogram(estado_familias_pct, x="Acompañamiento", y="count", color="Estado", labels={'Acompañamiento':'Pasajeros que viajaron solos o acompañados','count':'Porcentaje de Pasajeros'},barmode='group',orientation='v')
    fig15.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig15)

col3,col4 =st.columns(2)
with col3:
    genero_familias=titanic.groupby('Sex')['Acompañamiento'].value_counts()
    genero_familias_pct=pd.DataFrame(genero_familias.apply(lambda x:(x*100)/genero_familias.sum())).reset_index()
    fig16=px.histogram(genero_familias_pct, x="Acompañamiento", y="count", color="Sex", labels={'Acompañamiento':'Pasajeros que viajaron solos o acompañados','count':'Porcentaje de Pasajeros'},barmode='group',orientation='v')
    fig16.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig16)

with col4:
    clases_familias=titanic.groupby('Pclass')['Acompañamiento'].value_counts()
    clases_familias_pct=pd.DataFrame(clases_familias.apply(lambda x:(x*100)/clases_familias.sum())).reset_index()
    fig17=px.histogram(clases_familias_pct, x="Acompañamiento", y="count", color="Pclass", labels={'Acompañamiento':'Pasajeros que viajaron solos o acompañados','count':'Porcentaje de Pasajeros'},barmode='group',orientation='v')
    fig17.update_layout(height=500, width=800, title_text="Distribución de pasajeros", 
                  template='plotly_dark')
    st.plotly_chart(fig17)

st.markdown(
            """
De las siguientes gráficas se ha podido observar:
* Un ``60%`` de los pasajeros que viajaban en Titanic no estaban acompañados por su familia.
* De ellos, el ``42%`` falleció.
* De los pasajeros que viajaban con familia, la mitad consiguió sobrevivir y la otra falleció.
* Más de la mitad de pasajeros que viajaban en familia eran mujeres.
* Sólo un ``14%`` de las mujeres sobre los pasajeros totales viajaban solas.
    """
        )
#--------------Pasajeros que vaiajron solos vs acompañados--------------#



#--------------Correlaciones entre variables--------------#
st.markdown(
            """
            ## Correlaciones entre variables
        """
        )
st.markdown(
            """
Procedimiento:
* Se han codificado las variables categóricas del DataFrame mediante ``LabelEncoder()``, para obtener las correlaciones entre variables.
* Se ha hecho uso de un mapa de calor para representar dichas correlaciones.
        """
        )
code = """
titanic_corr=titanic[['Survived', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch',
       'Acompañamiento', 'Ticket', 'Fare', 'Level', 'Embarked']].copy()
le = LabelEncoder()
titanic_corr['Pasajero'] = le.fit_transform(titanic_corr['Pasajero'])
titanic_corr['Título'] = le.fit_transform(titanic_corr['Título'])
titanic_corr['Sex'] = le.fit_transform(titanic_corr['Sex'])
titanic_corr['MarriedName'] = le.fit_transform(titanic_corr['MarriedName'])
titanic_corr['FullName'] = le.fit_transform(titanic_corr['FullName'])
titanic_corr['Acompañamiento'] = le.fit_transform(titanic_corr['Acompañamiento'])
titanic_corr['Ticket'] = le.fit_transform(titanic_corr['Ticket'])
titanic_corr['Level'] = le.fit_transform(titanic_corr['Level'])
titanic_corr['Embarked']  = le.fit_transform(titanic_corr['Embarked'])
"""
st.code(code,language='python')

titanic_corr=titanic[['Survived', 'Pclass', 'Pasajero', 'Título',
       'MarriedName', 'FullName', 'Sex', 'Age', 'SibSp', 'Parch',
       'Acompañamiento', 'Ticket', 'Fare', 'Level', 'Embarked']].copy()
le = LabelEncoder()
titanic_corr['Pasajero'] = le.fit_transform(titanic_corr['Pasajero'])
titanic_corr['Título'] = le.fit_transform(titanic_corr['Título'])
titanic_corr['Sex'] = le.fit_transform(titanic_corr['Sex'])
titanic_corr['MarriedName'] = le.fit_transform(titanic_corr['MarriedName'])
titanic_corr['FullName'] = le.fit_transform(titanic_corr['FullName'])
titanic_corr['Acompañamiento'] = le.fit_transform(titanic_corr['Acompañamiento'])
titanic_corr['Ticket'] = le.fit_transform(titanic_corr['Ticket'])
titanic_corr['Level'] = le.fit_transform(titanic_corr['Level'])
titanic_corr['Embarked']  = le.fit_transform(titanic_corr['Embarked'])

corr=titanic_corr.corr()
fig18 = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns))
fig18.update_layout(
    width=800,
    height=800,
    title='Mapa de calor',
    template='plotly_dark'
)
st.plotly_chart(fig18)

st.markdown(
            """
Correlaciones significativas entre variables:
* Hay una correlación significativa de `` 0.95 `` entre la clase de los pasajeros y el nivel del barco donde se alojaban.
* Hay una correlación significativa de `` 0.55 `` entre la clase de los pasajeros, el nivel del barco donde se alojaban y el precio pagado por el billete.
* Hay una correlación significativa de `` 0.55 `` entre el género y la supervivencia de los pasajeros.
* Para el resto de variables parece no haber una relación significativa lineal entre ellas.
        """
        )

#--------------Correlaciones entre variables--------------#

