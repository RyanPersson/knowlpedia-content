+++
id = "langlands/global-nilpotent-cone"
title = "Global nilpotent cone for local systems"
kind = "definition"
summary = "The conical locus in the scheme of singularities of LocSys_G consisting of local systems equipped with a horizontal nilpotent coadjoint section."
aliases = ["spectral global nilpotent cone", "Nilp_LocSys"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/moduli-stack-of-g-local-systems", "fiber-bundles/local-system"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]] and \(G\) a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]. A point of
the scheme of singularities of
[[langlands/moduli-stack-of-g-local-systems|\(\operatorname{LocSys}_G(X)\)]]
can be represented by a pair \((E,\phi)\), where \(E\) is a \(G\)-local
system and \(\phi\) is a horizontal section of the coadjoint [[fiber-bundles/local-system|local system]]
\(\operatorname{ad}(E)^*\).

The **global nilpotent cone**
\[
\mathcal N_G\subseteq
\operatorname{Sing}\bigl(\operatorname{LocSys}_G(X)\bigr)
\]
is the conical substack of pairs for which \(\phi\) takes values in the
nilpotent cone of \(\mathfrak g^*\). For a reductive group in characteristic
zero, an invariant nondegenerate form may be used to identify this condition
with pointwise nilpotence in \(\mathfrak g\).

It is the support condition defining
[[langlands/ind-coherent-sheaves-with-nilpotent-singular-support|
\(\operatorname{IndCoh}_{\mathcal N_G}(\operatorname{LocSys}_G)\)]].

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
