import pandas as pd
import numpy as np

data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

pd.DataFrame(data)
df = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])

print(df.head())