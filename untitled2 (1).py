# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aK7vDhvzD69280myIE7EeOJ9iV9RvrUH
"""

import pandas as pd
baza={
 "FISH": ["Murotjonov Bekzod", "Erkinov Alisher", "Yunusaliyev Behruz", "Muhammadov Azizbek", "Yusupov Dilyorbek", "Mahsudov Zikrillo", "Abdusalimov Muhammadali"     ],
 "GURUH": ["614-23","612-23","614-23","614-23","614-23","614-23","614-23"],
 "MANZILI": ["Soylabi","GAmbay","soylabi","Beshariq","Yaypan","Dangara","Vadil"],
 "JINSI": ["erkak","erkak","erkak","erkak","erkak","erkak","erkak"],

}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['GURUH']=='614-23']
print(filtr)