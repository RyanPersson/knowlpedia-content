+++
id = "topology/cw-complex"
title = "CW complex"
kind = "definition"
summary = "A space built by attaching cells inductively and equipped with the closure-finite and weak topology conditions."
aliases = ["CW space", "cell complex"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/continuous-map", "topology/homeomorphism", "topology/quotient-topology"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a topological space. A **CW complex structure** on \(X\) consists of a filtration by subspaces
\[
\varnothing=X^{-1}\subseteq X^0\subseteq X^1\subseteq\cdots,\qquad X=\bigcup_{n\ge 0}X^n,
\]
and, for each \(n\ge 0\), a set \(I_n\) and continuous attaching maps
\[
\varphi_\alpha:S^{n-1}\longrightarrow X^{n-1}\qquad(\alpha\in I_n),
\]
such that \(X^n\) is obtained from \(X^{n-1}\) by attaching \(n\)-disks:
\[
X^n\cong
\left(X^{n-1}\sqcup\coprod_{\alpha\in I_n}D^n_\alpha\right)\Big/\!
\left(z\sim\varphi_\alpha(z)\ \text{for }z\in\partial D^n_\alpha=S^{n-1}\right),
\]
with the quotient topology, where the disjoint union has the topology in which a set is open exactly when its intersection with each summand is open. Here \(D^n\) is the closed \(n\)-disk, \(S^{n-1}=\partial D^n\), and for \(n=0\) one uses \(S^{-1}=\varnothing\) and \(D^0=\{\ast\}\), so \(X^0\) is a discrete set of points attached to \(X^{-1}=\varnothing\).

The image of the interior of \(D^n_\alpha\) is an **open \(n\)-cell**, denoted \(e^n_\alpha\), and its characteristic map \(D^n_\alpha\to X^n\) restricts to a homeomorphism from \(\operatorname{int}(D^n_\alpha)\) onto \(e^n_\alpha\). The cells are pairwise disjoint and \(X^n\) is the union of the cells of dimensions at most \(n\).

The structure satisfies two conditions:

1. **Closure-finite:** the closure of every cell meets only finitely many cells.
2. **Weak topology:** a subset \(U\subseteq X\) is open if and only if \(U\cap X^n\) is open in \(X^n\) for every \(n\ge0\).

The space \(X\), together with this cell decomposition, is called a CW complex. Its \(n\)-skeleton is \(X^n\), and the dimension of a cell \(e^n_\alpha\) is \(n\). A finite CW complex has finitely many cells; its dimension is the supremum of its cell dimensions (the empty complex has dimension \(-1\)).

## Examples

The \(0\)-sphere is a CW complex with two \(0\)-cells. Attaching one \(1\)-cell to two \(0\)-cells gives an interval, while attaching its two endpoints to one \(0\)-cell gives a circle. More generally, a sphere \(S^n\) has a CW structure with one \(0\)-cell and one \(n\)-cell.
