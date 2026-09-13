+++
id = "real-analysis/completing-the-square"
title = "Completing the square"
kind = "calculation"
summary = "Writing a quadratic polynomial as a shifted square plus a constant."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For real \(a\ne0,b,c\), **completing the square** is the identity
\[
ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2+c-\frac{b^2}{4a}.
\]
Expansion proves the formula. If \(a>0\), it shows that the minimum is \(c-b^2/(4a)\), attained at \(x=-b/(2a)\); if \(a<0\), the same value is the maximum.

## Gaussian factors

For \(a>0\),
\(e^{-ax^2+bx}=e^{b^2/(4a)}e^{-a(x-b/(2a))^2}\).
This separates an overall amplitude from a translated decaying profile. The sign of the quadratic coefficient is essential for decay.
