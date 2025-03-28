class RegularPolygon {
  double base;  //Private by default
  double height;
  public:
  //Prototyping for external implementation
  void SetBaseHeight(double,double);
  double TriangleAreas ();
  //Implementation inside the class declaration
  double TrianglePerimeter(){
        return 3*base;
  }
  double RettangleAreas(){
        return base*height;
  }
  double RettanglePerimeter(){
        return 2*(base+height);
  }
  double SquareAreas ();
  double SquarePerimeter ();
  double PentagonAreas ();
  double PentagonPerimeter();
};

//For example, external implementation of methods
//RegularPolygon
void RegularPolygon::SetBaseeheight(double a, double b){
  base=a;
  height=b;
  return;
  }
double RegularPolygon::TriangleAreas(){
        return base*height/2;
}
double RegularPolygon::SquarePerimeter(){
        return base*4;
}
double RegularPolygon::SquareAreas(){
        return base*base;
}
double RegularPolygon::PentagonPerimeter(){
        return base*5;
}
double RegularPolygon::PentagonAreas(){
        return (base*height/2)*5;
}

