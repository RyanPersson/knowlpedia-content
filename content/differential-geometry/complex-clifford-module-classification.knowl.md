+++
id = "differential-geometry/complex-clifford-module-classification"
title = "Classification of complex Clifford modules"
kind = "theorem"
summary = "The irreducible ungraded modules of a complex Clifford algebra are determined by the parity of the dimension."
aliases = ["complex Clifford algebra classification", "classification of complex spinor modules"]
domains = ["differential-geometry", "algebra-modules", "representation-theory"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/clifford-algebra", "differential-geometry/clifford-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(V\) be an \(n\)-dimensional complex vector space with a nondegenerate
[[linear-algebra/quadratic-form|quadratic form]]. Up to isomorphism, its complex
[[differential-geometry/clifford-algebra|Clifford algebra]] is
\[
\operatorname{Cl}(V)\cong
\begin{cases}
\operatorname{Mat}_{2^m}(\mathbb C),&n=2m,\\[2mm]
\operatorname{Mat}_{2^m}(\mathbb C)\oplus
\operatorname{Mat}_{2^m}(\mathbb C),&n=2m+1.
\end{cases}
\]
Consequently, in even dimension there is one irreducible ungraded complex
[[differential-geometry/clifford-module|Clifford module]], of dimension
\(2^m\). In odd dimension there are two inequivalent irreducible ungraded
modules, each of dimension \(2^m\).

## Restriction to the spin group

In dimension \(2m\), the restriction of the irreducible Clifford module to
the even Clifford algebra, and hence to the [[lie-groups/spin-group|spin group]], decomposes as
\[
\Delta_{2m}=\Delta_{2m}^{+}\oplus\Delta_{2m}^{-}.
\]
The two summands are the irreducible half-spin modules, and Clifford
multiplication by a vector interchanges them.

In dimension \(2m+1\), the two irreducible ungraded Clifford modules restrict
to equivalent irreducible spin representations. That odd-dimensional spin
representation has no intrinsic chiral decomposition.

## Scope

Over \(\mathbb C\), the classification depends on dimension parity but not on
the signature of a real form. The classification of real Clifford modules is
different: it depends on the signature and is \(8\)-periodic.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I,
   §§4–5.
2. Pierre Deligne, “Notes on spinors,” in *Quantum Fields and Strings: A
   Course for Mathematicians*, Volume 1, American Mathematical Society, 1999,
   pp. 99–135.
