#include <iostream>
using namespace std;
int main(){
 float data, sum =0;
 cout<<"please, give me 10 numbers and I'give you the sum\n";
 for(int i=0; i<10; i++){
  cin>>data;
  sum+=data;
 }
 cout<<"the sum of data is "<<sum<<endl;
 return 0;
 }
