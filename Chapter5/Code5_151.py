import numpy as np
import ROOT as rt
data = np.loadtxt("data10.dat")  # Load everything into a matrix
histograms = []  # A list that will contain the TH1F histograms
bins = 100
for column_index in range(len(data[0, :])):  # Loop over the columns
    current_column = data[:, column_index]
    histograms.append(rt.TH1F("histo" + str(column_index), "", bins, current_column.min(), current_column.max()))
    for value in current_column:
        histograms[column_index].Fill(value)

save_file = rt.TFile("histoall.root", "recreate")  # The 'recreate' option
for column_index in range(len(data[0, :])):
    histograms[column_index].Write()
save_file.Close()  # If you don't close it manually, it will close automatically at the end of the execution
for i in range(len(histograms)):
    write_file = open("histo" + str(i) + ".dat", "w")
    for j in range(bins):
        write_file.write(str(round(histograms[i].GetBinCenter(j), 3)) + "  " + str(histograms[i].GetBinContent(j)) + "\n")
    write_file.close()
