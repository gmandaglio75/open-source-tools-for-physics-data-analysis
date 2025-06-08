#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;
int main(){
  vector<float> data;
  float datum;
  ifstream reader("data.dat");//file in the same folder of the code
  if(!reader.is_open()){
    cout<<"I cannot find the file, please check!"<<endl;
    return 1;
  }
  while(reader>>datum){
    data.push_back(datum);
  }
  float sum =0;
  for (int i =0; i<data.size(); i++){
    sum+=data[i];
  }
  float mean = sum/data.size();
    for (int i =0; i<data.size(); i++){
    sum+=data[i];
  }
    sum =0;
    for (int i =0; i<data.size(); i++){
    sum+=pow(data[i]-mean,2);
  }
  float std = sqrt(sum/data.size());
  cout<<"the mean value is "<<mean<<"  the standard deviation "<<std<<endl;
  return 0;
 }
