package DailyCoding;

import java.util.ArrayList;
import java.util.Collections;

public class SegregatedArray
{ /* This class return a segregated/sorted array:
    that is given [R,B,B,B G,G] ---> [R,G,G,B,B,B]
  */
    ArrayList<String> array;
    public SegregatedArray(ArrayList<String> array)
    {
        this.array = array;
    }

    public ArrayList<String> sort()
    {
        //Easy solution for this: Collections.sort(array, Collections.reverseOrder())
        Collections.sort(this.array, Collections.reverseOrder());
        return this.array;
    }
}
