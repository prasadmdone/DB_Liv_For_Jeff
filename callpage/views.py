from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

arima=joblib.load('./models/CallPredModel.pkl')


def callindex(request):
    temp={}
    temp['interval']=12
    
    context ={'temp':temp}
    return render(request,'call.html',context)
 #   return HttpResponse({'a':1})

def cpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['interval']=request.POST.get('interval')
        
        #Datapreprocessing Convert the values to float
        interval=int(temp['interval'])
        
     #   result = [interval]
        #Passing data to model & loading the model from disks
       # prediction = arima.predict([result])[0]
        prediction=arima.forecast(steps=interval)
        pred=prediction[0]
        
        
        if len(pred)<12:
            for i in range(12-len(pred)):
                pred=np.append(pred,0)
        for i in range(len(pred)):
            pred[i]=int(pred[i])
      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        charttype ="bar"
        if prediction == 1 :
            context ={'a':'Error','temp':temp }
        else:
            context ={'a':list(pred),'charttype':charttype,'temp':temp,'y1':pred[0],'y2':pred[1],'y3':pred[2],'y4':pred[3],'y5':pred[4],'y6':pred[5],'y7':pred[6],'y8':pred[7],'y9':pred[8],'y10':pred[9],'y11':pred[10],'y12':pred[11] }
    return render(request,'call_new.html',context)