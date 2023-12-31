
from pathlib import Path
import logging
import logging.config

import pandas as pd

#Own
from utils.utils import bee
from variables import path_in_dict, path_out_str, genre_list, book_status_dict
from variables import data_columns


class Data_Processing():
    """
    A class for data processing operations.
    """
    
    def __init__(self, path_in: dict , path_out: str ):
        """
        Initializes the Data_Processing object.

        Args:
            path_in (dict): Dictionary containing input file paths.
            path_out (str): Output directory path.
        """
        self.path_in = path_in 
        self.path_out = path_out

        try:
            self.init_processing()
            self.chapters_process()
            #self.genre_process()
            self.genre_score_process()
            self.type_and_demography_to_score()
            self.tdg_score()
            self.book_status_to_score()
            self.data_out()
        except Exception as err:
            print(err)
        finally:
            bee()

    def init_processing(self):
        """
        Performs initialization and reads input data files.
        """
        try:
            self.book_df = pd.read_csv(self.path_in["book"], index_col="Unnamed: 0")
            self.chapters_df = pd.read_csv(self.path_in["chapters"], index_col="Unnamed: 0")
            self.multy_chapters_df = pd.read_csv(self.path_in["multy_chapters"], index_col="Unnamed: 0")
        except Exception as err:
            msn = f"{__name__}-init_processing: {err}"
            logging.exception(msn)
            raise msn

    def chapters_process(self):
        """
        Processes chapter data and creates a new DataFrame with chapter count.
        """
        try:
            total_chapters_df = pd.concat([self.chapters_df, self.multy_chapters_df])
            chapters_count = total_chapters_df.groupby(["uuid"])["uuid"].count()
            chapters_count_df = pd.DataFrame({"chapters_count": chapters_count})
            self.data_df = self.book_df.join(chapters_count_df, on='uuid')
            self.data_df['chapters_count'] = self.data_df['chapters_count'].fillna(0)
        except Exception as err:
            msn = f"{__name__}-chapters_process: {err}"
            logging.exception(msn)
            raise msn

    def genre_process(self):
        """
        Processes genre data and converts boolean values to 0 or 1.
        """
        try:
            for genre in genre_list:
                self.data_df[genre] = self.data_df[genre].replace({ True: 1, False: 0 })
        except Exception as err:
            msn = f"{__name__}-genre_process: {err}"
            logging.exception(msn)  
            raise msn     
        
    def genre_score_process(self):
        """
        Processes genre data and converts boolean values to mean score.
        """
        try:
            for genre in genre_list:
                mean_score_by_genre = self.data_df.groupby(genre)['score'].mean()           
                self.data_df[f'{genre}_score'] = self.data_df[genre].replace({ True: mean_score_by_genre[1], False: 0 })
        except Exception as err:
            msn = f"{__name__}-genre_score_process: {err}"
            logging.exception(msn)  
            raise msn     

    def type_and_demography_to_score(self):
        """
        Calculates mean scores by type and demography and assigns them to respective columns.
        """
        try:
            mean_scored = self.data_df['score'].mean()

            mean_score_by_type = self.data_df.groupby('type')['score'].mean()
            self.data_df['type_score'] = self.data_df['type'].map(mean_score_by_type).fillna(mean_scored)

            mean_score_by_demography = self.data_df.groupby('demography')['score'].mean()
            self.data_df['demography_score'] = self.data_df['demography'].map(mean_score_by_demography).fillna(mean_scored)
        except Exception as err:
            msn = f"{__name__}-type_and_demography_to_score: {err}"
            logging.exception(msn)
            raise msn
        
    def mean_row(self, row):
        try:
            lst = [e for e in row if e != 0]
            avg = sum(lst) / len(lst)
            return avg
        except Exception as err:
            msn = f"{__name__}-mean_row: {err}"
            logging.exception(msn)
            raise msn
        
    def tdg_score(self):
        try:
            score_df = self.data_df[[col for col in self.data_df.columns if 'score' in col]]
            self.data_df["tdg"] = score_df.apply(self.mean_row, axis=1);
        except Exception as err:
            msn = f"{__name__}-tdg_score: {err}"
            logging.exception(msn)
            raise msn

        
    def book_status_to_score(self):
        """
        Maps book status to corresponding scores.
        """
        try:
            self.data_df['book_status_score'] = self.data_df['book_status'].map(book_status_dict)
        except Exception as err:
            msn = f"{__name__}-book_status_to_score: {err}"
            logging.exception(msn)
            raise msn

        
    def data_out(self):
        """
        Writes processed data to output files.
        """
        try:
            light_df = self.data_df[data_columns["light"]]
            medium_df = self.data_df[data_columns["medium"]]
            heavy_df = self.data_df.drop(data_columns["heavy"], axis=1)

            light_df.to_csv(Path(f"{path_out_str}/light.csv"))
            medium_df.to_csv(Path(f"{path_out_str}/medium.csv"))
            heavy_df.to_csv(Path(f"{path_out_str}/heavy.csv"))
        except Exception as err:
            msn = f"{__name__}-data_out: {err}"
            logging.exception(msn)
            raise msn
        

if __name__ == '__main__':
    logging.config.fileConfig("./log/config/logger.ini", defaults={'filename': './log/mylog.log'}, disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    
    app = Data_Processing(path_in_dict, path_out_str)
else:
    logger = logging.getLogger(__name__)