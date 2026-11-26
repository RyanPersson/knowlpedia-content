+++
id = "proofs/grh/upper-divisibility/integral-values-of-source-forms-as-polynomials"
title = "Integral values of source forms as polynomials"
kind = "lemma"
summary = "A vector of the weight space of X_0 has gauge at most 1 at g exactly when its polynomial, after substituting g z for z, is an integral combination of the divided monomials of multidegree a at the a-places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.weylGauge_le_one_iff_mem_span"]
lean_files = ["src/New/UpperBound/Divisibility/ChainValuation.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(g\in G_f(X_0)\), and \(\zeta\) a vector of the weight space of \(X_0\) (weight: at each a-place one row of length \(a\), nothing in heights between \(2\) and \(k-1\); no determinant twist). Let \(\operatorname{pol}(\zeta)\) be the polynomial of \(\iota\zeta\) in the variables \(z_\tau=(z_{\tau,b})_{b}\), one vector of \(k\) variables for each place \(\tau\) ([[?lean:New.toPoly|`toPoly`]]), and let \(g_\tau\) be \(g\) read in \(\mathbb{C}_p\) through \(\iota\circ\tau\). Then the [[?lean:New.weylGauge|gauge]] of \(\zeta\) at \(g\) is at most \(1\) if and only if
\[
\operatorname{pol}(\zeta)\bigl((g_\tau z_\tau)_\tau\bigr)\in\operatorname{span}_{\mathcal O_{\mathbb{C}_p}}\Bigl\{\prod_\tau\frac{a_\tau!}{\alpha_\tau!}z_\tau^{\alpha_\tau}:\ \lvert\alpha_\tau\rvert=a_\tau\Bigr\},
\]
where \(a_\tau=a\) for \(\tau\in\Phi_a\) and \(a_\tau=0\) otherwise, and \(\alpha_\tau!=\prod_b\alpha_{\tau,b}!\).

## Proof

By definition the gauge at \(g\) is the maximum norm of the coordinates of \(\mathrm{Schur}(z)\,\iota\zeta\), where \(z_\tau\) is \(g^{-1}\) read through \(\iota\circ\tau\circ\mathrm{conj}\) (weight embedding). As \(g\) is unitary, \(g^{-1}=g^{*}\), so \(z_\tau^{T}=g_\tau\). On polynomials the Schur matrix of \(z\) acts by the substitution of \(z_\tau^{T}\) ([[?lean:New.toPoly_schur|`toPoly_schur`]], quoted). For a weight with one row at each place, the coordinates of a vector are the coefficients of its polynomial with respect to the divided monomials \(\prod_\tau(a_\tau!/\alpha_\tau!)z_\tau^{\alpha_\tau}\) ([[?lean:New.toPoly_mem_span_multinomialMonomial_iff|`toPoly_mem_span_multinomialMonomial_iff`]], quoted), so the maximum norm is at most \(1\) iff the polynomial lies in their integral span. \(\blacksquare\)

*Status.* Both properties of the polynomial model of the Weyl module are quoted.

## References

1. Lean: `New.Data.weylGauge_le_one_iff_mem_span` in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
