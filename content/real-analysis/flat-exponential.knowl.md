+++
id = "real-analysis/flat-exponential"
title = "Flat exponential"
kind = "construction"
summary = "An exponential cutoff whose extension by zero has vanishing derivatives of every order."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/flat-function", "real-analysis/chain-rule", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(c>0\) and a positive integer \(q\), the **flat exponential**
\[
h(t)=\begin{cases}e^{-c/t^q},&t>0,\\0,&t\le0\end{cases}
\]
is smooth on \(\mathbb R\) and [[real-analysis/flat-function|flat at zero]].

## Proof

Every derivative on \(t>0\) is a finite sum of terms \(C t^{-N}e^{-c/t^q}\). Each tends to zero as \(t\downarrow0\): put \(s=c/t^q\) and use \(s^M e^{-s}\to0\) for every fixed \(M\ge0\). One elementary bound follows from the exponential series: \(e^{s/2}\ge (s/2)^k/k!\) with an integer \(k>M\).

Extend all these derivatives by zero to the other side. Induction, using difference quotients or the fundamental theorem of calculus, proves that the extensions are successive derivatives of \(h\). This proves smoothness and flatness.

## Products and shifts

Translates produce flat endpoints at other locations. Multiplying two such factors yields a smooth function positive on a bounded interval and zero outside it, providing explicit [[differential-geometry/bump-function|bump functions]].

## References

- [Richard Schwartz, Partitions of Unity (Brown lecture notes)](https://www.math.brown.edu/reschwar/M114B/notes9.pdf).
