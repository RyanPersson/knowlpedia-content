+++
id = "lie-groups/center-of-universal-enveloping-algebra"
title = "Center of the universal enveloping algebra"
kind = "definition"
summary = "The commutative subalgebra of enveloping-algebra elements that commute with every element."
aliases = ["infinitesimal center", "Z(U(g))"]
domains = ["lie-groups", "algebra-rings"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]] over a [[algebra-rings/field|field]] \(k\), and let \(U(\mathfrak g)\) be its [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]. The **center of the universal enveloping algebra** is
\[
Z(U(\mathfrak g))=\{z\in U(\mathfrak g):zu=uz\text{ for every }u\in U(\mathfrak g)\}.
\]
Because \(U(\mathfrak g)\) is generated as an algebra by \(\mathfrak g\), it is enough to require \(zx=xz\) for every \(x\in\mathfrak g\). This center is a commutative unital subalgebra of \(U(\mathfrak g)\), distinct from the center of the Lie algebra \(\mathfrak g\) itself.

## Action on modules

Every \(z\in Z(U(\mathfrak g))\) acts on a \(U(\mathfrak g)\)-module by a module endomorphism. A module has a **central character** when this action is scalar through an [[algebra-modules/algebra-homomorphism|algebra homomorphism]] \(Z(U(\mathfrak g))\to k\); in real-reductive representation theory this scalar action is called an [[lie-groups/infinitesimal-character|infinitesimal character]]. Scalar action is automatic only under appropriate irreducibility and endomorphism hypotheses, not for an arbitrary module.

## Semisimple structure

When \(\mathfrak g\) is complex semisimple, the center is much larger than the scalars. The [[lie-groups/harish-chandra-isomorphism|Harish–Chandra isomorphism]] identifies it with the Weyl-invariant part of a polynomial algebra on a [[lie-groups/cartan-subalgebra|Cartan subalgebra]]. In particular, \(Z(U(\mathfrak g))\) is a polynomial algebra on \(\operatorname{rank}\mathfrak g\) algebraically independent generators. The quadratic [[lie-groups/casimir-element-and-casimir-operator|Casimir element]] is the most familiar generator in rank one.

## Filtration

The standard filtration of \(U(\mathfrak g)\) restricts to its center. Under the Poincaré–Birkhoff–Witt associated-graded map, leading terms of central elements become adjoint-invariant polynomial functions. This filtered viewpoint explains why invariant polynomial theory governs the center, although the precise algebra isomorphism requires the Harish–Chandra shift.

## References

1. Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: Chapter 7 on centers and central characters.
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [DOI record](https://doi.org/10.1007/978-1-4757-2453-0). Relevant: Chapter V, §5.
