+++
id = "analysis/separated-support-products"
title = "Vanishing products from separated auxiliary supports"
kind = "theorem"
summary = "Closed support separation makes all differentiated cross products vanish, including after evaluation along a smooth auxiliary map."
aliases = ["disjoint support derivative products"]
domains = ["analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/support-of-a-function", "real-analysis/class-ck-map", "real-analysis/auxiliary-variable-evaluation", "real-analysis/multi-index-notation", "analysis/locally-finite-smooth-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F_\gamma(x,Y)\) be globally [[real-analysis/class-ck-map|smooth functions]] with
\[
\operatorname{supp}F_\gamma\subset K_\gamma\times R_\gamma.
\]
Assume that, for distinct labels, \(K_\gamma\cap K_{\gamma'}\ne\varnothing\) implies \(R_\gamma\cap R_{\gamma'}=\varnothing\). Then every pair of mixed derivatives satisfies
\[
(\partial^\alpha F_\gamma)(\partial^\beta F_{\gamma'})=0
\qquad(\gamma\ne\gamma').
\]

## Why derivatives and evaluation preserve the conclusion

A derivative of a smooth function has [[shared-foundations/support-of-a-function|support]] contained in the support of the function. The assumed product supports are disjoint, proving the identity. After [[real-analysis/auxiliary-variable-evaluation|evaluation]] at \(Y=\Psi(x)\), the chain rule expresses each derivative using these same mixed derivatives, so cross products still vanish.

For a finite or locally finite sum this removes all cross-label terms from a quadratic differential expression. It says nothing about different harmonics with the same label. Smooth extension across the support boundaries is essential: differentiating a discontinuous cutoff can create boundary distributions, outside the hypotheses here.
