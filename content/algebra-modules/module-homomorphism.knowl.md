+++
id = "algebra-modules/module-homomorphism"
title = "Module homomorphism"
kind = "knowl"
summary = "A map preserving addition and scalar multiplication between modules."
aliases = ["module-homomorphism", "Module homomorphism"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/module-homomorphism.md"
+++

Let \(R\) be a ring and let \(M,N\) be left \(R\)-[[algebra-modules/module|modules]]. A **module homomorphism** is a [[shared-foundations/function|function]] \(f:M\to N\) such that for all \(m,m'\in M\) and \(r\in R\),
\[
f(m+m')=f(m)+f(m') \quad\text{and}\quad f(rm)=r f(m).
\]
## Equivalent characterizations

Equivalently, \(f\) is a homomorphism of the underlying additive groups and commutes with multiplication by every scalar in \(R\).

## Examples

- For the \(\mathbb Z\)-module \(\mathbb Z\), the map \(f(n)=kn\) is a module homomorphism for every fixed \(k\in\mathbb Z\).
- If \(R\) is commutative, then \(f:R^2\to R\), \(f(a,b)=a+rb\), is \(R\)-linear for each fixed \(r\in R\).
