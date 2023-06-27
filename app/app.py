import streamlit as st
import pandas as pd
from PIL import Image # !pip install Pillow
import streamlit.components.v1 as components
#import plotly.express as px
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Ajustamos la pagina con un icono en el buscador y el titulo
st.set_page_config(page_title="Cómics Asiáticos", page_icon=":snowboarder:", layout="wide")