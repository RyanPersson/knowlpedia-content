+++
id = "proofs/grh/reduction-zeros/jacobi-symbol-sums"
title = "Sums of Jacobi symbols with non-square odd modulus"
kind = "lemma"
summary = "The Jacobi symbol modulo b is a Dirichlet character, non-principal for odd non-square b; so its partial sums are bounded by Pólya–Vinogradov."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_dirichletCharacter_eq_jacobiSym", "New.dirichletCharacter_jacobiSym_ne_one", "New.norm_sum_jacobiSym_le", "New.norm_sum_jacobiSym_ordCompl_le", "New.norm_jacobiSym_le_one", "New.norm_mul_jacobiSym_le_one"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Lemma.** Let \((v/m)\) denote the [[?c:Jacobi symbol|Jacobi symbol]], extended to all integers \(m\ge1\) as the product over the prime factors \(p\) of \(m\), with multiplicity, of the Legendre symbols \((v/p)\), where for \(p=2\) the symbol \((v/2)\) is the quadratic character of \(\mathbb{Z}/2\): \(1\) for odd \(v\) and \(0\) for even \(v\). (This is not the Kronecker symbol; for odd \(m\) it is the usual Jacobi symbol, and only odd \(m\) occur in parts 2–4.) Also, for an integer \(n\ge1\) let \(n^{\circ}\) be its odd part (\(n=2^{e}n^{\circ}\), \(n^\circ\) odd).

1. For every integer \(b\ge1\) there is a complex [[?c:Dirichlet character|Dirichlet character]] \(\psi_b\) modulo \(b\) with \(\psi_b(v)=(v/b)\) for all integers \(v\).
2. If \(m\) is odd and not a square, such a character is not principal.
3. If \(m\) is odd and not a square, then for all \(X\ge0\): \(\bigl\lvert\sum_{1\le v\le X}(-v/m)\bigr\rvert\le2\sqrt m\,(1+\log m)\).
4. If \(\delta>0\), \(n\ge1\) and \(n^{\circ}\) is not a square, then \(\bigl\lvert\sum_{1\le v\le X}(-v/n^{\circ})\bigr\rvert\le2(1+2/\delta)\,n^{1/2+\delta/2}\).

## Proof

1. Induction on the number of prime factors: for \(b=1\) take the trivial character; for \(pb\) take the [[?lean:New.quadTwist|twist]] of \(\psi_b\) by \((\cdot/p)\), whose value at \(v\) is \(\psi_b(v)(v/p)=(v/pb)\) ([[proofs/grh/reduction-zeros/quad-twist-not-principal|values of the twist]]).

2. Write \(m=c^{2}a\) with \(a\) squarefree; \(a\ne1\), so \(a=pb\) with \(p\) an odd prime and \(\gcd(b,p)=1\). Suppose the character \(\psi\) modulo \(m\) with values \((v/m)\) is principal. For \(v\) prime to \(m\): \(1=(v/m)=(v/c)^{2}(v/p)(v/b)=(v/p)(v/b)\). So the twist of \(\psi_b\) by \((\cdot/p)\), a character modulo \(bp\), takes the value \(1\) at all integers prime to \(m\), hence induces the principal character modulo \(m\), hence is principal. This contradicts [[proofs/grh/reduction-zeros/quad-twist-not-principal|the lemma on twists]].

3. \((-v/m)=\psi(-1)\psi(v)\) with \(\lvert\psi(-1)\rvert=1\); apply the [[proofs/grh/reduction-zeros/polya-vinogradov|Pólya–Vinogradov inequality]] to \(\psi\).

4. By 3 with \(m=n^{\circ}\le n\): the sum is at most \(2\sqrt n(1+\log n)\), and \(1+\log n\le(1+2/\delta)n^{\delta/2}\) because \(\log n\le n^{\delta/2}/(\delta/2)\). \(\blacksquare\)

## References

1. Lean: the declarations named in the front matter, in `src/Lib/Analytic/QuadraticTwist.lean`.
