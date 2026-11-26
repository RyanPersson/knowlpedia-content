+++
id = "proofs/grh/reduction-main/field-e-properties"
title = "Properties of the field E: irreducibility, number of places, roots of unity, norms"
kind = "lemma"
summary = "The q1-th cyclotomic polynomial is irreducible over K; E has towerDeg(s)·phi(q0) infinite places, towerDeg(s) of class 1 modulo q0; every root of unity of E is a power of zeta; the product of the chosen embeddings is the norm to K."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.irreducible_cyclotomic", "New.Parameters.algHom_eq_of_mk_eq", "New.Parameters.phi_algebraMap", "New.Parameters.expand_pow_cyclotomic", "New.Parameters.expand_towerDeg_cyclotomic", "New.Parameters.numInfPlaces_E", "New.Parameters.card_placeClass_eq_one_eq_towerDeg", "New.Parameters.isPrimitiveRoot_zeta", "New.Parameters.phi_mul", "New.Parameters.star_zeta", "New.Parameters.galOfPlace_zeta", "New.Parameters.two_pow_dvd_q₁", "New.Parameters.placeOfInt_pow", "New.Parameters.placeMulEquiv_placeOfInt", "New.Parameters.placeClass_placeOfInt", "New.Parameters.galOfPlace_placeOfInt_zeta", "New.Parameters.placeClass_placeOfInt_eq_neg_one_iff", "New.Parameters.exists_zeta_pow_eq", "New.Parameters.norm_zeta_eq_one", "New.Parameters.prod_phi_eq_norm"]
lean_files = ["src/New/Reduction/Data/FieldsAndPlaces.lean"]
proof_status = "full"
+++

