from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

#classifier=joblib.load('./models/hrmodel.pkl')
classifier=joblib.load('./models/Emp_Turnover.pkl')


def hrindex(request):
    temp={}
    temp['Satisfaction']=0.59
    temp['Evaluation']=1
    temp['ProjectCount']=4
    temp['AvgMonthlyHours']=275
    temp['YearsAtCompany']=3
    temp['Work_accident']=0
    temp['Promotion']= 0
    temp['Dep_IT']=0
    temp['Dep_RandD']=1
    temp['Dep_accounting']=0
    temp['Dep_hr']=0
    temp['Dep_management']=0
    temp['Dep_marketing']= 0
    temp['Dep_product_mng']= 0
    temp['Dep_sales']=0
    temp['Dep_support']=0
    temp['Dep_technical']=0
    temp['Sal_high']=0
    temp['Sal_low']= 0
    temp['Sal_medium']= 1
      
    context ={'temp':temp}
    return render(request,'hr.html',context)
 #   return HttpResponse({'a':1})

def hpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['Satisfaction']=request.POST.get('Satisfaction')
        temp['Evaluation']=request.POST.get('Evaluation')
        temp['ProjectCount']=request.POST.get('ProjectCount')
        temp['AvgMonthlyHours']=request.POST.get('AvgMonthlyHours')
        temp['YearsAtCompany']=request.POST.get('YearsAtCompany')
        temp['Work_accident']=request.POST.get('Work_accident')
        temp['Promotion']=request.POST.get('Promotion')
        temp['Dep_IT']=request.POST.get('Dep_IT')
        temp['Dep_RandD']=request.POST.get('Dep_RandD')
        temp['Dep_accounting']=request.POST.get('Dep_accounting')
        temp['Dep_hr']=request.POST.get('Dep_hr')
        temp['Dep_management']=request.POST.get('Dep_management')
        temp['Dep_marketing']=request.POST.get('Dep_marketing')
        temp['Dep_product_mng']=request.POST.get('Dep_product_mng')
        temp['Dep_sales']=request.POST.get('Dep_sales')
        temp['Dep_support']=request.POST.get('Dep_support')
        temp['Dep_technical']=request.POST.get('Dep_technical')
        temp['Sal_high']=request.POST.get('Sal_high')
        temp['Sal_low']=request.POST.get('Sal_low')
        temp['Sal_medium']=request.POST.get('Sal_medium')
        
        #Datapreprocessing Convert the values to float
       
        Satisfaction = float(temp['Satisfaction'])
        Evaluation = float(temp['Evaluation'])
        ProjectCount = float(temp['ProjectCount'])
        AvgMonthlyHours = float(temp['AvgMonthlyHours'])
        YearsAtCompany = float(temp['YearsAtCompany'])
        Work_accident = float(temp['Work_accident'])
        Promotion = float(temp['Promotion'])
        Dep_IT = float(temp['Dep_IT'])
        Dep_RandD = float(temp['Dep_RandD'])
        Dep_accounting = float(temp['Dep_accounting'])
        Dep_hr = float(temp['Dep_hr'])
        Dep_management = float(temp['Dep_management'])
        Dep_marketing = float(temp['Dep_marketing'])
        Dep_product_mng = float(temp['Dep_product_mng'])
        Dep_sales = float(temp['Dep_sales'])
        Dep_support = float(temp['Dep_support'])
        Dep_technical = float(temp['Dep_technical'])
        Sal_high = float(temp['Sal_high'])
        Sal_low = float(temp['Sal_low'])
        Sal_medium = float(temp['Sal_medium'])
        
   
        #result = [Age,Alb,Alkaline,Alpha,Aspartate,Creatinine,Bilirubin,Ferritin,Gamma,Haemoglobin,INRatio,Iron,dimension,Nodules,Ascites,Encefalopathy,Performance_Status,Chronic_Renal,Diabetes,Hepatitis,Liver_Metastasis,Portal_Vein,Symptoms]
        #Passing data to model & loading the model from disks
        result = pd.DataFrame(columns=['Satisfaction', 'Evaluation',
       'ProjectCount','AvgMonthlyHours', 'YearsAtCompany', 'Work_accident',
       'Promotion', 'Dep_IT', 'Dep_RandD',
       'Dep_accounting', 'Dep_hr', 'Dep_management', 'Dep_marketing',
       'Dep_product_mng','Dep_sales','Dep_support','Dep_technical','Sal_high','Sal_low','Sal_medium'])
        result = result.append({'Satisfaction':Satisfaction, 'Evaluation': Evaluation, 'ProjectCount':ProjectCount,
       'AvgMonthlyHours':AvgMonthlyHours, 'YearsAtCompany':YearsAtCompany, 'Work_accident':Work_accident,
       'Promotion':Promotion, 'Dep_IT':Dep_IT, 'Dep_RandD':Dep_RandD,
       'Dep_accounting':Dep_accounting, 'Dep_hr':Dep_hr, 'Dep_management':Dep_management, 'Dep_marketing':Dep_marketing,
       'Dep_product_mng':Dep_product_mng,'Dep_sales':Dep_sales,'Dep_support':Dep_support,'Dep_technical':Dep_technical,'Sal_high':Sal_high,'Sal_low':Sal_low,'Sal_medium':Sal_medium}, ignore_index=True)
        prediction = classifier.predict(result)[0]
      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        if prediction == 1 :
            context ={'a':'HR Analytics : Leaving','temp':temp }
        else:
            context ={'a':'HR Analytics : No Leaving','temp':temp }
    return render(request,'hr.html',context)