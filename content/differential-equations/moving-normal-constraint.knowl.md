+++
id = "differential-equations/moving-normal-constraint"
title = "Linear evolution under a moving normal constraint"
kind = "lemma"
summary = "The projection term needed to preserve orthogonality to a time-dependent normal."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/linear-ode", "linear-algebra/orthogonal-projection", "linear-algebra/matrix-transpose", "real-analysis/product-rule", "linear-algebra/outer-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(n(t)\in\mathbb R^d\setminus\{0\}\) be \(C^1\), and let \(A(t),g(t)\) be continuous. Write
\[
P_n=I-\frac{n\otimes n}{|n|^2}.
\]
The constrained equation \(a'=Aa+g+\mu n\), \(n\cdot a=0\), is equivalent, for initially transverse data, to
\[
a'=P_n(Aa+g)-\frac{n(n'\cdot a)}{|n|^2},
\qquad
\mu=-\frac{n'\cdot a+n\cdot(Aa+g)}{|n|^2}.
\]
The [[linear-algebra/orthogonal-projection|projection]] alone is insufficient when the normal moves.

## Verification

Differentiate \(n\cdot a=0\) to obtain \(n'\cdot a+n\cdot a'=0\), then solve for \(\mu\). Conversely, the displayed evolution makes the derivative of \(n\cdot a\) zero for every solution, so an initially zero constraint remains zero. The same formulas hold for complex \(a,g\) by complex linear extension with the real normal \(n\).
