# import openpyxl 
  
# wb = openpyxl.load_workbook("esp6salt_pepper.xlsx") 
  
# sheet = wb.active 
  

userName = "Atharva"
simplehash = "simplehashAedtfb23"
saltHash = "simpsaltHashshAedtfb23"
pepperHash = "simpepperHashfb23"

data = [
    (userName, simplehash, saltHash, pepperHash)
]
  
# for row in data:
#     sheet.append(row)
    
# wb.save('esp6salt_pepper.xlsx')


import pandas as pd
data =pd.from_csv("data.csv")

data = pd.DataFrame(data)
data.to_csv("data.csv")

data.add()