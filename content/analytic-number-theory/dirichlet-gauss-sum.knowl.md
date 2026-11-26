+++
id = "analytic-number-theory/dirichlet-gauss-sum"
title = "Gauss sum of a Dirichlet character"
kind = "definition"
summary = "The first additive Fourier coefficient, with positive exponential, of a Dirichlet character."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character","analytic-number-theory/primitive-dirichlet-character","analytic-number-theory/induced-dirichlet-character","real-analysis/geometric-series","analytic-number-theory/euler-totient"]
+++

For a [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\bmod q\), set \(e_q(u)=\exp(2\pi i u/q)\). Its **Gauss sum** is
\[
\tau(\chi)=\sum_{a\bmod q}\chi(a)e_q(a).
\]

## Fourier coefficients for a primitive character

If \(\chi\) is [[analytic-number-theory/primitive-dirichlet-character|primitive]], then \(S_m=\sum_{a\bmod q}\chi(a)e_q(ma)=\overline{\chi(m)}\,\tau(\chi)\) for every integer \(m\), and \(|\tau(\chi)|=\sqrt q\).

For \(m\) a unit modulo \(q\), multiplication by \(m\) permutes the classes and \(\chi(m)^{-1}=\overline{\chi(m)}\). If \(g=\gcd(m,q)>1\), put \(f=q/g\). The map on units modulo \(q\) to units modulo \(f\) is surjective, as in [[analytic-number-theory/induced-dirichlet-character|induction of a character]]. Primitivity gives an element \(b\) of its kernel with \(\chi(b)\ne1\), since otherwise \(\chi\) would descend to modulus \(f\). Because \(mb\equiv m\bmod q\), replacing \(a\) by \(ba\) yields \(S_m=\chi(b)S_m\) and hence \(S_m=0\).

Expand \(\sum_{m\bmod q}|S_m|^2\) and use \(\sum_{m\bmod q}e_q(m(a-b))=q\) when \(a=b\bmod q\) and zero otherwise, by the finite [[real-analysis/geometric-series|geometric sum]]. This gives \(q\sum_a|\chi(a)|^2=q\varphi(q)\). The coefficient formula gives \(\varphi(q)|\tau(\chi)|^2\) for the same sum. The [[analytic-number-theory/euler-totient|totient]] is positive, so \(|\tau(\chi)|^2=q\).

## References

- [Primitive Gauss sums in the theta transformation](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L399)
