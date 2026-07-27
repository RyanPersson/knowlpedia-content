+++
id = "operator-algebras/regular-operator-hilbert-cstar-module"
title = "Regular operator on a Hilbert C*-module"
kind = "definition"
summary = "A closed densely defined Hilbert-module operator whose adjoint is densely defined and whose graph has the required complementability."
aliases = ["regular Hilbert-module operator", "regular unbounded operator"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(E\) be a
[[operator-algebras/hilbert-cstar-module|Hilbert \(C^*\)-module]] over a
\(C^*\)-algebra \(A\). A densely defined \(A\)-linear operator
\(T:\operatorname{Dom}(T)\to E\), whose domain is a dense right
\(A\)-submodule of \(E\), is
**regular** if \(T\) is closed, its adjoint \(T^*\) is densely defined, and
\[
\operatorname{Ran}(1+T^*T)
\]
is dense in \(E\). The adjoint is defined by requiring
\(\langle Tx,y\rangle=\langle x,T^*y\rangle\) for every
\(x\in\operatorname{Dom}(T)\). A regular operator is **self-adjoint** when
\(T=T^*\), including equality of domains. Regularity is additional structure
in Hilbert-module theory; closed [[functional-analysis/densely-defined-operator|densely defined operators]] need not be
regular.

## Graph and bounded transform

Regularity is equivalent to orthogonal complementability of the graph of
\(T\) in \(E\oplus E\), with the densely defined adjoint condition understood.
It also makes
\[
F_T=T(1+T^*T)^{-1/2}
\]
a bounded
[[operator-algebras/adjointable-operator-hilbert-module|adjointable operator]]
with \(\|F_T\|\leq1\). Conversely, suitable contractions arise as bounded
transforms of regular operators. This correspondence supplies the continuous
functional calculus used in unbounded \(KK\)-theory
[Lance, Chapters 9–10](https://doi.org/10.1017/CBO9780511526206).

## The self-adjoint case

For a self-adjoint regular \(T\), the operators \(T\pm i\) have bounded
adjointable inverses \(E\to\operatorname{Dom}(T)\subset E\), and continuous
functional calculus is available for functions on \(\mathbb R\). Conversely,
a closed [[functional-analysis/symmetric-operator|symmetric operator]] whose \(T+i\) and \(T-i\) have dense range is
self-adjoint and regular. These range conditions replace Hilbert-space
arguments that would otherwise rely on automatic [[linear-algebra/orthogonal-complement|orthogonal complements]].

## Comparison with Hilbert spaces

When the coefficient algebra is \(\mathbb C\), every closed densely defined
operator with densely defined adjoint is regular. This fails for general
Hilbert \(C^*\)-modules because closed submodules need not be orthogonally
complemented. Hence “regular” here is unrelated to regularity of a measure,
elliptic regularity, or a regular point of an operator pencil.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Publisher DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 9 on regular operators and Chapter 10 on the bounded transform.
2. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Publisher DOI record](https://doi.org/10.1017/9781009701907). Relevant: §13.3 on regular operators on Hilbert modules.
