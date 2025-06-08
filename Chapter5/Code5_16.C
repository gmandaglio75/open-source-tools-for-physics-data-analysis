{
 ifstream sc("daterelli2.dat");
 TH1D *hist=new TH1D("hist","",50,0,10);
 double a,b;
 while(sc>>a>>b)
 {
	hist->Fill(b);
 }

 // Fit of histogram 6 composed of Breit-Wigner and parabola
 TF1 * fun1= new TF1("fun1","[0]/(pow(x-[1],2)+pow([2]/2,2))", 3,5);      //((x-[2])*(x-[3])+[1]/4)[0]) alternative form of Breit-Wigner
  fun1->SetParameters(1,1,1,1);
  fun1->SetParNames("f","g","h","i");
  fun1->SetLineColor(3);
  TF1 * fun2= new TF1("fun2","[0]*x*x+[1]*x+[2]", 6,10);
  fun2->SetParameters(1,1,1);
  fun2->SetParNames("l","m","n");

 TCanvas * pippo = new TCanvas("pippo","",600,500);

  hist->Draw();
// Clone the working histogram to keep a clean copy
// not tainted by the fitting processes (just a graphical refinement)
TH1D *pino = (TH1D*)hist->Clone();
// Perform the fits for the component functions
hist->Fit("fun1","R");
hist->Fit("fun2","R+");
// IT IS ESSENTIAL to define the sum after fitting with fun1 and fun2
// sum automatically inherits the parameters from the preliminary fits
TF1 * sum = new TF1("sum","fun1+fun2", 0, 10);
sum->SetLineColor(1);
// Global fit with the sum function
hist->Fit("sum","R+");
// Container to copy parameters after the global fit
double parameters[6];
// Method to copy all parameters in one go
sum->GetParameters(parameters);
//sum->GetParameters(&parameters[0]); // equivalent command, specifying from which element to start copying
// VERY IMPORTANT -> Correct the definition range of the component functions
fun1->SetRange(0,10);
fun2->SetRange(0,10);
// Pass the parameters obtained from the global fit to the components
fun1->SetParameters(&parameters[0]);
fun2->SetParameters(&parameters[3]);
pino->Draw();
// Overlay the clean graph with the sum and component functions
sum->Draw("same");
fun1->Draw("same");
fun2->Draw("same");
pippo->SaveAs("fitsecondo.pdf");
}
