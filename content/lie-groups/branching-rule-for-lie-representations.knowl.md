+++
id = "lie-groups/branching-rule-for-lie-representations"
title = "Branching rule for Lie representations"
kind = "definition"
summary = "The decomposition of a representation after restriction from a Lie group or Lie algebra to a subgroup or subalgebra."
aliases = ["branching rule", "restriction rule", "branching decomposition"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(i:H\to G\) be a homomorphism of Lie groups and let \((\pi,V)\) be a finite-dimensional [[lie-groups/representation-of-a-lie-group|representation]] of \(G\). The **branching rule** for \(V\) along \(i\) is the decomposition of the restricted representation
\[
\operatorname{Res}^{G}_{H}V,
\qquad h\longmapsto \pi(i(h)),
\]
into irreducible \(H\)-representations. When restriction is completely reducible, it has the form
\[
\operatorname{Res}^{G}_{H}V\cong
\bigoplus_{\mu}m_{\mu}W_{\mu},
\]
and the branching rule records the occurring irreducibles \(W_\mu\) and their [[lie-groups/multiplicity-of-an-irreducible-representation|multiplicities]] \(m_\mu\).

The same terminology applies to a homomorphism of Lie algebras \(\mathfrak h\to\mathfrak g\): one restricts a [[lie-groups/representation-of-a-lie-algebra|\(\mathfrak g\)-representation]] to \(\mathfrak h\) and decomposes it there.

## Typical settings

Complete reducibility holds, for example, for finite-dimensional representations of compact groups and for finite-dimensional representations of complex semisimple Lie algebras. For a complex reductive Lie algebra, one must additionally require the center to act semisimply. In a highest-weight setting a branching rule is often presented as a formula
\[
V_\lambda\big|_H\cong\bigoplus_\mu m_{\lambda\mu}W_\mu
\]
relating the highest-weight labels for \(G\) and \(H\).

Restriction may be computed by comparing characters, by decomposing weight spaces, or by using invariant tensors. A multiplicity-free branching rule is one for which every coefficient \(m_{\lambda\mu}\) is at most one.

## Example

For the standard inclusion \(SO(n-1)\subset SO(n)\), the defining \(n\)-dimensional representation restricts as
\[
\mathbb R^n\big|_{SO(n-1)}\cong \mathbb R^{n-1}\oplus\mathbb R,
\]
where the last summand is the trivial representation carried by the fixed coordinate axis.

## Global and infinitesimal cautions

A Lie-group branching rule differentiates to the corresponding Lie-algebra restriction, but the converse need not determine the group-level rule. A Lie algebra cannot see disconnected components, and a representation of a Lie algebra may integrate only to a covering group rather than to the chosen global form of \(G\). Central quotients can therefore remove representations that are allowed infinitesimally.

If the restricted representation is not semisimple, a direct-sum branching formula may not exist. One must then specify whether the desired data are composition-factor multiplicities, a filtration, or a decomposition into indecomposable modules.

## References

1. Roe Goodman and Nolan R. Wallach, *Symmetry, Representations, and Invariants*, Springer, 2009, Chapters 5 and 8. [Publisher record](https://doi.org/10.1007/978-0-387-79852-3).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§8 and 25. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
