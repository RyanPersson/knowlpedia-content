+++
id = "harmonic-analysis/approximate-identity-l1-group-algebra"
title = "Approximate identity in L1(G)"
kind = "definition"
summary = "A bounded net in the group convolution algebra that converges to the identity in its left and right actions."
aliases = ["convolution approximate identity", "approximate unit in L1(G)", "Approximate identity in a group algebra"]
domains = ["harmonic-analysis", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/l1-group-algebra", "topology/neighborhood"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. An
**approximate identity in \(L^1(G)\)** is a net \((u_i)\) in the
[[harmonic-analysis/l1-group-algebra|group convolution algebra \(L^1(G)\)]]
such that
\[
\|u_i*f-f\|_1\longrightarrow 0
\quad\text{and}\quad
\|f*u_i-f\|_1\longrightarrow 0
\]
for every \(f\in L^1(G)\). It is **bounded** when
\(\sup_i\|u_i\|_1<\infty\). Every locally compact group admits a bounded
two-sided approximate identity with \(u_i\geq 0\), \(\|u_i\|_1=1\), and
supports shrinking through the [[topology/neighborhood|neighborhoods]] of the
identity element.

## Construction from small neighborhoods

Fix a left [[harmonic-analysis/haar-measure|Haar measure]] on \(G\). For each
identity neighborhood \(U\), one can choose
\(u_U\in C_c(G)\) satisfying
\[
u_U\geq 0,\qquad \int_Gu_U(x)\,dx=1,\qquad
\operatorname{supp}(u_U)\subseteq U.
\]
Order the neighborhoods by reverse inclusion. Continuity of translations in
\(L^1(G)\), followed by averaging against \(u_U\), gives the two convergence
statements in the definition. The functions need not have a common formula:
their normalization and concentration near the identity are the essential
features.

## Why it replaces an identity

Unless \(G\) is discrete, the point mass at the identity is not an element of
\(L^1(G)\), so convolution has no literal identity in the algebra. The net
\((u_i)\) nevertheless recovers each \(L^1\)-function in norm. It also detects
nondegeneracy: for a bounded representation \(T\) of \(L^1(G)\), the closed
linear span of \(T(L^1(G))H\) is the subspace on which \(T(u_i)\) converges
strongly to the identity.

## Distinctions and conventions

An approximate identity is not a sequence in general; the directed set of
neighborhoods may be uncountable. Nor is it a Dirac measure: each \(u_i\)
belongs to \(L^1(G)\), while the limiting point mass ordinarily belongs only
to the measure algebra. Some authors require boundedness in the term
“approximate identity”; the explicit norm-one construction removes that
convention-dependent ambiguity here.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781498727136). Relevant: Chapter 2 on Haar integration and approximate identities in \(L^1(G)\).
2. Hans Reiter and Jan D. Stegeman, *Classical Harmonic Analysis and Locally Compact Groups*, 2nd ed., Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/acprof:oso/9780198511892.001.0001). Relevant: the foundational theory of group convolution algebras.
