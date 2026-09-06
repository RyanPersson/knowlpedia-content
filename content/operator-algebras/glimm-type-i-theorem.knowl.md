+++
id = "operator-algebras/glimm-type-i-theorem"
title = "Glimm's type I theorem"
kind = "theorem"
summary = "Equivalent regularity criteria that characterize separable type I C*-algebras."
aliases = ["Glimm dichotomy", "Glimm theorem for separable C*-algebras"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/type-i-cstar-algebra", "operator-algebras/primitive-ideal-space", "algebra-representation-theory/irreducible-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a separable [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]
and let \(\widehat A\) be its unitary dual with the Fell topology. Glimm's
theorem says that the following are equivalent:

1. \(A\) is a [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]];
2. the kernel map from \(\widehat A\) to the
[[operator-algebras/primitive-ideal-space|primitive ideal space]]
\(\operatorname{Prim}(A)\) is bijective;
3. \(\widehat A\) is a \(T_0\) space; and
4. every nonempty closed subset of \(\widehat A\) contains a dense relatively
open Hausdorff subset.

Thus type I is exactly the regime in which [[algebra-representation-theory/irreducible-representation|irreducible representations]] are
topologically separated well enough to admit a tractable classification.

## Meaning of the kernel condition

The kernel map is always surjective. Its injectivity says that two
irreducible representations with the same primitive ideal are unitarily
equivalent. Because \(\operatorname{Prim}(A)\) is always \(T_0\), failure of
the theorem's conditions measures representation-theoretic ambiguity that the
primitive ideal alone cannot resolve.

## Almost Hausdorff structure

Condition 4 is often summarized by saying that \(\widehat A\) is almost
Hausdorff. It supplies Hausdorff pieces densely inside every closed
representation-theoretic stratum and underlies the construction of
transfinite composition series with continuous-trace layers.

## Conventions and scope

**Warning.** Separability is part of this formulation. There are
nonseparable extensions and refinements of type I characterization theorems,
but one should not drop the hypothesis from Glimm's four-way equivalence
without specifying the replacement conditions.

The name “Glimm dichotomy” is also used for stronger descriptive-set-theoretic
consequences on the non-type-I side. Those refinements are not included in the
statement above.

## References

1. James G. Glimm, “Type I \(C^*\)-algebras,” *Annals of Mathematics* 73 (1961), 572–612. [DOI record](https://doi.org/10.2307/1970319). Relevant: the main characterization of separable type I algebras.
2. Jacques Dixmier, *C*-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 4 on type I spectra and almost-Hausdorff structure.
