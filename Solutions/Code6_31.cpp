Double_t funz(Double_t *x, Double_t *par){
        if (x[0]<0) return sin(x[0])/x[0];
        if(x[0] >0) return -sin(x[0])/x[0];
        return 0;

}
void fun()
{
TCanvas *box= new TCanvas("box","",600,500);
TF1 *myfun= new TF1("myfun",funz,-10,10);
myfun->Draw();

return;
}
