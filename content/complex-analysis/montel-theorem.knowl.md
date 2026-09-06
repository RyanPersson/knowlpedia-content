+++
id = "complex-analysis/montel-theorem"
title = "Montel theorem"
kind = "theorem"
summary = "Every locally uniformly bounded family of holomorphic functions is normal."
aliases = ["Montel's theorem for holomorphic functions"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/complex-domain", "complex-analysis/normal-family", "complex-analysis/cauchy-integral-formula", "real-analysis/arzela-ascoli-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(D\subseteq\mathbb C\) be a [[complex-analysis/complex-domain|domain]], and let \(\mathcal F\) be a family of holomorphic functions \(D\to\mathbb C\). Suppose that \(\mathcal F\) is **locally uniformly bounded**: for every compact set \(K\subset D\), there is a constant \(M_K\) such that
\[
|f(z)|\le M_K
\qquad(f\in\mathcal F,\ z\in K).
\]
Then \(\mathcal F\) is a [[complex-analysis/normal-family|normal family]].

## Sequential conclusion

Every sequence in \(\mathcal F\) has a subsequence converging uniformly on compact subsets of \(D\) to a holomorphic function. The locally uniform boundedness prevents the subsequence from escaping locally uniformly to \(\infty\).

## Proof idea

On every relatively compact disc, the [[complex-analysis/cauchy-integral-formula|Cauchy estimates]] give common derivative bounds. The family is therefore equicontinuous there. The [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli theorem]] gives convergent subsequences on an exhaustion by compact sets, and a diagonal argument produces one subsequence converging locally uniformly throughout \(D\).

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter VII.
