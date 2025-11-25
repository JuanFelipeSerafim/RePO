##TA INCOMPLETO!

import os
import pandas as pd

actualPath='$HOME/novoDataset'
for dataset in os.listdir(actualPath):
    df=pd.read_csv(actualPath+dataset)
    
    df.columns = df.columns.str.strip()
    df.drop(columns=['Inbound','SimillarHTTP','Fwd Header Length.1'],inplace=True)
    df.to_csv(actualPath+dataset,mode='w')
    
    del df
    