import streamlit as st
import pandas as pd
from pathlib import Path
import yaml

def read_yaml(file_path: str):
    """
    Read data from a YAML file.

    Args:
        file_path (str): Path of the YAML file.

    Returns:
        object: Data loaded from the YAML file, or None if there is an error.
    """
    try:
        with open(Path(file_path)) as f:
            data = yaml.safe_load(f)
        return data
    except (FileNotFoundError, IOError, yaml.YAMLError) as err:
        return None

# Path de nustros ficheros de score
score_path = {
        "light": "../models/light/score.yaml",
        "medium": "../models/medium/score.yaml",
        "heavy": "../models/heavy/score.yaml",
    }

def load_score():

    try:
        score = {}
        for type_data, path in score_path.items():
            data = read_yaml(path)
            if data and type_data != "MAPE":
                score[type_data] = data

        light = pd.DataFrame(score["light"])
        light.fillna(0, inplace=True)

        medium = pd.DataFrame(score["medium"])
        medium.fillna(0, inplace=True)

        heavy = pd.DataFrame(score["heavy"])
        heavy.fillna(0, inplace=True)

        return light, medium, heavy

    except Exception as err:
        print(err)


# Ajustamos la pagina con un icono en el buscador y el titulo
st.set_page_config(page_title="Cómics Asiáticos", page_icon="☢️", layout="wide")

# Cargamos el Dataset con el que vamos a trabajar
heavy = pd.read_csv('../data/processed/heavy.csv', index_col="Unnamed: 0")

#Ponemos un titulo
st.title("Cómic Asiático en la Comunidad Fansub Hispanohablante")

st.image("../notebooks/img/ANDO-manga-manhwa-manhua.png")

menu = st.sidebar.selectbox("Seleccionamos la página", ['Home', 'Filtros', 'Dataset'])

if menu == 'Home':

    st.header('Datos con los que trabajamos')

    if st.checkbox('Mostrar'):
        heavy
    else:
        st.markdown('El dataset esta oculto')

    tab1, tab2, tab3 = st.tabs(["Puntuación de modelos", "Aprendizaje del modelos", "Distribución de erorres"])

    with tab1:
        st.subheader("Puntuación de modelos")
        light, medium, heavy = load_score()
        st.text('Light')
        st.dataframe(light, use_container_width=True)
        st.text('Medium')
        st.dataframe(medium, use_container_width=True)
        st.text('Heavy')
        st.dataframe(heavy, use_container_width=True)
        
    with tab2:

        st.subheader("Aprendizaje del modelos")
        st.text('Light')
        st.image("../notebooks/img/light_learning.png")
        st.text('Medium')
        st.image("../notebooks/img/medium_learning.png")
        st.text('Heavy')
        st.image("../notebooks/img/heavy_learning.png")


    with tab3:

        st.subheader('Distribución de erorres')
        st.text('Light')
        st.image("../notebooks/img/light_error.png")
        st.text('Medium')
        st.image("../notebooks/img/medium_error.png")
        st.text('Heavy')
        st.image("../notebooks/img/heavy_error.png")