+++
id = "measure-theory/mixed-lebesgue-norm"
title = "Mixed Lebesgue norm"
kind = "definition"
summary = "An iterated norm that measures space integrability first and time integrability second."
aliases = ["mixed time-space norm", "mixed Lp norm", "time-space Lebesgue norm"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "measure-theory/product-measure", "measure-theory/essential-supremum", "measure-theory/sigma-finite-measure"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a jointly measurable \(u(t,x)\) on a product of sigma-finite measure spaces, the **mixed Lebesgue norm** \(L^q_tL^p_x\) is
\[
\|u\|_{L^q_tL^p_x}
=\left(\int \|u(t,\cdot)\|_{L^p_x}^{q}\,dt\right)^{1/q},
\qquad 1\le p,q<\infty.
\]
Replace an integral norm by the corresponding [[measure-theory/essential-supremum|essential supremum]] when its exponent is infinite. For vector fields use the Euclidean magnitude inside the spatial norm.

## Order and examples

The order matters when \(p\ne q\). If \(p=q<\infty\), Tonelli's theorem identifies the mixed norm with the product-space \(L^p\) norm. For a separated function \(u(t,x)=a(t)b(x)\), it equals \(\|a\|_q\|b\|_p\). In particular, \(L^\infty_tL^2_x\) gives a bound on spatial energy for almost every time, not automatically a chosen representative at every time.

## Banach-valued notation

The notation \(L^q(I;L^p(X))\) also commonly denotes a Bochner space. For \(p=\infty\), strong measurability of the map into \(L^\infty(X)\) is an additional issue; joint scalar measurability alone does not always give that property.
