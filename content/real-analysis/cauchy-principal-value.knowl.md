+++
id = "real-analysis/cauchy-principal-value"
title = "Cauchy principal value"
kind = "definition"
summary = "A symmetric limiting prescription for certain singular or non-absolutely convergent integrals."
aliases = ["principal value integral", "p.v. integral", "PV integral"]
domains = ["real-analysis", "harmonic-analysis"]
section_mode = "progressive"
+++

For a function \(g\) singular at \(t=0\), its **Cauchy principal value** is
\[
\operatorname{p.v.}\!\int_{\mathbb R}g(t)\,dt
=\lim_{\varepsilon\downarrow0}
\int_{|t|>\varepsilon}g(t)\,dt,
\]
provided the limit exists, with any additional truncation at infinity stated
explicitly. The symmetric deletion around the singularity permits
cancellation that an ordinary improper integral may not have.

## Distributional interpretation

The prescription defines the [[functional-analysis/tempered-distribution|tempered distribution]]
\(\operatorname{p.v.}(1/t)\) by
\[
\left\langle\operatorname{p.v.}\frac1t,\varphi\right\rangle
=\lim_{\varepsilon\downarrow0}\int_{|t|>\varepsilon}
\frac{\varphi(t)}{t}\,dt.
\]
It is the kernel underlying the [[harmonic-analysis/hilbert-transform|Hilbert
transform]].

## Warning

Principal value convergence is weaker than absolute convergence and depends
on the prescribed symmetric truncation. It must not be silently replaced by a
[[measure-theory/lebesgue-integral|Lebesgue integral]].

## References

1. Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton University Press, 1970. [Publisher record](https://press.princeton.edu/books/paperback/9780691080796/singular-integrals-and-differentiability-properties-of-functions).
