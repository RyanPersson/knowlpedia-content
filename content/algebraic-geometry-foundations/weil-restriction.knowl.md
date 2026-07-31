+++
id = "algebraic-geometry-foundations/weil-restriction"
title = "Weil restriction"
kind = "construction"
summary = "A representable restriction-of-scalars functor for schemes over a finite locally free base."
aliases = ["restriction of scalars of schemes", "Res S prime over S", "Weil restriction of scalars"]
domains = ["algebraic-geometry-foundations", "lie-groups"]
section_mode = "progressive"
+++

Let \(S'\to S\) be a [[algebraic-geometry-foundations/finite-locally-free-morphism|finite locally free morphism]] and let \(X\) be an \(S'\)-scheme. The **Weil restriction** \(\operatorname{Res}_{S'/S}X\), when it exists, is the \(S\)-scheme representing the functor
\[
T\longmapsto
\operatorname{Hom}_{S'}(T\times_S S',X)
\]
on \(S\)-schemes. Equivalently, it is characterized by natural bijections
\[
\operatorname{Hom}_S(T,\operatorname{Res}_{S'/S}X)
\cong
\operatorname{Hom}_{S'}(T_{S'},X).
\]

## Existence and structure

If \(X\) is affine over \(S'\), the Weil restriction exists and is affine over \(S\). It also exists under standard broader hypotheses, including when \(X\) is quasi-projective and \(S'\to S\) is finite locally free. Constructions such as products and group laws transport through the representing property, so the Weil restriction of a group scheme is a group scheme.

## Complex groups viewed over the real numbers

For a group scheme \(G\) over \(\mathbb C\),
\[
\bigl(\operatorname{Res}_{\mathbb C/\mathbb R}G\bigr)(\mathbb R)
\cong G(\mathbb C).
\]
For example, the real points of \(\operatorname{Res}_{\mathbb C/\mathbb R}SL_2\) form \(SL(2,\mathbb C)_{\mathbb R}\). This explains algebraically why its real dimension is twice the complex dimension.

After base change back to \(\mathbb C\), one obtains
\[
\bigl(\operatorname{Res}_{\mathbb C/\mathbb R}G\bigr)_{\mathbb C}
\cong G\times\overline G,
\]
where \(\overline G\) is the conjugate group scheme. This reflects
\(\mathbb C\otimes_{\mathbb R}\mathbb C\cong\mathbb C\times\mathbb C\). Weil
restriction is therefore a representable algebraic universal construction,
not merely the smooth operation of
[[lie-groups/underlying-real-lie-group|forgetting a complex structure]],
though the two agree after taking real points and analytifying in this
setting.

## References

1. Siegfried Bosch, Werner Lütkebohmert, and Michel Raynaud, *Néron Models*, Springer, 1990, §7.6. [Publisher record](https://doi.org/10.1007/978-3-642-51438-8).
2. The Stacks Project Authors, *More on Morphisms*, Section 97.11, “Restriction of scalars.” [Stacks Project](https://stacks.math.columbia.edu/tag/05Y8).
