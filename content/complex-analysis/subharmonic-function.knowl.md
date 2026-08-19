+++
id = "complex-analysis/subharmonic-function"
title = "Subharmonic function"
kind = "definition"
summary = "An upper-semicontinuous function dominated at each point by its circular averages."
aliases = ["subharmonicity"]
domains = ["complex-analysis", "potential-theory", "partial-differential-equations"]
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb C\) be open. A function
\(u:U\to[-\infty,\infty\)), not identically \(-\infty\) on any component, is
**subharmonic** if it is
[[complex-analysis/upper-semicontinuous-function|upper-semicontinuous]] and
\[
u(z_0)\le\frac1{2\pi}\int_0^{2\pi}
u(z_0+re^{i\theta})\,d\theta
\]
whenever the closed disk \(\overline{B_r(z_0)}\\) lies in \(U\).

## Distributional characterization

If \(u\in L^1_{\mathrm{loc}}(U)\), subharmonicity is equivalent to
\(\Delta u\ge0\) in the distributional sense. For \(u\in C^2\), this becomes
the pointwise inequality \(\Delta u\ge0\).

## Examples

[[complex-analysis/harmonic-function|Harmonic functions]] satisfy equality in the mean-value formula and are
subharmonic. If \(f\) is holomorphic, then
[[complex-analysis/log-modulus-subharmonic|\(\log|f|\) is subharmonic]], with
its distributional Laplacian recording the zeros of \(f\).

## References

1. Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511623776).
