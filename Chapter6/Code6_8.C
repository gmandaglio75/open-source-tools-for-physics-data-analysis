 {
	TCanvas box;
 TGraph rcplot("RCSeguenza.dat");
 rcplot.GetXaxis()->SetNdivisions(905);
 rcplot.GetXaxis()->SetTitle("time (s)");
 rcplot.Draw();
 rcplot.GetYaxis()->SetTitleOffset(0.9);
 rcplot.GetYaxis()->SetTitle("DDP (volt)");
 rcplot.Draw();
 TF1 *charge = new TF1("charge", "[0]*(1-exp(-(x-[2])/[1]))",0,0.74);
 charge->SetParameters(5,0.03,0.421);
 charge->SetLineColor(4);
 charge->SetLineStyle(2);
 TF1 *discharge = new TF1("discharge", "[0]*exp(-(x-[2])/[1])",2.045,3);
 discharge->SetParameters(5,0.1,2);
 discharge->SetLineColor(2);
 discharge->SetLineStyle(2);
 rcplot.Fit("charge","R+");
 rcplot.Fit("discharge","R+");
 box.SaveAs("fitrcroot.pdf");
}
