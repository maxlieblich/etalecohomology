# Introduction: why do this?

### An example

Let's start with an example. Consider the polynomial
\[F(x, t) = x^2 + b(t)x + c(t)\in k[x,t]\]
for some field \(k\). This defines a curve \(C\subset\mathbf A^2\), and projecting to the $t$-coordinate gives a morphism \[f:C\to\mathbf A^1.\]

**Question**: where does \(f\) ramify? I.e., where does \(f\) have a double root?

If \(\operatorname{char}(k)\neq 2\), then we can just use the quadratic formula. The roots of \(F(x, \alpha)\) are given by 
\[\frac{-b(t)\pm\sqrt{b(t)^2-4c(t)}}{2},\]
so there is a double root exactly when \(b(t) = 4c(t)\). When \(k\) is algebraically closed and \(b\) and \(c\) are linearly independent (e.g., have different degrees!), this is guaranteed.

But what happens when \(\operatorname{char}(k)=2\)?