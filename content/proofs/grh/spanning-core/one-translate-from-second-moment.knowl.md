+++
id = "proofs/grh/spanning-core/one-translate-from-second-moment"
title = "One translate: a small second moment makes the translates spread"
kind = "theorem"
summary = "If pr0 B is a near isometry and the second moment of the operators B* s B is nearly minimal, then the translates pr0 s B form a spread family."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.isSpread_of_second_moment"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Theorem (one translate).** Let \(S\) and \(T\) be finite-dimensional complex [[linear-algebra/inner-product-space|inner product spaces]], \(\Gamma\) a [[algebra-groups/finite-group|finite group]] and \(\rho\) a [[algebra-representation-theory/group-representation|representation]] of \(\Gamma\) on \(T\) preserving the inner product. Let \(\mathrm{pr}_0\colon T\to T\) be an [[linear-algebra/orthogonal-projection|orthogonal projection]] (self-adjoint idempotent) that commutes with every \(\rho(s)\), with image \(T_0\). Let \(B\colon S\to T\) be linear and \(\varepsilon\ge0\). Assume

1. \(\mathrm{pr}_0B\) is a [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometry]] with error \(\varepsilon\);
2. \(\displaystyle\dim T_0\cdot\sum_{s\in\Gamma}\lVert B^*\rho(s)B\rVert_{\mathrm{HS}}^2\ \le\ \lvert\Gamma\rvert\,(1+\varepsilon)\,(\dim S)^2\) ([[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norm]]).

Then the family of maps \(\mathrm{pr}_0\,\rho(s)\,B\colon S\to T_0\), \(s\in\Gamma\), is [[proofs/grh/spanning-core/spread-family-of-linear-maps|spread]] with error \(\tfrac32\varepsilon\): for every subspace \(W\subseteq T_0\), with \(\alpha=\dim W/\dim T_0\) (and \(\alpha=0\) if \(T_0=0\)), some \(s\in\Gamma\) has
\[
\dim\,(\mathrm{pr}_0\rho(s)B)^{-1}(W)\le\frac{1+\alpha+3\varepsilon}{2}\,\dim S .
\]

## Proof

Let \(W\subseteq T_0\) and \(\alpha\) be as stated; then \(\alpha\ge0\) and \(\dim W=\alpha\dim T_0\) (also if \(T_0=0\)). Write \(M=\sum_s\lVert B^*\rho(s)B\rVert_{\mathrm{HS}}^2\).

*Step 1: the mean.* By [[proofs/grh/spanning-core/cauchy-schwarz-for-translates|Cauchy–Schwarz for translates]] and hypothesis 2,
\[
\Bigl(\sum_s\lVert\mathrm{pr}_W\rho(s)B\rVert_{\mathrm{HS}}^2\Bigr)^2\le\dim W\cdot\lvert\Gamma\rvert M=\alpha\lvert\Gamma\rvert\,(\dim T_0\cdot M)\le\alpha(1+\varepsilon)\bigl(\lvert\Gamma\rvert\dim S\bigr)^2\le\Bigl(\frac{\alpha+1+\varepsilon}2\Bigr)^2\bigl(\lvert\Gamma\rvert\dim S\bigr)^2 ,
\]
the last step being \(4\alpha(1+\varepsilon)\le(\alpha+1+\varepsilon)^2\). Taking square roots, the mean over \(s\) of \(\lVert\mathrm{pr}_W\rho(s)B\rVert_{\mathrm{HS}}^2\) is at most \(\tfrac{\alpha+1+\varepsilon}2\dim S\), so some \(s\) satisfies
\[
\lVert\mathrm{pr}_W\rho(s)B\rVert_{\mathrm{HS}}^2\le\frac{\alpha+1+\varepsilon}2\dim S .
\]

*Step 2: on the preimage the two maps agree.* Fix this \(s\), and let \(W'=(\mathrm{pr}_0\rho(s)B)^{-1}(W)\subseteq S\). For \(x\in W'\) put \(y=\rho(s)Bx\). Then \(\mathrm{pr}_0y\in W\), and \(y-\mathrm{pr}_0y\) is orthogonal to \(T_0\supseteq W\); hence \(\mathrm{pr}_Wy=\mathrm{pr}_0y\). As \(\mathrm{pr}_0\) commutes with \(\rho(s)\),
\[
\rho(s)\,\mathrm{pr}_0Bx=\mathrm{pr}_W\,\rho(s)Bx\qquad(x\in W').
\]

*Step 3.* Since \(\rho(s)\) is norm preserving, for every \(x\in S\) Step 2 applied to \(\mathrm{pr}_{W'}x\in W'\) gives \(\lVert\mathrm{pr}_0B\,\mathrm{pr}_{W'}x\rVert=\lVert\mathrm{pr}_W\rho(s)B\,\mathrm{pr}_{W'}x\rVert\). By Properties 3 and 5 of the Hilbert–Schmidt norm,
\[
\lVert\mathrm{pr}_0B\,\mathrm{pr}_{W'}\rVert_{\mathrm{HS}}\le\lVert\mathrm{pr}_W\rho(s)B\,\mathrm{pr}_{W'}\rVert_{\mathrm{HS}}\le\lVert\mathrm{pr}_W\rho(s)B\rVert_{\mathrm{HS}} .
\]
Hypothesis 1 for the subspace \(W'\) and Step 1 give
\[
\dim W'-\varepsilon\dim S\le\lVert\mathrm{pr}_0B\,\mathrm{pr}_{W'}\rVert_{\mathrm{HS}}^2\le\frac{\alpha+1+\varepsilon}{2}\dim S ,
\]
that is \(\dim W'\le\bigl(\tfrac{1+\alpha}2+\tfrac32\varepsilon\bigr)\dim S\). \(\blacksquare\)

## Remarks

By Cauchy–Schwarz (Step 1 with \(W=T_0\)) a map \(B\) with \(\lVert\mathrm{pr}_0B\rVert^2_{\mathrm{HS}}\approx\dim S\) always has \(\dim T_0\cdot M\gtrsim\lvert\Gamma\rvert(\dim S)^2\); hypothesis 2 says that the second moment is nearly as small as possible.

## References

1. Lean: `New.isSpread_of_second_moment` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
2. L. R. Welch, Lower bounds on the maximum cross correlation of signals, 1974 (cited in the Lean file head for rank bounds from second moments).
