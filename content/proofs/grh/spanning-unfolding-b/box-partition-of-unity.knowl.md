+++
id = "proofs/grh/spanning-unfolding-b/box-partition-of-unity"
title = "Box partition of unity for a class"
kind = "definition"
summary = "A measurable function on the product of real groups, bounded by one, invariant under the fixer of the frame, supported in boxes for the frame vectors, whose translates under the class unipotent group add up to one modulo the fixer."
aliases = ["IsBoxPartitionOfUnity"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsBoxPartitionOfUnity"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(c\) a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]], and \(G_\infty=\prod_vG_1\). A function \(\omega\colon G_\infty\to[0,\infty]\) is a **box partition of unity for \(c\)** if

1. \(\omega\) is measurable and \(\omega\le1\);
2. if \(\omega(y)\ne0\) then, for every infinite place \(v\), the component \(y_v\) lies in the [[?lean:New.frameBox|frame box]] of radius \(b^{27}\cdot\ell(y_v)\), where \(\ell\) is the [[?lean:New.besselLength|Bessel length]]: every frame vector of \(y_v\) has norm at most \(b^{27}\ell(y_v)\);
3. for every \(y\in G_\infty\) and every weight \(a\colon\mathsf{U}_c(M)\to[0,\infty]\) such that \(\sum_{u\in\mathsf{U}^0_c(M)}a(u\gamma)=1\) for all \(\gamma\in\mathsf{U}_c(M)\),
\[
\sum_{\gamma\in\mathsf{U}_c(M)}a(\gamma)\,\omega(\gamma_\infty y)=1 ;
\]
4. \(\omega(sy)=\omega(y)\) whenever every component \(s_v\) lies in the [[?lean:New.Shape.Form.besselFixer|fixer of the frame]] in \(G_1\).

## Remarks

Condition 3 says that the translates of \(\omega\) under \(\mathsf{U}_c(M)\) add up to one when each coset of \(\mathsf{U}^0_c(M)\) is counted with total weight one; this is the right notion because, by condition 4, \(\omega\) is invariant under \(\mathsf{U}^0_c(M)\), so its translates are constant along these cosets.

## References

1. Lean: `New.Filling.IsBoxPartitionOfUnity` in `src/New/Spanning/Unfolding/Setup.lean`.
