+++
id = "operator-algebras/cauchy-schwarz-hilbert-cstar-module"
title = "Cauchy–Schwarz inequality for Hilbert C*-modules"
kind = "theorem"
summary = "The algebra-valued inner product of a Hilbert C-star-module satisfies a norm-valued Cauchy–Schwarz bound."
aliases = ["Hilbert-module Cauchy-Schwarz inequality"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/hilbert-cstar-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a right
[[operator-algebras/hilbert-cstar-module|Hilbert \(C^*\)-module]] over a
\(C^*\)-algebra \(A\), with inner product linear in the second variable. For
all \(x,y\in E\),
\[
\langle x,y\rangle_A^*\langle x,y\rangle_A
\leq \lVert\langle x,x\rangle_A\rVert\,\langle y,y\rangle_A
\]
in the order on positive elements of \(A\). Taking norms gives
\[
\lVert\langle x,y\rangle_A\rVert
\leq \lVert x\rVert\,\lVert y\rVert,
\qquad
\lVert x\rVert=\lVert\langle x,x\rangle_A\rVert^{1/2}.
\]
This is the Hilbert-module Cauchy--Schwarz inequality. It makes the
algebra-valued inner product jointly continuous and justifies the triangle
inequality for the induced norm.

## Proof idea

After adjoining a unit if necessary, positivity of
\(\langle y-xa,y-xa\rangle_A\) is applied with
\[
a=(\langle x,x\rangle_A+\varepsilon1)^{-1}\langle x,y\rangle_A.
\]
Expanding the positive element and letting \(\varepsilon\downarrow0\) yields
the displayed order inequality. The scalar proof by direct division cannot simply be
copied, because \(\langle y,y\rangle_A\) need not be invertible or commute
with \(\langle x,y\rangle_A\).

## Consequences

For fixed \(x\), the map \(y\mapsto\langle x,y\rangle_A\) is bounded with
norm at most \(\lVert x\rVert\). Hence the inner product extends uniquely
across completion, and
\[
\lVert\langle x,y\rangle_A-\langle x',y'\rangle_A\rVert
\leq \lVert x-x'\rVert\lVert y\rVert
   +\lVert x'\rVert\lVert y-y'\rVert.
\]
The theorem also proves the [[real-analysis/triangle-inequality|triangle inequality]] for the module norm by
expanding \(\langle x+y,x+y\rangle_A\).

## Conventions and scope

If the inner product is linear in the first variable, the order-valued
formula is written with the variables and factors reversed. Unlike the
scalar [[linear-algebra/cauchy-schwarz-inequality|Cauchy--Schwarz
inequality]], equality does not in general admit a simple characterization
by linear dependence, because coefficients lie in a possibly
noncommutative algebra.

## References

1. E. C. Lance, *Hilbert \(C^*\)-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Proposition 1.1 on the module Cauchy--Schwarz inequality and induced norm.
