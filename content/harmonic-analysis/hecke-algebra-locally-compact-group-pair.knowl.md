+++
id = "harmonic-analysis/hecke-algebra-locally-compact-group-pair"
title = "Hecke algebra of a locally compact group pair"
kind = "definition"
summary = "The Hecke algebra of a locally compact group and compact subgroup is the convolution algebra of compactly supported continuous bi-invariant functions."
aliases = ["Hecke convolution algebra", "C_c(K backslash G slash K)", "spherical Hecke algebra", "Hecke algebra of compactly supported bi-invariant functions"]
domains = ["harmonic-analysis", "representation-theory", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "algebra-groups/subgroup", "harmonic-analysis/haar-measure", "harmonic-analysis/convolution-on-locally-compact-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]], let \(K\leq G\) be a compact [[algebra-groups/subgroup|subgroup]], and fix a left [[harmonic-analysis/haar-measure|Haar measure]] \(dg\). The **Hecke algebra of the pair \((G,K)\)** is
\[
\mathcal H(G,K)=C_c(K\backslash G/K),
\]
the continuous compactly supported functions \(f:G\to\mathbb C\) satisfying \(f(k_1gk_2)=f(g)\), with multiplication given by [[harmonic-analysis/convolution-on-locally-compact-group|convolution]]
\[
(f_1*f_2)(x)=\int_G f_1(y)f_2(y^{-1}x)\,dy.
\]
Compact support is understood on \(G\), equivalently on the double-coset space because \(K\) is compact.

## Algebraic structure

Bi-\(K\)-invariance is preserved by convolution, and associativity follows from associativity of group convolution. When \(K\) is compact open, one may normalize \(dg(K)=1\); then the [[measure-theory/characteristic-function-indicator-function|characteristic function]] \(1_K\) belongs to \(\mathcal H(G,K)\) and is its identity. With the group-convolution involution, \(\mathcal H(G,K)\) is a star-algebra.

## Compact-open and spherical cases

If \(G\) is totally disconnected and \(K\) is compact open, the double cosets \(KgK\) are open and compact. Their [[measure-theory/characteristic-function-indicator-function|characteristic functions]] span \(\mathcal H(G,K)\), and multiplication is encoded by finite double-coset decompositions. For a reductive group over a nonarchimedean local field and a hyperspecial maximal compact subgroup, this is the usual spherical Hecke algebra treated in the Satake theory.

## Representation-theoretic action

If \(\pi\) is a [[lie-groups/strongly-continuous-unitary-representation|continuous unitary representation]] of \(G\), integration gives operators
\[
\pi(f)=\int_G f(g)\pi(g)\,dg.
\]
For bi-\(K\)-invariant \(f\), the operator \(\pi(f)\) preserves the subspace of \(K\)-fixed vectors. Thus \(\mathcal H(G,K)\) packages the part of representation theory visible to \(K\)-spherical vectors.

**Warning.** For an abstract discrete Hecke pair, one often assumes that every double coset is a finite union of one-sided cosets. That definition is related to, but not identical with, the compact-subgroup function algebra defined here.

## References

1. D. Bump, *Automorphic Forms and Representations*, Cambridge University Press, 1997. [DOI record](https://doi.org/10.1017/CBO9780511609572). Relevant: spherical functions and spherical Hecke algebras.
2. C. J. Bushnell and P. C. Kutzko, *The Admissible Dual of GL(N) via Compact Open Subgroups*, Princeton University Press, 1993. [Publisher record](https://press.princeton.edu/books/paperback/9780691021140/the-admissible-dual-of-gln-via-compact-open-subgroups). Relevant: compact-open subgroup Hecke algebras and their representation-theoretic modules.
