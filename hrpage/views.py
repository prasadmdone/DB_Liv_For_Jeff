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
    temp['Salary']=0
    
      
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
        temp['Department']=request.POST.get('Department')
        temp['Salary']=request.POST.get('Salary')
        
        
        #Datapreprocessing Convert the values to float
       
        Satisfaction = float(temp['Satisfaction'])
        Evaluation = float(temp['Evaluation'])
        ProjectCount = float(temp['ProjectCount'])
        AvgMonthlyHours = float(temp['AvgMonthlyHours'])
        YearsAtCompany = float(temp['YearsAtCompany'])
        Work_accident = float(temp['Work_accident'])
        Promotion = float(temp['Promotion'])
        Department = temp['Department']
        Salary = temp['Salary']
        Dep_IT = 0
        Dep_RandD = 0
        Dep_accounting = 0
        Dep_hr = 0
        Dep_management = 0
        Dep_marketing = 0
        Dep_product_mng = 0
        Dep_sales = 0
        Dep_support = 0
        Dep_technical = 0
        if Department==0:
            Dep_IT=1
        elif Department==1:
            Dep_RandD=1
        elif Department==2:
            Dep_accounting=1
        elif Department==3:
            Dep_hr=1
        elif Department==4:
            Dep_management=1
        elif Department==5:
            Dep_marketing=1
        elif Department==6:
            Dep_product_mng=1
        elif Department==7:
            Dep_sales=1
        elif Department==8:
            Dep_support=1
        else:
            Dep_technical=1
        Sal_high=0
        Sal_low=0
        Sal_medium=0
        if Salary==0:
            Sal_low=1
        elif Salary==1:
            Sal_medium=1
        else:
            Sal_high=1     
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