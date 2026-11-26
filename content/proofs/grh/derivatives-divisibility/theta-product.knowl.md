+++
id = "proofs/grh/derivatives-divisibility/theta-product"
title = "Product of theta functions along linear forms"
kind = "definition"
summary = "The power series prod theta(mu_j z)^(m_j) over C_p for linear forms mu_j, and the ring of integral series in the y(mu_i z); behaviour under scaling and partial derivatives."
aliases = ["theta product", "ring of integral series in y(mu z)"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.thetaProd", "New.CMLattice.rescale_thetaProd", "New.CMLattice.rescale_mem_multiSeriesRing", "New.CMLattice.pderiv_mem_multiSeriesRing", "New.rescale_subst_linearSeries_eq_subst_smul", "New.Space.jetSeries_mul_eq_rescale", "New.map_rescale"]
lean_files = ["src/New/Derivatives/FormalGroup/Resolution.lean"]
+++

**Definition (theta product).** Let \(C\) be a CM lattice with theta function \(\theta\) and coordinate series \(y\), read in \(\mathbb{C}_p[[t]]\) through a \(p\)-adic place (see the [[proofs/grh/derivatives-divisibility/cm-curve-setting|CM lattice]]). Let \(X\) and \(J\) be finite sets, \(\mu_j=(\mu_{j,x})_{x\in X}\in\mathbb{C}_p^X\) for \(j\in J\), read as the linear forms \(\mu_jz=\sum_x\mu_{j,x}z_x\), and \(m_j\in\mathbb{N}\). The **theta product** is
\[
\theta_{\mu,m}(z)=\prod_{j\in J}\theta(\mu_jz)^{m_j}\in\mathbb{C}_p[[z_x:x\in X]] ,
\]
where \(\theta(\mu_jz)\) is the [[algebra-rings/substitution-of-formal-power-series|substitution]] of the linear form into the series \(\theta\). The ring \(\mathcal{O}[[y(\mu z)]]\) is the set of all series \(G\bigl((y(\mu_jz))_{j\in J}\bigr)\) with \(G\) an integral power series in variables indexed by \(J\); it is defined in the library as [[?lean:New.CMLattice.multiSeriesRing|the ring of integral series in the \(y(\mu_jz)\)]].

## Properties

1. \(\theta_{\mu,m}(az)=\theta_{a\mu,m}(z)\) for \(a\in\mathbb{C}_p\).
2. If \(H\in\mathcal{O}[[y(\mu z)]]\) and \(a\in\mathbb{C}_p\), then \(H(az)\in\mathcal{O}[[y((a\mu)z)]]\).
3. Let \(d\equiv 7\pmod 8\) be prime and all \(\lvert\mu_{j,x}\rvert\le1\). Then \(\mathcal{O}[[y(\mu z)]]\) is stable under the partial derivatives \(\partial/\partial z_x\).

## Proof

1 and 2 hold because scaling all variables by \(a\) in \(f(\mu_jz)\) gives \(f((a\mu_j)z)\), and scaling commutes with products and with substitution into \(G\). For 3, the chain rule gives \(\partial_x\,G(y(\mu z))=\sum_j(\partial_jG)(y(\mu z))\cdot\mu_{j,x}\,y'(\mu_jz)\); here \(\partial_jG\) is integral, \(\mu_{j,x}\in\mathcal{O}\), and \(y'\in\mathcal{O}[[y]]\) (fact 1 of the setting), so \(y'(\mu_jz)\) is an integral series in \(y(\mu_jz)\). \(\blacksquare\)

## Remarks

The source file also records that multiplying the scale \(b\) of the [[?lean:New.Space.jetSeries|jet series]] of a theta functional by \(a\) scales its variables by \(a\) (`New.Space.jetSeries_mul_eq_rescale`); this links the series treated here with the theta functionals of the other chapters.

## References

1. Lean: `New.CMLattice.thetaProd`, `New.CMLattice.rescale_thetaProd`, `New.CMLattice.rescale_mem_multiSeriesRing`, `New.CMLattice.pderiv_mem_multiSeriesRing` in `src/New/Derivatives/FormalGroup/Resolution.lean`.
