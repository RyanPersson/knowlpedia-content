+++
id = "proofs/grh/derivatives-divisibility/places-above-split-primes"
title = "Places of E above a prime congruent to 1 modulo q1 d"
kind = "proposition"
summary = "For a prime p congruent to 1 modulo q1 d and an integer a of E with a times its conjugate equal to p c, c prime to p, the places above p dividing a have norm p, divide a exactly once, and are in bijection with the infinite places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.nonempty_infinitePlace_equiv_finPlace", "New.Parameters.smul_eq_self_iff_eq_one", "New.Parameters.q_eq_of_modEq_one", "New.Parameters.star_mem_iff_notMem", "New.Parameters.intValuation_eq_of_mul_star", "New.Parameters.eq_of_smul_eq_or_smul_eq_star"]
lean_files = ["src/New/Derivatives/Field/WeilData.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E=K(\zeta)\) be as in the [[proofs/grh/derivatives-divisibility/field-setting|field \(E\)]], \(p\) a prime with \(p\equiv1\pmod{q_1d}\), and \(a\in\mathcal{O}_E\) with \(a\bar a=p\,c\) for a natural number \(c\) prime to \(p\). Let \(w\) be a finite place of \(E\) above \(p\).

1. \(Nw=p\); and \(v\bullet w=w\) only for \(v=1\).
2. Exactly one of \(a\), \(\bar a\) lies in \(w\); if \(a\in w\), then \(v_w(a)=1\).
3. If \(v\bullet w\) equals \(u\bullet w\) or \(\overline{u\bullet w}\), for \(u,v\in\Phi\), then \(u=v\).
4. There is a bijection between \(\Phi\) and the set of finite places of \(E\) that contain both \(a\) and \(p\).

## Proof

1 is the corollary for primes \(\equiv1\) of the [[proofs/grh/derivatives-divisibility/decomposition-of-primes-in-e|decomposition of primes in \(E\)]].

2. \(a\bar a=pc\in w\), so one of them lies in the prime \(w\). If both did, \(pc\in w^2\); as \(w\) is prime and \(c\notin w\) (\(c\) is prime to \(p\in w\)), this forces \(p\in w^2\), contradicting that \(p\) is unramified. If \(a\in w\), then \(\bar a\) and \(c\) are units at \(w\), so \(v_w(a)=v_w(pc)=v_w(p)=1\).

3. \((u^{-1}v)\bullet(u\bullet w)=v\bullet w\), and \(u\bullet w\) lies above \(p\). The Frobenius element is trivial, so no element of \(\Phi\) sends \(u\bullet w\) to its conjugate, and only \(1\) fixes it.

4. Fix \(w_0\) above \(p\). By 2 applied to \(v\bullet w_0\) (and \(\bar a\in\bar w\iff a\in w\)), exactly one of \(v\bullet w_0\), \(\overline{v\bullet w_0}\) contains \(a\); send \(v\) to it. The map is injective by 3 and surjective by transitivity (part 1 of the decomposition theorem). \(\blacksquare\)

## References

1. Lean: `New.Parameters.nonempty_infinitePlace_equiv_finPlace` and the lemmas before it in `src/New/Derivatives/Field/WeilData.lean`.
