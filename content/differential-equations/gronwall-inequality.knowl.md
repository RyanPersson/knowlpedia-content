+++
id = "differential-equations/gronwall-inequality"
title = "Gronwall inequality"
kind = "theorem"
summary = "An integral inequality bounds accumulated amplification by an exponential."
aliases = ["Grönwall inequality", "Gronwall lemma"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integral", "analysis/absolute-continuity", "real-analysis/exponential-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(u\ge0\) be continuous on \([a,b]\), let \(k\ge0\) be [[measure-theory/lebesgue-integrable-function|integrable]] there, and let \(A\ge0\). If
\[
u(t)\le A+\int_a^t k(s)u(s)\,ds,
\]
then **Gronwall's inequality** gives
\[
u(t)\le A\exp\left(\int_a^t k(s)\,ds\right).
\]

## Proof

For \(A>0\), let \(v(t)=A+\int_a^tku\). Then \(v'\le kv\) almost everywhere. The derivative of \(v(t)e^{-\int_a^tk}\) is nonpositive, so \(v(t)\le Ae^{\int_a^tk}\). If \(A=0\), apply the same argument with any positive \(A\) and let it decrease to zero.

## Source term

If an absolutely continuous \(u\) satisfies \(u'\le ku+g\) almost everywhere, with integrable \(k,g\), an integrating factor gives
\[
u(t)\le u(a)e^{\int_a^t k}+\int_a^t e^{\int_s^t k}g(s)\,ds.
\]
This version does not require \(k\ge0\). The coefficient must be integrable on the interval where the estimate is used.
