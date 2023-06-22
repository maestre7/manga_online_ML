path_in_dict = {
    "book": "../data/raw/dataset_4.csv",
    "chapters": "../data/raw/dataset_chapters.csv",
    "multy_chapters": "../data/raw/dataset_multy_chapters.csv",
    "params": {
        "light": "../models/light/model_config.yaml",
        "medium": "../models/medium/model_config.yaml",
        "heavy": "../models/heavy/model_config.yaml",
    },
    "score": {
        "light": "../models/light/score.yaml",
        "medium": "../models/medium/score.yaml",
        "heavy": "../models/heavy/score.yaml",
    }
}

path_out_str = "../data/processed"

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

book_status_dict = {'FINALIZADO': 0, 'PUBLICÁNDOSE': 1, 'PAUSADO': 2, 'CANCELADO': 3}

light_list = ['score', 'read', 'pending', 'following', 'favorite', 'have', 'abandoned']
medium_list = ['demography_score', 'type_score', 'score', 'read', 'book_status_score', 
                                      'pending', 'following', 'favorite', 'have', 'abandoned', 
                                      'chapters_count']
heavy_list = ['synopsis', 'demography', 'type', 'name', 'genre', 'book_status', 'book_cover', 'uuid']