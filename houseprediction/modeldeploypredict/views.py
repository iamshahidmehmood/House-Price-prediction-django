from django.shortcuts import render
from django.http import HttpResponse
#from django import urls
# Create your views here.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def index(request):

    return render(request,"index.html")


def prediction(request):
    return render(request,"predict.html")

def result(request):
    db = pd.read_csv("C:\\Users\\imuha\\OneDrive\\Desktop\\UetSlides complte\\USA_Housing.csv")
    db = db.drop(["Address"], axis=1)
    x = db.drop("Price", axis=1)
    # print(x)
    # y = db.iloc[:,-2].values
    y = db["Price"]
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30, random_state=0)
    lin_reg = LinearRegression()
    lin_reg.fit(xtrain, ytrain)

    val1 = float(request.GET(['n1']))
    val2 = float(request.GET(['n2']))
    val3 = float(request.GET(['n3']))
    val4 = float(request.GET(['n4']))
    val5 = float(request.GET(['n5']))
    #val6 = float(request.GET.get(['n6']))

    pred = lin_reg.predict(np.array([val1, val2, val3, val4, val5]).reshape(1,-1))

    pred = round(pred[0])
    #pred = tuple(pred)
    price = "how much price into $" + str(tuple(pred))

    # pred = lin_reg.predict(xtest)
    # print(pred)
    # error = np.sqrt(metrics.mean_absolute_error(ytest, pred))
    # print(error)
    return render(request,"predict.html",{"result2": "price"})
