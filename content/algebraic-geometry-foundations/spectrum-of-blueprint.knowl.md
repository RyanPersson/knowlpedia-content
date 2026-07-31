+++
id = "algebraic-geometry-foundations/spectrum-of-blueprint"
title = "Spectrum of a blueprint"
kind = "construction"
summary = "The prime spectrum of a blueprint with its Zariski topology and structure sheaf."
aliases = ["blueprint spectrum", "Spec of a blueprint", "blue spectrum"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
+++

For a [[algebraic-geometry-foundations/blueprint|blueprint]] \(B\), its **spectrum**
\[
\operatorname{Spec}B
\]
is the set of prime [[algebraic-geometry-foundations/k-ideal-of-a-blueprint|\(k\)-ideals]] of \(B\). It has the Zariski topology whose basic opens are
\[
U_h=\{\mathfrak p\mid h\notin\mathfrak p\}
\]
for \(h\in B\), together with a structure sheaf \(\mathcal O_{\operatorname{Spec}B}\) locally modeled on [[algebraic-geometry-foundations/localization-of-blueprint|blueprint localizations]].

This is the prime-\(k\)-ideal spectrum used in the original theory of blue schemes. Other blueprint geometries also use congruence spectra, which need not have the same points.

## Basic affine calculation

The structure sheaf satisfies
\[
\Gamma(U_h,\mathcal O_{\operatorname{Spec}B})\simeq B[h^{-1}]
\]
for basic opens under the standard blueprint-spectrum construction. In particular, \(\operatorname{Spec}B\) is the [[algebraic-geometry-foundations/affine-blue-scheme|affine blue scheme]] represented by \(B\).

## Convention warning

“Spectrum of a blueprint” is not a unique phrase across every later variant of blueprint geometry. This knowl records Lorscheid's prime-\(k\)-ideal spectrum underlying blue schemes. [[algebraic-geometry-foundations/ordered-blue-scheme|Ordered blue schemes]] use the corresponding ordered-blueprint theory.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I*, §§2–3](https://arxiv.org/abs/1103.1745).
