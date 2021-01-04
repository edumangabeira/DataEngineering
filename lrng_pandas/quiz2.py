import pandas as pd
import numpy as np

pd.set_option('precision', 1)
books = pd.Series(data=['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine',
                        'Alice in Wonderland'])
authors = pd.Series(data=['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells',
                          'Lewis Carroll'])

user_1 = pd.Series(data=[3.2, np.nan, 2.5])
user_2 = pd.Series(data=[5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data=[2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data=[4, 3.5, 4, 5, 4.2])

dat = {'book': books, 'author': authors, 'user_1': user_1, 'user_2': user_2, 'user_3': user_3,
       'user_4': user_4}

book_ratings = pd.DataFrame(dat)

book_ratings.fillna(book_ratings.mean(), inplace=True)

print(book_ratings)
