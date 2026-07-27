+++
id = "algebraic-geometry-foundations/covering-family"
title = "Covering family in a site"
kind = "knowl"
summary = "A family of morphisms whose generated sieve is covering in the site's Grothendieck topology."
aliases = ["covering-family", "Covering family", "Covering family in a site"]
domains = ["algebraic-geometry-foundations"]
+++

Let $(\mathcal C,J)$ be a [[algebraic-geometry-foundations/site|site]] and let $U$ be an object of $\mathcal C$. A family of morphisms
$$
\{f_i:U_i\to U\}_{i\in I}
$$
is a **covering family** if the [[algebraic-geometry-foundations/sieve|sieve]] it generates belongs to $J(U)$. The generated sieve consists of all morphisms $V\to U$ that factor through at least one $f_i$.

This definition depends on the chosen [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]]. For the [[algebraic-geometry-foundations/etale-topology|étale topology]], the covering families are precisely the jointly surjective families of [[algebraic-geometry-foundations/etale-morphism|étale morphisms]].
