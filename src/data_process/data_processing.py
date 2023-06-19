
from pathlib import Path
import logging
import logging.config

import pandas as pd


path_in_dict = {
    "book": "../data/raw/dataset_4.csv",
    "chapters": "../data/raw/dataset_chapters.csv",
    "multy_chapters": "../data/raw/dataset_multy_chapters.csv"
}

path_out_str = "../../data/processd"

genre_list = ['Magia', 'Mecha', 'Demonios',
       'Género Bender', 'Realidad Virtual', 'Drama', 'Niños', 'Guerra',
       'Harem', 'Vampiros', 'Horror', 'Acción', 'Realidad', 'Traps', 'Militar',
       'Crimen', 'Recuentos de la vida', 'Apocalíptico', 'Psicológico',
       'Misterio', 'Musica', 'Extranjero', 'Samurái', 'Girls Love',
       'Telenovela', 'Policiaco', 'Animación', 'Parodia', 'Deporte',
       'Supervivencia', 'Aventura', 'Oeste', 'Superpoderes', 'Ecchi',
       'Tragedia', 'Fantasia', 'Gore', 'Boys Love', 'Reencarnación',
       'Sobrenatural', 'Vida Escolar', 'Historia', 'Romance',
       'Ciencia Ficción', 'Thriller', 'Ciberpunk', 'Artes Marciales',
       'Comedia', 'Familia']

class Data_Processing():
    
    def init(self, path_in: dict , path_out: str ):
        self.path_in = path_in 
        self.path_out = path_out

        try:
            self.init_processing()
            self.chapters_process()
            self.genre_process()
            # type - demo - status

            self.data_out()
        except Exception as err:
            logger.exception(err)

    def init_processing(self):
        try:
            self.book_df = pd.read_csv(self.path_in.book, index_col="Unnamed: 0")
            self.chapters_df = pd.read_csv(self.path_in.chapters, index_col="Unnamed: 0")
            self.multy_chapters_df = pd.read_csv(self.path_in.multy_chapters, index_col="Unnamed: 0")
        except Exception as err:
            raise(f"{__name__}-init_processing: {err}")

    def chapters_process(self):
        try:
            total_chapters_df = pd.concat([self.chapters_df, self.multy_chapters_df])
            chapters_count = total_chapters_df.groupby(["uuid"])["uuid"].count()
            chapters_count_df = pd.DataFrame({"chapters_count": chapters_count})
            self.data_df = self.book_df.join(chapters_count_df, on='uuid')
            self.data_df['chapters_count'] = self.data_df['chapters_count'].fillna(0)
        except Exception as err:
            raise(f"{__name__}-chapters_process: {err}")

    def genre_process(self):
        try:
            for genre in genre_list:
                self.data_df[genre].where(self.data_df[genre], 1, 0)
        except Exception as err:
            raise(f"{__name__}-genre_process: {err}")
        
    def data_out(self): ###
        try:
            light_df = self.data_df[['score', 'read', 'pending', 'following', 'favorite', 'have', 'abandoned']]
            medium_df = self.data_df[['demography', 'type', 'score', 'read', 
                                      'pending', 'following', 'favorite', 'have', 'abandoned', 
                                      'chapters_count']]
            heavy_df = self.data_df.drop(['synopsis', 'genre', 'book_cover', 'uuid'])
        except Exception as err:
            raise(f"{__name__}-data_out: {err}")
        



if __name__ == '__main__':
    logging.config.fileConfig("../log/config/logger.ini", defaults={'filename': '../log/mylog.log'},disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    app = Data_Processing(path_in_dict, path_out_str)
else:
    logger = logging.getLogger(__name__)