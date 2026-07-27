+++
id = "linear-algebra/orthogonal-complement"
title = "Orthogonal complement"
kind = "knowl"
summary = "The subspace of vectors orthogonal to every vector in a given subset."
aliases = ["orthogonal complement"]
domains = ["linear-algebra"]
+++

For a subset \(S\) of an [[linear-algebra/inner-product-space|inner-product space]] \(H\), its **orthogonal complement** is
\[
S^\perp=\{x\in H:\langle s,x\rangle=0\text{ for every }s\in S\}.
\]
It is always a [[linear-algebra/closed-linear-subspace|closed linear subspace]]. If \(M\) is closed in a [[linear-algebra/hilbert-space|Hilbert space]], then every \(x\in H\) has a unique decomposition \(x=m+n\) with \(m\in M\) and \(n\in M^\perp\), so \(H=M\oplus M^\perp\).
