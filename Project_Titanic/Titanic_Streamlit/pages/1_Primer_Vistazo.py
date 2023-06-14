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

st.set_page_config(page_title='Primer Vistazo', page_icon='📈', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)

titanic = pd.read_csv(r"E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\datos\titanic.csv")

st.title('Primer vistazo de los datos')

image1 = Image.open(r'E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\img\logo.png')
st.sidebar.image(image1)


filtro_clase = st.sidebar.multiselect("Clase", titanic["Pclass"].unique())
if filtro_clase:
    titanic = titanic[titanic["Pclass"].isin(filtro_clase)]

filtro_genero = st.sidebar.multiselect("Género", titanic["Sex"].str.lower().unique())
if filtro_genero:
    titanic = titanic[titanic["Sex"].isin(filtro_genero)]

filtro_embarked = st.sidebar.multiselect("Puerto", titanic["Embarked"].unique())
if filtro_embarked:
    titanic = titanic[titanic["Embarked"].isin(filtro_embarked)]

filtro_survived= st.sidebar.multiselect("Estado", titanic["Survived"].unique())
if filtro_survived:
    titanic = titanic[titanic["Survived"].isin(filtro_survived)]

st.dataframe(titanic)


st.markdown(
                """
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
            """
            )
