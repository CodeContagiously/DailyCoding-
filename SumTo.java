package DailyCoding;

import java.util.ArrayList;

/* -Need to properly code this.*/
public class SumTo
{
    public static void main(String[] args)
    {
        int[] a = {10,15,3,7}; ArrayList<Integer> aa = new ArrayList();
        for (int n : a) aa.add(n); //create arrayList

        int val = 17;
        SumTo sumto = new SumTo(aa,val);
        System.out.println(Eval());
    }

    //traverse a given array and find elements A,B such that  A+B = Val
    static ArrayList<Integer> array; static int Val;
    public SumTo(ArrayList<Integer> array, int Val)
    {
        this.array = array;
        this.Val = Val;
    }

    public static boolean Eval()
    {
        //firs way
        for (int i=0; i<array.size(); i++)
        {//traverse array from index 0
            for (int j=i+1; j<array.size(); j++)
            {//traverse array from
                if(array.get(i) + array.get(j) == Val) return true;
            }
        }
        return false;
    }
}
