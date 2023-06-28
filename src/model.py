#from pathlib import Path
import logging
import logging.config

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split 

# Own
from utils.utils import read_yaml, write_yaml, write_pickle, bee
from variables import path_in_dict, data_columns


#logger = logging.getLogger(__name__)


class Model():

    def __init__(self):
        try:
            self.select_type_model()
            self.load_model()
            self.load_pipe()
            self.data_train_test_split()
            self.exec_grid()
        except Exception as err:
            print(err)
        finally:
            #bee()
            pass

    def select_type_model(self):
        score_dict = {}
        try:
            for tipe_df, path in path_in_dict["score"].items():
                data = read_yaml(path)
                if data:
                    for model, score in data.items():
                        if model != "rnn":
                            score_dict[f"{tipe_df}_{model}"] = score["MAE"]
            type_model = sorted(score_dict.items(), key=lambda x:x[1])[0][0]
            self.type_df, self.model = type_model.split("_")
        except Exception as err:
            msn = f"{__name__}-select_type_model: {err}"
            logger.exception(msn)
            raise msn
        
    def load_model(self):
        try:
            data = read_yaml(path_in_dict["params"][self.type_df])
            self.params = data[self.model]
            write_yaml("../models/model_config.yaml", self.params)
        except Exception as err:
            msn = f"{__name__}-load_model: {err}"
            logger.exception(msn)
            raise msn
        
    def load_pipe(self):
        try:
            model = {"rfr": RandomForestRegressor(), "en": ElasticNet()}

            if self.model == "plr":
                self.pipe = Pipeline([("poly", PolynomialFeatures()), ("regressor", LinearRegression())])
            elif self.model == "svr":
                self.pipe = Pipeline([("scaler",StandardScaler()), ("regressor", SVR())])
            else:
                self.pipe= Pipeline([("regressor", model[self.model])])

        except Exception as err:
            msn = f"{__name__}-load_pipe: {err}"
            logger.exception(msn)
            raise msn
        
    def data_train_test_split(self):
        try:
            # Cargamos los datos procesados
            data = pd.read_csv(f"../data/processed/{self.type_df}.csv")

            if self.type_df == "heavy":
                X = data.drop(["score"], axis=1)
            else:
                X = data[data_columns[self.type_df]]

            y = data["score"]

            self.X_train, X_test, self.y_train, y_test = train_test_split(X, y,
                                                                test_size=0.20,
                                                                random_state=777)
            
            self.X_train.to_csv("../data/train/x_train.csv")
            self.y_train.to_csv("../data/train/y_train.csv")
            X_test.to_csv("../data/test/x_test.csv")
            y_test.to_csv("../data/test/y_test.csv")

        except Exception as err:
            msn = f"{__name__}-data_train_test_split: {err}"
            logger.exception(msn)
            raise msn

        
    def exec_grid(self):
        try:
            model_gs = GridSearchCV(self.pipe, self.params, 
                                          cv=10,
                                          scoring="neg_mean_absolute_error",
                                          n_jobs=-1)
            
            model_gs.fit(self.X_train, self.y_train)

            write_pickle("../models/trained_model.pkl", model_gs.best_estimator_, )

        except Exception as err:
            msn = f"{__name__}-exec_grid: {err}"
            logger.exception(msn)
            raise msn

        

if __name__ == '__main__':
    logging.config.fileConfig("./log/config/logger.ini", defaults={'filename': './log/mylog.log'}, disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    
    app = Model()
else:
    logger = logging.getLogger(__name__)

