+++
id = "noncommutative-geometry/semifinite-index-pairing"
title = "Semifinite K-theory index pairing"
kind = "definition"
summary = "The pairing of a semifinite spectral triple with K-theory through a trace-valued Breuer index."
aliases = ["Breuer index pairing", "tau-index pairing", "semifinite spectral-flow pairing"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/semifinite-spectral-triple", "operator-algebras/breuer-fredholm-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((\mathcal A,\mathcal N,D,\tau)\) be a [[noncommutative-geometry/semifinite-spectral-triple|semifinite spectral triple]] and put \(P=1_{[0,\infty)}(D)\). Its **semifinite K-theory index pairing** is the homomorphism obtained by replacing the ordinary Fredholm index with the [[operator-algebras/breuer-fredholm-operator|\(\tau\)-Breuer index]]. In odd parity, a unitary \(u\in M_n(\mathcal A)\) represents a class in \(K_1(\mathcal A)\), and
\[
\langle [u],[D]\rangle_\tau=\operatorname{Ind}_\tau(PuP),
\]
where \(PuP:P(H^n)\to P(H^n)\) is Breuer-Fredholm. In even parity, a projection \(e\in M_n(\mathcal A)\) is paired with the Breuer index of the compression \(eD^+e:eH_+^n\to eH_-^n\). The value is real in general because \(\tau\)-dimensions need not be integers.

## Spectral-flow realization

For the odd pairing, the Breuer index can equivalently be computed as the semifinite [[noncommutative-geometry/spectral-flow|spectral flow]] from \(D\) to \(uDu^*\), with the sign determined by the orientation of the chosen path. This equality is the analytic bridge between K-theory and the trace-valued crossing count.

The pairing depends only on the K-theory class and the homotopy class of the semifinite [[noncommutative-geometry/fredholm-module|Fredholm module]], provided the usual matrix amplification and unitization conventions are used.

## Examples and scope

When \(\mathcal N=B(H)\) and \(\tau\) is the ordinary operator trace, the Breuer index is the integer Fredholm index, so the construction reduces to the usual spectral-triple pairing. In a type \(\mathrm{II}_\infty\) factor, [[operator-algebras/finite-projection|finite projections]] can have arbitrary nonnegative real trace, and the pairing can therefore take nonintegral real values.

**Warning.** The numerical pairing requires a specified trace. A [[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann algebra]] without a chosen [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] does not determine these values by itself.

## References

1. A. L. Carey and J. Phillips, “Unbounded Fredholm Modules and Spectral Flow,” *Canadian Journal of Mathematics* 50 (1998), 673–718. [DOI record](https://doi.org/10.4153/CJM-1998-038-X). Relevant: §§1–2 on the Breuer index and spectral-flow formula.
2. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The Local Index Formula in Semifinite von Neumann Algebras I: Spectral Flow,” *Advances in Mathematics* 202 (2006), 451–516. [DOI record](https://doi.org/10.1016/j.aim.2005.03.011). Relevant: §§2–4 on semifinite triples, spectral flow, and the odd pairing.
