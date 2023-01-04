<h2><a href="https://leetcode.com/problems/bulls-and-cows/">299. Bulls and Cows </a></h2><h3>Medium</h3><hr><div><p>
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

<li>The number of "bulls", which are digits in the guess that are in the correct position.</li>
<li>The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.</li>
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.</p>

<p>&nbsp;</p>
  
  
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> secret = "1807", guess = "7810"
<strong>Output:</strong> "1A3B"
<strong>Explanation:</strong> Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>"1123", guess = "0111"
<strong>Output:</strong> "1A1B"
<strong>Explanation:</strong>  Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>



  <li>1 <= secret.length, guess.length <= 1000</li>
  <li>secret.length == guess.length</li>
  <li>secret and guess consist of digits only.</li>
</ul>

<p>&nbsp;</p>
 