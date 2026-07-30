+++
id = "differential-geometry/spinor-module"
title = "Spinor module"
kind = "definition"
summary = "A Clifford module whose restriction realizes a spin representation."
aliases = ["spin module", "space of algebraic spinors"]
domains = ["differential-geometry", "representation-theory"]
section_mode = "progressive"
+++

Let \((V,q)\) be a finite-dimensional nondegenerate real or complex quadratic
space. A **spinor module** \(\Delta\) is a specified
[[differential-geometry/clifford-module|module]] for the corresponding real,
complex, or complexified [[differential-geometry/clifford-algebra|Clifford
algebra]], usually chosen irreducible in the relevant module category. Since
the spin group lies in the group of units of the even Clifford algebra, the
Clifford action restricts to a representation
\[
\rho:\operatorname{Spin}(V,q)\longrightarrow\operatorname{GL}(\Delta),
\]
called a **spin representation**.

## Complex spinors by dimension

Over \(\mathbb C\), signature does not change the isomorphism class of the
Clifford algebra, but dimension parity does. In dimension \(2m\), the complex
Clifford algebra has a unique irreducible module \(\Delta_{2m}\) of dimension
\(2^m\). Its restriction to the spin group decomposes into the two half-spin
or Weyl modules
\[
\Delta_{2m}=\Delta_{2m}^+\oplus\Delta_{2m}^-.
\]
Clifford multiplication by a vector interchanges these two summands.

In dimension \(2m+1\), the complex Clifford algebra has two inequivalent
irreducible ungraded modules, but their restrictions give equivalent
irreducible spin representations of dimension \(2^m\). There is no intrinsic
chiral splitting of that irreducible odd-dimensional spin representation.

## Dirac, Weyl, Majorana, and Majorana–Weyl terminology

| Term | Algebraic meaning | Existence caution |
|---|---|---|
| Dirac spinor | An element of a chosen complex spinor module, often containing both chiralities in even dimension. | Depends on the chosen complex Clifford-module convention. |
| Weyl spinor | An element of one half-spin module \(\Delta^+\) or \(\Delta^-\). | Requires even dimension and a chiral decomposition. |
| Majorana spinor | A spinor fixed by a compatible \(\operatorname{Spin}(p,q)\)-equivariant real structure on a complex spin module. | Such a real structure exists only in appropriate signatures. |
| Majorana–Weyl spinor | A spinor that is simultaneously Majorana and of one chirality. | Requires a compatible real structure that preserves a half-spin module; this is strongly signature-dependent. |

“Majorana” is not a synonym for “real coefficients in a selected gamma-matrix
basis.” It refers invariantly to a real structure on the representation.
Whether that structure exists, squares to \(+1\) rather than \(-1\), and
preserves chirality is governed by the real Clifford algebra and its
mod-\(8\) classification. Signature order and the convention
\(v^2=\pm q(v)\) must be fixed before quoting a residue-class table.

## From modules to bundles

Given a spin structure on a manifold, a chosen spinor module produces the
[[differential-geometry/spinor-bundle|spinor bundle]] by the associated-bundle
construction. Clifford multiplication then acts fiberwise, and a lifted
metric connection yields the corresponding Dirac operator.

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
