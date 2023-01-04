<h2><a href="https://leetcode.com/problems/rotate-function/">396. Rotate Function </a></h2><h3>Medium</h3><hr><div><p>
You are given an integer array <code>nums</code> of length <code>n</code>.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

<li><code>F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].</code></li>
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.</p>

<p>&nbsp;</p>
  
  
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,6]
<strong>Output:</strong> 26
<strong>Explanation:</strong> 
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>[100]
<strong>Output:</strong> 0
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>



  <li><code>n == nums.length</code></li>
  <li><code>1 <= n <= 105</code></li>
  <li><code>-100 <= nums[i] <= 100</code></li>
</ul>

<p>&nbsp;</p>
 