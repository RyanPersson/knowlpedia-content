+++
id = "lie-groups/stone-theorem-one-parameter-unitary-groups"
title = "Stone's theorem for one-parameter unitary groups"
kind = "theorem"
summary = "Strongly continuous one-parameter unitary groups are exactly exponentials of self-adjoint operators."
aliases = ["Stone theorem", "infinitesimal generator theorem"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "lie-groups/one-parameter-subgroup", "functional-analysis/self-adjoint-unbounded-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U:\mathbb R\to U(\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of the additive group, equivalently a strongly continuous unitary [[lie-groups/one-parameter-subgroup|one-parameter group]]. **Stone's theorem** states that there is a unique, possibly unbounded, [[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]] \(A\) on \(\mathcal H\) such that
\[
U(t)=e^{itA}\qquad(t\in\mathbb R).
\]
Conversely, every self-adjoint \(A\) defines such a group through the spectral functional calculus. Its domain is
\[
\operatorname{Dom}(A)=\left\{\xi:\lim_{t\to0}\frac{U(t)\xi-\xi}{t}\text{ exists in norm}\right\},
\]
and the displayed limit equals \(iA\xi\).

## Generator and domain

The strong derivative at \(0\) is therefore not defined on every vector unless \(A\) is bounded. On its dense domain it gives the closed skew-adjoint operator \(iA\). The group determines both the operator and its domain: specifying only a formal derivative or an eigenvalue formula does not specify an unbounded generator.

## Consequences

Strong continuity, the group law, and unitarity force differentiability precisely on \(\operatorname{Dom}(A)\), even though no differentiability is assumed initially. The spectral theorem then yields
\[
U(t)=\int_{\mathbb R}e^{it\lambda}\,dE_A(\lambda).
\]
In a unitary [[lie-groups/representation-of-a-lie-group|representation of a Lie group]], applying Stone's theorem to \(t\mapsto\pi(\exp(tX))\) produces the self-adjoint generator associated with each Lie-algebra element \(X\).

## Sign conventions

Some authors write \(U(t)=e^{-itH}\). Their self-adjoint generator \(H\) is \(-A\), and the strong derivative is \(-iH\). Other authors call the skew-adjoint operator \(iA\), rather than \(A\), the infinitesimal generator. The exponential formula and derivative-domain identity must be stated together to remove this ambiguity.

## References

1. M. H. Stone, “On One-Parameter Unitary Groups in Hilbert Space,” *Annals of Mathematics* 33 (1932), 643–648. [DOI record](https://doi.org/10.2307/1968538). Relevant: the original correspondence theorem.
2. M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [DOI record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Theorem VIII.8.
