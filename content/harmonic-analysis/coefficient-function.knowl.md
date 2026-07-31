+++
id = "harmonic-analysis/coefficient-function"
title = "Matrix coefficient of a unitary representation"
kind = "definition"
summary = "A scalar-valued function obtained by pairing the orbit of one Hilbert-space vector with another."
aliases = ["coefficient function", "matrix coefficient"]
domains = ["harmonic-analysis", "lie-groups"]
section_mode = "progressive"
+++

Let \(\pi:G\to U(\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] on a complex [[linear-algebra/hilbert-space|Hilbert space]], whose [[linear-algebra/inner-product|inner product]] is linear in the first variable. For \(\xi,\eta\in\mathcal H\), the **matrix coefficient** determined by \(\xi\) and \(\eta\) is
\[
c_{\xi,\eta}(g)=\langle \pi(g)\xi,\eta\rangle,\qquad g\in G.
\]
It is a bounded continuous complex-valued function, with \(\lvert c_{\xi,\eta}(g)\rvert\leq \|\xi\|\,\|\eta\|\). A coefficient with \(\xi=\eta\) is called diagonal; it is [[harmonic-analysis/positive-definite-function|positive-definite]].

## Basic properties

Coefficients are linear in \(\xi\) and conjugate-linear in \(\eta\) under the stated convention. Translation of the argument produces another coefficient: for \(x\in G\),
\[
c_{\xi,\eta}(xg)=c_{\xi,\pi(x^{-1})\eta}(g),
\qquad
c_{\xi,\eta}(gx)=c_{\pi(x)\xi,\eta}(g).
\]
Thus the coefficient space attached to a representation is stable under left and [[lie-groups/right-translation|right translation]]. The estimate in the core is the [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] together with unitarity.

## Structural role

Diagonal coefficients record the positive kernel associated with a vector, while polarization recovers every \(c_{\xi,\eta}\) from diagonal coefficients. Conversely, the [[harmonic-analysis/gns-construction-positive-definite-function|GNS construction for positive-definite functions]] realizes every continuous positive-definite function as a diagonal coefficient of a cyclic unitary representation. This makes coefficients the scalar observables used to compare representations without choosing operator coordinates [Folland, §3.1–3.3].

## Conventions and scope

If the inner product is taken linear in the second variable, the displayed formula remains meaningful but its linearity and the standard positive-definiteness convention must be adjusted consistently. The term **representative function** is often restricted to coefficients of finite-dimensional representations, so it should not be treated as an unrestricted synonym here.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §§3.1–3.3 on unitary representations, coefficients, and functions of positive type.
