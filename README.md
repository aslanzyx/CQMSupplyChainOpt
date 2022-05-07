# Description
A set of constraint quadratic model for the supply chain problem.

# Set Cover
The set cover is defined as follows. Given a universe set $U$ and a set of sets $V$. We want to find a set $S\subseteq V$ which covers all elements in $U$.
$$
\forall u\in U,\exists s\in S, u\in s
$$
We then minimize the set $S$.
$$
\min |S|
$$
## Constraint Quadratic(Linear in fact) Model
Set cover can be reduced as a binary linear programming problem. Take the size of the universe to be $m=|U|$ and the size of sets provided to be $n=|V|$. Denote the selected sets as a binary word $x\in\Z_2^n$ such that $x_i=1$ if set $v_i\in V$ is selected or $x_i=0$. Denote $A\in\Z_2^{m\times n}$ as the matrix representation of $V$. $A_{i,j}=1$ if element $u_j\in U$ is present in set $v_i\in V$. The coverage constraint can be expressed as a series of linear inequalities. $e=(1,1,...)$ denotes the 1 vector.
$$
Ax\ge e
$$
The objective is therefore as follows. It is simply the sum of the binary word $x$. Now it is natural to run on the hybrid CQM sampler.
$$
\min f(x)=e^Tx
$$

## Relaxed Linear Programming
The idea is to relax the problem to a continuous linear programming problem with additional constraint $x\le e$. This intermediate solution $\bar{x}$ shall be bound $[0, e]$. Now the problem is how to round each variable to an integer number.

A descrete optimization problem like this can be treat as a searching problem over a series of decision problems. The decision problem is as follows. Given an integer $k\in[0,n]$ we ask the question: is there a feasible solution $x^*$ such that $f(x^*)\le k$. We then do binary search for a minimized $k$.

(Implementation still in progress)

## Greedy Algorithm
Choose the supplier covers the most items at each iteration. Iterate util full coverage. This greedy algorithm should provide a $\log(n)$-approximation.

## Demo run
| data set            | num of suppliers | QPU access time | runtime |
| ------------------- | ---------------- | --------------- | ------- |
| small data set      | 2                | 15220           | 5019865 |
| medium data set     | 2                | 15236           | 4955606 |
| large data set      | 2                | 15321           | 4990371 |
| real world data set | 1                | 15147           | 4904876 |

# Knapsack
The knapsack problem is a descrete linear programming model on itself. Denote descrete vector $x\in\Z^n$ as the amount of products to purchase. Denote vector $c$ as the profit for each vector, and vector $a$ as the cost for each product. The cost constraint is represent as follows.
$$
a^Tx\le w
$$
There might be an upper bound on each item denoted by vector $b$.
$$
x\le b
$$
Finally the constraint is to maximize the profit, or to minimize the negative profit.
$$
\max f(x)=c^Tx
\iff
\min -f(x)=-c^Tx
$$

(Demo still in progress)
<!-- | Solvers               | num of suppliers | runtime |
| --------------------- | ---------------- | ------- |
| Leap Hybrid Solver    |                  |         |
| Simplex Approximation |                  |         |
| Greedy Solver         |                  |         |
| DP with Rounding      |                  |         | -->