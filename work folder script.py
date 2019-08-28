import pandas as pd
import os

#claims list is a list of the claim numbers as a string
for claim in claims_list:
    os.system("mkdir " + claim)
    for j in range (1):
        os.system("touch " +str(claim)+"/"+"Contentions"+".docx")