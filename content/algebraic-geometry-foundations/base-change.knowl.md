+++
id = "algebraic-geometry-foundations/base-change"
title = "Base change"
kind = "definition"
summary = "Pulling an object over a base back along a morphism to a new base."
aliases = ["base change", "change of base", "pullback along the base"]
domains = ["algebraic-geometry-foundations"]
+++

For morphisms $X\to S$ and $S'\to S$, the **base change of $X$ along $S'\to S$** is the morphism

$$
X_{S'}:=X\times_S S'\longrightarrow S'.
$$

It is formed using the [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product]]. A morphism $f:X\to Y$ over $S$ similarly pulls back to

$$
f_{S'}:X\times_S S'\longrightarrow Y\times_S S'.
$$

On [[algebraic-geometry-foundations/affine-scheme|affine schemes]], if $R\to R'$ changes the base and $X=\operatorname{Spec}A$, then

$$
X_{R'}\cong\operatorname{Spec}(A\otimes_R R').
$$

## Remarks

Base change is a categorical pullback, not merely a substitution of coordinates or a restriction of underlying topological spaces. Whether a geometric property is preserved by base change must be checked for that property.
