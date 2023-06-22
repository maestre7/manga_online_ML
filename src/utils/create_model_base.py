
# Own
from utils import write_yaml

path_model = "../../models/model_config.yaml"

parameters = {
    # ElasticNet
    "en": {
        'regressor__alpha': [0.1],  # Parámetro de regularización (alpha)
        'regressor__l1_ratio': [0.3],  # Proporción entre L1 (Lasso) y L2 (Ridge)
    },
    # SVR
    "svr": {
        'regressor__kernel': ['rbf'],  # Kernel utilizado en el SVR
        'regressor__C': [2],  # Parámetro de regularización (C)
        'regressor__epsilon': [0.01],  # Tolerancia del margen de error
    },
    # RandomForestRegressor
    "rfr": {
        'regressor__n_estimators': [200],  # Número de árboles en el bosque
        'regressor__max_depth': [13],  # Profundidad máxima de los árboles
        'regressor__min_samples_split': [3],  # Número mínimo de muestras requeridas para dividir un nodo interno
    },
    # PolynomialFeatures - LinearRegression 
    "plr": {
        "poli__degree": 2
    }
}

a = write_yaml(path_model, parameters)
print(a)