+++
id = "differential-geometry/bianchi-orbifold-volume-formula"
title = "Volume formula for a Bianchi orbifold"
kind = "theorem"
summary = "The curvature-minus-one volume is the discriminant factor times a Dedekind zeta value."
aliases = []
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/bianchi-orbifold", "algebra-fields-galois/number-field-discriminant", "algebra-fields-galois/dedekind-zeta-function"]
+++

Let \(K\) be an imaginary quadratic field with [[algebra-fields-galois/number-field-discriminant|discriminant]] \(D_K\). For the [[differential-geometry/bianchi-orbifold|Bianchi orbifold]] with curvature \(-1\),
\[
\operatorname{vol}\bigl(\operatorname{PSL}_2(\mathcal O_K)\backslash\mathbb H^3\bigr)
=\frac{|D_K|^{3/2}}{4\pi^2}\,\zeta_K(2),
\]
where \(\zeta_K\) is the [[algebra-fields-galois/dedekind-zeta-function|Dedekind zeta function]].

## Normalization checks

The formula uses the full ring of integers, the projective SL group, and the curvature-\(-1\) metric. For \(K=\mathbb Q(i)\), \(|D_K|=4\), so the coefficient becomes \(2/\pi^2\).

Passing to a subgroup of index \(m\) multiplies the quotient volume by \(m\). Replacing PSL by a larger projective group therefore requires a separate index calculation; the formula cannot be transferred unchanged.

## Interpretation

The finite positive zeta value yields finite positive hyperbolic volume even though the quotient has cusp ends and is noncompact.

## References

1. F. Paulin, *Regards croisés sur les séries de Poincaré et leurs applications*, Theorem 6, p. 12. [Author’s text](https://www.imo.universite-paris-saclay.fr/~frederic.paulin/preprints/Neuchatel.pdf)
