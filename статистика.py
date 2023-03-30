'''Расчёт моды, медианы и среднего с помощью библиотек numpy и scipy'''
import numpy as np
from scipy import stats
sample = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
# в numpy почему-то нет моды

print('median:', np.median(sample))
print('mean:', np.mean(sample))
'''Расчёт моды, медианы и среднего с помощью библиотеки pandas'''
import pandas as pd
sample = pd.Series([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

print('mode:', sample.mode())
print('median:', sample.median())
print('mean:', sample.mean())

# df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C'],
#  'points': [1, 5, 2, 7, 1, 9, 3, 8, 5, 9],
#  'assists': [5, 7, 7, 9, 12, 9, 9, 4],
#  'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C','c','c'],
 'points': [1, 5, 2, 7, 1, 9, 3, 8, 5, 9],
 'assists': [5, 7, 7, 9, 12, 9, 9, 4,3,3],
 'rebounds': [11, 8, 10, 6, 6, 5, 9, 12,3,3]})
print(df['points'].std())