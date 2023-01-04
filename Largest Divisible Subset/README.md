<h2><a href="https://leetcode.com/problems/largest-divisible-subset/">368. Largest Divisible Subset </a></h2><h3>Medium</h3><hr><div><p>
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

<li><code>answer[i] % answer[j] == 0</code>, or</li>
<li><code>answer[j] % answer[i] == 0</code></li>
If there are multiple solutions, return any of them.</p>

<p>&nbsp;</p>
  
  
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> [1,3] is also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>nums = [1,2,4,8]
<strong>Output:</strong> [1,2,4,8]
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>



  <li><code>1 <= nums.length <= 1000</code></li>
  <li><code>1 <= nums[i] <= 2 * 109</code></li>
  <li>All the integers in <code>nums</code> are unique.</li>
</ul>

<p>&nbsp;</p>
 