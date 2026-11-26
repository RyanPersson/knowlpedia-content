+++
id = "proofs/grh/reduction-main/data"
title = "The data: scales, ranks, places, weights and primes"
kind = "definition"
summary = "The objects that grow with the length x of the prime sum: integer scales x, x1, b, the number m of lifts, the rank r, the tower exponent s, a sparse set of b-places with weights, primes p0, p1, N and integers of norm p0 p1 and N."
aliases = ["Data", "admissible data", "data of the proof", "constant bound", "lower end of the level range"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data", "New.Parameters.constantBound", "New.Parameters.logLevelMin"]
lean_files = ["src/New/Reduction/Data/AdmissibleData.lean"]
+++

Let \(P=(q_0,d)\) be [[proofs/grh/reduction-main/parameters|parameters]], with \(K=\mathbb Q(\sqrt{-d})\). **Data** \(D\) for \(P\) consist of the following objects, subject to the listed conditions. (All conditions are part of the definition; "\(\log\)" is the natural logarithm.)

**Scales.** Natural numbers \(x,x_1,b\ge1\) (the length of the prime sum, the second cut-off, the weight at the \(b\)-places), such that, with \(c_P\) the constant bound defined below,

- (S1) \(\log\log b\ \ge\ 10^{12}\,c_P\);
- (S2) \(100\log\log b\le\log x\), i.e. \((\log b)^{100}\le x\);
- (S3) \(10^6\log x\le\log x_1\), i.e. \(x^{10^6}\le x_1\);
- (S4) \(10^6\log x_1\le\log b\), i.e. \(x_1^{10^6}\le b\);
- (S5) \(6\log\log x_1\le\log\log b\), i.e. \((\log x_1)^6\le\log b\).

**Ranks and tower exponent.** Natural numbers \(m\) (the number of lifts), \(r\) (the rank of the target) and \(s\) (the tower exponent) with

- (R1) \(\sqrt x\le m\le2\sqrt x\), and \(m=2^{e+1}\) for some integer \(e\ge0\), with \(s=22(e+1)\) (so \(2^s=m^{22}\));
- (R2) \(x^5\le r\le3x^5\), and \(r=3^{e'+1}\) for some integer \(e'\ge0\);
- (R3) \(s\le32\log x\);
- (R4) \(q_1x_1\mid b\), where \(q_1=q_1(s)\).

These fix the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E=E_s=K(\zeta)\), \(\zeta\) of order \(q_1\), and its group \(\Phi\) of infinite places]].

**Places and weights.** A finite set \(\Phi_b\subseteq\Phi\) (the *\(b\)-places*) and a function \(\kappa:\Phi\to\mathbb N\) (the *weight*) with

- (P1) every \(\sigma\in\Phi_b\) is \(\equiv-1\) modulo \(q_0\);
- (P2) \(\operatorname{towerDeg}(s)\le\#\Phi_b\cdot\log b\);
- (P3) \(\Phi_b\) is [[proofs/grh/reduction-main/sparse-set-of-places|sparse for the primes up to]] \(k\,t\), where \(k=r+1-m\) and \(t=5r\);
- (P4) \(\kappa(\tau)=b\) for \(\tau\in\Phi_b\), and \(\kappa(\tau)=\lfloor xb/x_1\rfloor\) for \(\tau\notin\Phi_b\). (By (R4) the quotient \(xb/x_1\) is an integer; with \(a=xb\) the weights are \(a/x\) and \(a/x_1\).)

**Primes and level.** Primes \(p_0\ne p_1\) and \(N\), an [[algebra-fields-galois/algebraic-integer|integer]] \(\bar\pi_M\in\mathcal O_K\) and an integer \(\pi_N\in\mathcal O_E\) with

- (L1) \(p_0\equiv p_1\equiv N\equiv1\pmod{q_2(s)^2}\);
- (L2) \(b^{10}\le p_i\le b^{11}\) for \(i=0,1\);
- (L3) \(\bar\pi_M\cdot\overline{\bar\pi_M}=p_0p_1\) (complex conjugation of \(K\));
- (L4) \(\log N_-\le\log N\le\log N_-+\sqrt{\log b}\), where \(M=p_0p_1\) and
\[
\log N_-:=m\cdot\frac{1}{\#\Phi}\sum_{\tau\in\Phi}\log\kappa(\tau)+(m-1)\log\frac{M\,\mathrm{rd}_E}{2\pi}-\frac{15}{2}\log b ,
\]
i.e. \(N_-=\bar\kappa^{\,m}(M\,\mathrm{rd}_E/2\pi)^{m-1}b^{-15/2}\) with \(\bar\kappa\) the geometric mean of the weights and \(\mathrm{rd}_E\) the root discriminant of \(E\);
- (L5) \(\pi_N\cdot\overline{\pi_N}=N\) (complex conjugation of the CM field \(E\)).

**The constant bound.** \(c_P\) bounds the constants depending only on \(P\):
\[
c_P:=c_{\mathrm{vac}}(P)+(2d+6)+q_0+\Bigl\lvert\gamma-\operatorname{Re}\tfrac{L'}{L}(1,\chi_K)\Bigr\rvert+\sum_{w}\bigl\lvert\log\lvert\Phi_{q_0}'(w)\rvert\bigr\rvert ,
\]
where \(c_{\mathrm{vac}}(P)\) is the natural number [[?lean:New.Parameters.vacuumBoundConst|bounding the conjugates of the integral vacuum]], \(\gamma\) is Euler's constant, and \(w\) runs over the primitive \(q_0\)-th roots of unity in \(\mathbb C\), \(\Phi_{q_0}\) being the cyclotomic polynomial. One has \(c_P\ge64\), \(c_P\ge q_0\), \(c_P\ge d\), \(c_P\ge\varphi(q_0)\).

## Remarks

- In the Lean source the scales are stored as natural numbers together with real numbers `logX`, `logX₁`, `logB` whose exponentials equal them; (S1)–(S5) are stated for these logarithms. The element \(\bar\pi_M\) is the field `piMBar`; its conjugate is written \(\pi_M\).
- The scales and ranks are only required to lie in ranges. Data with explicit values exist for every large integer \(x\): [[proofs/grh/reduction-main/data-exist|existence of the data]].
- Quantities read off from the data (\(k,t,n_j,\Delta,a,M,f,\Phi_a,\kappa_j,\dots\)) are in [[proofs/grh/reduction-main/data-derived-quantities|derived quantities of the data]]; their sizes in [[proofs/grh/reduction-main/data-sizes|sizes of the data]].
- Property (P1) uses the class of a place modulo \(q_0\mid q_1\).

## References

1. Lean: `New.Data`, `New.Parameters.constantBound`, `New.Parameters.logLevelMin` in `src/New/Reduction/Data/AdmissibleData.lean`; the bounds for \(c_P\) are `New.Data.le_constantBound` and (S1)–(S5) are collected in `New.Data.scale_inequalities`, in `src/New/Reduction/Data/Magnitudes.lean`.
