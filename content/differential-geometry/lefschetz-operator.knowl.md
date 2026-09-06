+++
id = "differential-geometry/lefschetz-operator"
title = "Lefschetz operator"
kind = "definition"
summary = "The degree-two operator given by wedging with a symplectic form or multiplying by its cohomology class."
aliases = ["L operator", "cup product with the Kähler class"]
domains = ["differential-geometry", "topology"]
prerequisites = ["differential-geometry/symplectic-manifold", "linear-algebra/linear-map", "fiber-bundles/exterior-derivative"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((X,\omega)\) be a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]]. The **Lefschetz operator** on differential forms is the degree-two [[linear-algebra/linear-map|linear map]]
\[
L:\Omega^k(X)\longrightarrow\Omega^{k+2}(X),\qquad L(\alpha)=\omega\wedge\alpha.
\]
Because \(d\omega=0\), it commutes with the [[fiber-bundles/exterior-derivative|exterior derivative]] and induces
\[
L:H^k_{\mathrm{dR}}(X)\longrightarrow H^{k+2}_{\mathrm{dR}}(X),\qquad
L[\alpha]=[\omega]\smile[\alpha].
\]
When \(X\) is Kähler, \(\omega\) has type \((1,1)\), so \(L\) also maps \((p,q)\)-forms to \((p+1,q+1)\)-forms. The same symbol \(L\) is conventionally used for all these compatible operators.

## Linear-algebraic structure

On a [[differential-geometry/symplectic-vector-space|symplectic vector space]], multiplication by \(\omega\) has an adjoint lowering operator \(\Lambda\), defined using contraction with the inverse bivector after conventions are fixed. Together with their grading commutator, \(L\) and \(\Lambda\) form an \(\mathfrak{sl}_2\)-triple. This representation-theoretic structure yields the decomposition of forms into powers of \(L\) applied to primitive forms.

## Cohomological consequences

On a compact [[differential-geometry/kahler-manifold|Kähler manifold]], the [[differential-geometry/hard-lefschetz-theorem|Hard Lefschetz theorem]] says that appropriate powers of the cohomological operator are isomorphisms between complementary degrees. It follows that cohomology also has a primitive Lefschetz decomposition. For a general symplectic manifold, \(L\) is still defined, but these cohomological isomorphisms can fail.

## Conventions and examples

On [[algebraic-geometry-foundations/projective-space|complex projective space]] with its Fubini–Study form, \(L\) is multiplication by the degree-two generator of real cohomology. Some authors normalize \(\omega\) by a scalar or define the lowering operator first; these choices change numerical formulas but not the definition \(L(\alpha)=\omega\wedge\alpha\). This operator is unrelated to the Lefschetz number of a self-map.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §6.2, Lefschetz operators, primitive forms, and the associated \(\mathfrak{sl}_2\)-action.
