{
    TCanvas *window = new TCanvas("window", "window", 600, 500);
    ifstream dati1x("dati1x.dat");
    TH1D *histogram = new TH1D("Histogram", "", 100, 0, 20);
    double a;
    while (dati1x >> a) {
        histogram->Fill(a);
    }
    histogram->Draw();
//    window->SaveAs("fiststep.pdf");
  // Create a copy of the original histogram
    TH1D *copy1 = (TH1D*)histogram->Clone();
    TH1D *copy2 = (TH1D*)histogram->Clone();
    // Define the component functions

    TF1 *exponential = new TF1("exponential", "[0]*exp(-x/[1])", 4, 10);
    exponential->SetParameters(1, 1);
    exponential->SetParNames("Aparameter", "Bparameter");
    exponential->SetLineColor(2);
    exponential->SetLineStyle(2);

    TF1 *breit_wigner = new TF1("breit_wigner", "[0]/(pow(x-[1],2)+pow([2]/2, 2))", 1, 3.5);
    breit_wigner->SetParameters(1, 1, 1);
    breit_wigner->SetParNames("Cparameter", "Dparameter", "Eparameter");
    breit_wigner->SetLineColor(4);

    TF1 *breit_wigner2 = new TF1("breit_wigner2", "gaus", 13, 15);
    breit_wigner2->SetParameters(1, 1, 1);
    breit_wigner2->SetParNames("Fparameter", "Gparameter", "Hparameter");
    breit_wigner2->SetLineColor(5);

    TF1 *gaussian = new TF1("gaussian", "gaus", 11.5, 13);
    gaussian->SetParameters(1, 1, 1);
    gaussian->SetParNames("Iparameter", "Lparameter", "Mparameter");
    gaussian->SetLineColor(3);

    histogram->Fit("exponential", "R");
    histogram->Fit("breit_wigner", "R+");
    histogram->Fit("breit_wigner2", "R+");
    histogram->Fit("gaussian", "R+");
    // After fitting the components, define the sum function
    TF1 *sum_function = new TF1("sum_function", "exponential + breit_wigner + breit_wigner2 + gaussian", 0, 20);
    sum_function->SetLineColor(1);
    sum_function->SetLineStyle(3);

    histogram->Fit("sum_function", "R+");
    // Extract fundamental statistical parameters from the sum function
    double ndf = sum_function->GetNDF();
    double chi_square = sum_function->GetChisquare();
    double prob = sum_function->GetProb();

    cout << "Degrees of freedom: " << ndf << " Chi-Square: " << chi_square << " Prob: " << prob << endl;
    cout << "The reduced chi-square is: " << chi_square / ndf << endl;
    window->SaveAs("secondstep.pdf");

}
