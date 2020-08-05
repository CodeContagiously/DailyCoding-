package DailyCoding;

public class NperfectNum
{/*this program defines a simple function that takes a number "n" and returns a perfect norm "nm"
    such that n + m == 10*/
    public static void main(String[] args)
    {
        NperfectNum pf = new NperfectNum();
        int rslt = pf.perfectNum(8);
        System.out.println(rslt);
    }

    public int perfectNum(int number)
    { /* algorithm: 10 - number to get number compliment
           to combine number and compliment; e.g if number == 2, compliment == 8; --> 28
           so take multiple of 10 (10 * number) then add compliment
      */
        //Implementation
        return 10*number + (10-number);
    }
}
