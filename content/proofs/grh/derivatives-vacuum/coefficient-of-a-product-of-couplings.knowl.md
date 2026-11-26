+++
id = "proofs/grh/derivatives-vacuum/coefficient-of-a-product-of-couplings"
title = "The coefficient of a product of couplings in a product of copies"
kind = "theorem"
summary = "For F = W exp(kappa Xi) with Xi the coupling sum and a coupling family, the coefficient of z'^(nu') z''^(nu'') in F(z'+z'') times the product of F(delta_c z') has valuation |j| v(kappa) - v(nu''!)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsCouplingFamily.norm_coeff_pairExponent"]
lean_files = ["src/New/Derivatives/Sharpness/Couplings.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/unit-coefficient-at-the-power-degree|the lemma on the power degree]].

**Theorem.** Let \((\Phi_0,e)\) be a [[proofs/grh/derivatives-vacuum/coupling-family|coupling family]], \(l_{a,0}\) units for odd \(a\), \(\kappa\in\mathbb{C}_p\) with \(\lvert\kappa\rvert_p>1\), \(W\in\mathcal{O}[\![z]\!]\) a unit, and \(F=W\exp(\kappa\Xi)\). Let \(\delta_0=1,\delta_1,\dots,\delta_n\in\mathbb{C}_p\) be such that \(\prod_{c=0}^nF(\delta_cz)=U\) is integral with constant term \(1\). Then for every \(j\colon\Phi\to\mathbb{N}\), with \(G(z',z'')=F(z'+z'')\prod_{c\ne0}F(\delta_cz')\),
\[ \bigl\lvert\nu''!\bigr\rvert_p\cdot\bigl\lvert[z'^{\nu'}z''^{\nu''}]\,G\bigr\rvert_p=\lvert\kappa\rvert_p^{\,\lvert j\rvert},\qquad\nu''!=\prod_x\nu''_x!,\quad\lvert j\rvert=\sum_{\tau\in\Phi_0}j_\tau . \]

## Proof

Apply [[proofs/grh/derivatives-vacuum/derivatives-of-exponential-factorizations|the lemma on derivatives]] to the family of variables consisting of \(j_\tau\) copies of \(\tau^+\) for each \(\tau\in\Phi_0\) (so \(\prod\partial_{z''_{t_i}}=\partial_{z''}^{\nu''}\)) and \(f=z'^{\nu'}\):
\[ \bigl(\partial_{z'}^{\nu'}\partial_{z''}^{\nu''}G\bigr)(0)=\kappa^{\lvert j\rvert}\bigl(\partial_{z'}^{\nu'}(gG)\bigr)(0),\qquad g(z',0)\equiv\prod_{\tau\in\Phi_0}(\partial_{z_{\tau^+}}\Xi)^{j_\tau}(z'). \]
The right-hand jet only involves \(z''=0\), where \(G(z',0)=\prod_cF(\delta_cz')=U(z')\). So it equals \(\nu'!\) times the coefficient of \(z'^{\nu'}\) in \(g(z',0)U(z')\), which is a unit by [[proofs/grh/derivatives-vacuum/unit-coefficient-at-the-power-degree|the lemma on the power degree]]. The left side is \(\nu'!\,\nu''!\,[z'^{\nu'}z''^{\nu''}]G\). Cancel \(\nu'!\) and take absolute values.

## References

1. Lean: `New.IsCouplingFamily.norm_coeff_pairExponent` in `src/New/Derivatives/Sharpness/Couplings.lean`.
