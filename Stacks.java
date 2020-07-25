package DailyCoding;

public class Stacks
{
    public int[] array = new int[20]; public int indx = -1;//instantiate the array for the stack
    public void push(int val)
    {
        if(isFull()) {extendStack();}
        indx++; array[indx] = val; // add element to the array
    }
    public int pop()
    {
        indx--;
        return array[indx+1]; // return the element at the top of array
    }
    public boolean isEmpty(){return indx==-1;}

    public boolean isFull()
    {//return True if stack is full; false otherwise
        if(indx==array.length-1) return true;
        return false;
    }
    public int[] extendStack()
    {//double length of stack
        int O_len = array.length;//original length of array
        int[] tempArr = new int[2*O_len];
        for (int n=0;n<O_len;n++) {tempArr[n] = array[n];}
        array = tempArr;
        return array;
    }
}
