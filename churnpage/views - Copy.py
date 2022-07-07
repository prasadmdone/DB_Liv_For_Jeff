from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
#classifier=joblib.load('./models/ChurnModel.pkl')
from keras.models import load_model
classifier = load_model('./models/churn.h5')


def home(request):
  
    context ={'temp':'Welcome!'}
    return render(request,'index.html',context)

def churnindex(request):
    temp={}
    temp['CreditScore']=850
    temp['Geography']='France'
    temp['Gender']='Female'
    temp['Age']=50
    temp['Tenure']=4
    temp['Balance']=150000
    temp['NumOfProducts']=5
    temp['HasCrCard']='Yes'
    temp['IsActiveMember']='Yes'
    temp['EstimatedSalary']=85000
    #temp['Exited']=62
    context ={'temp':temp}
    return render(request,'churn.html',context)
 #   return HttpResponse({'a':1})


def chpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['CreditScore']=request.POST.get('CreditScore')
        temp['Geography']=request.POST.get('Geography')
        temp['Gender']=request.POST.get('Gender')
        temp['Age']=request.POST.get('Age')
        temp['Tenure']=request.POST.get('Tenure')
        temp['Balance']=request.POST.get('Balance')
        temp['NumOfProducts']=request.POST.get('NumOfProducts')
        temp['HasCrCard']=request.POST.get('HasCrCard')
        temp['IsActiveMember']=request.POST.get('IsActiveMember')
        temp['EstimatedSalary']=request.POST.get('EstimatedSalary')
        #temp['Exited']=request.POST.get('Exited')
        
#   testDtaa=pd.DataFrame({'x':temp2}).transpose()
#  scoreval=reloadModel.predict(testDtaa)[0]
#   context={'scoreval':scoreval,'temp':temp}
        #Datapreprocessing Convert the values to float
        CreditScore = float(temp['CreditScore'])
        Geography = temp['Geography']
        Gender = temp['Gender']
        Age = float(temp['Age'])
        Tenure = float(temp['Tenure'])
        Balance = float(temp['Balance'])
        NumOfProducts = float(temp['NumOfProducts'])
        HasCrCard = temp['HasCrCard']
        IsActiveMember = temp['IsActiveMember']
        EstimatedSalary = temp['EstimatedSalary']
        #Exited = float(temp['Exited'])

        result = [CreditScore, Geography, Gender, Age, Tenure, Balance,
        NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]
        #Passing data to model & loading the model from disks
        #model_path = 'ml_model/model.pkl'
        #classifier = pickle.load(open(model_path, 'rb'))
        prediction="Testing...."
        #prediction = classifier.predict([result])[0]
       # prediction = classifier.predict(np.array([[850, 50, 4, 150000, 5, 1, 1, 85000, 1, 0, 0, 1, 0]]))
        Geography_France=1
        Geography_Germany=0
        Geography_Spain=0
        Gender_Female=1
        Gender_Male=0
        HasCrCard=1
        IsActiveMember=1
        prediction = classifier.predict(np.array([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, 1, 0, 0, 1, 0]]))
        if prediction[[0]]==0:
            pred="No Churn"
        else:
            pred="Churn"            

        #conf_score =  np.max(classifier.predict_proba([result]))*100
        context ={'a':pred  ,'temp':temp}
    return render(request,'churn.html',context)
