+++
id = "proofs/grh/reduction-main/height-calculus"
title = "Calculus of heights: monotonicity, products, powers"
kind = "lemma"
summary = "Height bounds are monotone, add under pointwise products, scale under powers, and follow from l-adic bounds with exponents of any sign."
aliases = ["heights add in products"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HeightLe.mono", "New.HeightLe.rpow_mul", "New.HeightLe.of_mul_le", "New.HeightLe.of_le", "New.HeightLe.inv_const", "New.HeightLe.mul", "New.HeightLe.prod", "New.HeightLe.pow"]
lean_files = ["src/New/Reduction/Lattices/Heights.lean"]
proof_status = "full"
+++

**Lemma.** Let \(y,y'\) be families of complex numbers indexed by the [[proofs/grh/reduction-main/prime-padic-iso|finite places \(\iota\mid\ell\) of \(\mathbb C\)]], and \(c,c'\in\mathbb R\). We use the relation [[proofs/grh/reduction-main/height-bound|\(\operatorname{ht}(y)\le c\)]].

1. **(Monotonicity.)** If \(\operatorname{ht}(y)\le c\), \(c\le c'\), and \(\lvert y'_\iota\rvert_\iota\le\lvert y_\iota\rvert_\iota\) for all \(\iota\), then \(\operatorname{ht}(y')\le c'\).
2. **(Units.)** If \(\operatorname{ht}(y)\le c\le c'\), and for each \(\iota\mid\ell\) a natural number \(N_\iota\) prime to \(\ell\) and a rational number \(e_\iota\) are given, then the family \(N_\iota^{\,e_\iota}y_\iota\) (positive real power) has height at most \(c'\).
3. **(Exponents of any sign.)** Let \(H\ne0\), \(\alpha\in\mathbb R\) and real numbers \(e_\ell\) (of any sign) satisfy: \(\lvert\sigma H\rvert\le e^\alpha\) for all \(\sigma\in\operatorname{Aut}(\mathbb C)\); \(\lvert Hy_\iota\rvert_\iota\le\exp(e_\ell)\) for all \(\iota\mid\ell\); and \(\alpha+\sum_{\ell\in T}e_\ell\le c\) for every finite set \(T\) of primes. Then \(\operatorname{ht}(y)\le c\).
4. **(Purely \(\ell\)-adic bounds.)** If \(\lvert y_\iota\rvert_\iota\le\exp(e_\ell)\) for all \(\iota\mid\ell\) and \(\sum_{\ell\in T}e_\ell\le c\) for every finite set \(T\) of primes, then \(\operatorname{ht}(y)\le c\).
5. **(Inverse of a constant.)** If \(H\ne0\) and \(\lvert\sigma H\rvert\le e^{c}\) for all \(\sigma\in\operatorname{Aut}(\mathbb C)\), then the constant family \(H^{-1}\) has height at most \(c\).
6. **(Products.)** If \(\operatorname{ht}(y)\le c\) and \(\operatorname{ht}(y')\le c'\), then \(\operatorname{ht}(yy')\le c+c'\) for the pointwise product. More generally, for a finite family \(y^{(i)}\), \(i\in s\), with \(\operatorname{ht}(y^{(i)})\le c_i\): \(\operatorname{ht}\bigl(\prod_{i\in s}y^{(i)}\bigr)\le\sum_{i\in s}c_i\).
7. **(Powers.)** If \(\operatorname{ht}(y)\le c\) and \(n\ge0\) is an integer, then \(\operatorname{ht}(y^n)\le nc\).

## Proof

Throughout, \((H,\alpha,(h_\ell))\) denotes data witnessing \(\operatorname{ht}(y)\le c\).

(1) The same \(H,\alpha,h\) serve: \(\lvert Hy'_\iota\rvert_\iota=\lvert H\rvert_\iota\lvert y'_\iota\rvert_\iota\le\lvert Hy_\iota\rvert_\iota\le\ell^{h_\ell}\), and the sums are at most \(c\le c'\).

(2) Write \(e_\iota=u/w\) in lowest terms, \(w\ge1\). The real number \(r=N_\iota^{e_\iota}\) satisfies \(r^{w}=N_\iota^{u}\), and \(\lvert N_\iota\rvert_\iota=1\) because \(N_\iota\) is a nonzero integer prime to \(\ell\). Hence \(\lvert r\rvert_\iota^{w}=1\), so \(\lvert r\rvert_\iota=1\) and \(\lvert ry_\iota\rvert_\iota=\lvert y_\iota\rvert_\iota\). Apply (1).

(3) Put \(h_\ell=\max(e_\ell,0)/\log\ell\) for primes \(\ell\) (and anything nonnegative otherwise). Then \(\ell^{h_\ell}=\exp(\max(e_\ell,0))\ge\exp(e_\ell)\ge\lvert Hy_\iota\rvert_\iota\). For a finite set \(T\) of primes, \(\alpha+\sum_{\ell\in T}h_\ell\log\ell=\alpha+\sum_{\ell\in T,\,e_\ell\ge0}e_\ell\le c\), by the hypothesis applied to the finite set \(\{\ell\in T:e_\ell\ge0\}\).

(4) This is (3) with \(H=1\), \(\alpha=0\).

(5) This is (3) for the constant family \(H^{-1}\) with multiplier \(H\), \(\alpha=c\) and \(e_\ell=0\): \(\lvert H\cdot H^{-1}\rvert_\iota=1\).

(6) Let \((H',\alpha',h')\) witness \(\operatorname{ht}(y')\le c'\). Take the multiplier \(HH'\ne0\), the number \(\alpha+\alpha'\) and the exponents \(h_\ell+h'_\ell\ge0\): \(\lvert\sigma(HH')\rvert\le e^{\alpha}e^{\alpha'}\); \(\lvert HH'y_\iota y'_\iota\rvert_\iota=\lvert Hy_\iota\rvert_\iota\lvert H'y'_\iota\rvert_\iota\le\ell^{h_\ell+h'_\ell}\); and the sums add. The case of a finite family follows by induction, the empty product being the constant family \(1\), of height at most \(0\) by (4).

(7) This is (6) for \(n\) copies of \(y\).

## References

1. Lean: `New.HeightLe.mono`, `.rpow_mul`, `.of_mul_le`, `.of_le`, `.inv_const`, `.mul`, `.prod`, `.pow` in `src/New/Reduction/Lattices/Heights.lean`.
