from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

classifier=joblib.load('./models/FraudModel.pkl')


def fraudindex(request):
    temp={}
    temp['AMT_GOODS_PRICEVal']=463500
    temp['REGION_POPULATION_RELATIVEVal']=0.035792
    temp['DAYS_EMPLOYEDVal']=365243
    temp['FLAG_EMP_PHONEVal']=0
    temp['REGION_RATING_CLIENTVal']=2
    temp['REGION_RATING_CLIENT_W_CITYVal']=2
    temp['REG_CITY_NOT_LIVE_CITYVal']= 0
    temp['REG_CITY_NOT_WORK_CITYVal']=0
    temp['EXT_SOURCE_1Val']=0.524685
    temp['EXT_SOURCE_2Val']=0.358568
    temp['EXT_SOURCE_3Val']=0.56383
    temp['FLOORSMAX_AVGVal']=0.1667
    temp['FLOORSMAX_MODEVal']= 0.1667
    temp['FLOORSMAX_MEDIVal']= 0.1667
    temp['FLAG_DOCUMENT_3Val']=1
    temp['CODE_GENDER_MVal']=0
    temp['PensionerVal']=1
    temp['WorkingVal']=0
    temp['Higher_educationVal']=0
    temp['secondary_specialVal']=1
   
    context ={'temp':temp}
    return render(request,'fraud.html',context)
 #   return HttpResponse({'a':1})

def fpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['AMT_GOODS_PRICEVal']=request.POST.get('AMT_GOODS_PRICEVal')
        temp['REGION_POPULATION_RELATIVEVal']=request.POST.get('REGION_POPULATION_RELATIVEVal')
        temp['DAYS_EMPLOYEDVal']=request.POST.get('DAYS_EMPLOYEDVal')
        temp['FLAG_EMP_PHONEVal']=request.POST.get('FLAG_EMP_PHONEVal')
        temp['REGION_RATING_CLIENTVal']=request.POST.get('REGION_RATING_CLIENTVal')
        temp['REGION_RATING_CLIENT_W_CITYVal']=request.POST.get('REGION_RATING_CLIENT_W_CITYVal')
        temp['REG_CITY_NOT_LIVE_CITYVal']=request.POST.get('REG_CITY_NOT_LIVE_CITYVal')
        temp['REG_CITY_NOT_WORK_CITYVal']=request.POST.get('REG_CITY_NOT_WORK_CITYVal')
        temp['EXT_SOURCE_1Val']=request.POST.get('EXT_SOURCE_1Val')
        temp['EXT_SOURCE_2Val']=request.POST.get('EXT_SOURCE_2Val')
        temp['EXT_SOURCE_3Val']=request.POST.get('EXT_SOURCE_3Val')
        temp['FLOORSMAX_AVGVal']=request.POST.get('FLOORSMAX_AVGVal')
        temp['FLOORSMAX_MODEVal']=request.POST.get('FLOORSMAX_MODEVal')
        temp['FLOORSMAX_MEDIVal']=request.POST.get('FLOORSMAX_MEDIVal')
        temp['FLAG_DOCUMENT_3Val']=request.POST.get('FLAG_DOCUMENT_3Val')
        temp['CODE_GENDER_MVal']=request.POST.get('CODE_GENDER_MVal')
        temp['PensionerVal']=request.POST.get('PensionerVal')
        temp['WorkingVal']=request.POST.get('WorkingVal')
        temp['Higher_educationVal']=request.POST.get('Higher_educationVal')
        temp['secondary_specialVal']=request.POST.get('secondary_specialVal')
        #Datapreprocessing Convert the values to float
   
        #result = [Age,Alb,Alkaline,Alpha,Aspartate,Creatinine,Bilirubin,Ferritin,Gamma,Haemoglobin,INRatio,Iron,dimension,Nodules,Ascites,Encefalopathy,Performance_Status,Chronic_Renal,Diabetes,Hepatitis,Liver_Metastasis,Portal_Vein,Symptoms]
        #Passing data to model & loading the model from disks
        result = pd.DataFrame(columns=['AMT_GOODS_PRICE', 'REGION_POPULATION_RELATIVE', 'DAYS_EMPLOYED',
       'FLAG_EMP_PHONE', 'REGION_RATING_CLIENT', 'REGION_RATING_CLIENT_W_CITY',
       'REG_CITY_NOT_LIVE_CITY', 'REG_CITY_NOT_WORK_CITY', 'EXT_SOURCE_1',
       'EXT_SOURCE_2', 'EXT_SOURCE_3', 'FLOORSMAX_AVG', 'FLOORSMAX_MODE',
       'FLOORSMAX_MEDI', 'FLAG_DOCUMENT_3', 'CODE_GENDER_M',
       'NAME_INCOME_TYPE_Pensioner', 'NAME_INCOME_TYPE_Working',
       'NAME_EDUCATION_TYPE_Higher_education',
       'NAME_EDUCATION_TYPE_Secondary_/_secondary_special'])
        result = result.append({'AMT_GOODS_PRICE':float(temp['AMT_GOODS_PRICEVal']), 'REGION_POPULATION_RELATIVE': float(temp['REGION_POPULATION_RELATIVEVal']), 'DAYS_EMPLOYED':float(temp['DAYS_EMPLOYEDVal']),
       'FLAG_EMP_PHONE':float(temp['FLAG_EMP_PHONEVal']), 'REGION_RATING_CLIENT':float(temp['REGION_RATING_CLIENTVal']), 'REGION_RATING_CLIENT_W_CITY':float(temp['REGION_RATING_CLIENT_W_CITYVal']),
       'REG_CITY_NOT_LIVE_CITY':float(temp['REG_CITY_NOT_LIVE_CITYVal']), 'REG_CITY_NOT_WORK_CITY':float( temp['REG_CITY_NOT_WORK_CITYVal']), 'EXT_SOURCE_1':float(temp['EXT_SOURCE_1Val']),
       'EXT_SOURCE_2':float(temp['EXT_SOURCE_2Val']), 'EXT_SOURCE_3':float(temp['EXT_SOURCE_3Val']), 'FLOORSMAX_AVG':float(temp['FLOORSMAX_AVGVal']), 'FLOORSMAX_MODE':float(temp['FLOORSMAX_MODEVal']),
       'FLOORSMAX_MEDI':float(temp['FLOORSMAX_MEDIVal']), 'FLAG_DOCUMENT_3':float(temp['FLAG_DOCUMENT_3Val']), 'CODE_GENDER_M':float(temp['CODE_GENDER_MVal']),
       'NAME_INCOME_TYPE_Pensioner':float(temp['PensionerVal']), 'NAME_INCOME_TYPE_Working':float(temp['WorkingVal']),
       'NAME_EDUCATION_TYPE_Higher_education':float(temp['Higher_educationVal']),
       'NAME_EDUCATION_TYPE_Secondary_/_secondary_special':float(temp['secondary_specialVal'])}, ignore_index=True)
        prediction = classifier.predict(result)[0]
      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        if prediction == 1 :
            context ={'a':'Fraud Analytics : Fraud','temp':temp }
        else:
            context ={'a':'Fraud Analytics : Not Fraud','temp':temp }
    return render(request,'fraud.html',context)