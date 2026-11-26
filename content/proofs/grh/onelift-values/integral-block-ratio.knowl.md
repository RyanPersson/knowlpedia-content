+++
id = "proofs/grh/onelift-values/integral-block-ratio"
title = "Integral block ratio and annihilating rows"
kind = "definition"
summary = "A local n-by-r matrix has an integral block ratio when its distinguished r-by-r block is invertible and the remaining rows, divided by that block, are integral (and zero modulo the place at a chosen place)."
aliases = ["integral block ratio", "annihilating row"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasIntegralBlockRatio", "New.IsAnnihilatingRow"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
+++

Let \(E\) be a [[algebra-fields-galois/number-field|number field]], \(w\) a finite
[[algebra-fields-galois/place-of-global-field|place]] of \(E\), \(E_w\) the
[[algebra-fields-galois/completion-at-place|completion]], \(\mathcal{O}_w\subset E_w\) its
[[algebra-fields-galois/valuation-ring|valuation ring]] with maximal ideal \(\mathfrak{p}_w\) and
[[algebra-commutative/residue-field|residue field]] \(k_w\). Let \(\iota\colon R\hookrightarrow N\) be an
injection of finite index sets, and let \(x\in M_{N\times R}(E_w)\). Write \(x'\) for the square block of
the rows of \(x\) indexed by \(\iota(R)\) and \(x''\) for the block of the other rows. Fix a truth value
"\(w\) is chosen".

The matrix \(x\) **has an integral block ratio** (at \(w\), with respect to \(\iota\)) if

1. \(\det x'\ne 0\);
2. every entry of \(x''x'^{-1}\) lies in \(\mathcal{O}_w\);
3. if \(w\) is chosen, every entry of \(x''x'^{-1}\) lies in \(\mathfrak{p}_w\).

An **annihilating row** for \(x\) is a row vector \(l=(\lambda,\lambda')\in\mathcal{O}_w^{N}\) (with
\(\lambda\) the entries indexed by \(\iota(R)\) and \(\lambda'\) the others) such that

1. \(l\,x=\lambda x'+\lambda' x''=0\);
2. \(\lambda\not\equiv 0 \pmod{\mathfrak{p}_w}\);
3. if \(w\) is not chosen, \(\lambda'\equiv 0\pmod{\mathfrak{p}_w}\).

## Remarks

In the application \(\iota\) is the embedding of the index set of a basis of \(W\) into that of \(V\) carried
by a [[?lean:New.DescentPair|descent pair]], and "chosen" means that \(w\) is one of its chosen places
(as opposed to a twist place). A matrix with an integral block ratio is, up to right multiplication by
\(x'^{-1}\), of the shape \((1,\,x''x'^{-1})^{\mathsf T}\), which lies in the support of the block datum.
By [[proofs/grh/onelift-values/annihilating-row-exists|the dichotomy lemma]], every other matrix has an
annihilating row.

## References

1. Lean: `New.HasIntegralBlockRatio`, `New.IsAnnihilatingRow` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
