<h2><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/">150. Evaluate Reverse Polish Notation</a></h2><h3>Medium</h3><hr><div><p>
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an <code>integer</code> that represents the value of the expression.</p>

<p>&nbsp;</p>
  
Note that:

  <p>The valid operators are '+', '-', '*', and '/'. <br>
  Each operand may be an integer or another expression.<br>
  The division between two integers always truncates toward zero.<br>
  There will not be any division by zero.<br>
  The input represents a valid arithmetic expression in a reverse polish notation.<br>
  The answer and all the intermediate calculations can be represented in a 32-bit integer.</p>
  
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> tokens = ["2","1","+","3","*"]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>tokens = ["4","13","5","/","+"]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong>tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
<strong>Output:</strong> 22
<strong>Explanation:</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li>1 <= tokens.length <= 104</li>
  <li>tokens[i] is either an operator: <code>"+", "-", "*", or "/"</code>, or an integer in the range [-200, 200].</li>
</ul>

<p>&nbsp;</p>
 
