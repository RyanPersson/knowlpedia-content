+++
id = "langlands/ind-coherent-sheaves-with-nilpotent-singular-support"
title = "Ind-coherent sheaves with nilpotent singular support"
kind = "definition"
summary = "The spectral category IndCoh_Nilp on the stack of dual-group local systems."
aliases = ["IndCoh_Nilp", "nilpotent singular-support category"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

For the derived stack
\(\operatorname{LocSys}_{\widehat G}(X)\), let \(\mathcal N\) denote its
global nilpotent cone in the scheme of singularities. The category
\[
\operatorname{IndCoh}_{\mathcal N}
\bigl(\operatorname{LocSys}_{\widehat G}(X)\bigr)
\]
consists of ind-coherent sheaves whose singular support lies in
\(\mathcal N\).

This is the spectral category in the modern de Rham
[[langlands/geometric-langlands-correspondence|geometric Langlands
correspondence]] for a general reductive group.

## Why QCoh is not enough

On a smooth stack, quasi-coherent and ind-coherent theories are closely
related. The derived stack of local systems is singular, and additional
directions detected by singular support are needed to match all automorphic
\(D\)-modules. The zero-section condition recovers the quasi-coherent
subcategory; allowing the global nilpotent cone is the required enlargement.

## Scope

Both “ind-coherent” and “singular support” are derived notions here. The
nilpotent cone is not simply the ordinary nilpotent cone in one Lie algebra:
it is defined globally over the stack of local systems.

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
