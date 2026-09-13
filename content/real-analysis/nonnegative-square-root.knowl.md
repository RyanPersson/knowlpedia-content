+++
id = "real-analysis/nonnegative-square-root"
title = "Nonnegative square root"
kind = "definition"
summary = "The unique nonnegative real number whose square is a prescribed nonnegative real number."
aliases = ["square root", "positive square root"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers", "real-analysis/supremum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a\ge0\), its **nonnegative square root** is the unique real number \(s\ge0\) satisfying \(s^2=a\), denoted \(\sqrt a\). The sign convention matters: if \(a>0\), the equation \(x^2=a\) has two real solutions, \(\sqrt a\) and \(-\sqrt a\).

## Existence from completeness

For \(a>0\), let \(S=\{x\ge0:x^2\le a\}\). This set is nonempty and bounded above, so it has a [[real-analysis/supremum|supremum]] \(s\). If \(s^2<a\), a sufficiently small positive increment still has square below \(a\), contradicting the upper-bound property. If \(s^2>a\), a sufficiently small decrement is an upper bound of \(S\), contradicting minimality. Thus \(s^2=a\). Uniqueness follows because squaring is strictly increasing on the nonnegative real numbers.

## Identities

For \(a,b\ge0\), \(\sqrt{ab}=\sqrt a\sqrt b\), and for real \(x\), \(\sqrt{x^2}=|x|\). The map is smooth for \(a>0\); differentiability at zero is a separate issue.

## References

- [John K. Hunter, Introduction to Analysis, Chapter 2: Numbers](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch2.pdf).
