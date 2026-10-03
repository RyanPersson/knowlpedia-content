+++
id = "ergodic-theory/doubling-map"
title = "Doubling map of the circle"
kind = "example"
summary = "A noninvertible measure-preserving mixing map with an isometric, nonsurjective Koopman operator."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["topology/flat-torus", "ergodic-theory/koopman-operator", "harmonic-analysis/characters-compact-abelian-fourier-basis", "ergodic-theory/strong-mixing"]
+++

The **doubling map** is \(D:\mathbb R/\mathbb Z\to\mathbb R/\mathbb Z\), \(D(x)=2x\bmod1\), with [[measure-theory/lebesgue-measure|Lebesgue probability]]. It preserves measure, is strongly mixing, and is not invertible modulo null sets.

## Measure preservation

The two inverse branches \(x\mapsto x/2\) and \(x\mapsto(x+1)/2\) each halve lengths. Changing variables on the two half-intervals gives \(\int f\circ D=\int f\) for integrable \(f\).

## Koopman proof of mixing

The Fourier basis satisfies \(U_De_k=e_{2k}\), so \(\langle U_D^ne_k,e_\ell\rangle=0\) eventually for fixed \(k\ne0,\ell\). Trigonometric approximation and the isometry bound extend this to mean-zero \(L^2\) observables. This proves mixing.

The range of \(U_D\) is the closed span of even frequencies, and omits \(e_1\). An invertible measure-space transformation would give a surjective [[ergodic-theory/koopman-operator|Koopman operator]], so \(D\) is not invertible even modulo null sets.
