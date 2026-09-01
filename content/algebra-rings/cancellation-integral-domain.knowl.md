+++
id = "algebra-rings/cancellation-integral-domain"
title = "Cancellation in integral domains"
kind = "knowl"
summary = "In an integral domain, nonzero elements satisfy left and right cancellation."
aliases = ["cancellation-integral-domain", "Cancellation in integral domains"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/integral-domain", "algebra-rings/regular-element", "algebra-rings/zero-divisor", "algebra-rings/fraction-field"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/cancellation-integral-domain.md"
+++

**Cancellation in integral domains**: Let \(D\) be an integral domain and let \(a,b,c\in D\) with \(a\neq 0\). If \(ab=ac\), then \(b=c\). Likewise, if \(ba=ca\), then \(b=c\).

In an [[algebra-rings/integral-domain|integral domain]], every nonzero element is a [[algebra-rings/regular-element|regular element]] (equivalently, there are no nonzero [[algebra-rings/zero-divisor|zero divisors]]), and this is exactly what makes cancellation possible. The same injectivity argument is the starting point for constructing the [[algebra-rings/fraction-field|field of fractions]].
