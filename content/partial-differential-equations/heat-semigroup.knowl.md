+++
id = "partial-differential-equations/heat-semigroup"
title = "Heat semigroup"
kind = "definition"
summary = "The family of Gaussian convolution operators with addition of times as its composition law."
aliases = ["Gaussian convolution semigroup"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/euclidean-heat-kernel", "harmonic-analysis/convolution-on-locally-compact-group", "measure-theory/lp-space", "algebra-groups/semigroup", "harmonic-analysis/young-convolution-inequality"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On \(L^p(\mathbb R^n)\), \(1\le p\le\infty\), the **heat semigroup** is
\[
T_0f=f,\qquad T_tf=G_\nu(t,\cdot)*f\quad(t>0).
\]
The star denotes [[harmonic-analysis/convolution-on-locally-compact-group|Euclidean convolution]]. Completing the square in the Gaussian integral gives \(G_\nu(t)*G_\nu(s)=G_\nu(t+s)\), hence \(T_tT_s=T_{t+s}\).

## Contraction and continuity

Mass one and Young's inequality give \(\|T_tf\|_p\le\|f\|_p\). For \(1\le p<\infty\), \(T_tf\to f\) in \(L^p\) as \(t\downarrow0\), by continuity of translations and concentration of the Gaussian near zero. On bounded uniformly continuous functions the convergence is uniform. It need not be uniform for a general \(L^\infty\) function; a jump discontinuity supplies a counterexample.
