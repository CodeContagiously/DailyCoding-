package DailyCoding;
/*this Program implements a simple Queue using two Stacks*/
public class QueueOnStacks
{/*this Program implements a simple Queue using two Stacks*/
    Stacks stack1; Stacks stack2;
    public void enqueue(String val)
    {/*adds elements to queue*/
        //always enqueue into stack1
        stack1.push(val);//add element to stack1
    }
    public void enqueu(int val)
    {
        stack1.push(val);
    }
    public int dequeue()
    {/*removes element from queue*/
        //Always dequeue from stack2 as it contains first-IN values
        if(!stack2.isEmpty()){return stack2.pop();}//
        else//else if stack2 is empty;
            {//move all item in stack1 to stack2 then return the top element
                while (!stack1.isEmpty())
                {
                    stack2.push(stack1.pop());//remove values from stack1 to stack2
                }
                return stack2.pop();
            }
    }
}