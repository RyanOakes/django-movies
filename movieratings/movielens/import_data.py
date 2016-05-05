import pandas as pd

def import_data():

    with open('../data/user_ratings.csv') as f:
        user_ratings = pd.read_csv(f, delimiter='\t')

    with open('../data/movie_data.csv', 'r', encoding='latin_1') as f:
        movie_data = pd.read_csv(f, delimiter='|')

    with open('../data/rater_info.csv') as f:
        rater_info = pd.read_csv(f, delimiter='|')

    print(user_ratings)
    return user_ratings, movie_data, rater_info

import_data()
