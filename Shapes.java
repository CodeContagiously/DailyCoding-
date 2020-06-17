package DailyCoding;

class Shapes
{
    private java.lang.Object Object;

    public double Area()
    {return (double) Object;}
}

class Shape3D extends Shapes
{
    private double Object;
    double radius;
    public Shape3D(double radius)
    {
        this.radius = radius;
    }
    public double volume() {return Object;}
}

class Shape2D extends Shapes
{/*defines the 2D shapes
    Overrides methode Area in Parent class Shapes
  */
    double dimension1; double dimension2;//instantiate variables for sides of 2D shape
    public Shape2D(double dimension1, double dimension2)
    {//define constructor
        this.dimension1 = dimension1;
        this.dimension2 = dimension2;
    }


}

class Triangle extends Shape2D
{
    public Triangle(double dimension1, double dimension2)
    {
        super(dimension1,dimension2);
    }

    @Override
    public double Area()//return s Area of triangle
    {return 0.5*dimension1*dimension2;}
}

class Rectangle extends Shape2D
{
    public Rectangle(double dimension1, double dimension2)
    {
        super(dimension1,dimension2);
    }

    @Override
    public double Area()
    {return dimension1*dimension2;}
}
class Square extends Shape2D
{
    public Square(double dimension1, double dimension2)
    {
        super(dimension1,dimension2);
    }
}

class Sphere extends Shape3D
{
    public Sphere(double radius)
    {super(radius);}

    @Override
    public double Area()
    {return (4/3) * 3.147 * pow(radius,3);}

    public double pow(double base, int exponent)
    {
        while (exponent >= 0) {base *= base; exponent--;}
        return base;
    }
}

