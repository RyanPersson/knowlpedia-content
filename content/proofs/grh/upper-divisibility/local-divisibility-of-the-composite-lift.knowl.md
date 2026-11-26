+++
id = "proofs/grh/upper-divisibility/local-divisibility-of-the-composite-lift"
title = "Divisibility of the composite lift"
kind = "theorem"
summary = "There are errors err(p), zero at split and large primes other than N and with total weighted by log p at most the error unit, such that at every prime the composite lift has valuation at least gain(p) - err(p) on a submodule of the integral ramified source forms of colength at most err(p) times the dimension."
aliases = ["local divisibility theorem", "divisibility of the composite lift"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_err_gaugeLe_compositeLift"]
lean_files = ["src/New/UpperBound/Divisibility/LocalDivisibility.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] for the parameters \((q_0,d)\). There is a function \(\operatorname{err}\colon\mathbb{N}\to\mathbb{R}\) such that:

(a) \(\operatorname{err}(p)\ge0\) for all \(p\);

(b) if \(p\ne N\), and \(\chi_K(p)=1\) or \(p\ge x_1\), then \(\operatorname{err}(p)=0\);

(c) for every finite set \(U\) of natural numbers, \(\sum_{p\in U}\operatorname{err}(p)\log p\le fa(\log b)^{3}\), the [[?lean:New.Data.errorUnit|error unit]];

(d) for every prime \(p\) and every embedding \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), with \(O_\iota=\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\) and \(\mathcal M^{\mathrm{ram}}\) the \(O_\iota\)-module of [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source forms]] that are [[proofs/grh/upper-divisibility/marked-set-of-primes|integral]] at \(\iota\), there are a natural number \(l\le\operatorname{err}(p)\dim_{\mathbb{C}}\mathcal S\) and an \(O_\iota\)-submodule \(S\subset\mathcal M^{\mathrm{ram}}\) such that

- every finite family \(\varphi_1,\dots,\varphi_n\in\mathcal M^{\mathrm{ram}}\) is carried into \(S\) by an \(n\times n\) matrix over \(O_\iota\) whose determinant divides \(p^{l}\) (the [[?lean:New.ColengthDvd|colength]] of \(S\) in \(\mathcal M^{\mathrm{ram}}\) divides \(p^{l}\)); and
- for every [[?lean:New.Data.Twist|twist]] \(\vartheta\) whose modulus has norm prime to \(p\), every [[?lean:New.Data.IsChainDatum|chain datum]] \(\Psi\) for \(\vartheta\) and every \(\varphi\in S\), the [[?lean:New.Data.compositeLift|composite lift]] \(C_{\vartheta,\Psi}(\varphi)\) on \(Y_m\) satisfies: for all \(g\), the coordinates of \(g^{-1}\cdot\iota\bigl(C_{\vartheta,\Psi}(\varphi)(g)\bigr)\) have \(p\)-adic absolute value at most \(p^{\operatorname{err}(p)-\operatorname{gain}(p)}\), where \(\operatorname{gain}\) is the [[proofs/grh/upper-divisibility/gain|gain]].

## Proof

Take \(\operatorname{err}=\operatorname{al}\), the [[proofs/grh/upper-divisibility/allowed-loss|allowed loss]]. (a) and (c) are the proposition on the allowed loss. (b): such a \(p\) is not a small non-split prime and is not \(N\), so \(\operatorname{al}(p)=0\). (d): let \(l\) and \(S_0\) be given by the theorem on [[proofs/grh/upper-divisibility/divisibility-at-one-prime|divisibility at one prime]] and put \(S=\mathcal M^{\mathrm{ram}}\cap S_0\). A matrix that carries a family of \(\mathcal M^{\mathrm{ram}}\subset\mathcal M\) into \(S_0\) carries it into \(S\), because \(\mathcal M^{\mathrm{ram}}\) is a module; so the colength of \(S\) in \(\mathcal M^{\mathrm{ram}}\) divides \(p^{l}\). The members of \(S\) are ramified and lie in \(S_0\), so the gauge bound holds. \(\blacksquare\)

*Status.* Complete relative to the cited knowls. The chain of dependencies ends in several results of other areas that are quoted, notably the divisibility of jets of theta series (chapter on derivatives of theta functions), the theorem on elementary divisors of an edge Hecke operator, the transfer of Hecke operators through a theta lift, and the trade of gluing for powers of \(U\) at \(N\).

## Remarks

This is the divisibility side of the upper bound: with the [[proofs/grh/upper-divisibility/size-of-the-composite-lift|size of the composite lift]], whose exponent contains \(+2\sum_p\operatorname{gain}(p)\log p\), the product formula for heights makes the gains cancel, leaving \(h_{\mathrm{main}}-m\,\mathrm{rem}\) and errors of the order of the error unit. The head of the source file names as related work on integrality of theta lifts: X. Zhang (2022), T. Berger (2009), K. Prasanna (2006).

## References

1. Lean: `New.Data.exists_err_gaugeLe_compositeLift` in `src/New/UpperBound/Divisibility/LocalDivisibility.lean`.
