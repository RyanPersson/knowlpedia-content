+++
id = "harmonic-analysis/unramified-hecke-polynomial"
title = "Unramified Hecke polynomial for the general linear group"
kind = "definition"
summary = "A polynomial with spherical Hecke operators as coefficients."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/hecke-operator", "harmonic-analysis/spherical-hecke-algebra-satake", "algebra-fields-galois/uniformizer"]
+++

Let \(F\) be a nonarchimedean local field with residue cardinality \(q\), [[algebra-fields-galois/uniformizer|uniformizer]] \(\pi\), and \(K=\mathrm{GL}_n(\mathcal O_F)\). Write \(T_i\) for the [[harmonic-analysis/hecke-operator|Hecke operator]] of \(K\operatorname{diag}(\pi I_i,I_{n-i})K\), with \(\operatorname{vol}(K)=1\). In the constant-term-one normalization the **Hecke polynomial** is
\[
 H(X)=\sum_{i=0}^n(-X)^i q^{i(i-1)/2}T_i
\]
in the [[harmonic-analysis/spherical-hecke-algebra-satake|spherical Hecke algebra]].

## On an eigensystem

Evaluating the coefficients on a [[harmonic-analysis/hecke-eigensystem|Hecke eigensystem]] gives a scalar polynomial. Evaluating \(X\) at a proposed lift parameter gives a linear operator on forms. Its kernel imposes the corresponding local polynomial condition.

## References

- [New/UpperBound/Objects/AuxiliaryPair.lean, heckePolyOnForms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L383)
