+++
id = "real-analysis/intermediate-value-theorem"
title = "Intermediate value theorem"
kind = "knowl"
summary = "A continuous function on an interval takes all values between its endpoint values."
aliases = ["intermediate-value-theorem", "Intermediate value theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/intermediate-value-theorem.md"
prerequisites = ["real-analysis/continuity-on-a-set", "real-analysis/interval", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

**Intermediate value theorem:** Let \(f:[a,b]\to\mathbb{R}\) be [[real-analysis/continuity-on-a-set|continuous]] on \([a,b]\). If \(y\) is any number between \(f(a)\) and \(f(b)\) (that is, \(\min\{f(a),f(b)\}\le y\le \max\{f(a),f(b)\}\)), then there exists \(c\in[a,b]\) such that
\[
f(c)=y.
\]

## Remarks

This is one of the basic consequences of being a [[topology/continuous-map|continuous map]] on an [[real-analysis/interval|interval]]. A notable application is [[real-analysis/darboux-theorem|Darboux's theorem]], which shows that derivatives also satisfy an intermediate value property.

## Proof from completeness

It suffices to treat \(f(a)<y<f(b)\); endpoint equalities are immediate, and replacing \(f\) by \(-f\) handles the reversed case. Let \(c\) be the supremum of \(S=\{x\in[a,b]:f(x)\le y\}\). The set is nonempty and bounded. If \(f(c)<y\), continuity provides points of \(S\) strictly to the right of \(c\), a contradiction. If \(f(c)>y\), continuity excludes \(S\) from a left neighborhood of \(c\), also contradicting the definition of supremum. Hence \(f(c)=y\).
