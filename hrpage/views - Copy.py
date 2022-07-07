from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

classifier=joblib.load('./models/hrmodel.pkl')


def hrindex(request):
    temp={}
    temp['efficiency_low']=0
    temp['efficiency_verylow']=0
    temp['satisfaction_level_bin_0.00_.11']=1
    temp['satisfaction_level_bin_0.92_1.0']=0
    temp['attitude_normal']=0
    temp['attitude_unhappy']=0
    temp['attitude_veryhappy']= 0
    temp['attitude_veryunhappy']=1
    temp['time_spend_company_cat_nodeparture']=0
    temp['time_spend_company_cat_veryhighdeparture']=0
    temp['number_project_cat_extreme']=0
    temp['workload_extreme']=0
    temp['workload_normal']= 0
    temp['average_montly_hours_bin_287_310']= 0
      
    context ={'temp':temp}
    return render(request,'hr.html',context)
 #   return HttpResponse({'a':1})

def hpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['efficiency_low']=request.POST.get('efficiency_low')
        temp['efficiency_verylow']=request.POST.get('efficiency_verylow')
        temp['satisfaction_level_bin_0_11']=request.POST.get('satisfaction_level_bin_0_11')
        temp['satisfaction_level_bin_092_1']=request.POST.get('satisfaction_level_bin_092_1')
        temp['attitude_normal']=request.POST.get('attitude_normal')
        temp['attitude_unhappy']=request.POST.get('attitude_unhappy')
        temp['attitude_veryhappy']=request.POST.get('attitude_veryhappy')
        temp['attitude_veryunhappy']=request.POST.get('attitude_veryunhappy')
        temp['time_spend_company_cat_nodeparture']=request.POST.get('time_spend_company_cat_nodeparture')
        temp['time_spend_company_cat_veryhighdeparture']=request.POST.get('time_spend_company_cat_veryhighdeparture')
        temp['number_project_cat_extreme']=request.POST.get('number_project_cat_extreme')
        temp['workload_extreme']=request.POST.get('workload_extreme')
        temp['workload_normal']=request.POST.get('workload_normal')
        temp['average_montly_hours_bin_287_310']=request.POST.get('average_montly_hours_bin_287_310')
        
        #Datapreprocessing Convert the values to float
       
        efficiency_low = float(temp['efficiency_low'])
        efficiency_verylow = float(temp['efficiency_verylow'])
        satisfaction_level_bin_0_11 = float(temp['satisfaction_level_bin_0_11'])
        satisfaction_level_bin_092_1 = float(temp['satisfaction_level_bin_092_1'])
        attitude_normal = float(temp['attitude_normal'])
        attitude_unhappy = float(temp['attitude_unhappy'])
        attitude_veryhappy = float(temp['attitude_veryhappy'])
        attitude_veryunhappy = float(temp['attitude_veryunhappy'])
        time_spend_company_cat_nodeparture = float(temp['time_spend_company_cat_nodeparture'])
        time_spend_company_cat_veryhighdeparture = float(temp['time_spend_company_cat_veryhighdeparture'])
        number_project_cat_extreme = float(temp['number_project_cat_extreme'])
        workload_extreme = float(temp['workload_extreme'])
        workload_normal = float(temp['workload_normal'])
        efficiencyaverage_montly_hours_bin_287_310_low = float(temp['average_montly_hours_bin_287_310'])
        
   
        #result = [Age,Alb,Alkaline,Alpha,Aspartate,Creatinine,Bilirubin,Ferritin,Gamma,Haemoglobin,INRatio,Iron,dimension,Nodules,Ascites,Encefalopathy,Performance_Status,Chronic_Renal,Diabetes,Hepatitis,Liver_Metastasis,Portal_Vein,Symptoms]
        #Passing data to model & loading the model from disks
        result = pd.DataFrame(columns=['efficiency_low', 'efficiency_very low',
       'satisfaction_level_bin_(0.00, 0.11]','satisfaction_level_bin_(0.92, 1.00]', 'attitude_normal', 'attitude_unhappy',
       'attitude_very happy', 'attitude_very unhappy', 'time_spend_company_cat_no departure',
       'time_spend_company_cat_very high departure', 'number_project_cat_extreme', 'workload_extreme', 'workload_normal',
       'average_montly_hours_bin_(287, 310]'])
        result = result.append({'efficiency_low':efficiency_low, 'efficiency_very low': efficiency_verylow, 'satisfaction_level_bin_(0.00, 0.11]':satisfaction_level_bin_0_11,
       'satisfaction_level_bin_(0.92, 1.00]':satisfaction_level_bin_092_1, 'attitude_normal':attitude_normal, 'attitude_unhappy':attitude_unhappy,
       'attitude_very happy':attitude_veryhappy, 'attitude_very unhappy':attitude_veryunhappy, 'time_spend_company_cat_no departure':time_spend_company_cat_nodeparture,
       'time_spend_company_cat_very high departure':time_spend_company_cat_veryhighdeparture, 'number_project_cat_extreme':number_project_cat_extreme, 'workload_extreme':workload_extreme, 'workload_normal':workload_normal,
       'average_montly_hours_bin_(287, 310]':efficiencyaverage_montly_hours_bin_287_310_low}, ignore_index=True)
        prediction = classifier.predict(result)[0]
      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        if prediction == 1 :
            context ={'a':'HR Analytics : Leaving','temp':temp }
        else:
            context ={'a':'HR Analytics : No Leaving','temp':temp }
    return render(request,'hr.html',context)