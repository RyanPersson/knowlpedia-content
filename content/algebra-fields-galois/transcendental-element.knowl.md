+++
id = "algebra-fields-galois/transcendental-element"
title = "Transcendental element"
kind = "knowl"
summary = "An element is transcendental over a field if it satisfies no nonzero polynomial with coefficients in that field."
aliases = ["transcendental-element", "Transcendental element"]
domains = ["algebra-fields-galois"]
prerequisites = ["algebra-fields-galois/field-extension", "algebra-fields-galois/algebraic-element"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-fields-galois/transcendental-element.md"
+++

Let \(E/F\) be a [[algebra-fields-galois/field-extension|field extension]] and let \(\alpha\in E\). The element \(\alpha\) is **transcendental over \(F\)** if there is no nonzero polynomial \(f(x)\in F[x]\) such that \(f(\alpha)=0\). Equivalently, \(\alpha\) is transcendental over \(F\) iff \(\alpha\) is not [[algebra-fields-galois/algebraic-element|algebraic over F]].

## Equivalent characterizations

A useful equivalent condition is: \(\alpha\) is transcendental over \(F\) iff the evaluation map
\[
\operatorname{ev}_\alpha:F[x]\to E,\quad f\mapsto f(\alpha),
\]
is injective. When \(\alpha\) is transcendental, the simple extension \(F(\alpha)/F\) is a [[algebra-fields-galois/transcendental-extension|transcendental extension]] and has infinite [[algebra-fields-galois/degree-of-extension|degree]].

## Remarks

Transcendence depends on the base field: an element may be transcendental over \(F\) but algebraic over a larger intermediate field \(K\) with \(F\subseteq K\subseteq E\) (see [[algebra-fields-galois/intermediate-field|intermediate field]]).

## Examples
1. If \(t\) is an indeterminate, then \(t\) is transcendental over \(\mathbb{Q}\) inside \(\mathbb{Q}(t)\): no nonzero polynomial in \(\mathbb{Q}[x]\) vanishes at \(t\).
2. The classical constants \(\pi\) and \(e\) are transcendental over \(\mathbb{Q}\) (deep theorems, e.g. Lindemann–Weierstrass).
3. Let \(t\) be an indeterminate. Then \(t\) is transcendental over \(\mathbb{Q}\), but \(t\) is algebraic over the intermediate field \(\mathbb{Q}(t^2)\subseteq \mathbb{Q}(t)\), because \(t\) satisfies the polynomial \(x^2-t^2=0\) with coefficients in \(\mathbb{Q}(t^2)[x]\).
