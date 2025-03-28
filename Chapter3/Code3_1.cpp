#include <iostream>
using namespace std;
class operation{
//private by default
float first, second;
    public://the subsequent instructions are public
    operation(){ //first constructor 
        return;
    }
    operation(double a, double b){ //second constructor
        first = a;
        second = b;
        return;
    }
    void changeFS(float a, float b){
        first  = a;
        second = b;
        return;
    }
    void changeF(float a){
        first =a;
        return;
    }
    void changeS(float a){
        second =a;
        return;
    }
    float Sum(){
        return first + second;
    }
    float FminusS(){
        return first - second;
    }
    float SminusF(){
        return second - first;
    }
    float product(){
        return first*secondo;
    }
    float FdividedbyS(){
        return first/second;
    }
    float SdividedbyF(){
        return second/first;
        ~operation(){
           cout<<"hello, I'm killing your object"<<endl;// Comment just as a joke! Normally no comment in the distructor
           return;
        };
    }
};//note the semi column at the end of the implementation
int main(){
    //first example of the use of the class
    operation objcalc1; //objcalc is an object of operation class
    float numb1, numb2;
    court<<"give me two numbers"<<endl;
    cin>>numb1>>numb2;
    objcalc1.changeFS(numb1, numb2);//operator point "." give access to methods!
    cout<<numb1<<" + "<<numb2<<" = "<<objcalc1.sum()<<endl;
    //second example of the use of the class 
    operation objcalc2(numb1,numb2);//we using the second constructor
    cout<<numb1<<" - "<<numb2<<" = "<<objcalc2.FminusS()<<endl;
    //third example of the use of the class
    operation *objpointercalc = new operation(numb1,numb2);
    cout<<numb1<<" / "<<numb2<<" = "<<objpointercalc->FdivededbyS()<<endl;
    //in the last case, the object pointer variable
    //access to method by operator arrow "->" (minus + major symbols)
    return 0;
} 

