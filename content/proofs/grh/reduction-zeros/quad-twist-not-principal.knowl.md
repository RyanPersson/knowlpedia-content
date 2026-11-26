+++
id = "proofs/grh/reduction-zeros/quad-twist-not-principal"
title = "A quadratic twist by an odd prime not dividing the modulus is not principal"
kind = "lemma"
summary = "The product of a character modulo N and the Legendre symbol of an odd prime d prime to N is a non-principal character modulo Nd."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.quadTwist_ne_one", "New.quadTwist_apply"]
lean_files = ["src/Lib/Analytic/EntireLFunction.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\), let \(d\) be a prime, and let \(\chi\chi_K\) denote the [[?lean:New.quadTwist|quadratic twist]] of \(\chi\) by the [[?c:Legendre symbol|Legendre symbol]] \(\chi_K=(\cdot/d)\): the character modulo \(Nd\) obtained by multiplying the characters [[?c:induced Dirichlet character|induced]] by \(\chi\) and by \(\chi_K\).

1. For every integer \(n\), \((\chi\chi_K)(n)=\chi(n)\,(n/d)\).
2. If \(d\ne2\) and \(\gcd(N,d)=1\), then \(\chi\chi_K\) is not [[?c:principal Dirichlet character|principal]].

## Proof

1. If \(\gcd(n,Nd)=1\), both induced characters take the values of the original ones at \(n\), so the product is \(\chi(n)(n/d)\). Otherwise the left side is \(0\), and \(n\) has a common factor with \(N\) or with \(d\), so \(\chi(n)=0\) or \((n/d)=0\).

2. Since \(d\) is odd there is a non-residue \(a\) modulo \(d\), with \((a/d)=-1\). By the [[algebra-rings/chinese-remainder-theorem|Chinese remainder theorem]] there is an integer \(n\) with \(n\equiv1\pmod N\) and \(n\equiv a\pmod d\). By 1, \((\chi\chi_K)(n)=\chi(1)\cdot(-1)=-1\). A principal character takes only the values \(0\) and \(1\). \(\blacksquare\)

## References

1. Lean: `New.quadTwist_apply`, `New.quadTwist_ne_one` in `src/Lib/Analytic/EntireLFunction.lean`.
