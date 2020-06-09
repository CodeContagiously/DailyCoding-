package DailyCoding;

import java.util.ArrayList;

public class ProdctArray
{
    static void main(String[] args)
    {
        ArrayList<Integer> arr = new ArrayList<>();
        int[] array = {1,2,3};
        for(int num:array) arr.add(num);
        ProdctArray ProdCl = new ProdctArray(arr);
    }

    ArrayList<Integer> Array;
    public ProdctArray(ArrayList<Integer> Array) //constructor for Product Array class
    {
        this.Array = Array;
    }

    static void Eval(ArrayList<Integer> Array)
    {
        int ArrSize = Array.size();
        ArrayList<Integer> NewList = new ArrayList<>();
        for(int num=0; num<ArrSize; num++)
        {
            int result = 1;
            ArrayList<Integer> subList1 = (ArrayList<Integer>) Array.subList(0,num);
            ArrayList<Integer> subList2 = (ArrayList<Integer>) Array.subList(num,ArrSize);
            subList1.addAll(subList2); //combine the two subList
            for (int nums : subList1)
            {
                result *= nums;
            }
            NewList.add(result);

        }
        System.out.println(NewList);

    }
}