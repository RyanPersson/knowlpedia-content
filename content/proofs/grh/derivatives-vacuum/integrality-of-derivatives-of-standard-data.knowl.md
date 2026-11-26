+++
id = "proofs/grh/derivatives-vacuum/integrality-of-derivatives-of-standard-data"
title = "Integrality and divisibility of the derivatives of standard data at all primes"
kind = "theorem"
summary = "Jets of the jet series of standard data of level delta at scale c times the jet scale, along a homogeneous p-integral polynomial of degree l, have p-adic absolute value at most that of c / (conj(delta) d) to the power l."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_jet_jetSeries_le_pow", "New.Parameters.norm_jet_jetSeries_le_one"]
lean_files = ["src/New/Derivatives/Vacuum/Divisibility.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E=K(\zeta)\) with finite index set \(n\), \(p\) a prime, \(\iota_p\) a \(p\)-adic place of \(\mathbb{C}\) with valuation ring \(R_p\), and \(\lambda\) the [[proofs/grh/derivatives-vacuum/jet-scale|jet scale]].

**Theorem.** Let \(\delta\in\mathcal{O}_K\), \(\delta\ne0\), and \(f\) [[proofs/grh/derivatives-vacuum/standard-data|standard data]] of level \(\delta\) at \(p\). Let \(Q\) be a polynomial in the variables \(X_{(\tau,i)}\) with coefficients in \(R_p\).

1. \(\bigl\lvert\iota_p\bigl(Q(\partial)J_{\bar\delta d\lambda}(f)\bigr)(0)\bigr\rvert_p\le1\).
2. If \(Q\) is homogeneous of degree \(l\) and \(c\in\mathbb{C}\), then
\[ \bigl\lvert\iota_p\bigl(Q(\partial)J_{c\lambda}(f)\bigr)(0)\bigr\rvert_p\le\Bigl\lvert\iota_p\Bigl(\frac{c}{\bar\delta\,d}\Bigr)\Bigr\rvert_p^{\,l}. \]

## Proof

1. Let \(N=\delta\bar\delta\in\mathbb{N}\). By [[proofs/grh/derivatives-vacuum/standard-data-as-theta-products|standard data as theta products]] there are \(u_j\), \(m_j\) with \(\alpha^{-1}u_j\) integral above \(p\) and \(H\in\mathcal{O}[\![y(u^\dagger z)]\!]\) such that \(\iota_pJ_{\bar\delta c_A/\Omega_0}(f)=\Theta^NH\), \(\Theta=\prod_j\theta(u_j^\dagger z)^{m_j}\). Now \(\bar\delta d\lambda=a\cdot\bar\delta c_A/\Omega_0\) with \(a=d\varpi\), and changing the scale by \(a\) rescales all variables by \(a\). Hence
\[ \iota_pJ_{\bar\delta d\lambda}(f)=\Bigl(\prod_j\theta(d\,\nu_jz)^{m_j}\Bigr)^NH',\qquad\nu_j=\iota_p(\varpi)\,u_j^\dagger, \]
where \(H'(z)=H(\iota_p(a)z)\) is an integral series in the \(y(d\nu_jz)\). By [[proofs/grh/derivatives-vacuum/scaled-linear-forms-are-p-integral|integrality of scaled linear forms]] the coefficients of \(\nu_j\) are integral. So [[proofs/grh/derivatives-vacuum/integrality-of-jets-of-theta-products|integrality of jets of theta products]] applies (with \(\varphi=\iota_p\) on \(R_p\)).

2. \(c\lambda=\frac{c}{\bar\delta d}\cdot\bar\delta d\lambda\), and rescaling the variables by a constant multiplies the jet along a homogeneous polynomial of degree \(l\) by its \(l\)-th power ([[proofs/grh/derivatives-vacuum/jets-along-homogeneous-polynomials|jets along homogeneous polynomials]]). Apply 1.

## References

1. Lean: `New.Parameters.norm_jet_jetSeries_le_pow`, `New.Parameters.norm_jet_jetSeries_le_one` in `src/New/Derivatives/Vacuum/Divisibility.lean`.
