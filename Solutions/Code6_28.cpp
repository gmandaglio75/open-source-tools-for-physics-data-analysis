#include <iostream>
#include <fstream>

using namespace std;
int main(){

  ifstream reader("data.dat");//file in the same folder of the code
  if(!reader.is_open()){
    cout<<"I cannot find the file, please check!"<<endl;
    return 1;
  }

  return 0;
 }
