#include <iostream>
using namespace std;
int main(){
    cout<<"HI! I'm a calculator program."<<endl;
    int pass = 1;
    do{
    cout<<"Give me the two numbers"<<endl;
    float number1, number2;
    cin>>number1>>number2;
    cout<<"if you wish to perform a sum digit 1, a difference digit 2, a product 3, a ratio 4"<<endl;
    int choice;
    cin >>choice;
    if(choice ==1) {cout<<"the sum of the values is "<<number1 +number2<<endl; }
    if(choice ==2) {cout<<"the difference of the values is "<<number1 - number2<<endl; }
    if(choice ==3) {cout<<"the product of the values is "<<number1 +number2<<endl; }
    if(choice ==4) {cout<<"the ratio of the values is "<<number1 +number2<<endl; } 
    cout<<"if you wish another ride digit 1, if not whatever numbers"<<endl;
    cin>>pass;
    }while(pass==1);
    return 0;
}
