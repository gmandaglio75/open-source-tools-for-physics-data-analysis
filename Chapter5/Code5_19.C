{
   // To be added to the previous code!
   
    TCanvas *window2 = new TCanvas("window2", "window2", 600, 500);
    // Plot the first copy, free from the attributions added by the fit
    copy1->Draw();
    double parameters[11];
    //Getting in a vector the parameters of the sum  function after the global fit
    sum_function->GetParameters(parameters);
    // Transfer the global fit parameters to the component functions
    exponential->SetParameters(&parameters[0]);
    breit_wigner->SetParameters(&parameters[2]);
    breit_wigner2->SetParameters(&parameters[5]);
    gaussian->SetParameters(&parameters[8]);
    // Modify the range of definitions for the component functions
    exponential->SetRange(0, 20);
    breit_wigner->SetRange(0, 20);
    breit_wigner2->SetRange(0, 20);
    gaussian->SetRange(0, 20);

    exponential->Draw("same");
    window2->SaveAs("databackgd.pdf");
    TCanvas *window3 = new TCanvas("window3", "window3", 600, 500);
    // Perform the background subtraction!!!!!
    copy2->Add(exponential, -1);
    copy2->Draw();
    //copy2->Draw("same");
    window3->SaveAs("signals.pdf");
    TCanvas *window4 = new TCanvas("window4", "window4", 600, 500);
    // Plot the components
 //   exponential->Draw("same");
    breit_wigner2->SetLineColor(2);
    gaussian->Draw();
    breit_wigner->Draw("same");
    breit_wigner2->Draw("same");
     window4->SaveAs("models.pdf");
}
