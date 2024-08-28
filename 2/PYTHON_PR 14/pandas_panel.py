# pandas_panel   * error
import pandas as pd
import numpy as np
data= {'Data1':pd.DataFrame(np.random.randn(2,4)), 'Data2': pd.DataFrame(np.random.randn(3,2))}
df= pd.Panel(data)
print(df)