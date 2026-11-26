+++
id = "proofs/grh/upper-divisibility/valuation-and-colength-at-a-full-mark"
title = "Exceptional primes: valuation and colength at a full mark"
kind = "theorem"
summary = "For a full mark, the chain has valuation at least gain minus twice the loss on the image of the m-th power of the product of the scaled Hecke operators, and that image plus p^(j_p) times the integral forms has colength at most loss times the dimension."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_of_isFullMark", "New.Data.IsMarked.isOntoUpToColength_prod_scaledHeckeOperator_pow", "New.Data.IsMarked.mul_sum_heckeScalingExponent_le_loss", "New.Data.IsChainDatum.gaugeLe_compositeLift_of_isFullMark"]
lean_files = ["src/New/UpperBound/Divisibility/LocalDivisibility.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]], \(Y=\prod_{\mathfrak l\in\Lambda}\widetilde T_{\mathfrak l}\) the product of the [[proofs/grh/upper-divisibility/scaled-hecke-operator|scaled Hecke operators]], \(\mathcal M\) the module of integral source forms and \(j_p=\lceil2mfa/p\rceil\).

**Theorem.**

1. (**Valuation.**) Let \(\Lambda\) be a full mark, \(\vartheta\) a twist with modulus prime to \(p\), \(\Psi\) a weak chain datum for \(\vartheta\) and \(v\in\mathcal M\). Then \(R_\Psi(Y^{m}v)\) has valuation at least \(\operatorname{gain}(p)-2\operatorname{loss}(p)\).
2. (**Colength.**) \(Y^{m}\mathcal M\subset\mathcal M\), and there is a natural number \(c\le\operatorname{loss}(p)\dim_{\mathbb{C}}\mathcal S\) such that every finite family in \(\mathcal M\) is carried into \(Y^{m}\mathcal M+p^{j_p}\mathcal M\) by a square matrix over \(O_\iota\) whose determinant divides \(p^{c}\).
3. Let \(\Lambda\) be a full mark and \(\Psi\) a chain datum for \(\vartheta\) (modulus prime to \(p\)). For every source form \(\varphi\in Y^{m}\mathcal M+p^{j_p}\mathcal M\) the composite lift \(C_{\vartheta,\Psi}(\varphi)\) has valuation at least \(\operatorname{gain}(p)-2\operatorname{loss}(p)\).

## Proof

(1) By the [[proofs/grh/upper-divisibility/valuation-of-a-chain-at-a-non-split-prime|valuation on the image of the scaled Hecke operators]], the gauge is at most \(p^{\sum_{j<m}(\lvert\Lambda\rvert\nu_p+\operatorname{ll}_\Lambda(j))}\), where \(\operatorname{ll}_\Lambda(j)=\mathfrak r\sum_{\sigma\in\Phi_\Lambda}c_j(\sigma)-\operatorname{db}_{p,j}(\Phi_\Lambda)\). For \(j<m\):

- [[proofs/grh/upper-divisibility/only-collisions-lose|only collisions lose]] with \(S=\Phi_\Lambda\), where the collision sum vanishes ([[proofs/grh/upper-divisibility/full-mark-exists|full mark]]) and \(v(\pi_p)=1\) (as \(p\ne d\)): \(\operatorname{db}_{p,j}(\Phi_\Lambda)\ge\operatorname{gain}(p)/m+\lvert\Phi_a\cap\Phi_\Lambda\rvert a/x_1-f(\log b)^2(a/p)/m\);
- the [[proofs/grh/upper-divisibility/cost-of-low-columns-at-marked-places|cost of the transfer and of the low columns]]: \(\lvert\Lambda\rvert\nu_p+\mathfrak r\sum_{\Phi_\Lambda}c_j\le\operatorname{loss}(p)/m+\lvert\Phi_a\cap\Phi_\Lambda\rvert a/x_1\).

The surplus \(a/x_1\) per marked a-place cancels, and \(f(\log b)^2(a/p)\le\operatorname{loss}(p)\); so \(\lvert\Lambda\rvert\nu_p+\operatorname{ll}_\Lambda(j)\le(2\operatorname{loss}(p)-\operatorname{gain}(p))/m\). Sum over \(j<m\).

(2) \(Y^{m}\) is the product of \(m\lvert\Lambda\rvert\) scaled Hecke operators. Each is onto modulo \(p^{j_p}\) up to colength \((12A_{\mathfrak l}/(mp)+j_p/(m^2f))\dim\mathcal S\) ([[proofs/grh/upper-divisibility/mark-operator|elementary divisors of one operator]]), and these bounds add under products of operators preserving \(\mathcal M\) ([[?lean:New.IsOntoUpToColength.prod|`IsOntoUpToColength.prod`]], quoted). It remains to check
\[
m\sum_{\mathfrak l\in\Lambda}\Bigl(\frac{12A_{\mathfrak l}}{mp}+\frac{j_p}{m^{2}f}\Bigr)\le\operatorname{loss}(p).
\]
Now \(\sum_{\mathfrak l}A_{\mathfrak l}\le af\), \(\lvert\Lambda\rvert\le f\), \(j_p\le2mfa/p+1\); so the left side is at most \(12af/p+(2fa/p+1/m)=(14fa+p/m)/p\le f(\log b)^2a/p\le\operatorname{loss}(p)\), the middle step being a size comparison (quoted).

(3) By [[proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum|expanding the gluing]] the composite lift is \(R_{\Psi'}\) for a weak chain datum \(\Psi'\). Write \(\varphi=Y^{m}u+p^{j_p}v\) with \(u,v\in\mathcal M\). The first term is handled by (1); the second has valuation at least \(\operatorname{gain}-\operatorname{loss}\ge\operatorname{gain}-2\operatorname{loss}\) by the [[proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes|crude bound]]. Gauges are ultrametric. \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/LocalDivisibility.lean`.
2. Related work named in the head of the Lean file: S. Rallis, *Langlands' functoriality and the Weil representation*, 1982; V. Lafforgue, *Estimées pour les valuations p-adiques des valeurs propres des opérateurs de Hecke*, 2011.
