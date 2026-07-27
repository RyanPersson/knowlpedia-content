+++
id = "convex-analysis/affine-sets-are-translates-of-subspaces"
title = "Affine Sets are Translates of Subspaces"
kind = "knowl"
summary = "A nonempty set is affine exactly when it is a translate of a linear subspace."
aliases = ["affine-sets-are-translates-of-subspaces", "Affine Sets are Translates of Subspaces"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/affine-sets-are-translates-of-subspaces.md"
+++

Let \(X\) be a [[linear-algebra/vector-space|vector space]] and let \(\Omega\subseteq X\) be nonempty. Then \(\Omega\) is [[convex-analysis/affine-set|affine]] if and only if, for any \(\omega\in\Omega\),
\[
\Omega-\omega:=\{x-\omega:x\in\Omega\}
\]
is a [[convex-analysis/linear-subspace|linear subspace]] of \(X\).

Equivalently, \(\Omega\) is affine if and only if \(\Omega=\omega+L\) for some \(\omega\in X\) and linear subspace \(L\subseteq X\).
