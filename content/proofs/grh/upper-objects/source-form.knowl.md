+++
id = "proofs/grh/upper-objects/source-form"
title = "Source form"
kind = "definition"
summary = "An algebraic modular form on the definite unitary group U(X_0) of weight (a,0,...,0) at the a-places and 0 elsewhere, fixed by the level of stage 0."
aliases = ["source forms", "column"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.SourceForm"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and \(X_0\) the standard definite hermitian space of rank \(k=n_0\) over \(E\).

**Definition.** A **source form** is an [[?lean:New.AlgForm|algebraic modular form]] \(\varphi\) on \(U(X_0)\) — a function on \(U(X_0)(\mathbb A_f)\) with values in the Weyl module \(\mathcal V_0\) of rank \(k\), with open stabiliser under right translation, such that \(\varphi(\gamma g)=\rho(\gamma)\varphi(g)\) for rational \(\gamma\) — where \(\mathcal V_0\) has [[proofs/grh/upper-objects/weights-of-the-definite-spaces|column numbers \(c_\tau\) and determinant exponent \(\ell_0=0\)]], and which is fixed by the [[proofs/grh/upper-objects/level-places-of-the-data|level \(K_{X_0}\) of stage 0]].

Since only columns of height \(<k\) matter in rank \(k\) and the only such height with \(c_\tau\ne0\) is \(1\), the highest weight is \(\mu(X_0)_\tau=(a,0,\dots,0)\) at the \(a\)-places \(\tau\) and \(0\) at the other infinite places. The level is principal at the chosen places (the primes dividing \(\pi_M\)) and has last row \(\equiv(0,\dots,0,1)\) modulo \(\pi_N\).

## Remarks

Other files call source forms *columns*. The ramified source forms (mean zero under the scalings at each prime dividing \(\pi_N\)) are defined in [[?lean:New.Data.ramifiedSourceForms|another area]].

## References

1. Lean: `New.Data.SourceForm` in `src/New/UpperBound/Objects/Columns.lean`.
