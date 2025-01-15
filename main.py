import pandas as pd
 
import fromArfftoCsv as convert

# convert.getCSVFromArff("nsl-kdd/KDDTest+")

filename = './KDDTest+.csv'

kdd_file = pd.read_csv(filename)

row_count = len(kdd_file.index)
column_count  = len(kdd_file.columns)

# row amount  = 22544
print(row_count)
print(column_count)