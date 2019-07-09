# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:13:39 2019

@author: VAAKASH
"""


from patientFunctions import PatientFunctions


if __name__ == "__main__":
    
    pf = PatientFunctions()
    
    #First Time 
    pf.firstRead("../Files/inputPS5a.txt")
    
    #OutPut File
    pf.firstWrite("../Files/outputPS5.txt")
    
    #Second Read
    pf.SecondRead("../Files/inputPS5b.txt","../Files/outputPS5.txt")