+++
id = "proofs/grh/upper-divisibility/valuation-of-the-composite-lift-at-n"
title = "The prime N: valuation of the composite lift"
kind = "theorem"
summary = "On ramified source forms in the module A', the composite lift loses at most 2 m f b powers of N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.gaugeLe_compositeLift_at_N"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtLevel.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(\iota\colon\mathbb{C}\to\mathbb{C}_N\) an embedding, \(\vartheta\) a [[?lean:New.Data.Twist|twist]] and \(\Psi\) a [[?lean:New.Data.IsChainDatum|chain datum]] for \(\vartheta\). Let \(\varphi\) be a [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source form]] lying in the module \(\mathcal A'\) of [[proofs/grh/upper-divisibility/setup-at-the-level-prime|up-integral forms]]. Then the [[?lean:New.Data.compositeLift|composite lift]] \(C_{\vartheta,\Psi}(\varphi)\), a form on \(Y_m\), has \(N\)-adic gauge at most \(N^{2mfb}\) at base point \(1\): for every \(g\), the coordinates of \(g^{-1}\cdot\iota\bigl(C_{\vartheta,\Psi}(\varphi)(g)\bigr)\) have absolute value at most \(N^{2mfb}\).

## Proof

Let \(\psi=U^{\varrho+1}\varphi\); by hypothesis \(\psi\) is a source form of gauge at most \(1\) at base point \(\delta_0\).

1. For \(x\) in the support of \(\Psi\) the translated vacua \(\Phi^{0}_{x,j}\) are fixed by the projection on the vacuum above \(N\) ([[proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum|proof of part 2 there]]). By the theorem that [[proofs/grh/upper-divisibility/all-lifts-become-direct|all lifts become direct]], the chain of glued double lifts with data from \(x\), applied to \(\varphi\), is \(c\) times the chain of direct lifts with data \(\mathrm{Dir}_j(\Phi^{0}_{x,j})\) applied to \(\psi\), with one \(c\), \(\lvert\iota c\rvert\le N^{mfb}\). Summing with the coefficients \(\Psi(x)\): the composite lift is the restriction to \(Y_m\) of \(c\cdot C^{\mathrm{dir}}_\Psi(\psi)\), the \(\Psi\)-combination of chains of direct lifts.
2. \(\Psi\) is a weak chain datum ([[proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum|part 2]]) and \(N\) is prime to the modulus of \(\vartheta\). The operators \(t_j=\mathrm{Dir}_j\) commute with the levels and \(\mathrm{Dir}_j(\Phi^{0}_{x,j})\) raises gauges by at most \(N^{fb}\) from \(\delta_j\) to \(\delta_{j+1}\) ([[proofs/grh/upper-divisibility/direct-lifts-lose-little|direct lifts lose little]]). By the [[proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts|gauge bound for chains]], \(C^{\mathrm{dir}}_\Psi(\psi)\) has gauge at most \(N^{mfb}\) at base point \(\delta_m\).
3. The base point \(\delta_m\) is, read at \(\overline{w_\tau}\), \(\operatorname{diag}(1,\dots,1,N)\) if \(\overline{w_\tau}\mid\pi_N\) and \(1\) otherwise; this is exactly the hypothesis under which [[proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m|restriction to \(Y_m\)]] turns a gauge bound at \(\delta_m\) into the same bound at \(1\) (the change of lattice cancels the normalising power of \(\bar\pi_N\) in the restriction). With the factor \(c\): \(N^{mfb}\cdot N^{mfb}=N^{2mfb}\). \(\blacksquare\)

*Status.* Complete relative to the cited knowls, which are themselves outlines.

## References

1. Lean: `New.Data.gaugeLe_compositeLift_at_N` in `src/New/UpperBound/Divisibility/ValuationAtLevel.lean`.
