package DailyCoding;
import java.util.Random;

public class Rand7
{/*this class defines computes a and return a random number from 1 to 7 with the use of a rand5() method
  */
    public static void main(String[] args)
    {
        //test
        Rand7 Ra = new Rand7();
        System.out.println(Ra.Rand());
    }

    Random rand = new Random();

    private int Rand5(){ return rand.nextInt(6);} //This methode returns random number in from 1 - 5 (inclusive)

    public int Rand()
    {/*Return random number from 1 - 7*/
        //we have two choices; a random number from 1-5 and 6-7;
        int[] A = new int[]{Rand5(),6,7}; ///list of possible numbers
        int randomChoice = rand.nextInt(3); //Get random number from o - 2 for the options in list
        return A[randomChoice];
    }
}

