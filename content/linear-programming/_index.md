---
date: "2021-09-15T15:26:15Z"
lastmod: "2021-10-13T15:26:15Z"
draft: false
title: Linear Programming
weight: 30
---

{{% panel status="primary" title="Note" icon="far fa-lightbulb" %}}
Linear programming is an optimization model to find an optimal solution with
a linear objective function over a set of all solutions defined by a system of
linear equations and linear inequalities. Even though they're relatively
simple, they're still useful for resource allocation problems. In any LP 
problem, they come with 4 features:

* **Objective Function:** The function we're trying to maximize/minimize
* **Decision Variables:** The unknown values we're trying to find 
* **Constraints:** The restrictions and requirements that need to be
satisfied
* **Sign Restrictions:** Specify that decision variables can be either non-negative
or positive, zero, or negative 

If we wanted to maximize revenue, our decision variables in our objective function
are the products along with its objective function coefficients. Using LP,
we want to find the optimal amount of each decision variable to get the best
result from our objective function. However, we can't simply choose the 
decision variable with the highest coefficient as in reality, constraints exist 
(i.e. budget, labor force, raw materials, time). In addition, most sign 
restrictions will be non-negative as its pretty much impossible to have
negative resources. The next subsections will feature common examples in a 
supply chain environment.