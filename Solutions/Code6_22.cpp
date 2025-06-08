#include <iostream>
using namespace std;
int main(){
 int solution[3][100];
 for(int i=0; i<50; i++){
    solution[0][i]=2*i;
    solution[1][i]=2*i+1;
    solution[2][i]=solution[0][i]+solution[1][i];
 }
 for(int i=0; i<50; i++){
    for(int j=0; j<3; j++){
        cout<<solution[j][i]<<"  ";
    }
    cout<<endl;
 }
 return 0;
 }
