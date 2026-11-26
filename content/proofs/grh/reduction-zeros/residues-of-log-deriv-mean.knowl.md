+++
id = "proofs/grh/reduction-zeros/residues-of-log-deriv-mean"
title = "Residues of G_q and of the transform"
kind = "lemma"
summary = "G_q has at most simple poles, with residue the mean of the differences of orders of vanishing; the same for (G_q(z)/z - kappa)/(z-1) after division by rho(rho-1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.tendsto_sub_mul_logDerivMean", "New.tendsto_logDerivMean_residue"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime, \(q\ge1\), and \(G_q\), \(E_\psi\), \(E_{\psi\chi_K}\) as in the [[proofs/grh/reduction-zeros/log-deriv-mean|definition of \(G_q\)]]. For \(\rho\in\mathbb{C}\) put
\[
m(\rho)=\frac1{\varphi(q)}\sum_{\psi\bmod q}\bigl(\operatorname{ord}_\rho E_{\psi\chi_K}-\operatorname{ord}_\rho E_\psi\bigr).
\]

1. \(\displaystyle\lim_{z\to\rho,\,z\ne\rho}(z-\rho)\,G_q(z)=m(\rho)\).
2. For every constant \(\kappa\in\mathbb{C}\) and every \(\rho\notin\{0,1\}\),
\[
\lim_{z\to\rho,\,z\neq\rho}(z-\rho)\,\frac{G_q(z)/z-\kappa}{z-1}=\frac{-m(\rho)}{\rho(1-\rho)}=\frac{1}{\varphi(q)\,\rho(1-\rho)}\sum_{\psi}\bigl(\operatorname{ord}_\rho E_{\psi}-\operatorname{ord}_\rho E_{\psi\chi_K}\bigr).
\]

## Proof

1. By the [[proofs/grh/reduction-zeros/residue-of-log-deriv-entire-l|residue lemma for one \(L\)-function]], \((z-\rho)E_\chi'(z)/E_\chi(z)\to\operatorname{ord}_\rho E_\chi\) for each character \(\chi\). Multiply the definition of \(G_q\) by \(z-\rho\); the term \(-(z-\rho)/\varphi(q)\) tends to \(0\).

2. \((z-\rho)\dfrac{G_q(z)/z-\kappa}{z-1}=\dfrac{(z-\rho)G_q(z)/z-(z-\rho)\kappa}{z-1}\to\dfrac{m(\rho)/\rho}{\rho-1}\), since \(\rho\ne0\) and \(\rho\ne1\). \(\blacksquare\)

## References

1. Lean: `New.tendsto_sub_mul_logDerivMean`, `New.tendsto_logDerivMean_residue` in `src/New/Reduction/Zeros/PrimeError.lean`.
