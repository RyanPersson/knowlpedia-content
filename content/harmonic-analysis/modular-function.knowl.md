+++
id = "harmonic-analysis/modular-function"
title = "Modular function of a locally compact group"
kind = "definition"
summary = "The positive continuous homomorphism measuring how a left Haar measure scales under right translation."
aliases = ["modular homomorphism", "Haar modular function", "Delta_G"]
domains = ["harmonic-analysis", "measure-theory", "topology"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "algebra-groups/group-homomorphism", "lie-groups/right-translation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and let \(\mu\) be a left [[harmonic-analysis/haar-measure|Haar measure]]. The **modular function** is the unique map
\[
\Delta_G:G\longrightarrow \mathbb R_{>0}
\]
satisfying
\[
\int_G f(xg)\,d\mu(x)
=
\Delta_G(g)^{-1}\int_G f(x)\,d\mu(x)
\]
for every \(g\in G\) and every compactly supported continuous \(f\). It is a continuous [[algebra-groups/group-homomorphism|group homomorphism]] and does not depend on rescaling \(\mu\). Thus \(\Delta_G\) measures precisely the failure of a left Haar measure to be invariant under [[lie-groups/right-translation|right translations]]. The inverse in the displayed convention is important; some references define the reciprocal modular function.

## Measure-theoretic meaning

For fixed \(g\), right translation sends \(\mu\) to another left Haar measure, so uniqueness of Haar measure produces a positive scale factor. Those factors multiply under composition of right translations, which gives the homomorphism law
\[
\Delta_G(gh)=\Delta_G(g)\Delta_G(h).
\]
Inversion transports a left Haar measure to a right Haar measure. The modular function compares these two invariant-measure conventions.

## Unimodularity

The group \(G\) is [[harmonic-analysis/unimodular-group|unimodular]] exactly when \(\Delta_G\equiv 1\), equivalently when a left Haar measure is also right invariant. Abelian, compact, and discrete groups are unimodular. Nontrivial [[algebra-groups/semidirect-product|semidirect products]] supply many non-unimodular examples.

## Role in harmonic analysis

The modular factor is required in the [[harmonic-analysis/convolution-involution|involution on a group convolution algebra]] and in unitary formulas involving right translation. It also enters [[algebra-representation-theory/induced-representation|induced representations]] and [[lie-groups/normalized-parabolic-induction|normalized parabolic induction]]. Ignoring it silently imports the unimodular case into formulas that are otherwise false.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Routledge publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218). Relevant: §2.4, “The Modular Function.”
2. Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [Springer DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: invariant functionals, translations, and convolution.
