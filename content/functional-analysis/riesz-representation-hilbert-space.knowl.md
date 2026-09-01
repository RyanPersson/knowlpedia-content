+++
id = "functional-analysis/riesz-representation-hilbert-space"
title = "Riesz representation theorem for Hilbert spaces"
kind = "theorem"
summary = "Every continuous linear functional on a Hilbert space is inner product with a unique vector."
aliases = ["Fréchet–Riesz theorem", "Riesz representation theorem for functionals"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/inner-product", "functional-analysis/topological-dual"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H\) be a real or complex [[linear-algebra/hilbert-space|Hilbert space]].
Adopt the convention that its [[linear-algebra/inner-product|inner product]] is linear in the first variable.
For every \(\varphi\) in the [[functional-analysis/topological-dual|continuous
dual]] \(H^*\), there is a unique \(y\in H\) such that
\[
\varphi(x)=\langle x,y\rangle\qquad(x\in H).
\]
Moreover, \(\lVert\varphi\rVert=\lVert y\rVert\). Consequently the map
\[
J:H\longrightarrow H^*,\qquad J(y)(x)=\langle x,y\rangle,
\]
is a conjugate-linear isometric bijection in the complex case and a linear
isometric bijection in the real case. This identification depends on the
inner product, not only on the normed-space structure.

## Proof idea

If \(\varphi\neq0\), its kernel is a closed hyperplane. Choose a nonzero
vector \(z\) orthogonal to \(\ker\varphi\); decomposing each \(x\) into its
kernel component and its component along \(z\) produces the representing
vector after a scalar normalization. Cauchy--Schwarz gives continuity and
the norm identity, while nondegeneracy gives uniqueness.

## Consequences

The theorem converts statements about continuous functionals into
Hilbert-space geometry. It yields
[[linear-algebra/orthogonal-projection|orthogonal projection]] onto closed
subspaces, identifies weak convergence with convergence of all inner
products against fixed vectors, and permits the adjoint of a bounded
operator to be defined by representing the functional
\(x\mapsto\langle Tx,y\rangle\).

## Conventions and scope

**Warning.** If the inner product is instead linear in the second variable,
the representing formula is written \(\varphi(x)=\langle y,x\rangle\), and
the linear versus conjugate-linear bookkeeping reverses. This theorem is not
the Riesz--Markov representation theorem, which represents functionals on
spaces of continuous functions by measures.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990. [DOI record](https://doi.org/10.1007/978-1-4757-3828-5). Relevant: Chapter II, §2 on the Riesz representation theorem.
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw--Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 4 on Hilbert spaces and continuous linear functionals.
