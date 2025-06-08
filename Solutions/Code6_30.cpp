#include <iostream>
using namespace std;
class changer{
float rateEtoD=1.08 ;
float rateEtoF=0.95 ;
        public:
        changer(){
                cout<<"rate Euro to US-Dollar I know is "<<rateEtoD<<endl;
                cout<<"rate Euro to Swiss-Franc I know is "<<rateEtoF<<endl;
        }
        changer(float a, float b){
                rateEtoD=a;
                rateEtoF=b;
        }
        float ConvEtoD(float a){
                return a*rateEtoD;
        }
        float ConvDtoE(float a){
                return a/rateEtoD;
        }
        float ConvEtoF(float a){
                return a*rateEtoF;
        }
        float ConvFtoE(float a){
                return a/rateEtoF;
        }
        float ConvFtoD(float a){
                return ConvEtoD(ConvFtoE(a));
        }
        float ConvDtoF(float a){
                return ConvEtoF(ConvDtoE(a));
        }

};
int main(){
        changer pino;
        float euro;
        cout<<"how many euros you wish to change?\n";
        cin>>euro;
        cout<<"corresponds in US-dollar to "<<pino.ConvEtoD(euro)<<endl;
        cout<<"corresponds in Swiss-Franc to "<<pino.ConvEtoF(euro)<<endl;

return 0;
}
