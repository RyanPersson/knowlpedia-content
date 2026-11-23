+++
id = "analytic-number-theory/finite-fourier-inversion"
title = "Fourier inversion on a finite abelian group"
kind = "identity"
summary = "A function on a finite abelian group is recovered from its coefficients against all group characters."
aliases = ["finite Fourier identity", "finite Fourier transform"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-representation-theory/character-orthogonality", "harmonic-analysis/pontryagin-dual"]
+++

Let \(G\) be a finite abelian group and \(\widehat G\) its [[harmonic-analysis/pontryagin-dual|group of complex characters]]. For \(f:G\to\mathbb C\), define \(\widehat f(\chi)=|G|^{-1}\sum_{g\in G} f(g)\overline{\chi(g)}\). **Finite Fourier inversion** says
\[
f(h)=\sum_{\chi\in\widehat G}\widehat f(\chi)\chi(h).
\]
Indeed, [[algebra-representation-theory/character-orthogonality|character orthogonality]] gives \(\sum_{\chi}\overline{\chi(g)}\chi(h)=|G|\) if \(h=g\) and zero otherwise.

## Selecting inert primes

If \(G=\{1,c\}\) and \(\chi(c)=-1\), then \(\mathbf 1_{\{c\}}(g)=(1-\chi(g))/2\). At an unramified prime in a quadratic field, inserting Frobenius for \(g\) turns this identity into the indicator that the prime is [[arithmetic-geometry/inert-prime|inert]]. The longer [[analytic-number-theory/prime-sum-balance|balance identity]] uses the character expansion on a larger field.
