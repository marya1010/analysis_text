# -*- coding: utf-8 -*-
"""Практикум_подсчёт-слов.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LPp8r3gm3c780kXIdD-LAWXpjAf0G6lh
"""

import numpy as np
import pandas as pd
import io
from collections import Counter
import seaborn as sns

with io.open('Уэллс_-_Война_миров.txt','r',encoding='windows-1251') as f:
    text = f.read()

text

text = text.replace('\n',' ',text.count('\n'))

text

text = text.replace('\xa0','',text.count('\xa0'))

text

words = Counter(text.split(' '))

words

sorted_words = sorted(words.items(), key=lambda item: item[1], reverse=True)

sorted_words

sorted1 = sorted_words[0:20]

sorted1

len(sorted1)

a = []
b = []
for i in range(len(sorted1)):
    a.append(sorted1[i][0])
    b.append(sorted1[i][1])
df = pd.DataFrame({'Word':a,'Number':b})

df

sns.histplot(x=df['Word'], y = df['Number'])

with io.open('/content/Уэллс_-_Война_миров.txt','r',encoding='windows-1251') as f:
    text = f.read()

text.count('\n') #число строк

sum(words.values()) #Число слов

len(text) #Число символов с пробелами

len(text.replace('\n','').replace(' ','')) #Число символов без пробелов

words.keys()

