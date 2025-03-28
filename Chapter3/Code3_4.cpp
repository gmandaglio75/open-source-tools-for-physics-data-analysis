#include <iostream>

using namespace std; 

class shape{
protected:
double base, height;
public:
shape();
shape(double, double);	//constructor
//~shape();		//destructor
void SetBaseHeight(double a, double b){
  base=a;
  height=b; 
  return;
}
double GetHeight(){
  return height;
}
};

//Constructor external implementation
shape::shape(){
cout<<"Just created a shape class object"<<endl;
}
shape::shape(double p, double m){
	base=p;
	height=m;
}

//implementazione distruttore
shape::~shape(){
	cout<<"\n destroyed"<<endl;
}

//Derivate class
class rectangle:public shape{
public:
rectangle(double,double);   //Constructor
~rectangle(); 		     //destructor
double area(){
  return base*height;
  }
};

//Constructor implementation
rectangle::rectangle(double a, double b){
  base=a;
  height=b;
};

//implementazione distruttore
rectangle::~rectangle(){
  cout<<"destroyed"<<endl;
}

int main(){
  cout<<"this program estimate the areas of a rettangle\n";
  double a, b;
  cout<<"give me base and height of rectangle: "<<endl;
  cin>>a>>b;
  shape pippo(a,b);
  cout<<"Testing the GetHeight method: "<<pippo.GetHeight()<<endl;
  rectangle pina(a,b);
  cout<<"Areas is : "<<pina.area()<<endl;
  return 0;
}

