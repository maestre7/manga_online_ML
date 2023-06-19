
#from sklearn.linear_model import ElasticNet
#from sklearn.svm import SVR
#from sklearn.ensemble import RandomForestRegressor

# Own
from utils import write_yaml

path_model = "../models/model_config.yaml"

parameters = {
    # ElasticNet
    "en": {
        'regressor__alpha': [0.1, 0.5, 1.0],  # Parámetro de regularización (alpha)
        'regressor__l1_ratio': [0.3, 0.5, 0.7],  # Proporción entre L1 (Lasso) y L2 (Ridge)
    },
    # SVR
    "svr": {
        'regressor__kernel': ['linear', 'rbf', 'poly'],  # Kernel utilizado en el SVR
        'regressor__C': [0.1, 1.0, 10.0],  # Parámetro de regularización (C)
        'regressor__epsilon': [0.01, 0.1, 0.5],  # Tolerancia del margen de error
    },
    # RandomForestRegressor
    "rfr": {
        'regressor__n_estimators': [50, 100, 200],  # Número de árboles en el bosque
        'regressor__max_depth': [5, 10],  # Profundidad máxima de los árboles
        'regressor__min_samples_split': [2, 5, 10],  # Número mínimo de muestras requeridas para dividir un nodo interno
    }
}

a = write_yaml(path_model, parameters)