+++
id = "operator-algebras/dimension-function-on-projections"
title = "Dimension function on projections"
kind = "definition"
summary = "An additive normal numerical invariant of Murray-von Neumann equivalence classes of projections in a factor."
aliases = ["Murray–von Neumann dimension"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-factor", "operator-algebras/murray-von-neumann-equivalence", "linear-algebra/orthogonal-projection", "operator-algebras/type-i-factor", "operator-algebras/minimal-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-factor|factor]] with separable
predual and let \(\mathcal P(M)\) be its projections. A **dimension function
on projections** is a map
\[
d:\mathcal P(M)\longrightarrow[0,\infty]
\]
that is invariant under
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann equivalence]], additive on [[linear-algebra/orthogonal-projection|orthogonal projections]], faithful
\((d(p)=0\Rightarrow p=0)\), and normal:
\[
p_i\uparrow p\quad\Longrightarrow\quad d(p_i)\uparrow d(p).
\]
In a finite factor one requires \(d(1)=1\). In an infinite semifinite factor a
choice of scale is required; in a
[[operator-algebras/type-i-factor|type I factor]] it is customary to give
every [[operator-algebras/minimal-projection|minimal projection]] dimension
\(1\). These normalizations make dimension an extension of matrix rank or
normalized rank.

## Dimension scales and factor types

With the standard normalization, the possible finite values distinguish the
factor types. They are
\(\{0,1/n,\ldots,1\}\) for type \(\mathrm I_n\), \([0,1]\) for type
\(\mathrm{II}_1\), \(\{0,1,2,\ldots\}\) for type
\(\mathrm I_\infty\), and \([0,\infty)\) for type
\(\mathrm{II}_\infty\). For a
[[operator-algebras/type-iii-factor|type III factor]] the only scalar
dimension function has values \(0\) and \(\infty\). This is the
continuous-dimension
theory underlying the classification of factors.

## Finite factors and traces

If \(M\) is finite, its unique normalized center-valued trace is scalar
because \(M\) is a factor. Its restriction to projections is the normalized
dimension function. In a type \(\mathrm{II}_1\) factor, this gives
\[
p\sim q\quad\Longleftrightarrow\quad d(p)=d(q),
\]
and every value in \([0,1]\) occurs. Thus dimension is a complete invariant
of projection equivalence in this setting, not merely a numerical estimate.

## Conventions and scope

**Warning.** On a general
[[operator-algebras/von-neumann-algebra|von Neumann algebra]], projection
dimension is center-valued rather than scalar-valued, and non-countably
decomposable factors require cardinal-valued refinements. The scalar
formulation in the core is intentionally restricted to factors with
separable predual. In a type \(\mathrm{II}_\infty\) factor, multiplying
\(d\) by a positive constant changes the scale but not the induced
comparison of projections.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §§1–2 on equivalence, comparison, dimension, and factor types.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: Chapter 6 on comparison theory and dimension of projections.
