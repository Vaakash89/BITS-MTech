# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:05:27 2019

@author: VAAKASH
"""

from patientRecord import PatientRecord

class PatientFunctions:
    def __init__(self):
        self.head=None
        self.counter = 1000
        self.patients = []

    
    def registerPatient(self, name, age):
        pid = self.counter
        new_patient = PatientRecord(age, name, pid)
        if self.head == None:
            self.head = new_patient
        else:
            n = self.head
            while n.right is not None:
                n = n.right
            n.right = new_patient
            new_patient.left = n
            new_patient.right = None
        
        self.enqueuePatient(new_patient.PatId)
        self.counter = self.counter + 1
        

    def enqueuePatient(self, PatId):
        
        self.patients.append([PatId])
        self.fullHeap()
    
    def dequeuePatient(self, PatId):
        temp = self.head
        self.head = self.head.right
        self.head.left = None
        temp.right = None
        self.patients = self.patients[1:]
        return temp
    
    def getAge(self,n):
        return n[0][-2:]
        
    def heapify(self, arr, n, i): 
        largest = i 
        l = 2 * i + 1     
        r = 2 * i + 2 

        if l < n and self.getAge(arr[i]) < self.getAge(arr[l]):
            largest = l 
        if r < n and self.getAge(arr[largest]) < self.getAge(arr[r]): 
            largest = r 
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] #swap
            self.heapify(arr, n, largest) 
        
    def fullHeap(self):
        for i in range(int(len(self.patients)/2)-1,-1,-1):
            self.heapify(self.patients, len(self.patients),i)    
    
    def getPatientDetails(self, iD):
        n=self.head
        name=""
        patid=""
        while n is not None:
            if(n.PatId == iD):
                name = n.name
                patid = n.PatId
            n=n.right
        return patid,name
    
    def nextPatient(self):
        self.getPatientDetails(self.patients[0])
        
    
    def firstRead(self,fileName):
        f = open(fileName, "r")
        for x in f:
            self.registerPatient(x.split(",")[0],(x.split(",")[1]).rstrip("\n\r").lstrip(" "))
    
    def writePatientDetails(self,fileName):
        f= open(fileName,"a+")
        f.write("Refreshed queue: \r\n") 
        
        n=len(self.patients)
        dummy = self.patients[:]
        
        #HeapSort
        for i in range(n-1, -1, -1): 
            dummy[i], dummy[0] = dummy[0], dummy[i] # swap
            f.write(self.getPatientDetails(dummy[i][0])[0]+","+self.getPatientDetails(dummy[i][0])[1]+"\r\n")
            self.heapify(dummy, i, 0 )             
        f.close()
            
    def firstWrite(self,fileName):
        f= open(fileName,"w+")
        f.write("--- initial queue ---------------\r\n")
        f.write("No of patients added: "+str(len(self.patients))+"\r\n")
        f.close()        
        self.writePatientDetails(fileName)
        
        

    def SecondRead(self,inputFile,outputFile):
        f1 = open(inputFile, "r")
        for x in f1:
            y = x.split(":")
            task = y[0].rstrip("\n\r").lstrip(" ")
            if len(x.split(":")) > 1:
                name = (y[1].split(",")[0]).rstrip("\n\r").lstrip(" ")
                age = (y[1].split(",")[1]).rstrip("\n\r").lstrip(" ")
        
            if (task == "newPatient"):
                self.registerPatient(name, age)
                f= open(outputFile,"a+")
                f.write("---------------------------\r\n")
                f.write("---new patient entered-----\r\n")
                f.write("Patient details: " + name+", " + age+"\r\n")
                f.close()        
                self.writePatientDetails(outputFile)
        
            if (task == "nextPatient"):
                f= open(outputFile,"a+")
                f.write("---------------------------\r\n")
                f.write("---next patient -----------\r\n")
                f.write("Next patient for consulation is: " + self.getPatientDetails(self.patients[0][0])[0]+", " + self.getPatientDetails(self.patients[0][0])[1]+"\r\n")
                f.close()        
                temp = self.dequeuePatient(self.patients[0][0])
        f1.close()
        



