+++
id = "proofs/grh/reduction-main/sparse-places-exist"
title = "Existence of a large sparse set of places (Behrend's construction)"
kind = "lemma"
summary = "Behrend-type sets of exponents give a set of at least H^n/(n H^2) places of class -1 modulo q0 that is sparse for the primes up to L."
aliases = ["Behrend sets", "exists_three_term_free", "exists_large_isSparse"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eq_of_add_mul_eq_of_sum_sq_eq", "New.exists_three_term_free", "New.Parameters.exists_orderOf_placeClass_eq", "New.Parameters.placeClass_sq_eq", "New.modEq_orderOf_of_div_pow_eq", "New.Parameters.exists_large_isSparse", "New.Parameters.exists_isSparse", "New.Parameters.exists_isSparse_of_ranks"]
lean_files = ["src/New/Reduction/Data/Existence.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(P\) be [[proofs/grh/reduction-main/parameters|parameters]], \(s\ge0\), \(l_0=l_0(s)\), and \(\Phi\cong(\mathbb Z/q_1)^\times\) the [[proofs/grh/reduction-main/field-e-and-its-places|places of \(E_s\)]].

Convention: in the bounds \(H^n/(nH^2)\) below, the quotient is read as \(0\) when \(nH=0\) (as in the Lean source), so that those cases assert nothing about the size.

1. **(Behrend's sets.)** Let \(n,H,L',o\) be natural numbers with \(L'>0\) and \((L'H)^n\le o\). There is a set \(S\subseteq\{0,\dots,o-1\}\) with \(\#S\ge H^n/(nH^2)\) such that for \(e_1,e_2,e_3\in S\) and integers \(\alpha,\alpha'>0\) with \(\alpha+\alpha'\le L'\): \((\alpha+\alpha')e_2\equiv\alpha e_1+\alpha'e_3\pmod o\) implies \(e_1=e_2=e_3\).
2. **(Sparse places.)** If \((2l_0H)^n\le2^s\) and \(2l_0(L+1)<2^s\), there is a set \(T\subseteq\Phi\) of places \(\equiv-1\) modulo \(q_0\), with \(\#T\ge H^n/(nH^2)\), that is [[proofs/grh/reduction-main/sparse-set-of-places|sparse for the primes up to \(L\)]].
3. **(Size in terms of a scale \(W\).)** Let \(n\ge1\), \(1\le W\le2^s\le W^n\), \((2l_0)^n\le W\), \(3l_0n2^n\le W^3\), \(2l_0(L+1)<2^s\). Then there is such a \(T\) with \(\operatorname{towerDeg}(s)\le\#T\cdot W^6\).

## Proof

(1) By [[?c:Behrend's construction|Behrend's pigeonhole]], some sphere \(\{v\in\{0,\dots,H-1\}^n:\sum v_l^2=k\}\) has at least \(H^n/(nH^2)\) points (for \(n,H\ge1\) there are at most \(nH^2\) values of \(k\); for \(nH=0\) the bound is \(0\) and any sphere serves); this is quoted from Mathlib (`Behrend.exists_large_sphere`). Let \(S\) be the set of integers with digit vector \(v\) in base \(L'H\), \(v\) on that sphere; they are \(<(L'H)^n\le o\) and distinct. Given a congruence as stated for digit vectors \(u,v,w\): both \((\alpha+\alpha')v\) and \(\alpha u+\alpha'w\) have all coordinates \(<L'H\), so they are digit vectors of two numbers \(<o\) congruent modulo \(o\), hence equal: \((\alpha+\alpha')v=\alpha u+\alpha'w\). Then \(\alpha\alpha'\sum_l(u_l-w_l)^2=(\alpha+\alpha')(\alpha\lvert u\rvert^2+\alpha'\lvert w\rvert^2)-\lvert(\alpha+\alpha')v\rvert^2=0\) as the three squared lengths are equal; so \(u=w\) and then \(v=u\).

(2) Let \(g=\operatorname{place}(1+3l_0q_0)\). Writing \(q_0=2^vu\) with \(u\) odd, \(v\ge2\), the class of \(g\) modulo \(2^{s+v}\mid q_1\) is \(1+2^v\cdot(\text{odd})\), of order \(2^s\). Apply (1) with \(o=2^s\), \(L'=2l_0\) to get \(S\), and let \(T=\{-g^e:e\in S\}\) (i.e. \(\operatorname{place}(-1)g^e\)). These places are distinct (already modulo \(2^{s+v}\)) and are \(\equiv-1\) modulo every common divisor of \(q_1\) and \(3l_0q_0\), in particular modulo \(q_0\) and modulo \(3l_0=3^c\). Suppose \(\sigma=-g^{e_1},\tau=-g^{e_2},\rho=-g^{e_3}\) with \(\tau/\sigma\equiv\pm\ell^i\), \(\rho/\sigma\equiv\pm\ell^j\) modulo the prime-to-\(\ell\) part of \(q_1\), \(0<i<j<l_0\), \(\ell\le L\). Squaring removes the signs: \((\tau/\sigma)^2\equiv\ell^{2i}\), \((\rho/\sigma)^2\equiv\ell^{2j}\) modulo every divisor of \(q_1\) prime to \(\ell\).

*\(\ell=2\).* Modulo \(3^c\) the ratio \(\tau/\sigma\) is \(1\), so \(4^i\equiv1\pmod{3^c}\); but \(4=1+3\) has order \(3^{c-1}=l_0>i\) modulo \(3^c\). Contradiction.

*\(\ell\) odd.* Modulo \(2^{s+v}\): \((\tau/\sigma)^{2j}\equiv\ell^{2ij}\equiv(\rho/\sigma)^{2i}\), i.e. \(g^{2j(e_2-e_1)}=g^{2i(e_3-e_1)}\) there, so with \(a=j-i>0\): \((2a+2i)e_2\equiv2a\,e_1+2i\,e_3\pmod{2^s}\), with weights \(2a+2i=2j\le2l_0\). By (1), \(e_1=e_2=e_3\), so \(\tau=\sigma\) and \(\ell^{2i}\equiv1\pmod{2^{s+1}}\) (recall \(2^{s+1}\mid q_1\)). For an odd \(\ell>1\) this forces \(2^s\le(\ell+1)\cdot2i\) (`two_pow_le_of_pow_eq_one`: \(v_2(\ell^{2i}-1)=v_2(\ell^2-1)+v_2(i)\)), while \((\ell+1)2i\le(L+1)2l_0<2^s\). Contradiction.

(3) Choose \(H=2^k\) with \(H^n\le2^s/W<(2H)^n\); then \(H\le W\) and \((2l_0H)^n\le W\cdot2^s/W=2^s\). Apply (2): \(\#T\ge H^n/(nH^2)\), and \(\operatorname{towerDeg}(s)=3l_02^s\le3l_0\,2^nH^nW\le\#T\cdot(3l_0n2^n)\,W\,H^2\le\#T\,W^6\).

The proof is marked *outline* because the order computations in \((\mathbb Z/2^k)^\times\) and \((\mathbb Z/3^c)^\times\) and Behrend's counting are quoted (`ZMod.orderOf_one_add_mul_prime_pow`, `ZMod.orderOf_one_add_prime`, `two_pow_le_of_pow_eq_one`, `Behrend.exists_large_sphere`). The corollary `New.Parameters.exists_isSparse_of_ranks` specialises (3) to \(L=kt\) under the size conditions of the data.

## References

1. Lean: the declarations in the front matter, in `src/New/Reduction/Data/Existence.lean`.
2. Sources named in the Lean file head: A. Shapira, *Behrend-type constructions for sets of linear equations*, Acta Arith., 2006; F. A. Behrend, *On sets of integers which contain no three terms in arithmetical progression*, Proc. Nat. Acad. Sci. 32, 1946.
