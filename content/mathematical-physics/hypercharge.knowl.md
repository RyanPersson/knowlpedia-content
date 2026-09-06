+++
id = "mathematical-physics/hypercharge"
title = "Weak hypercharge"
kind = "definition"
summary = "The U(1) weight that combines with weak isospin to determine electric charge."
aliases = ["hypercharge", "weak hypercharge", "U(1)_Y"]
domains = ["mathematical-physics", "lie-groups"]
prerequisites = ["mathematical-physics/standard-model-gauge-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

**Weak hypercharge** \(Y\) is the weight labeling a one-dimensional representation of the \(U(1)_Y\) factor of the [[mathematical-physics/standard-model-gauge-group|Standard Model internal symmetry group]]. In the convention used here,
\[
Q=T_3+\frac{Y}{2},
\]
where \(T_3\) is the third weak-isospin generator. Since Standard Model hypercharges lie in \(\frac13\mathbb Z\), one may let \(z\in U(1)\) act on hypercharge \(Y\) as multiplication by \(z^{3Y}\), whose exponent is integral.

## Values in one generation

\[
Y(Q_L)=\frac13,\quad Y(L_L)=-1,\quad
Y(u_R)=\frac43,\quad Y(d_R)=-\frac23,\quad
Y(e_R)=-2,\quad Y(\nu_R)=0.
\]
Antiparticle or charge-conjugate representations carry the opposite hypercharge.

## Normalization conventions

Another widespread convention writes \(Q=T_3+Y_{\mathrm{half}}\), with
\[
Y_{\mathrm{half}}=Y/2.
\]
Thus the left-handed quark doublet has \(Y=1/3\) here and \(Y_{\mathrm{half}}=1/6\) there. A bare numerical hypercharge is ambiguous unless the convention is given.

## Generator in the \(SU(5)\) embedding

For \(\mathbb C^5=\mathbb C^2\oplus\mathbb C^3\), the defining-representation hypercharge operator is
\[
\widehat Y=\operatorname{diag}\left(1,1,-\frac23,-\frac23,-\frac23\right).
\]
The integral generator \(3\widehat Y=\operatorname{diag}(3,3,-2,-2,-2)\) exponentiates to
\[
z\longmapsto\operatorname{diag}(z^3I_2,z^{-2}I_3).
\]
Changing block order permutes the entries; dualizing reverses their signs.

## Hypercharge and the central quotient

Compatibility of these weights with weak isospin and color makes the central \(\mathbb Z_6\subset U(1)\times SU(2)\times SU(3)\) act trivially on every Standard Model multiplet. Thus the assignments factor through the effective quotient.

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §§2.3.2 and 3.1.
2. David Tong, “The Standard Model,” lecture notes, 2017. [arXiv record](https://arxiv.org/abs/1606.06687).
3. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§2–3.