**Lemma.** Let \(P=(q_0,d)\) be [[proofs/grh/reduction-main/parameters|parameters]], \(s\ge0\), \(q_1=q_1(s)\), and \(E=K(\zeta)\), \(\Phi\), \(\sigma_v\), \(\Phi_v\), \(\operatorname{place}(\nu)\) as in [[proofs/grh/reduction-main/field-e-and-its-places|the field \(E\) and its places]]. Let \(\varphi\) be [[?c:Euler totient function|Euler's totient function]].

1. The [[algebra-fields-galois/cyclotomic-polynomial|cyclotomic polynomial]] of order \(q_1\) is irreducible over \(K\). \(E\) embeds in \(\mathbb Q(\zeta_{q_1d})\), so \(E/\mathbb Q\) is abelian, and \(E\) is totally complex.
2. Two \(K\)-embeddings \(E\to\mathbb C\) inducing the same infinite place are equal, and \(g\mapsto\) (place of \(\varphi_0\circ g\)) is a bijection from \(\operatorname{Gal}(E/K)\) to \(\Phi\).
3. \(\#\Phi=\varphi(q_1)=\operatorname{towerDeg}(s)\,\varphi(q_0)\), and exactly \(\operatorname{towerDeg}(s)\) places are \(\equiv1\) modulo \(q_0\).
4. \(\Phi_{vv'}(x)=\Phi_v(\sigma_{v'}(x))\); \(\bar\zeta=\zeta^{-1}\); \(\sigma_v(\zeta)=\zeta^{a}\) if \(v\equiv a\) modulo \(q_1\); \(2^{s+1}\mid q_1\).
5. \(\operatorname{place}(\nu)^i=\operatorname{place}(\nu^i)\) for all \(\nu\in\mathbb Z\), \(i\ge0\). If \(\gcd(\nu,q_0)=1\), then \(\operatorname{place}(\nu)\equiv\nu\) modulo \(q_1\) (and modulo every \(m\mid q_1\)), and \(\sigma_{\operatorname{place}(\nu)}(\zeta)=\zeta^\nu\). For every \(\nu\in\mathbb Z\): \(\operatorname{place}(\nu)\equiv-1\) modulo \(q_0\) if and only if \(\nu\equiv-1\pmod{q_0}\).
6. Every root of unity of \(E\) is \(\zeta^k\) for some \(0\le k<q_1\).
7. \(\mathrm N_{E/K}(\zeta)=1\), and for \(y\in E\): \(\prod_{v\in\Phi}\Phi_v(y)=\mathrm N_{E/K}(y)\), viewed in \(\mathbb C\).

## Proof

(1) \(K\) embeds in \(M=\mathbb Q(\zeta_d)\) (the quadratic Gauss sum is a square root of \(-d\), as \(d\equiv3\bmod4\)). The field \(M(\zeta_{q_1})\) contains primitive roots of unity of the coprime orders \(d\) and \(q_1\) ([[proofs/grh/reduction-main/parameters|parameters]], property 5), so it contains \(\mathbb Q(\zeta_{q_1d})\) and has degree at least \(\varphi(d)\varphi(q_1)\) over \(\mathbb Q\), hence at least \(\varphi(q_1)\) over \(M\). So the minimal polynomial of \(\zeta_{q_1}\) over \(M\), a divisor of the cyclotomic polynomial of degree \(\varphi(q_1)\), is that polynomial, which is thus irreducible over \(M\) and a fortiori over \(K\subseteq M\). In \(\mathbb Q(\zeta_{q_1d})\), \(\zeta_{q_1d}^{q_1}\) has order \(d\) (embedding \(K\)) and \(\zeta_{q_1d}^{d}\) has order \(q_1\), giving an embedding of \(E\); subextensions of abelian extensions are abelian. \(E\) is totally complex because it contains the imaginary field \(K\).

(2) If \(\varphi,\psi\) induce the same place then \(\psi=\varphi\) or \(\psi=\bar\varphi\); the latter, restricted to \(K\), would say the inclusion \(K\subset\mathbb C\) is real. So the map is injective. It is surjective because \(\operatorname{Gal}(E/K)\) acts transitively on the infinite places of \(E\) above the unique infinite place of \(K\).

(3) By (2) and (1), \(\#\Phi=\#(\mathbb Z/q_1)^\times=\varphi(q_1)\). Since \(2,3\mid q_0\), substituting \(X^{p^k}\) (\(p\in\{2,3\}\)) into a cyclotomic polynomial of order divisible by \(p\) gives the cyclotomic polynomial of order multiplied by \(p^k\); so \(\Phi_{q_1}(X)=\Phi_{q_0}(X^{\operatorname{towerDeg}(s)})\) and, comparing degrees, \(\varphi(q_1)=\varphi(q_0)\operatorname{towerDeg}(s)\). Reduction \((\mathbb Z/q_1)^\times\to(\mathbb Z/q_0)^\times\) is surjective, so its kernel has \(\varphi(q_1)/\varphi(q_0)\) elements.

(4) The first formula is the definition \(\Phi_v=\varphi_0\circ\sigma_v\) with \(\sigma_{vv'}=\sigma_v\sigma_{v'}\). Under \(\Phi_1\) the root of unity \(\zeta\) has absolute value \(1\), so its complex conjugate is its inverse. The third is the definition of the isomorphism with \((\mathbb Z/q_1)^\times\). \(2\mid q_0\) and \(2^s\mid\operatorname{towerDeg}(s)\).

(5) If \(\nu\) is a unit modulo \(q_1\), both sides are the place of \(\nu^i\); otherwise \(\nu^i\) is a nonunit for \(i\ge1\) and both sides are the identity (for \(i=0\) both are the identity). If \(\gcd(\nu,q_0)=1\) then \(\nu\) is prime to \(2\) and \(3\) and hence to \(q_1=q_0\,3^c2^s\), so \(\operatorname{place}(\nu)\) corresponds to \(\nu\), and \(\zeta^{\nu\bmod q_1}=\zeta^\nu\). For the last claim: if \(\nu\) is a nonunit modulo \(q_1\) the place is the identity, of class \(1\ne-1\) in \(\mathbb Z/q_0\) (property 6 of the parameters with exponent \(0\)), and also \(\nu\not\equiv-1\pmod{q_0}\) since \(-1\) is prime to \(q_0\) and so would make \(\nu\) a unit modulo \(q_1\). If \(\nu\) is a unit modulo \(q_1\), the class is \(\nu\bmod q_0\).

(6) Let \(y\) have finite order. Via \(E\hookrightarrow\mathbb Q(\zeta_{q_1d})\), whose roots of unity have order dividing \(q_1d\) (this number is even), \(y^{q_1d}=1\). If \(y^{q_1}\ne1\), then \(y^{q_1}\) has prime order \(d\); \(E\) then contains primitive roots of unity of coprime orders \(q_1\) and \(d\), so \(\varphi(d)\varphi(q_1)\le[E:\mathbb Q]=2\varphi(q_1)\) and \(d-1\le2\), contradicting \(d>64\). Hence \(y^{q_1}=1\) and \(y\) is a power of the primitive root \(\zeta\).

(7) For a primitive \(n\)-th root of unity with \(n>2\) whose cyclotomic polynomial is irreducible over the base, the norm is the constant term \(\Phi_n(0)=1\) (the degree being even); here \(n=q_1\ge18480\). For the second claim, \(\mathrm N_{E/K}(y)=\prod_{g\in\operatorname{Gal}(E/K)}g(y)=\prod_v\sigma_v(y)\) in \(E\); apply \(\Phi_1=\varphi_0\), which fixes \(K\) and sends \(\sigma_v(y)\) to \(\Phi_v(y)\).

## References

1. Lean: the declarations listed in the front matter, in `src/New/Reduction/Data/FieldsAndPlaces.lean`. The degree bound for coprime roots of unity is `New.totient_mul_totient_le_finrank`, and the embedding of \(K\) into \(\mathbb Q(\zeta_d)\) is `QuadField.embOfPrimitiveRoot`, both in `src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean`.
