+++
id = "algebraic-geometry-foundations/etale-topology"
title = "Étale topology"
kind = "knowl"
summary = "The Grothendieck topology in which jointly surjective families of étale morphisms are covers."
aliases = ["etale-topology", "Etale topology", "Étale topology"]
domains = ["algebraic-geometry-foundations"]
+++

The **étale topology** is the [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]] on [[algebraic-geometry-foundations/scheme|schemes]] in which a family
\[
\{U_i\to U\}_{i\in I}
\]
is a [[algebraic-geometry-foundations/covering-family|covering family]] exactly when every \(U_i\to U\) is [[algebraic-geometry-foundations/etale-morphism|étale]] and the family is jointly surjective on underlying points:
\[
|U|=\bigcup_{i\in I}\operatorname{im}(|U_i|\to |U|).
\]

Unlike the [[algebra-commutative/zariski-topology|Zariski topology]], this is not merely a point-set topology on one scheme. It permits étale morphisms as local charts. Restricting it to [[algebraic-geometry-foundations/scheme-over-a-base|schemes over a fixed scheme \(X\)]] that are étale gives the [[algebraic-geometry-foundations/small-etale-site|small étale site]] of \(X\).

For a finite separable field extension \(K/F\), \(\operatorname{Spec}K\to\operatorname{Spec}F\) is a one-map étale cover.
