+++
id = "algebraic-geometry-foundations/derived-algebraic-stack"
title = "Derived algebraic stack"
kind = "definition"
summary = "A derived stack with representable diagonal and a smooth surjective atlas by derived affine schemes."
aliases = ["derived Artin stack", "derived algebraic stack"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/grothendieck-topology", "shared-foundations/surjective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **derived algebraic stack**, or **derived Artin stack**, is a stack
\(\mathcal X\) on derived affine schemes such that:

1. the diagonal
   \(\mathcal X\to\mathcal X\times\mathcal X\) is representable by derived
   algebraic spaces; and
2. there is a family of derived affine schemes \(U_i\) and a smooth
   surjective morphism
   \[
   \coprod_i U_i\longrightarrow\mathcal X.
   \]

The precise definition is made recursively by geometric level: the
representability required of the diagonal is one level lower than that
required of \(\mathcal X\). It also depends on a chosen model of derived
commutative rings and a [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]].

## Classical truncation

The classical truncation \(t_0(\mathcal X)\) is an
[[algebraic-geometry-foundations/algebraic-stack|ordinary algebraic stack]].
The higher homotopy sheaves of the derived structure sheaf retain
infinitesimal intersection and deformation data that truncation forgets.

## References

1. Bertrand Toën and Gabriele Vezzosi, “Homotopical Algebraic Geometry II:
   Geometric stacks and applications,” *Memoirs of the American Mathematical
   Society* 193 (2008), no. 902.
   [DOI](https://doi.org/10.1090/memo/0902).
