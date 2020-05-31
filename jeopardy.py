import pandas as pd
import numpy as np


pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')


#def find_in_question (words, df):
    #questions = df[df.question.isin(words)]
    #return questions

jeopardy['float_values'] = jeopardy.value.split('$')[-1]

print(values)