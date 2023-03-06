"""Calculate TPR, FPR, TNR, FNR based on predictions and labels
"""

import random
import datetime
import numpy as np
import h5py
import math
import os
import sys


def performance(all_preds, all_labels):
    TP = TN = FP = FN = 0 # Initialize variables
    TPR = FNR = prec = BA = []
    a = np.where(all_labels == all_preds)[0] #prediction was correct
    for aa in range(len(a)):
        element = a[aa]
        if all_labels[element] == 1: #if the label was true
            TP += 1
        if all_labels[element] == 0: #if the label was false
            TN += 1


    a = np.where(all_labels != all_preds)[0] #prediction was incorrect
    for aa in range(len(a)):
        element = a[aa]
        if all_labels[element] == 1: #if the label was true
            FN += 1
        if all_labels[element] == 0: #if the label was false
            FP += 1

    # ## Calculate TPR and FPR
    Accuracy = (TP + TN)/(len(all_preds))
    
    FPR = FP / (FP + TN) #fall-out: incorrect positives over all actual negatives
    TNR = TN / (TN + FP) #specificity, selectivity, or true negative rate

    # If sample has true positives
    if TP != 0: 
        TPR = TP / (TP + FN) #sensitivity/recall: correct positives over all actual positives
        FNR = FN / (FN + TP) #miss rate or false negative rate
        prec = TP / (TP + FP) #prevision or positive predictive value (PPV)
        BA = (TPR + TNR) / 2 #balanced accuracy
        F1 = (2*prec*TPR) / (prec + TPR)
    return FPR, TNR, TPR, FNR, Accuracy, prec, BA, TP
    