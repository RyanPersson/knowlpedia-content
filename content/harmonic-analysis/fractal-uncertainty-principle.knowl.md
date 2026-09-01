+++
id = "harmonic-analysis/fractal-uncertainty-principle"
title = "Fractal uncertainty principle"
kind = "definition"
summary = "A power-saving estimate forbidding simultaneous concentration on porous or fractal sets in physical and Fourier space."
aliases = ["FUP", "fractal uncertainty estimate"]
domains = ["harmonic-analysis", "mathematical-physics", "quantum-chaos"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **fractal uncertainty principle** is a quantitative estimate asserting that
a function cannot concentrate simultaneously near a fractal set \(X\) in
physical space and a fractal set \(Y\) in Fourier space. In the scaled
Euclidean form used here, it is an implication
\[
\operatorname{supp}\widehat f\subseteq Y
\quad\Longrightarrow\quad
\|f\mathbf1_X\|_{L^2}\le C h^\beta\|f\|_{L^2},
\]
where \(0<h\ll1\), \(C<\infty\), and the gain exponent \(\beta>0\) are uniform
over sets satisfying the stated multiscale hypotheses.

## Why the power saving matters

An estimate obtained only from the volumes of \(X\) and \(Y\) is called the
trivial uncertainty bound. An FUP supplies an additional positive power of
\(h\), or remains nontrivial in a regime where the volume bound gives no
decay. Its force comes from holes occurring at many scales rather than from
small measure at just one scale.

## Higher-dimensional geometry

In dimensions at least two, [[analysis/porosity-on-balls|ball porosity]] of
both sets is insufficient because physical and Fourier concentration can live
on orthogonal subspaces. The
[[harmonic-analysis/higher-dimensional-line-porous-fup|line-porous FUP]] rules
out that obstruction by requiring [[analysis/porosity-on-lines|line porosity]]
on the Fourier-side set.

## Quantum-chaos role

Fractal sets arise from trajectories that avoid an observation region in a
chaotic flow. The FUP turns their geometric holes into observability,
eigenfunction mass bounds, or resonance gaps.

## References

1. Semyon Dyatlov, “An introduction to fractal uncertainty principle,” *Journal of Mathematical Physics* 60 (2019), 081505. [DOI record](https://doi.org/10.1063/1.5093938).
2. Jean Bourgain and Semyon Dyatlov, “Spectral gaps without the pressure condition,” *Annals of Mathematics* 187 (2018), 825–867. [DOI record](https://doi.org/10.4007/annals.2018.187.3.5).
