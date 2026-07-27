+++
id = "algebra-commutative/integrally-closed-domain"
title = "Integrally closed domain"
kind = "knowl"
summary = "A domain that already contains every element of its fraction field that is integral over it."
aliases = ["integrally-closed-domain", "Integrally closed domain"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/integrally-closed-domain.md"
+++

Let \(R\) be an integral domain with fraction field \(K\).

The domain \(R\) is **integrally closed** if every \(x\in K\) that is [[algebra-commutative/integral-element|integral over \(R\)]] already lies in \(R\).

## Equivalent characterizations

Equivalently, the [[algebra-commutative/integral-closure|integral closure]] of \(R\) in \(K\) is \(R\):
\[
\overline{R}^{\,K} = R.
\]

## Remarks

This condition is often phrased by saying that \(R\) has no new integral elements in its fraction field.

## Useful perspective
Because \(K=S^{-1}R\) for \(S=R\setminus\{0\}\), integral closedness concerns elements obtained after [[algebra-commutative/localization-ring|inverting]] all nonzero elements.

Integral closedness is local: \(R\) is integrally closed if and only if \(R_{\mathfrak p}\) is integrally closed for every prime ideal \(\mathfrak p\).

## Examples
1. **Principal ideal domains, such as \(\mathbb Z\).**
   Every PID is integrally closed. In particular, any rational number integral over \(\mathbb Z\) is an integer.

2. **Polynomial rings over a field.**
   If \(k\) is a field, then \(k[x_1,\dots,x_n]\) is integrally closed in \(k(x_1,\dots,x_n)\). More generally, every unique factorization domain is integrally closed.

3. **Discrete valuation rings.**
   Any [[algebra-commutative/dvr|discrete valuation ring]] is integrally closed. For example, \(k\llbracket t\rrbracket\) is integrally closed in \(k((t))\).

## Non-examples
- **A cusp subring.**
  The ring \(R=k[x^2,x^3]\subset k(x)\) is not integrally closed: \(x\) is integral over \(R\), since it satisfies \(T^2-x^2=0\), but \(x\notin R\). Its integral closure in \(k(x)\) is \(k[x]\).

- **A classical quadratic example.**
  The ring \(\mathbb Z[\sqrt5]\) is not integrally closed in \(\mathbb Q(\sqrt5)\): the element \((1+\sqrt5)/2\) satisfies \(T^2-T-1=0\) but does not belong to \(\mathbb Z[\sqrt5]\).
