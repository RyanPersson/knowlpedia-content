+++
id = "harmonic-analysis/diophantine-directional-inverse"
title = "Directional inverse with a Diophantine bound"
kind = "theorem"
summary = "A zero-mean smooth periodic function has a unique zero-mean directional primitive with finite derivative loss under a polynomial divisor bound."
aliases = ["Diophantine cohomological equation", "zero-mean directional primitive"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/diophantine-direction", "harmonic-analysis/small-divisor", "harmonic-analysis/fourier-coefficient", "harmonic-analysis/smooth-fourier-coefficient-decay", "harmonic-analysis/smooth-fourier-reconstruction", "measure-theory/zero-mean-function", "functional-analysis/derivative-loss", "real-analysis/compact-derivative-seminorm", "real-analysis/multi-index-notation", "real-analysis/directional-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(v\) be a [[harmonic-analysis/diophantine-direction|Diophantine direction]] with constants \(c,\tau\). Every smooth zero-mean \(f\) on \(\mathbb T^n\) has a unique smooth zero-mean solution of \(v\cdot\nabla u=f\), given by
\[
\widehat u(0)=0,\qquad
\widehat u(m)=\frac{\widehat f(m)}{2\pi i\,v\cdot m}\quad(m\ne0).
\]

## Finite loss estimate

Fix an even integer \(s>\tau+n\). For every integer \(k\ge0\),
\[
\|u\|_{C^k}\le C_{k,s,n,c,\tau,v}\|f\|_{C^{k+s}}.
\]
Indeed, smooth Fourier coefficient decay bounds the coefficient of \(\partial^\beta f\) by \(C\|f\|_{C^{k+s}}(1+|m|)^{-s}\) for \(|\beta|\le k\). Dividing by the directional eigenvalue costs at most \(c^{-1}(1+|m|)^\tau\); the resulting series is absolutely summable because \(s-\tau>n\). This proves the estimate and smooth reconstruction at every fixed order. Any two solutions differ only in the zero mode, so the zero-mean normalization gives uniqueness.

This inverse is a Fourier multiplier. It preserves a prescribed pullback frequency lattice and therefore the corresponding torus descent condition. It need not preserve compact support within the auxiliary torus.
