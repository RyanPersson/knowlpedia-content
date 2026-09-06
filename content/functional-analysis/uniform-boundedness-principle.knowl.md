+++
id = "functional-analysis/uniform-boundedness-principle"
title = "Uniform boundedness principle"
kind = "theorem"
summary = "A pointwise bounded family of bounded operators on a Banach space is uniformly bounded in operator norm."
aliases = ["Banach–Steinhaus theorem", "uniform boundedness theorem"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/banach-space", "linear-algebra/normed-vector-space", "functional-analysis/bounded-linear-operator", "linear-algebra/operator-norm"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[linear-algebra/banach-space|Banach space]] over
\(\mathbb R\) or \(\mathbb C\), let \(Y\) be a
[[linear-algebra/normed-vector-space|normed vector space]] over the same
field, and let \(\mathcal F\subseteq B(X,Y)\) be any family of
[[functional-analysis/bounded-linear-operator|bounded linear operators]]. If
\(\mathcal F\) is pointwise bounded, meaning
\[
\sup_{T\in\mathcal F}\lVert Tx\rVert<\infty
\quad\text{for every }x\in X,
\]
then it is uniformly bounded in
[[linear-algebra/operator-norm|operator norm]]:
\[
\sup_{T\in\mathcal F}\lVert T\rVert<\infty.
\]
The conclusion turns individual bounds into one constant valid for the whole
family. No countability assumption on \(\mathcal F\) is required.

## Proof mechanism

For each positive integer \(n\), set
\[
E_n=\{x\in X:\sup_{T\in\mathcal F}\lVert Tx\rVert\leq n\}.
\]
The sets \(E_n\) are closed and cover \(X\). The
[[topology/baire-category-theorem|Baire category theorem]] makes one \(E_n\)
contain a ball. Subtracting two points in that ball and using linearity bounds
every \(T\in\mathcal F\) on a ball about \(0\); rescaling yields a common
operator-norm bound.

## Consequences and sharpness

If a sequence \(T_nx\) converges for every \(x\in X\), then
\((T_nx)\) is bounded for each \(x\), so \(\sup_n\lVert T_n\rVert<\infty\).
This is a standard route from [[real-analysis/pointwise-convergence|pointwise convergence]] to continuous dependence.

Completeness of the domain is essential. Let \(c_{00}\) carry the supremum
norm and define \(T_nx=nx_n\). Every \(x\in c_{00}\) has only finitely many
nonzero coordinates, so \(\sup_n|T_nx|<\infty\), but
\(\lVert T_n\rVert=n\). The incomplete space \(c_{00}\) is therefore a
decisive near-miss.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter VI, “Linear Operators on a Banach Space.”
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 2, the uniform boundedness principle.
