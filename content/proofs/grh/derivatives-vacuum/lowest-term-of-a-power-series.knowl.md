+++
id = "proofs/grh/derivatives-vacuum/lowest-term-of-a-power-series"
title = "Lowest term of a power series for a weight"
kind = "definition"
summary = "A monomial c z^m is the lowest term of a power series for a weight if the series agrees with it in all weights at most that of m; lowest terms multiply."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsLowestTerm", "New.IsLowestTerm.mul", "New.IsLowestTerm.prod", "New.IsLowestTerm.pow"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
+++

Let \(R\) be a commutative ring, \(X\) a set of variables, and \(w\colon X\to\mathbb{N}\) a weight; the weight of an exponent \(d\) is \(w(d)=\sum_xw(x)d_x\). For \(f\in R[\![z_x:x\in X]\!]\), an exponent \(m\) and \(c\in R\) (possibly \(0\)), the monomial \(c\,z^m\) is the **lowest term of \(f\) for \(w\)** if for every exponent \(d\) with \(w(d)\le w(m)\) the coefficient of \(z^d\) in \(f\) equals that of \(c\,z^m\) (that is, \(c\) if \(d=m\) and \(0\) otherwise).

## Properties

If \(f\) has lowest term \(c\,z^{D}\) and \(g\) has lowest term \(c'z^{D'}\), then \(fg\) has lowest term \(cc'z^{D+D'}\). Indeed, for \(w(e)\le w(D)+w(D')\) the coefficient of \(z^e\) in \(fg\) is \(\sum_{x+y=e}f_xg_y\); in each term either \(w(x)\le w(D)\) and \(w(y)\le w(D')\), where the coefficients are those of the monomials, or one of \(x,y\) is strictly lighter than \(D\) resp. \(D'\), hence different from it, and the corresponding coefficient vanishes on both sides. By induction the same holds for finite products and powers.

## References

1. Lean: `New.IsLowestTerm`, `New.IsLowestTerm.mul`, `New.IsLowestTerm.prod`, `New.IsLowestTerm.pow` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
