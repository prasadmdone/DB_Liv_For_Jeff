from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import pickle
import joblib

rating = pd.read_pickle("./models/Recommend.pkl")


def home(request):
  
    context ={'temp':'Welcome!'}
    return render(request,'index.html',context)

def recindex(request):
    temp={}
    temp['prodid']='B00000K135'
    
    #temp['Exited']=62
    context ={'temp':temp}
    return render(request,'rec.html',context)
 #   return HttpResponse({'a':1})


def recpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['prodid']=request.POST.get('prodid')
   
        #temp['Exited']=request.POST.get('Exited')
        
#   testDtaa=pd.DataFrame({'x':temp2}).transpose()
#  scoreval=reloadModel.predict(testDtaa)[0]
#   context={'scoreval':scoreval,'temp':temp}
        #Datapreprocessing Convert the values to float
        
        Productid = temp['prodid']
        
        #Exited = float(temp['Exited'])

       # result = [CreditScore, Geography, Gender, Age, Tenure, Balance,
        #NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]
        #Passing data to model & loading the model from disks
        #model_path = 'ml_model/model.pkl'
        #classifier = pickle.load(open(model_path, 'rb'))
        prediction="Testing...."
        #prediction = classifier.predict([result])[0]
       # prediction = classifier.predict(np.array([[850, 50, 4, 150000, 5, 1, 1, 85000, 1, 0, 0, 1, 0]]))
        
        #HasCrCard=1
        #IsActiveMember=1
       # prediction = classifier.predict(np.array([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_France, Geography_Germany, Geography_Spain, Gender_Female, Gender_Male]]))
        if prediction[[0]]==0:
            pred="No Churn"
        else:
            pred="Churn"            

        #conf_score =  np.max(classifier.predict_proba([result]))*100
        context ={'a':pred  ,'temp':temp}
    return render(request,'rec.html',context)
