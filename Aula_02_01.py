import pandas as pd
nota_01 = pd.Series([100,50,40,30,80])
nota_02 = pd.Series([60,20,90,40,10])
media = (nota_01 + nota_02) / 2
print(media)
