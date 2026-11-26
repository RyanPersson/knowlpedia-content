+++
id = "proofs/grh/upper-elementary-divisors/substitution-respects-gauss-filtration"
title = "Substitution respects weights, with a gain on the difference"
kind = "lemma"
summary = "If two substitutions send each variable into its weight level and differ by a gain of 1/20, then their values on a polynomial of Gauss level t differ in level t + 1/20."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.algHom_sub_mem_of_mem_gaussFiltration"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/RootLemma.lean"]
proof_status = "full"
+++

**Lemma.** Let \(A\) be a commutative \(R\)-algebra, \(F\) a family of additive subgroups of \(R\) indexed by \(\mathbb{R}\), \(G\) a [[proofs/grh/upper-elementary-divisors/gauss-filtration|real filtration]] of \(A\) such that the structure map sends \(F_s\) into \(G_s\) for all \(s\), and \(c\) real weights of the variables \(x_i\), \(i\in\sigma\). Let \(\chi,\psi\colon R[x_i]\to A\) be \(R\)-algebra homomorphisms with \(\chi(x_i)\in G_{c_i}\) and \(\psi(x_i)-\chi(x_i)\in G_{c_i+1/20}\) for all \(i\). If \(f\in\mathrm{G}_t(F,c)\), then \(\psi(f)\in G_t\) and \(\psi(f)-\chi(f)\in G_{t+1/20}\).

## Proof

Note \(\psi(x_i)\in G_{c_i}\) too, since \(G_{c_i+1/20}\subseteq G_{c_i}\). Induct on the structure of \(f\) (constants; sums of a monomial not in the support and a polynomial; products \(g\,x_i\)), for all \(t\) simultaneously. For a constant \(x\in F_t\) both claims hold since \(\psi(x)=\chi(x)\) is its image in \(G_t\). The Gauss level is checked coefficientwise, so if \(f=m+f'\) with the monomial \(m\) outside the support of \(f'\), both lie in \(\mathrm{G}_t\), and the claims add. If \(f=g\,x_i\in\mathrm{G}_t\), then \(g\in\mathrm{G}_{t-c_i}\), so by induction \(\psi(g)\in G_{t-c_i}\) and \(\psi(g)-\chi(g)\in G_{t-c_i+1/20}\). Then \(\psi(f)=\psi(g)\psi(x_i)\in G_t\) and
\[
\psi(f)-\chi(f)=(\psi(g)-\chi(g))\,\chi(x_i)+\psi(g)\,(\psi(x_i)-\chi(x_i))\in G_{t+1/20}.\qquad\square
\]

## References

1. Lean: `New.algHom_sub_mem_of_mem_gaussFiltration` in `src/New/UpperBound/ElementaryDivisors/RootLemma.lean`.
