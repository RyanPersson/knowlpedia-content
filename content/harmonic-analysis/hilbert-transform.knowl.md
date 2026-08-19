+++
id = "harmonic-analysis/hilbert-transform"
title = "Hilbert transform"
kind = "definition"
summary = "The singular integral operator with principal-value kernel 1/(pi x), equivalently the Fourier multiplier -i sign(xi)."
aliases = ["Hilbert singular integral", "conjugate-function operator"]
domains = ["harmonic-analysis", "complex-analysis"]
section_mode = "progressive"
+++

For \(f\) in the [[functional-analysis/schwartz-space|Schwartz space]] on
\(\mathbb R\), its **Hilbert transform**
is
\[
Hf(x)=\frac1\pi\operatorname{p.v.}\!\int_{\mathbb R}
\frac{f(x-t)}{t}\,dt.
\]
The operator extends uniquely to a bounded [[linear-algebra/linear-map|linear map]] on \(L^2(\mathbb R)\).

## Fourier multiplier

With the Fourier convention \(e^{-2\pi i x\xi}\),
\[
\widehat{Hf}(\xi)=-i\,\operatorname{sgn}(\xi)\widehat f(\xi).
\]
This identity proves \(L^2\)-boundedness using the
[[harmonic-analysis/plancherel-theorem-lca|Plancherel theorem]].

## Harmonic conjugates

If \(u\) is the [[harmonic-analysis/poisson-extension-upper-half-plane|Poisson
extension]] of boundary data \(f\), then \(Hf\), up to the chosen sign, is the
boundary value of a harmonic conjugate. Consequently the
[[harmonic-analysis/dirichlet-to-neumann-upper-half-plane|Dirichlet-to-Neumann
operator]] is \(f\mapsto H[-f']\).

## References

1. Loukas Grafakos, *Classical Fourier Analysis*, 3rd ed., Springer, 2014. [DOI record](https://doi.org/10.1007/978-1-4939-1194-3).
