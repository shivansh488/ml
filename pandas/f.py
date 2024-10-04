import numpy as np
import pandas as pd
from IPython.display import display
dict1={
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]

}
df=pd.DataFrame(dict1)
display(df)
df.to_csv('friends.csv',index=False)
display(df.describe)

