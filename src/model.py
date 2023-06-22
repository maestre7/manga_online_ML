#from pathlib import Path
import logging
import logging.config


# Own
from utils.utils import read_yaml
from variables import path_in_dict


logger = logging.getLogger(__name__)


class Model():

    def __init__(self):
        try:
            self.select_type_model()
        except Exception as err:
            print(err)

    def select_type_model(self):
        score_dict = {}
        try:
            for tipe_df, path in path_in_dict["score"].items():
                data = read_yaml(path)
                if data:
                    for model, score in data.items():
                        score_dict[f"{tipe_df}_{model}"] = score["MAE"]
            type_model = sorted(score_dict.items(), key=lambda x:x[1])[0][0]
            self.type_df, self.model = type_model.split("_")
        except Exception as err:
            msn = f"{__name__}-recover_score: {err}"
            logger.exception(msn)
            raise msn
        

if __name__ == '__main__':
    logging.config.fileConfig("./log/config/logger.ini", defaults={'filename': './log/mylog.log'}, disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    
    app = Model()
else:
    logger = logging.getLogger(__name__)

