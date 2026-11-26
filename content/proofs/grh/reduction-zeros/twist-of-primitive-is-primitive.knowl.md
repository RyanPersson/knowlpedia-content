+++
id = "proofs/grh/reduction-zeros/twist-of-primitive-is-primitive"
title = "A quadratic twist of a primitive character is primitive"
kind = "lemma"
summary = "The twist of a primitive character modulo M by the Legendre symbol of an odd prime d not dividing M is primitive modulo Md."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.isPrimitive_quadTwist"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\psi\) be a [[?c:primitive Dirichlet character|primitive]] complex Dirichlet character modulo \(M\ge1\) and \(d\) an odd prime with \(\gcd(M,d)=1\). Then the [[?lean:New.quadTwist|twist]] \(\psi\chi_K\) by \(\chi_K=(\cdot/d)\) is primitive modulo \(Md\).

## Proof

Let \(n\) be the [[?c:conductor of a Dirichlet character|conductor]] of \(\psi\chi_K\); it divides \(Md\). The character \(\chi_K\) modulo the prime \(d\) is not principal (\(d\) odd), so its conductor is \(d\); the conductor of \(\psi\) is \(M\). The conductor of a product divides the least common multiple of the conductors, and a character and its inverse have the same conductor. Since \(\psi=(\psi\chi_K)\chi_K^{-1}\) (as characters modulo \(Md\), up to induction), \(M\mid nd\), hence \(M\mid n\). Likewise \(\chi_K=(\psi\chi_K)\psi^{-1}\) gives \(d\mid nM\), hence \(d\mid n\). So \(Md\mid n\) and \(n=Md\). \(\blacksquare\)

## References

1. Lean: `New.isPrimitive_quadTwist` in `src/Lib/Analytic/QuadraticTwist.lean`.
