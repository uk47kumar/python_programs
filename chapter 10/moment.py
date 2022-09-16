from scipy import stats
import numpy as np
import math

print("\nFor Bionomial")

X = stats.binom(10, 0.2)  # Declare X to be a binomial random variable
print(X.pmf(3))          # P(X = 3)
print(X.cdf(4))          # P(X <= 4)
print(X.mean())          # E[X]
print(X.var())          # Var(X)
print(X.std())          # Std(X)
print(X.rvs())          # Get a random sample from X
print(X.rvs(10))          # Get 10 random samples form X

print("\nFor poission")

Y = stats.poisson(2)  # Declare Y to be a poisson random variable
print(Y.pmf(3))       # P(Y = 3)
print(Y.rvs())       # Get a random sample from Y

print("\nFor Geometric")

G = stats.geom(0.75)  # Declare X to be a geometric random variable
print(G.pmf(3))       # P(X = 3)
print(G.rvs())       # Get a random sample from Y

print("\nFor Normal")

A = stats.norm(3, math.sqrt(16))  # Declare A to be a normal random variable
print(A.pdf(4))      # f(3), the probability density at 3
print(A.cdf(2))       # F(2), which is also P(Y < 2)
print(A.rvs())      # Get a random sample from A

print("\nFor exponential")

B = stats.expon(4)   # Declare B to be a normal random variable
print(B.pdf(1))       # f(1), the probability density at 1
print(B.cdf(2))       # F(2) which is also P(B < 2)
print(B.rvs())       # Get a random sample from B

print("\nFor Beta")

C = stats.beta(1, 3)  # Declare X to be a beta random variable
print(C.pdf(0.5))     # f(0.5), the probability density at 1
print(C.cdf(0.7))     # F(0.7) which is also P(X < 0.7)
print(C.rvs())     # Get a random sample from X

print("\nFor Moment")

arr1 = np.array([[1, 3, 7, 3, 1, 9],
                [8, 2, 8, 4, 7, 1]])


print("6th moment : ", stats.moment(arr1, moment=6))
