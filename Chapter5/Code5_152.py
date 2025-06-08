import ROOT as rt
import numpy as np
#histoname = input("give me the file name\n")
data = np.loadtxt("notsoeasy.dat")
histo = rt.TH1F("histo", "MyFit", 100, 0, 0)  # 0,0: the boundaries will be automatically set
for a in data:
    histo.Fill(a)
histo.Draw()
function = rt.TF1("function", "[2]+[1]*x+[0]*pow(x,2)", 3.1, 3.7)
function.SetParNames("A", "B", "C")
function2 = rt.TF1("function2", "[0]*exp(-0.5*pow((x-[1])/[2],2))", 3.7, 4.3)
function2.SetParNames("D", "E", "F")
function2.SetParameters(1000, 4, 0.2)  # initial parameters for the fit
# the default fit method works on the variability domain of the histogram
# if we want it to work on the function's domain instead
histo.Fit("function2", "R")  # R stands for Range (interval) ... function's domain
histo.Fit("function", "R+")  # + to superimpose the other fit
sum_function = rt.TF1("sum_function", "function+function2", 3, 5)
sum_function.SetLineColor(2)
histo.Fit("sum_function", "R")
