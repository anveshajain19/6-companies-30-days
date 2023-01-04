<h2><a href="https://leetcode.com/problems/perfect-rectangle/"> 391. Perfect Rectangle </a></h2><h3>Hard</h3><hr><div><p>
Given an array rectangles where <code>rectangles[i] = [xi, yi, ai, bi]</code> represents an axis-aligned rectangle. The bottom-left point of the rectangle is <code>(xi, yi)</code> and the top-right point of it is <code>(ai, bi)</code>.
Return true if all the rectangles together form an exact cover of a rectangular region.
</p>

<p>&nbsp;</p>
  
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
<strong>Output:</strong> true
<strong>Explanation:</strong> All 5 rectangles together form an exact cover of a rectangular region.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Because there is a gap between the two rectangular regions.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong>rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Because two of the rectangles overlap with each other.
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>



  <li>1 <= rectangles.length <= 2 * 104</li>
  <li>rectangles[i].length == 4</li>
  <li> -105 <= xi, yi, ai, bi <= 105 </li>
</ul>

<p>&nbsp;</p>
 