#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main(){
  string line, number;
  ifstream reader("data.dat");//file in the same folder of the code
  if(!reader.is_open()){
    cout<<"I cannot find the file, please check!"<<endl;
    return 1;
  }
  getline(reader,line);
  stringstream stringer(line);
  int columns=0;
  while(stringer>>number){
    columns++;
    }
    int rows = 1;
    while(getline(reader,line)){
	rows++; //mi conto tutte le righe
	}
    cout<<"number of rows is "<<rows<<" numbers of columns is "<<columns<<endl;
  return 0;
 }
