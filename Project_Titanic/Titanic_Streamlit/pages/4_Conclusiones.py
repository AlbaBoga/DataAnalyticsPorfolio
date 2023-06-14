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

st.set_page_config(page_title='Conclusiones', page_icon='📓', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)

image2 = Image.open(r'E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\img\hundido.jpg')
st.image(image2, width=500)

st.title('Conclusiones')

image1 = Image.open(r'E:\COPIA_DAWN\DAWN\CURSOSYLIBROS\Data\Upgrade Hub Data Analytics Bootcamp\Tareas\Module1_0_SoftSkillsProyecto\Notebooks_ejercicios\Titanic_Streamlit\img\logo.png')
st.sidebar.image(image1)

st.markdown(
            """
* Gracias a la utilización de fuentes externas, se pudo conservar la columna `Cabin`, para posterior análisis.
* A pesar de la incertidumbre dentro de la columna `Age`, el uso de un modelo predictivo permitió obtener los datos faltantes sin modificar la distribución de las variables.
* Los valores atípicos dentro de la columna `Fare`, que se correspondían con los precios más caros de los billetes, hacían referencia a los pasajeros que se alojaban en los camarotes más lujosos del barco.
* La mayoría de pasajeros en tercera clase eran adultos de entre ``19 y 38 años``, mientras que la mayoría de pasajeros entre ``42 y 80 años``, eran de primera clase, lo cuál hace referencia a la disparidad de recursos entre las clases.
* La mayoría de pasajeros pagaron entre ``5 y 15 libras`` por sus billetes, mientras que lo máximo pagado fue ``512 libras``.
* El ``65%`` de los pasajeros era de género masculino y sólo sobrevivió el ``13%`` de ellos, es decir, ``116 personas de 891 pasajeros``.
* De las mujeres sólo falleció un ``9%``, es decir, ``80 personas de 891 pasajeros``.
* El ``mayor porcentaje de supervivencia`` se correspondía con los pasajeros de género fememnino y la primera clase, mientras que ``el menor``, con la tercera clase y los de género masculino.
"""
        )

st.markdown(
    """
        ## Posibles aplicaciones
    """
)

st.markdown(
    """
        El análisis realizado permite vislumbrar la distribución de pasajeros según su clase económica, lo cuál puede ser de interés a la hora de estudiar los diferentes roles en Inglaterra durante el siglo XX y como éstos impactaron en la supervivencia de ciertos pasajeros.
    """
)

st.markdown(
    """
        ## Análisis futuros
    """
)

st.markdown(
    """
De la información obtenida, se observa una clara disparidad entre clases, lo cuál fue clave para la supervivencia de los pasajeros y es un área que se podría seguir estudiando en futuros análisis.
"""
)
