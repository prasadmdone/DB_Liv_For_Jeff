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
#from keras.models import load_model
import pickle
rating_df = pd.read_pickle("./models/Recommend.pkl")
new_df=rating_df.head(10000)
ratings_matrix = new_df.pivot_table(values='Rating', index='userId', columns='productId', fill_value=0)
X = ratings_matrix.T
#Decomposing the Matrix
from sklearn.decomposition import TruncatedSVD
SVD = TruncatedSVD(n_components=10)
decomposed_matrix = SVD.fit_transform(X)
correlation_matrix = np.corrcoef(decomposed_matrix)
popular_products = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)
most_popularten=most_popular.index[0:9]
relatedprodflag= ""
relatedprod=""

def home(request):
  
    context ={'temp':'Welcome!'}
    return render(request,'index.html',context)

def recindex(request):
    temp={}
    temp['prodid']="B00000K135"
    
    context ={'temp':temp}
    return render(request,'rec.html',context)
 #   return HttpResponse({'a':1})


def rpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['prodid']=request.POST.get('prodid')
                
        product_ID = temp['prodid']
        #i=X.index[correlation_matrix.shape[0]-1]
        product_names = list(X.index)
   #     i=product_names.index(product_ID)
        found=0
        for i in range(len(product_names)):
            if product_names[i]==product_ID:
                found=1
                break

        relatedprodflag= ""
        relatedprod=""
        if found == 0:
            relatedprodflag= "No such Product found"
        else:
            correlation_product_ID = correlation_matrix[i]

            Recommend = list(X.index[correlation_product_ID > 0.65])
            Recommend.remove(product_ID)
            relatedprod=Recommend[0:9]
        context ={'a':relatedprodflag  ,'b':relatedprod,'temp':temp,'popular':most_popularten}
    return render(request,'rec.html',context)
