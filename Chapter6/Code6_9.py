import ROOT
import pyfirmata
import time
import numpy as np

h = ROOT.TH1F("myHist", "", 20000, 0, 20)
h2 = ROOT.TH1F("myHist2", "", 20, 0, 1200)
h.GetXaxis().SetTitle("#Delta T (second)")
h.GetXaxis().CenterTitle(1)
h.GetYaxis().SetTitle("Counts")
h.GetXaxis().SetTitleOffset(0.95);
h.GetYaxis().CenterTitle(1)
h.GetYaxis().SetTitleOffset(0.90);
h2.GetXaxis().SetTitle("Time (second)")
h2.GetXaxis().CenterTitle(1)
h2.GetYaxis().SetTitle("#muSv/hr")
h2.GetXaxis().SetTitleOffset(0.95);
h2.GetYaxis().SetTitleOffset(1.05);
h2.GetYaxis().CenterTitle(1)
c1 = ROOT.TCanvas("c1","",600,500)
c2 = ROOT.TCanvas("c2","",600,500)
c2.SetLeftMargin(0.16);
board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
digital_input = board.get_pin('d:2:i')
previous = time.perf_counter()
tempo = 0.
deltat = 0.
T = []
D = []
contami = 0
#while contami < 10: #condizionato al numero di eventi
while tempo < 1200:#condizionato al tempo

    pippo = digital_input.read()
   # print(pippo)
    if pippo is False:
        print(time.perf_counter())
        contami = contami + 1
        now = time.perf_counter()
        deltat = now - previous
        previous = now
        tempo = tempo + deltat
        T.append(tempo)
        D.append(deltat)
        print(tempo,"   ",deltat)
        h2.Fill(tempo,0.0057)#0.0057 peso muSv/hr
        c2.Clear()
        h2.Draw()
        c2.Update()
        h.Fill(deltat)
        c1.Clear()
        h.Draw()
        c1.Update()
        print(time.perf_counter())
        time.sleep(0.001)
npT = np.array(T)
npD = np.array(D)
outputFile = "datiGeiger.dat"
np.savetxt(outputFile, np.column_stack((npT, npD)),fmt='%7.4f   %7.4f')
F = ROOT.TFile("geigerambiente_2.root", "recreate")
h.Write()
h2.Write()
F.Close()
