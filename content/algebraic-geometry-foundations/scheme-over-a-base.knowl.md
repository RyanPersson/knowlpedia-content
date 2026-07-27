+++
id = "algebraic-geometry-foundations/scheme-over-a-base"
title = "Scheme over a base"
kind = "knowl"
summary = "A scheme equipped with a specified morphism to a fixed base scheme."
aliases = ["scheme-over-a-base", "Scheme over a base", "scheme over a scheme", "S-scheme"]
domains = ["algebraic-geometry-foundations"]
+++

Let $S$ be a [[algebraic-geometry-foundations/scheme|scheme]]. A **scheme over $S$**, or **$S$-scheme**, is a scheme $X$ equipped with a specified [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]]
$$
X\longrightarrow S,
$$
called its structure morphism.

Given $S$-schemes $X\to S$ and $Y\to S$, an **$S$-morphism** $f:X\to Y$ is a morphism for which the composite $X\to Y\to S$ equals the specified map $X\to S$. Schemes over $S$, together with their $S$-morphisms, form the category customarily denoted $\mathbf{Sch}/S$.

For example, a ring homomorphism $R\to A$ makes $\operatorname{Spec}A$ a scheme over $\operatorname{Spec}R$. Constructions such as [[algebraic-geometry-foundations/base-change|base change]] and the [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product]] keep track of these specified maps to the base.
