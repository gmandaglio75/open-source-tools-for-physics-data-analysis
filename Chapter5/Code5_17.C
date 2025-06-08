{
    TCanvas *window = new TCanvas("window", "window", 600, 500);
    ifstream dati1x("dati1x.dat");
    TH1D *histogram = new TH1D("Histogram", "", 100, 0, 20);
    double a;
    while (dati1x >> a) {
        histogram->Fill(a);
    }
    histogram->Draw();
    window->SaveAs("fiststep.pdf");
}
