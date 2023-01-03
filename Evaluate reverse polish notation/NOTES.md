The reverse polish is a mathematical notation in which operators follow their operands. So, we will get the operands first and then the operators.

We store all the operands in the order we receive it in.
If we get an operator, we operate it on the previous two operands.
We store the resultant operand as it will be used for future operations.
We use a stack to store all the operands.
So the algorithm is:

If the character is a number (operand), push it into the stack
If the character is an operator,
Pop the top two operands (numbers) from the stack.
Find the result of the operation using the operator
Push the result back in the stack
After traversal, the top of the stack will be the result of evaluated reverse polish expression.
Complexity
Time complexity: O(N), where N is the number of tokens
Space complexity: O(N), for maintaining the stack