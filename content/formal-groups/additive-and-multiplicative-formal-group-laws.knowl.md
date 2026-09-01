+++
id = "formal-groups/additive-and-multiplicative-formal-group-laws"
title = "Additive and multiplicative formal group laws"
kind = "example"
summary = "The standard one-dimensional laws F_a(X,Y)=X+Y and F_m(X,Y)=X+Y+XY."
aliases = ["additive formal group law", "multiplicative formal group law", "formal additive group", "formal multiplicative group"]
domains = ["formal-groups"]
prerequisites = ["algebra-rings/commutative-ring", "formal-groups/one-dimensional-formal-group-law"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Over a [[algebra-rings/commutative-ring|commutative ring]] \(R\), the **additive formal group law** and
**multiplicative formal group law** are
\[
F_a(X,Y)=X+Y,
\qquad
F_m(X,Y)=X+Y+XY.
\]
Both are [[formal-groups/one-dimensional-formal-group-law|one-dimensional
commutative formal group laws]]. Their inverse series are
\[
i_a(X)=-X,
\qquad
i_m(X)=-\frac{X}{1+X}=-X+X^2-X^3+\cdots.
\]

## Why the multiplicative formula appears

Use the coordinate \(X=u-1\) near the identity \(u=1\) of the multiplicative
group. Since
\[
(1+X)(1+Y)-1=X+Y+XY,
\]
ordinary multiplication becomes \(F_m\) in this identity-centered coordinate.
Thus \(F_a\) is the law near \(0\) on the additive group, while \(F_m\) is the
law near \(1\) on the multiplicative group.

## Logarithms over characteristic zero

Over a \(\mathbb Q\)-algebra,
\[
\log_{F_a}(X)=X,\qquad
\log_{F_m}(X)=\log(1+X)
=\sum_{n\geq1}(-1)^{n+1}\frac{X^n}{n}.
\]
The identity
\[
\log(1+F_m(X,Y))
=\log(1+X)+\log(1+Y)
\]
exhibits the multiplicative law as strictly isomorphic to the additive law
after rational denominators are allowed.

## Positive-characteristic distinction

In characteristic \(p\),
\[
[p]_{F_a}(X)=0,
\qquad
[p]_{F_m}(X)=(1+X)^p-1=X^p.
\]
Therefore these laws can have the same one-dimensional abelian tangent Lie
algebra without being isomorphic. This is the basic example behind the
[[formal-groups/positive-characteristic-warning|positive-characteristic
warning]].

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapter 1, basic one-dimensional examples.
2. J. F. Adams, *Stable Homotopy and Generalised Homology*, University of Chicago Press, 1974. Relevant: Part II, additive and multiplicative formal group laws.
