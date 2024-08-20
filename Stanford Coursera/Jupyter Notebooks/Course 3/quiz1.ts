1.
Question 1
Which of these best describes unsupervised learning? 

1 point

A form of machine learning that finds patterns in data using only labels (y) but without any inputs (x) . 


A form of machine learning that finds patterns without using a cost function.


A form of machine learning that finds patterns using unlabeled data (x). 


A form of machine learning that finds patterns using labeled data (x, y) 

2.
Question 2

Which of these statements are true about K-means? Check all that apply.

1 point

If you are running K-means with 
K
=
3
K=3 clusters, then each 
c
(
i
)
c 
(i)
  should be 1, 2, or 3. 


The number of cluster centroids 
μ
k
μ 
k
​
  is equal to the number of examples.


If each example x is a vector of 5 numbers, then each cluster centroid 
μ
k
μ 
k
​
  is also going to be a vector of 5 numbers.


The number of cluster assignment variables 
c
(
i
)
c 
(i)
  is equal to the number of training examples.

3.
Question 3

You run K-means 100 times with different initializations. How should you pick from the 100 resulting solutions?

1 point

Average all 100 solutions together. 


Pick the one with the lowest cost 
J
J


Pick randomly -- that was the point of random initialization.


Pick the last one (i.e., the 100th random initialization) because K-means always improves over time

4.
Question 4
You run K-means and compute the value of the cost function 
J
(
c
(
1
)
,
…
,
c
(
m
)
,
μ
1
,
…
,
μ
K
)
J(c 
(1)
 ,…,c 
(m)
 ,μ 
1
​
 ,…,μ 
K
​
 ) after each iteration. Which of these statements should be true? 

1 point

The cost can be greater or smaller than the cost in the previous iteration, but it decreases in the long run.


The cost will either decrease or stay the same after each iteration. .


There is no cost function for the K-means algorithm.


Because K-means tries to maximize cost, the cost is always greater than or equal to the cost in the previous iteration.

5.
Question 5
In K-means, the elbow method is a method to 

1 point

Choose the best random initialization


Choose the number of clusters K


Choose the best number of samples in the dataset


Choose the maximum number of examples for each cluster
