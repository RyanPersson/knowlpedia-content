+++
id = "algebra-commutative/jacobson-radical-intersection-maximals"
title = "Jacobson radical as intersection of maximal ideals"
kind = "knowl"
summary = "In a commutative ring, the Jacobson radical equals the intersection of all maximal ideals."
aliases = ["jacobson-radical-intersection-maximals", "Jacobson radical as intersection of maximal ideals"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/jacobson-radical-intersection-maximals.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]]. Its **Jacobson radical** is
$$
J(R)=\bigcap_{\mathfrak m\in\operatorname{MaxSpec}(R)} \mathfrak m,
$$
the intersection of all maximal ideals of $R$. Here $\operatorname{MaxSpec}(R)$ denotes the [[algebra-commutative/maximal-spectrum|maximal spectrum]].

## Equivalent characterizations

An element $r\in R$ lies in $J(R)$ if and only if its image in every [[algebra-commutative/residue-field|residue field]] $R/\mathfrak m$ is zero; equivalently, $r\in\mathfrak m$ for every maximal ideal $\mathfrak m$.

## Examples

1. **The integers.**
   In $R=\mathbb Z$, maximal ideals are precisely $(p)$ for primes $p$. Their intersection is $(0)$, so $J(\mathbb Z)=0$.

2. **A local example from localization.**
   Let $R=\mathbb Z_{(p)}$ be the [[algebra-commutative/localization-at-prime|localization]] of $\mathbb Z$ at the prime $(p)$. This is a [[algebra-commutative/local-ring|local ring]] whose unique maximal ideal is $p\mathbb Z_{(p)}$, hence
   $$
   J(\mathbb Z_{(p)}) = p\mathbb Z_{(p)}.
   $$

3. **Dual numbers.**
   Let $R=k[\varepsilon]/(\varepsilon^2)$ for a field $k$. The ideal $(\bar\varepsilon)$ is the unique maximal ideal because $R/(\bar\varepsilon)\cong k$. Therefore $J(R)=(\bar\varepsilon)$.

## Remarks

If $R$ is a [[algebra-commutative/local-ring|local ring]] with maximal ideal $\mathfrak m$, then
$$
J(R)=\mathfrak m.
$$

Thus, in a local ring, the Jacobson radical is precisely the set of nonunits. Compare the module-theoretic characterization that the [[algebra-commutative/jacobson-annihilates-simples|Jacobson radical annihilates simple modules]].
