+++
id = "proofs/grh/spanning-frames-b/shell-inverse-height"
title = "A few factors of the gain pay for the height of a shell"
kind = "proposition"
summary = "If the volume exponent is large, the integral over a shell of height h is at most 1/h times a bound independent of h."
aliases = ["shell bound with inverse height"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.Gauge.IsShell.setLIntegral_le_inv_height"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
proof_status = "full"
+++

**Proposition.** In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], suppose that \(\mathsf{M}\) is a Haar measure on \(G\). Let \(S\) be a [[proofs/grh/spanning-frames-b/shell|shell]] of height \(h\) for \((\Gamma,j,p,q,W)\), with \(j\le\varrho\), \(W\) a cut Bessel function and \(p,q\) heads of length \(j\) for \(\Gamma\). Let \(V\ge1\) bound the mass of floor \(j\), let \(e\in[0,1]\), let \(r\ge0\) be an integer with
\[
9\cdot10^7n^4+r\le s
\]
(\(s\) the volume exponent), and let \(f\colon G\to[0,\infty]\) satisfy
\[
f(x)\le\mathsf{N}_j(p,q;W;x)\ \ (x\in G),\qquad f(x)^2\le\bigl(Ve^{s}\bigr)^2\,\mathsf{P}^\Gamma_j(p,q;W;x)\ \ (x\in S).
\]
Then
\[
\kappa_j(p,q)\int_Sf\,d\mathsf{M}\;\le\;h^{-1}\cdot V\,e^{r}\,\Lambda^{3\cdot10^8n^4}\,\mathsf{c}_F(W).
\]

## Proof

*Reduction.* It suffices to find \(g\in[0,e]\) such that

\[
\text{(a)}\ \ g^{9\cdot10^7n^4}\,h^{1+10^5n^2}\le\Lambda^{29\cdot10^7n^4},\qquad\text{(b)}\ \ \kappa_j(p,q)\int_Sf\,d\mathsf{M}\le V g^{s}\Lambda^{2\cdot10^6n^3}h^{10^5n^2}\mathsf{c}_F(W).
\]
Indeed, since \(g\le e\le1\) and \(s\ge9\cdot10^7n^4+r\), we have \(g^{s}\le g^{9\cdot10^7n^4}g^{r}\le g^{9\cdot10^7n^4}e^{r}\). Writing \(1=h^{-1}h\) (the height is finite and nonzero) and inserting (b) and then (a),
\[
\kappa_j(p,q)\int_Sf\,d\mathsf{M}\le h^{-1}\,V e^{r}\,\bigl(g^{9\cdot10^7n^4}h^{1+10^5n^2}\bigr)\Lambda^{2\cdot10^6n^3}\mathsf{c}_F(W)\le h^{-1}Ve^r\Lambda^{29\cdot10^7n^4+2\cdot10^6n^3}\mathsf{c}_F(W),
\]
and \(29\cdot10^7n^4+2\cdot10^6n^3\le3\cdot10^8n^4\).

*Near shells: \(h\le\Lambda^{2400n^2}\).* Take \(g=e\). Then (a) holds because \(e\le1\) and \(h^{1+10^5n^2}\le\Lambda^{2400n^2(1+10^5n^2)}\le\Lambda^{29\cdot10^7n^4}\); and (b) is [[proofs/grh/spanning-frames-b/one-shell-bound|the bound on one shell]] for the gain \(Ve^s\).

*Remote shells: \(h>\Lambda^{2400n^2}\).* Let \(\tau=(h^{-1})^{1/(800n^2)}\), so \(\tau^{800n^2}=h^{-1}\), and take \(g=\min(e,\tau)\). For (a), using \(g\le\tau\), \(h\ge1\), \(1+10^5n^2\le112500n^2\) and \(800n^2\cdot112500n^2=9\cdot10^7n^4\),
\[
g^{9\cdot10^7n^4}h^{1+10^5n^2}\le\bigl(\tau^{800n^2}\bigr)^{112500n^2}h^{112500n^2}=\bigl(h^{-1}h\bigr)^{112500n^2}=1\le\Lambda^{29\cdot10^7n^4}.
\]
For (b): if \(e\le\tau\) then \(g=e\) and (b) is again the bound on one shell. If \(\tau\le e\) then \(g=\tau\); since \(f\le\mathsf{N}_j(p,q;W;\cdot)\) everywhere, (b) follows from [[proofs/grh/spanning-frames-b/remote-shell-gain|the gain on a remote shell]].

## References

1. Lean: `New.Floors.Gauge.IsShell.setLIntegral_le_inv_height` in `src/New/Spanning/Frames/Shells.lean`.
