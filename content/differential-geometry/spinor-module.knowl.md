+++
id = "differential-geometry/spinor-module"
title = "Spinor module"
kind = "definition"
summary = "A chosen Clifford module whose restriction to the spin group is a spin representation."
aliases = ["spin module", "space of algebraic spinors"]
domains = ["differential-geometry", "representation-theory"]
section_mode = "progressive"
prerequisites = ["differential-geometry/clifford-module", "differential-geometry/clifford-algebra", "lie-groups/spin-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((V,q)\) be a finite-dimensional nondegenerate real or complex quadratic
space. A **spinor module** \(\Delta\) is a specified
[[differential-geometry/clifford-module|module]] for the corresponding real,
complex, or complexified [[differential-geometry/clifford-algebra|Clifford
algebra]], usually chosen irreducible in the relevant module category. Since
the [[lie-groups/spin-group|spin group]] lies in the group of units of the even Clifford algebra, the
Clifford action restricts to a representation
\[
\rho:\operatorname{Spin}(V,q)\longrightarrow\operatorname{GL}(\Delta),
\]
called a **spin representation**.

## Irreducibility and scalar field

The phrase “a spinor module” does not specify a unique module until the scalar
field, signature, grading convention, and irreducibility condition have been
fixed. Over \(\mathbb C\), the possibilities are described by the
[[differential-geometry/complex-clifford-module-classification|classification
of complex Clifford modules]]. Over \(\mathbb R\), the answer depends on the
signature modulo \(8\).

These choices also determine which additional spinor conditions exist. A
[[differential-geometry/dirac-spinor|Dirac spinor]] is complex, a
[[differential-geometry/weyl-spinor|Weyl spinor]] has a specified chirality,
and [[differential-geometry/majorana-spinor|Majorana]] and
[[differential-geometry/majorana-weyl-spinor|Majorana–Weyl spinors]] use
compatible real structures. These are distinct definitions rather than
interchangeable names for elements of \(\Delta\).

## From modules to bundles

Given a [[fiber-bundles/spin-structure|spin structure]] on a manifold, a chosen spinor module produces the
[[differential-geometry/spinor-bundle|spinor bundle]] by the associated-bundle
construction. Clifford multiplication then acts fiberwise, and a lifted
metric connection yields the corresponding [[noncommutative-geometry/dirac-operator|Dirac operator]].

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I,
   Sections 4–5.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
3. Pierre Deligne, “Notes on spinors,” in *Quantum Fields and Strings: A
   Course for Mathematicians*, Volume 1, American Mathematical Society, 1999,
   pp. 99–135. Relevant: signature-dependent real and complex spinors.
