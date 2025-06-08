//To be added to the previous macro
//.....

TCanvas *box = new TCanvas("box","",800,400);
box->Divide(5,2); //ten sub-canvas  

for(int i=0; i<10;i++){
 box->cd(i+1); //to move into the sub-canvas
 hist[i]->Draw();
}
//To save the figures:
box->SaveAs("10histo.pdf");
}//end of macro
