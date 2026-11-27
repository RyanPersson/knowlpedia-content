+++
id = "proofs/grh/upper-divisibility/size-of-the-composite-lift"
title = "Archimedean size of the composite lift"
kind = "theorem"
summary = "For the trivial twist the composite lift multiplies the squared norms of all conjugates of the values by at most exp(h_main - m rem + 2 sum gain(p) log p + error unit)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.weylNormSq_compositeLift_le", "New.Data.weylNormSq_restrictedChain_le"]
lean_files = ["src/New/UpperBound/Size/ArchimedeanSize.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(\Psi\) a [[?lean:New.Data.IsChainDatum|chain datum]] for the trivial twist, \(\sigma\) an automorphism of \(\mathbb{C}\), \(\varphi\) a source form and \(B\in\mathbb{R}\) with \(\lVert\sigma(\varphi(g))\rVert^{2}\le e^{B}\) for all \(g\in G_f(X_0)\). Then for every \(y\in G_f(Y_m)\) the [[?lean:New.Data.compositeLift|composite lift]] satisfies
\[
\bigl\lVert\sigma\bigl(C_{1,\Psi}(\varphi)(y)\bigr)\bigr\rVert^{2}\le\exp\Bigl(B+h_{\mathrm{main}}-m\,\mathrm{rem}+2\!\!\sum_{\substack{p<x_1\ \mathrm{prime}\\\chi_K(p)\ne1}}\!\!\operatorname{gain}(p)\log p+\mathrm{err}\Bigr),
\]
where \(h_{\mathrm{main}}\) is the [[?lean:New.Data.mainAmount|main amount]], \(\mathrm{rem}\) the [[?lean:New.Data.totalRemainder|total remainder]], \(\operatorname{gain}\) the [[proofs/grh/upper-divisibility/gain|gain]] and \(\mathrm{err}=fa(\log b)^{3}\). The same bound holds for the [[?lean:New.Data.restrictedChain|restricted chain]] of any weak chain datum for the trivial twist.

## Proof

By [[proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum|expanding the gluing]], the composite lift is the restricted chain of a weak chain datum \(\Psi'\) for the trivial twist; so let \(\Psi\) be a weak chain datum.

1. *Sum over classes.* The value at \(\operatorname{diag}(y,1)\) of the \(\Psi\)-combination \(\psi\) of chains is a sum over tuples of classes \(c\) and \(t\in\operatorname{supp}\Psi\) of \(\Psi(t)\) times a product of \(m\) kernels applied to a value of \(\varphi\) ([[proofs/grh/upper-divisibility/chain-of-lifts-as-a-sum-over-classes|plain sum]]).
2. *One term.* By the bound for [[proofs/grh/upper-divisibility/size-of-one-kernel|one kernel]], applied \(m\) times, each product has \(\lVert\sigma(\cdot)\rVert\le R=\prod_{j<m}\exp(x^{50}+\tfrac12\operatorname{rs}(j))\cdot e^{B/2}\).
3. *Count.* There are at most \(\exp(x^{30})^{m}\) tuples of classes ([[proofs/grh/upper-divisibility/class-count-at-levels-containing-a-principal-level|class count]]; the levels contain the principal level \(\pi_M\pi_N\) and the ranks are at most \(n_m\)), and \(\sum_t\lvert\sigma\Psi(t)\rvert\le\exp(x^{60})\) (weak chain datum, trivial twist). By the triangle inequality, \(\lVert\sigma\psi(\operatorname{diag}(y,1))\rVert\le\exp(mx^{30}+x^{60})R\).
4. *Restriction.* By the [[proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m|size of the restriction]], the squared norm is multiplied by at most \(\exp(x^{70}-\sum_\tau n_\tau\log N)\), and \(\sum_\tau n_\tau=\lvert\Phi_a\rvert a-fm\Delta/2\) ([[?lean:New.Data.sum_branchExponent|formula for the branching exponents]], quoted).
5. *Exponent.* Altogether the exponent is
\[
B+x^{70}-\bigl(\lvert\Phi_a\rvert a-fm\tfrac\Delta2\bigr)\log N+2mx^{30}+2x^{60}+2mx^{50}+\sum_{j<m}\operatorname{rs}(j).
\]
By the bound for the rows, \(\sum_j\operatorname{rs}(j)\le\operatorname{cs}+\tfrac12\mathrm{err}\); by the lemma that [[proofs/grh/upper-divisibility/level-compensates-the-excess|the level compensates the excess]], \(\operatorname{cs}-\lvert\Phi_a\rvert a\log N\le h_{\mathrm{main}}-m\,\mathrm{rem}+2\sum\operatorname{gain}(p)\log p+32fa\log b\); and \(x^{70}+fm\tfrac\Delta2\log N+2(mx^{30}+x^{60}+mx^{50})+32fa\log b\le\tfrac12\mathrm{err}\) (size comparison, quoted). \(\blacksquare\)

*Status.* Complete relative to the cited knowls and the quoted comparisons.

## Remarks

The head of the source file names as related work on algebraic modular forms as values on lattice classes: Gross, *Algebraic modular forms* (1999); Greenberg–Voight, *Lattice methods for algebraic modular forms on classical groups* (2014).

## References

1. Lean: `New.Data.weylNormSq_compositeLift_le`, `New.Data.weylNormSq_restrictedChain_le` in `src/New/UpperBound/Size/ArchimedeanSize.lean`.
