    {
        TCanvas pina;
 TGraph pino("RCSeguenza2.dat");
 pino.GetXaxis()->SetNdivisions(905);
 pino.GetXaxis()->SetTitle("time (s)");
 pino.Draw();
 pino.GetYaxis()->SetTitleOffset(0.9);
 pino.GetYaxis()->SetTitle("DDP (volt)");
 pino.Draw();
 pina.SaveAs("figura.pdf");
}
