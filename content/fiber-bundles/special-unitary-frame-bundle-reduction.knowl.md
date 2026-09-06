+++
id = "fiber-bundles/special-unitary-frame-bundle-reduction"
title = "Special unitary frame bundle"
kind = "definition"
summary = "The principal SU(n)-bundle of unitary frames calibrated by a chosen unit determinant trivialization."
aliases = ["special-unitary-frame-bundle-reduction", "Special unitary frame bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/hermitian-metric", "fiber-bundles/nowhere-vanishing-section", "fiber-bundles/unitary-frame-bundle-reduction"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "fiber-bundles/special-unitary-frame-bundle-reduction.md"
+++

Let \(E\to M\) be a rank-\(n\) complex [[fiber-bundles/vector-bundle|vector bundle]] with a [[fiber-bundles/hermitian-metric|Hermitian metric]], and let
\[
\det(E):=\Lambda^nE.
\]
Choose a unit-norm [[fiber-bundles/nowhere-vanishing-section|nowhere-vanishing section]]
\(\Omega\in\Gamma(\det(E))\). The **special unitary frame bundle determined by \(\Omega\)** is
\[
\mathrm{SU}(E,\Omega)
=
\left\{(e_1,\ldots,e_n)\in\mathrm U(E):
e_1\wedge\cdots\wedge e_n=\Omega_{\pi(e_1,\ldots,e_n)}
\right\},
\]
where \(\mathrm U(E)\) is the [[fiber-bundles/unitary-frame-bundle-reduction|unitary frame bundle]]. It is a principal \(\mathrm{SU}(n)\)-subbundle of \(\mathrm U(E)\).

## Existence and equivalent data

The Hermitian metric on \(E\) induces one on the [[fiber-bundles/exterior-power-bundle|determinant line bundle]] \(\det(E)\). The following data are equivalent:

1. a reduction of \(\mathrm U(E)\) from \(\mathrm U(n)\) to \(\mathrm{SU}(n)\);
2. a unit-norm trivializing section \(\Omega\) of \(\det(E)\);
3. a trivialization of \(\det(E)\) as a Hermitian line bundle.

Consequently, an \(\mathrm{SU}(n)\)-reduction exists exactly when \(\det(E)\) is trivial as a complex [[fiber-bundles/line-bundle|line bundle]]. The reduction is not determined by \(E\) and its metric alone: different unit determinant sections generally give different reductions.

There is no intrinsic condition that a unitary frame have “determinant \(1\)” until such a section is chosen. Intrinsically, the determinant homomorphism gives the associated principal bundle
\[
\mathrm U(E)\times_{\det}\mathrm U(1)\cong \mathrm U(\det E),
\]
and \(\Omega\) selects its identity frame in every fiber.

## Examples

1. **Trivial bundle.** For \(E=M\times\mathbb C^n\) and
   \(\Omega=\mathbf e_1\wedge\cdots\wedge\mathbf e_n\),
   \(\mathrm{SU}(E,\Omega)\cong M\times\mathrm{SU}(n)\).
2. **Rank one.** When \(n=1\), an \(\mathrm{SU}(1)\)-reduction exists exactly when \(E\) is trivial. A chosen unit section \(\Omega\) identifies the reduced bundle with \(M\), but this identification depends on \(\Omega\).
