+++
id = "proofs/grh/derivatives-vacuum/standard-data"
title = "Standard data at a prime"
kind = "definition"
summary = "The module over the ring of p-integral complex numbers spanned by the translates of the integral vacuum by the finite adelic vectors that delta makes integral above p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.standardData", "New.Parameters.integralAfter"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
+++

Let \(V\) be a [[?lean:New.Space|hermitian space]] over \(E\) with finite index set \(n\), \(p\) a prime, \(\iota_p\colon\mathbb{C}\to\mathbb{C}_p\) a [[?lean:New.PadicPlace|\(p\)-adic place]] with valuation ring \(R_p=\{z\in\mathbb{C}:\lvert\iota_pz\rvert_p\le1\}\), and \(\delta\in\mathcal{O}_K\).

For a set \(S\) of finite places of \(E\), a finite adelic vector \(x\in\mathbb{A}_{E,f}^{\,n}\) is **integral after \(\delta\) on \(S\)** if for every coordinate \(i\) and every \(w\in S\) the component \((\delta x_i)_w\) lies in the ring of integers of the completion \(E_w\), that is \(\lvert\delta x_{i}\rvert_w\le1\), equivalently \(\operatorname{ord}_w(\delta x_i)\ge0\); these \(x\) form an additive subgroup.

The module of **standard data at \(p\)** (for \(\delta\)) is the \(R_p\)-submodule of \(\mathcal{S}(V)\)
\[ \mathcal{D}_p(V,\delta)=\operatorname{span}_{R_p}\bigl\{h(x)\,\theta^\circ:\ x\text{ integral after }\delta\text{ at the places of }E\text{ above }p\bigr\}, \]
where \(\theta^\circ\) is the [[proofs/grh/derivatives-vacuum/integral-vacuum|integral vacuum]] and \(h(x)\) the [[?lean:New.Space.finHeisenbergOp|finite Heisenberg operator]].

## References

1. Lean: `New.Parameters.standardData`, `New.Parameters.integralAfter` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
