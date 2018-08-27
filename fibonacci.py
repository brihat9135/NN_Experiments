#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 02:54:12 2018

@author: cs
"""

import pandas as pd
from sklearn.model_selection import train_test_split

class ProcessData:
    
    def Fibonacci(self, n):
        
        if n<0:
            print("non negative inputs please!!")
        
        elif n == 1:
            return 0
    
        elif n == 2:
            return 1
        
        else:
            return PD.Fibonacci(n-1) + PD.Fibonacci(n-2)
        
        
    def list_Fibonaccis(self, x):
        fibonacci_numbers = [0, 1]
        x_train = [1, 2]
        for i in range(2, x):
            x_train.append(i+1)
            fibonacci_numbers.append(float(fibonacci_numbers[i-1]+fibonacci_numbers[i-2]))
        patient_df = pd.DataFrame({"X_train" : x_train, "y_train" : fibonacci_numbers})
        return patient_df
    

if __name__ == '__main__':

    PD = ProcessData()
    patient_df = PD.list_Fibonaccis(1477)             #gives infinity beyond 1477, better solution?
   
    X_train1, X_test = train_test_split(patient_df, test_size = 0.2, random_state=42)
    X_train, X_val = train_test_split(X_train1, test_size = 0.2, random_state=42)
    print(X_train)
    print(X_train.shape)
    
    
    
    
    
    
    