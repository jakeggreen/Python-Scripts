import pandas as pd
import os
import re

directory = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(directory, 'sentences.xlsx')

df = pd.read_excel(file_path)

values = [7, 6, 'bang', ['decreased', 6]]

for x in zip(df['sentences'], values):
    i = 0
    for re.findall('\{\}', x[0])
    string = x[0].format(x[1])
    print(string)