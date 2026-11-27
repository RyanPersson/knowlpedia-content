+++
id = "proofs/grh/derivatives-vacuum/normal-form-of-standard-data"
title = "Normal form of standard data at a non-split prime"
kind = "theorem"
summary = "At a prime that does not split in K, the p-adic jet series of standard data of level one at a p-integral multiple of the jet scale has the normal form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_hasNormalForm_jetSeries", "New.Parameters.isIntegralAbove_of_finiteImage_mem"]
lean_files = ["src/New/Derivatives/Vacuum/Divisibility.lean"]
proof_status = "outline"
+++

Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E=K(\zeta)\) with index set \(n\), \(p\) a prime with \(\chi_K(p)\ne1\) (inert, or \(p=d\)), and \(\iota_p\) a \(p\)-adic place.

**Theorem.** Let \(f\) be [[proofs/grh/derivatives-vacuum/standard-data|standard data]] of level \(1\) at \(p\) and \(c\in\mathbb{C}\) with \(\lvert\iota_pc\rvert_p\le1\). Then there are \(\varpi_p\in\mathbb{C}_p\) with \(\lvert\varpi_p\rvert_p=p^{-v}\), \(v\) the [[?lean:New.varpiValuation|valuation of \(\varpi\)]] (\(1/(p^2-1)\) if \(p\) is inert, \(1/(2p-2)\) if \(p=d\)), and integral coefficients \(l_{e,j}\in\mathcal{O}_{\mathbb{C}_p}\) such that \(F=\iota_pJ_{c\lambda}(f)\) [[proofs/grh/derivatives-divisibility/normal-form|has the normal form]]
\[ F(\varpi_pz)=W\cdot\exp\Bigl(\frac{\varpi_p^{\,p+1}}{p}\sum_{e}\sum_jl_{e,j}\,\Gamma_e^{\,p^j}\Bigr), \]
with \(W\) a power series with integral coefficients, \(e\) running over the [[?lean:New.partnerExponents|partner exponents]] of \(p\) (the odd \(e\) if \(p\) is inert; all \(e\ge0\), including \(e=0\), if \(p=d\)), and \(\Gamma_e=\sum_{\tau,i}z_{(\tau,i)}^{p^e}z_{(\tau',i)}\) the [[proofs/grh/derivatives-divisibility/coupling|coupling]] of the pairs \((\tau,\tau')\) (so the exponent is \(c_{\varpi}\) times the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]] \(\Xi_{S,\mathrm{pr},l}\) with \(S\) the set of partner exponents, exactly as in the Lean definition), \(\tau'\) the [[?lean:New.Parameters.partner|partner]] of \(\tau\) (the place \(\tau\) moved by the class of \(-p^e\)).

## Proof

Primes dividing \(q_1\) split in \(K\), so \(p\nmid q_1\). By [[proofs/grh/derivatives-vacuum/standard-data-as-theta-products|standard data as theta products]] with \(\delta=1\), \(N=1\): \(\iota_pJ_{c_A/\Omega_0}(f)=\prod_j\theta(u_j^\dagger z)^{m_j}\cdot H\) for a resolution of the identity \((u_j,m_j)\) with \(\alpha^{-1}u_j\) integral above \(p\) and \(H\) an integral series in the \(y(u_j^\dagger z)\). Since \(q_1\alpha\) is integral and \(q_1\) is a unit above \(p\), \(\alpha\) is integral above \(p\), so the coordinates of \(u_j\) themselves are integral above \(p\). The theorem of the formal-group chapter ([[proofs/grh/derivatives-divisibility/normal-form-of-theta-products|normal form of theta products at non-split primes]]; not reproved here) says exactly that such a product has the normal form. Finally \(c\lambda=c\varpi\cdot c_A/\Omega_0\) and \(\lvert\iota_p(c\varpi)\rvert_p\le1\) because \(\varpi\) is a unit at \(p\nmid q_1\) ([[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|size of the period factor]]); rescaling the variables by an integral constant preserves the normal form (Lean `New.HasNormalForm.rescale`; asserted).

## References

1. Lean: `New.Parameters.exists_hasNormalForm_jetSeries`, `New.Parameters.isIntegralAbove_of_finiteImage_mem` in `src/New/Derivatives/Vacuum/Divisibility.lean`.
