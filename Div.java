package DailyCoding;

public class Div
{
    public static void main(String[] args)
    {
        Div test = new Div();
        System.out.println(test.divide(10,2));
    }
    private int divident; private int divisor;
    public int divide(int divident, int divisor)
    {
        if (divisor > divident) return 0; //if divisor greater than divident, then quotient is 0 and remainder==divident
        else//ortherwise substract divisor from divident untill divident is less than divisor
            {
                int quotient = 0;
                while(divisor <= divident)
                {
                    quotient ++;
                    divident = divident-divisor; //deduct the quantity of divisor from divident
                }
                return quotient;
            }
    }
}
