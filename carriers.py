import pandas as pd
import interface

bgxp = []
#data = pd.ExcelFile(r'C:\Users\us\Desktop\grauation project\Deliveries 12-3-2017.xlsx') 
data = pd.concat(pd.read_excel('Deliveries 12-3-2017.xlsx', sheet_name=None), ignore_index=True)
cr = pd.DataFrame(data, columns= ['Carrier'])
rf = pd.DataFrame(data, columns= ['Ref/Lic Nr'])
#Locks data from column 
amtg = data.loc[data.Carrier=='AMTG', 'Ref/Lic Nr']
bgxp = data.loc[data.Carrier=='BGXP', 'Ref/Lic Nr']
dtcv = data.loc[data.Carrier=='DTCV', 'Ref/Lic Nr']
#prints list without index
 
amtg1=(amtg.to_string(index=False, header=False))
bgxp1=(bgxp.to_string(index=False, header=False))
dtcv1=(dtcv.to_string(index=False, header=False))
