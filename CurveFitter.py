#Imports:
import streamlit as st
import numpy as np
import latex
import math as maths
from matplotlib import pyplot as plt
import scipy
from scipy.optimize import curve_fit
from sympy import *
import pandas as pd
import SessionState
import time
import random

#GUI
st.title("Curve Fitter")
st.sidebar.write("Welcome to Curve Fitter, a programme that takes your data and models a function to it.\nSimply input your data, choose a function, sit back, and watch.\n\n- Saumya Shah")
#Functions:
    #Derivative & Integral:
def deriv(func):
    x = symbols("x")
    return(str(latex(diff(func)) + "\n").replace("⋅",""))
def integral(func):
    x = symbols("x")
    return(str(latex(integrate(func)) + " + c\n").replace("⋅",""))
    #Tests:
def sinReg(x, a, b, c, d): 
    return a * np.sin(b * x + c) + d
def linReg(x, m, c): 
    return m * x + c
def quadReg(x,a,b,c):
    return a*x**2 + b*x + c
def cubReg(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
def quarReg(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e
def quinReg(x,a,b,c,d,e,f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
def expReg(x,a,b,c,d):
    return a*maths.e**(b * x + c) + d
def factReg(x,a,b,c,d):
    return a*scipy.special.factorial(b*x+c)+d
def powReg(x,a,b,c):
    return a*(x**b) + c
    #Graph
def graph(type,param):
    plt.scatter(x, y, color ='red', label ="data")
    newX = (np.linspace(max(x),min(x),500)).tolist()
    newY = []
    if (type == 1):
        for n in newX:
            newY.append(param[0] * np.sin(param[1] * n + param[2]) + param[3])
        optimFunc = (latex(simplify("%f*sin(%f*x + %f) + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 2):
        for n in newX:
            newY.append(param[0] * n + param[1])
        optimFunc = (latex(simplify("%f*x + %f\n"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 3):
        for n in newX:
            newY.append(param[0] * n**2 + param[1]*n + param[2])
        optimFunc = (latex(simplify("%f*x^2 + %f*x + %f\n"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 4):
        for n in newX:
            newY.append(param[0] * n**3 + param[1]*n**2 + param[2]*n + param[3])
        optimFunc = (latex(simplify("%f*x^3 + %f*x^2 + %f*x + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 5):
        for n in newX:
            newY.append(param[0] * n**4 + param[1]*n**3 + param[2]*n**2 + param[3]*n + param[4])
        optimFunc = (latex(simplify("%f*x^4 + %f*x^3 + %f*x^2 + %f*x + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 6):
        for n in newX:
            newY.append(param[0] * n**5 + param[1]*n**4 + param[2]*n**3 + param[3]*n**2 + param[4]*n + param[5])
        optimFunc = (latex(simplify("%f*x^5 + %f*x^4 + %f*x^3 + %f*x^2 + %f*x + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 7):
        for n in newX:
            newY.append(param[0] * maths.exp(param[1] * n + param[2]) + param[3])
        optimFunc = (latex(simplify("%f*e^(%f*x + %f) + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 8):
        for n in newX:
            newY.append(param[0] * scipy.special.factorial(param[1] * n + param[2]) + param[3])
        optimFunc = (latex(simplify("%f*(%f*x + %f)! + %f"%(tuple(float(round(num, 3)) for num in param)))))
    elif (type == 9):
        for n in newX:
            newY.append(param[0] * (n ** param[1]) + param[2])
        optimFunc = (latex(simplify("%f*x^%f + %f"%(tuple(float(round(num, 3)) for num in param)))))
    plt.plot(newX,newY, '--', color ='blue', label ="optimised function ($f(x) = %s$)"%optimFunc)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)       
    plt.show()
    st.pyplot(plt)
def rvalue(type, param):
    predY = []
    if (type == 1):
        for n in x:
            predY.append(param[0] * np.sin(param[1] * n + param[2]) + param[3])
    elif (type == 2):
        for n in x:
            predY.append(param[0] * n + param[1])
    elif (type == 3):
        for n in x:
            predY.append(param[0] * n**2 + param[1]*n + param[2])
    elif (type == 4):
        for n in x:
            predY.append(param[0] * n**3 + param[1]*n**2 + param[2]*n + param[3])
    elif (type == 5):
        for n in x:
            predY.append(param[0] * n**4 + param[1]*n**3 + param[2]*n**2 + param[3]*n + param[4])
    elif (type == 6):
        for n in x:
            predY.append(param[0] * n**5 + param[1]*n**4 + param[2]*n**3 + param[3]*n**2 + param[4]*n + param[5])
    elif (type == 7):
        for n in x:
            predY.append(param[0] * maths.exp(param[1] * n + param[2]) + param[3])
    elif (type == 8):
        for n in x:
            predY.append(param[0] * scipy.special.factorial(param[1] * n + param[2]) + param[3])
    elif (type == 9):
        for n in x:
            predY.append(param[0] * (n ** param[1]) + param[2])
    sqdiff = []
    meandiff = []
    meanY = sum(y)/len(y)
    for i in range(len(y)):
        sqdiff.append(float((predY[i] - y[i]) ** 2))
        meandiff.append(float((y[i] - meanY)**2))
    avgsqdiff = sum(sqdiff)/len(sqdiff)
    rmse = float(round(maths.sqrt(avgsqdiff),3))
    st.markdown("**Root Mean Squared Error:** " + str(rmse))
    RSS = sum(sqdiff)
    TSS = sum(meandiff)
    st.markdown("**Coefficient of Determination:** " + str(100*round(1 - RSS/TSS,4)) + "%")

def cont():
    DataInpBtn.empty()
    funcInp1 = st.empty()
    funcInp2 = st.empty()
    try:
        funcInp = funcInp1.radio("Which function would you like to fit to your data?",("Sine wave","Linear function","Quadratic function","Cubic function","Quartic function","Quintic function","Exponential function","Factorial function","Power function"))
        if (funcInp == "Sine wave"):
            func = 1
        elif (funcInp == "Linear function"):
            func = 2
        elif (funcInp == "Quadratic function"):
            func = 3
        elif (funcInp == "Cubic function"):
            func = 4
        elif (funcInp == "Quartic function"):
            func = 5
        elif (funcInp == "Quintic function"):
            func = 6
        elif (funcInp == "Exponential function"):
            func = 7
        elif (funcInp == "Factorial function"):
            func = 8
        elif (funcInp == "Power function"):
            func = 9
        if (funcInp2.button("Enter","6") or ss.FuncChsBtn):
            ss.FuncChsBtn = True
            funcInp1.empty()
            funcInp2.empty()
                #Sine Function
            st.header("Results")
            with st.spinner("Processing..."):
                time.sleep(random.randrange(3,5))
            st.balloons()
            if (func == 1):
                ff = np.fft.fftfreq(len(np.array(x)), (np.array(x)[1]-np.array(x)[0]))
                Fyy = abs(np.fft.fft(y))
                p0=[np.std(y) * 2.**0.5,abs(ff[np.argmax(Fyy[1:])+1]),0,np.mean(y)]
                param, param_cov = curve_fit(sinReg, x, y,p0=p0, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nSine Function:\n")
                st.latex("f(x) =  %s"%(latex(simplify("%f*sin(%f*x + %f) + %f"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*sin(%f*x+%f)+%f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*sin(%f*x+%f)+%f"%(tuple(round(num, 3) for num in param)))))
                #Linear Function
            elif (func == 2):
                param, param_cov = curve_fit(linReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nLinear Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x+%f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*x+%f"%(tuple(round(num, 3) for num in param)))))
                #Quadratic Function
            elif (func == 3):
                param, param_cov = curve_fit(quadReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nQuadratic Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x^2 + %f*x + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x**2+%f*x+%f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*x**2+%f*x+%f"%(tuple(round(num, 3) for num in param)))))
                #Cubic Function
            elif (func == 4):
                param, param_cov = curve_fit(cubReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nCubic Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x^3 + %f*x^2 + %f*x + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                #Quartic Function
            elif (func == 5):
                param, param_cov = curve_fit(quarReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nQuartic Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x^4 + %f*x^3 + %f*x^2 + %f*x + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                #Quintic Function
            elif (func == 6):
                param, param_cov = curve_fit(quinReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nQuintic Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x^5 + %f*x^4 + %f*x^3 + %f*x^2 + %f*x + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x**5 + %f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) =  \n\n%s"%(integral("%f*x**5 + %f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
                #Exponential Function
            elif (func == 7):
                param, param_cov = curve_fit(expReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nExponential Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*e^(%f*x + %f) + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*exp(%f*x + %f) + %f"%(tuple(round(num, 3) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*exp(%f*x + %f) + %f"%(tuple(round(num, 3) for num in param)))))
                #Factorial Function
            elif (func == 8):
                param, param_cov = curve_fit(factReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nFactorial Function:\n")
                st.latex("f(x) =  %s"%(latex(simplify("%f*(%f*x + %f)! + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*(factorial((%f*x + %f))) + %f"%(tuple(float(round(num, 3)) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*(factorial((%f*x + %f))) + %f"%(tuple(float(round(num, 3)) for num in param)))))
                #Power function
            elif (func == 9):
                param, param_cov = curve_fit(powReg, x, y, maxfev=10000)
                param = param.tolist()
                st.subheader("\n\nPower Function:\n")
                st.latex("f(x) = %s"%(latex(simplify("%f*x^%f + %f\n"%(tuple(float(round(num, 3)) for num in param))))))
                st.latex("f'(x) = \n%s"%(deriv("%f*x**%f + %f"%(tuple(float(round(num, 3)) for num in param)))))
                st.latex("F(x) = \n%s"%(integral("%f*x**%f + %f"%(tuple(float(round(num, 3)) for num in param)))))
            rvalue(func,param)
            graph(func,param)
    except TypeError:
        st.error("The number of datapoints are too less to model an accurate function. Please add more datapoints and try again")
    except:
        st.error("Unknown error occurred. Refresh and try again. If the issue persists, please contact the developer")
#Variables:
x = []
y = []
ask = True

#Code:
ss = SessionState.get(x = [],y = [], stopBtn = False, InpOptBtn = False, XYInpBtn = False, XYInpBtn2 = False, FuncChsBtn = False, InpOpt = "Enter x-data and y-data separately")
InpOpt = ""
opt1 = st.empty()
opt2 = st.empty() 
InpOpt = opt1.radio("How would you like to enter your data?",("Enter x-data and y-data separately","Enter datapoints individually [Not yet functional]"), help = "Warning: 'Enter Datapoints Individually' is not yet fully developed and contains bugs")
if (opt2.button("Enter") or ss.InpOptBtn):
    ss.InpOptBtn = True
    opt1.empty()
    opt2.empty() 
    st.header("Data Entry")
    if(InpOpt == "Enter datapoints individually" or ss.InpOpt == "Enter datapoints individually"):
        ss.InpOpt = "Enter datapoints individually"
        st.write("\nPlease enter your datapoints in this format: \n\n x,y\n\n(x and y MUST be numbers)")
        with st.empty():
            if(st.button("Stop entering datapoints?")):
                ss.stopBtn = True
                st.empty()
        i = 1
        while not(ss.stopBtn):
            i += 1
            inp = st.text_input("\nPlease enter a datapoint: ", key = str(i)).replace(" ","")
            inp = inp.split(",")
            try:
                ss.x.append(float(inp[0]))
                ss.y.append(float(inp[1]))
            except:
                pass
    elif (InpOpt == "Enter x-data and y-data separately" or ss.InpOpt == "Enter x-data and y-data separately"):
        ss.InpOpt = "Enter x-data and y-data separately"
        st.write("\nPlease enter all of your data in this format:\n\na,b,c,...\n\n(a,b,c... MUST be numbers)")
        xin = (st.text_input("Please enter all of your x data:")).replace(" ","").split(",")
        yin = (st.text_input("\nPlease enter all of your y data:")).replace(" ","").split(",")
        DataInpBtn = st.empty()
        if ((DataInpBtn.button("Done") and len(xin) == len(yin)) or ss.XYInpBtn):
            ss.XYInpBtn = True
            for a in xin:
                x.append(float(a))
            for b in yin:
                y.append(float(b))
            Data = pd.DataFrame(list(zip(x,y)))
            Data.columns = ["x","y"]
            st.sidebar.subheader("Your Data:")
            st.sidebar.dataframe(Data)
            ss.x = x
            ss.y = y
            cont()
        elif (len(xin) != len(yin)):
            st.warning("You must input an equal number of values in both fields")
