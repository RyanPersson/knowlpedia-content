+++
id = "proofs/grh/upper-elementary-divisors/defect-of-monomial"
title = "Defect of a monomial at a letter along a root"
kind = "definition"
summary = "A real weighted degree of a monomial, with weights supported on the two variables of a root in each letter and proportional to powers of P."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.rootVar", "New.FrobeniusCycle.defectWeight", "New.FrobeniusCycle.one_add_val_sub_one_sub"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge 1\), let \(a,a'\in\{0,\dots,k-1\}\) (a **root** \((a,a')\)) and let \(i\in\mathbb{Z}/N\) be a letter. For each letter \(s\) put
\[
Y_s=\begin{cases}x_{a',s}& s\text{ even}\\ x_{a,s}& s\text{ odd}\end{cases},\qquad
X_s=\begin{cases}x_{a,s}& s\text{ even}\\ x_{a',s}& s\text{ odd}\end{cases},
\]
and let \(P_s=P^{[s-i]}\), where \([s-i]\in\{0,\dots,N-1\}\) is the representative of \(s-i\). The **defect weight** \(\omega_{i,a,a'}\) is the real-valued function on variables
\[
\omega_{i,a,a'}(Y_s)=\frac{P_s}{q-1}\ (s\ne i),\qquad \omega_{i,a,a'}(Y_i)=\frac{q}{q-1}=\frac{1}{q-1}+1,\qquad \omega_{i,a,a'}(X_s)=-\frac{P_s}{q-1},
\]
and \(\omega_{i,a,a'}=0\) on all other variables (if \(a=a'\), so that \(X_s=Y_s\), the two contributions are added). The **defect at the letter \(i\) along the root \((a,a')\)** of a monomial \(x^{\alpha}\) is its weighted degree
\[
\operatorname{def}_{i,a,a'}(\alpha)=\sum_{b,s}\alpha(b,s)\,\omega_{i,a,a'}(x_{b,s})\in\mathbb{R}.
\]

## Remarks

Writing \(\nu=q\,\alpha(Y_i)+\sum_{s\ne i}P_s\,\alpha(Y_s)\) and \(\nu'=\sum_s P_s\,\alpha(X_s)\), one has \(\operatorname{def}_{i,a,a'}(\alpha)=(\nu-\nu')/(q-1)\). In the [[proofs/grh/upper-elementary-divisors/root-lemma|root lemma]], \(\nu\) is a lower bound for an order of vanishing at each of \(q\) points and \(q\nu'\) is a degree.

## References

1. Lean: `New.FrobeniusCycle.rootVar`, `New.FrobeniusCycle.defectWeight`, `New.FrobeniusCycle.one_add_val_sub_one_sub` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.
