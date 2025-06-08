# 1) Generate two Gaussian distributions with 100,000 events each,
#    centered at and with mean values respectively: 3 and 0.12,  3.7 and 0.32,
#    plus a parabolic background of the form -x**2 + 5*x in the interval 0-5 with 500,000 events.

import ROOT as rt  # type: ignore
import numpy as np

neventi1 = 100000

gaus1 = np.random.normal(3, 0.12, neventi1)
gaus2 = np.random.normal(3.7, 0.32, neventi1)

neventi2 = 500000
par_f = rt.TF1("par_f", "-x**2 + 5*x", 0, 5)
par_random = [par_f.GetRandom() for _ in range(neventi2)]

# a) Use the generated events to create a single histogram.
c = rt.TCanvas("c", "", 1800, 1200)
h = rt.TH1F("h", "Histogram", 100, 0, 5)
for a in gaus1:
    h.Fill(a)

for b in gaus2:
    h.Fill(b)

for c in par_random:
    h.Fill(c)

h.SetLineColor(rt.kBlack)
h.Draw()

# b) Fit the histogram and assess how well the original generation parameters are recovered:
#    from the code, evaluate how accurately the fit retrieves the parameters used to generate the events: 3, 0.12, 3.7, -1, 5, 0
g1 = rt.TF1("g1", "gaus", 2.85, 3.15)
g1.SetParNames("A", "B", "C")
g1.SetParameters(24225.4, 3.005, 0.153)
g1.Draw("same")
h.Fit("g1", "R+")

fit_result1 = h.Fit("g1", "RS")
print(f"The reduced chi2 value is {fit_result1.Chi2()/fit_result1.Ndf()}")

g2 = rt.TF1("g2", "gaus", 3.45, 4.10)
g2.SetParNames("D", "E", "F")
g2.SetParameters(12095.1, 3.65, 0.438)
g2.Draw("same")
h.Fit("g2", "R+")

fit_result2 = h.Fit("g2", "RS")
print(f"The reduced chi2 value is {fit_result2.Chi2()/fit_result2.Ndf()}")

par = rt.TF1("par", "pol2", 0, 2.65)
par.SetParNames("G", "H", "I")
par.SetParameters(6.04, 5953.81, -1169.82)
par.SetLineColor(rt.kMagenta)
par.Draw("same")
h.Fit("par", "R+")

fit_result3 = h.Fit("par", "RS")
print(f"The reduced chi2 value is {fit_result3.Chi2()/fit_result3.Ndf()}")
par.SetRange(0, 5)

sum_fit = rt.TF1("sum_fit", "g1+g2+par", 0, 5)
sum_fit.SetLineColor(rt.kBlue)
sum_fit.Draw("same")
h.Fit("sum_fit", "R+")

fit_result4 = h.Fit("sum_fit", "RS")
# print(f"The reduced chi2 value is {fit_result4.Chi2()/fit_result4.Ndf()}")

# 1st Gaussian: mean = 3, std dev = 0.12
print(f"The parameters of the 1st Gaussian are: mean = {sum_fit.GetParameter('B')}, std dev = {sum_fit.GetParameter('C')}")
# 2nd Gaussian: mean = 3.7, std dev = 0.32
print(f"The parameters of the 2nd Gaussian are: mean = {sum_fit.GetParameter('E')}, std dev = {sum_fit.GetParameter('F')}")
# a*x**2 + b*x + c = -x**2 + 5*x
print(f"The parameters of the parabolic background are: a = {sum_fit.GetParameter('G')}, b = {sum_fit.GetParameter('H')}, c = {sum_fit.GetParameter('I')}")

print("The parameters of the two Gaussians obtained from the fit match the original ones.")

# c) Repeat exercise b) applying Gaussian smearing to the two distributions
#    with standard deviation 0.1 and 1. Comment on what happens in both cases.

# Create a for loop over the given sigma values.
# For each loop, create a canvas and a histogram for the current sigma.
# Each histogram is fitted with functions defined using previous fit parameters.
# For each histogram, compare the fitted parameter values.

sigmas = [0.1, 1]
canvas = []
histograms = []

for a in sigmas:
    c2 = rt.TCanvas(f"c2{a}", f"Canvas {a}", 1200, 800)
    canvas.append(c2)

    gaus1_sm = gaus1 + np.random.normal(0, a, neventi1)
    gaus2_sm = gaus2 + np.random.normal(0, a, neventi1)

    h2 = rt.TH1F(f"h2{a}", f"Distributions with smearing: sigma = {a}", 100, 0, 7)
    histograms.append(h2)

    for i in gaus1_sm:
        h2.Fill(i)
    for j in gaus2_sm:
        h2.Fill(j)
    for k in par_random:
        h2.Fill(k)
        h2.SetLineColor(rt.kBlack)
    h2.Draw()
    c2.Update()

    c2.cd()
    g1_sm = rt.TF1("g1_sm", "gaus", 2.85, 3.15)
    g1_sm.SetParNames("L", "M", "N")
    g1_sm.SetParameters(24225.4, 3.005, 0.153)
    g1_sm.Draw("same")
    h2.Fit("g1_sm", "R+")

    fit_result5 = h2.Fit("g1_sm", "RS")
    print(f"The reduced chi2 value is {fit_result5.Chi2()/fit_result5.Ndf()}")

    g2_sm = rt.TF1("g2_sm", "gaus", 3.45, 4.10)
    g2_sm.SetParNames("O", "P", "Q")
    g2_sm.SetParameters(12095.1, 3.65, 0.438)
    g2_sm.Draw("same")
    h2.Fit("g2_sm", "R+")

    fit_result6 = h2.Fit("g2_sm", "RS")
    print(f"The reduced chi2 value is {fit_result6.Chi2()/fit_result6.Ndf()}")

    par_sm = rt.TF1("par_sm", "pol2", 0, 2.65)
    par_sm.SetParNames("R", "S", "T")
    par_sm.SetParameters(6.04, 5953.81, -1169.82)
    par_sm.SetLineColor(rt.kMagenta)
    par_sm.Draw("same")
    h2.Fit("par_sm", "R+")

    fit_result7 = h2.Fit("par_sm", "RS")
    print(f"The reduced chi2 value is {fit_result7.Chi2()/fit_result7.Ndf()}")
    par_sm.SetRange(0, 5)

    sum_sm = rt.TF1("sum_sm", "g1_sm + g2_sm + par_sm", 0, 7)
    sum_sm.SetLineColor(rt.kBlue)
    sum_sm.Draw("same")
    h2.Fit("sum_sm", "R+")

    fit_result8 = h2.Fit("sum_sm", "RS")
    # print(f"The reduced chi2 value is {fit_result8.Chi2()/fit_result8.Ndf()}")
    c2.Update()

    print(f"\nAnalysis of fit results for the combined function with Gaussian smearing (sigma = {a}):")
    print(f" 1st Gaussian: mean = {sum_sm.GetParameter('M')}, std dev = {sum_sm.GetParameter('N')}")
    print(f" 2nd Gaussian: mean = {sum_sm.GetParameter('P')}, std dev = {sum_sm.GetParameter('Q')}")
    print(" These values can be compared with the ones obtained from the fit without smearing:")
    print(f" 1st Gaussian: mean = {sum_fit.GetParameter('B')}, std dev = {sum_fit.GetParameter('C')}")
    print(f" 2nd Gaussian: mean = {sum_fit.GetParameter('E')}, std dev = {sum_fit.GetParameter('F')}")

input("")
