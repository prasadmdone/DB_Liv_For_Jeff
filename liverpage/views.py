from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

classifier=joblib.load('./models/LiverModel.pkl')


def liverindex(request):
    temp={}
    temp['ageVal']=51
    temp['AlbVal']=2.70
    temp['AlkalineVal']=397.00
    temp['AlphaVal']=1898.00
    temp['AspartateVal']=298.00
    temp['CreatinineVal']=0.82
    temp['BilirubinVal']= 4.58
    temp['FerritinVal']=742.00
    temp['GammaVal']=433.00
    temp['HaemoglobinVal']=12.40
    temp['INRatioVal']=1.35
    temp['IronVal']=56.00
    temp['dimensionVal']= 2.10
    temp['NodulesVal']=1
    temp['AscitesVal']=2
    temp['EncefalopathyVal']=1
    temp['Performance_StatusVal']=3
    temp['Chronic_RenalVal']=0
    temp['DiabetesVal']=0
    temp['Hepatitis_BVal']=0
    temp['Liver_MetastasisVal']=0
    temp['Portal_VeinVal']=1
    temp['SymptomsVal']=1
    context ={'temp':temp}
    return render(request,'liver.html',context)
 #   return HttpResponse({'a':1})

def lpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['ageVal']=request.POST.get('ageVal')
        temp['AlbVal']=request.POST.get('AlbVal')
        temp['AlkalineVal']=request.POST.get('AlkalineVal')
        temp['AlphaVal']=request.POST.get('AlphaVal')
        temp['AspartateVal']=request.POST.get('AspartateVal')
        temp['CreatinineVal']=request.POST.get('CreatinineVal')
        temp['BilirubinVal']=request.POST.get('BilirubinVal')
        temp['FerritinVal']=request.POST.get('FerritinVal')
        temp['GammaVal']=request.POST.get('GammaVal')
        temp['HaemoglobinVal']=request.POST.get('HaemoglobinVal')
        temp['INRatioVal']=request.POST.get('INRatioVal')
        temp['IronVal']=request.POST.get('IronVal')
        temp['dimensionVal']=request.POST.get('dimensionVal')
        temp['NodulesVal']=request.POST.get('NodulesVal')
        temp['AscitesVal']=request.POST.get('AscitesVal')
        temp['EncefalopathyVal']=request.POST.get('EncefalopathyVal')
        temp['Performance_StatusVal']=request.POST.get('Performance_StatusVal')
        temp['Chronic_RenalVal']=request.POST.get('Chronic_RenalVal')
        temp['DiabetesVal']=request.POST.get('DiabetesVal')
        temp['Hepatitis_BVal']=request.POST.get('Hepatitis_BVal')
        temp['Liver_MetastasisVal']=request.POST.get('Hepatitis_BVal')
        temp['Portal_VeinVal']=request.POST.get('Portal_VeinVal')
        temp['SymptomsVal']=request.POST.get('SymptomsVal')
        #Datapreprocessing Convert the values to float
        Age=float(temp['ageVal'])
        Alb=float(temp['AlbVal'])
        Alkaline=float(temp['AlkalineVal'])
        Alpha=float(temp['AlphaVal'])
        Aspartate=float(temp['AspartateVal'])
        Creatinine=float(temp['CreatinineVal'])
        Bilirubin=float(temp['BilirubinVal'])
        Ferritin=float(temp['FerritinVal'])
        Gamma=float(temp['GammaVal'])
        Haemoglobin=float(temp['HaemoglobinVal'])
        INRatio=float(temp['INRatioVal'])
        Iron=float(temp['IronVal'])
        dimension=float(temp['dimensionVal'])
        Nodules=float(temp['NodulesVal'])
        Ascites=float(temp['AscitesVal'])
        Encefalopathy=float(temp['EncefalopathyVal'])
        Performance_Status=float(temp['Performance_StatusVal'])
        Chronic_Renal=float(temp['Chronic_RenalVal'])
        Diabetes=float(temp['DiabetesVal'])
        Hepatitis=float(temp['Hepatitis_BVal'])
        Liver_Metastasis=float(temp['Liver_MetastasisVal'])
        Portal_Vein=float(temp['Portal_VeinVal'])
        Symptoms=float(temp['SymptomsVal'])
        result = [Age,Alb,Alkaline,Alpha,Aspartate,Creatinine,Bilirubin,Ferritin,Gamma,Haemoglobin,INRatio,Iron,dimension,Nodules,Ascites,Encefalopathy,Performance_Status,Chronic_Renal,Diabetes,Hepatitis,Liver_Metastasis,Portal_Vein,Symptoms]
        #Passing data to model & loading the model from disks
        prediction = classifier.predict([result])[0]
      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        if prediction == 1 :
            context ={'a':'Liver Disease Prediction : Infected','temp':temp }
        else:
            context ={'a':'Liver Disease Prediction : Normal','temp':temp }
    return render(request,'liver.html',context)