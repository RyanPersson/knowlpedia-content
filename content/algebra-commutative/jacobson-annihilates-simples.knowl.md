+++
id = "algebra-commutative/jacobson-annihilates-simples"
title = "Jacobson radical annihilates simple modules"
kind = "knowl"
summary = "For every simple right R-module S, the Jacobson radical satisfies S J(R) = 0."
aliases = ["jacobson-annihilates-simples", "Jacobson radical annihilates simple modules"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/jacobson-annihilates-simples.md"
+++

Let $R$ be a ring, let $J(R)$ be its Jacobson radical, and let $S$ be a simple right $R$-module. Then
$$
S J(R)=0.
$$

## Equivalent characterizations

Equivalently, every element of $J(R)$ acts as zero on $S$, so
$$
J(R)\subseteq \operatorname{Ann}_R(S)
$$
for every simple right module $S$, where [[algebra-modules/annihilator-module|the annihilator]] consists of the ring elements acting as zero on $S$.

## Remarks

If $R$ is commutative, every simple $R$-module is isomorphic to $R/\mathfrak m$ for some maximal ideal $\mathfrak m$. The theorem then gives
$$
J(R)\subseteq \mathfrak m
\quad\text{for all maximal ideals }\mathfrak m,
$$
in agreement with [[algebra-commutative/jacobson-radical-intersection-maximals|the commutative characterization]] of $J(R)$.

## Examples

1. **Local rings.**
   If $(R,\mathfrak m)$ is a commutative [[algebra-commutative/local-ring|local ring]], then $J(R)=\mathfrak m$, and every simple $R$-module is isomorphic to the [[algebra-commutative/residue-field|residue field $R/\mathfrak m$]]. The ideal $\mathfrak m$ acts as zero on it.

2. **The integers.**
   In $R=\mathbb Z$, $J(\mathbb Z)=0$. The simple $\mathbb Z$-modules are $\mathbb Z/p\mathbb Z$, so the assertion is immediate.

3. **Dual numbers.**
   Let $R=k[\varepsilon]/(\varepsilon^2)$. Then $J(R)=(\bar\varepsilon)$, and every simple module is isomorphic to $R/(\bar\varepsilon)\cong k$. Thus $kJ(R)=0$.
