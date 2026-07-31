+++
id = "langlands/ind-coherent-sheaves-with-nilpotent-singular-support"
title = "Ind-coherent sheaves with nilpotent singular support"
kind = "definition"
summary = "The spectral category IndCoh_Nilp on the stack of dual-group local systems."
aliases = ["IndCoh_Nilp", "nilpotent singular-support category"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(X\) be a smooth projective curve and let \(\widehat G\) be a reductive
group. For the quasi-smooth derived stack
\(\operatorname{LocSys}_{\widehat G}(X)\), let
\(\mathcal N_{\widehat G}\) denote its
[[langlands/global-nilpotent-cone|global nilpotent cone]] in the scheme of
singularities. The category
\[
\operatorname{IndCoh}_{\mathcal N_{\widehat G}}
\bigl(\operatorname{LocSys}_{\widehat G}(X)\bigr)
\]
is the full subcategory of [[langlands/ind-coherent-sheaf|ind-coherent
sheaves]] \(\mathcal F\) satisfying
\[
\operatorname{SS}(\mathcal F)\subseteq\mathcal N_{\widehat G},
\]
where \(\operatorname{SS}\) is
[[langlands/singular-support-of-coherent-sheaf|coherent singular support]].

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

The support condition is a condition on the derived singularities of the
entire moduli stack, not ordinary set-theoretic support on
\(\operatorname{LocSys}_{\widehat G}(X)\).

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
