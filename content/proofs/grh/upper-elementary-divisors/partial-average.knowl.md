+++
id = "proofs/grh/upper-elementary-divisors/partial-average"
title = "Contraction of the substitution operator by linear forms; partial averages"
kind = "construction"
summary = "Linear forms, one for each copy of the generic matrix, are applied to the entries of the substitution operator; applying averages in the copies of a set J and scaled evaluation at 1 in the others gives the partial average Av_J."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.tensorDual", "New.tensorDualExcept", "New.FrobeniusCycle.frobContraction", "New.FrobeniusCycle.contractOtherCopies", "New.FrobeniusCycle.partialAverage", "New.FrobeniusCycle.frobContraction_evalAtOne", "New.FrobeniusCycle.partialAverage_empty", "New.tensorDual_monomial", "New.map_tensorDualExcept", "New.tensorDual_evalAtOne"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/AveragingMap.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), and let \(O[X_j]=O[X_{j,b,c}]\) be the polynomial ring in the entries of the copy \(X_j\), \(j\in\mathbb{Z}/N\); so \(O[X_{\bullet}]=\bigotimes_jO[X_j]\).

- For linear forms \(l_j\colon O[X_j]\to O\) (identifying every \(O[X_j]\) with the ring \(O[X]\) of one generic matrix), \(\bigotimes_jl_j\colon O[X_\bullet]\to O\) is the linear form with value \(\prod_jl_j(X_j^{\nu_j})\) on a monomial \(\prod_jX_j^{\nu_j}\). For a copy \(j\), the **partial contraction** \(\bigotimes_{i\ne j}l_i\colon O[X_\bullet]\to O[X]\) sends \(\prod_iX_i^{\nu_i}\) to \(\bigl(\prod_{i\ne j}l_i(X_i^{\nu_i})\bigr)X^{\nu_j}\); for any \(m\colon O[X]\to O\), \(m\circ\bigotimes_{i\ne j}l_i\) is the tensor product with \(l_j\) replaced by \(m\).
- **Contraction.** With the [[proofs/grh/upper-elementary-divisors/substitution-operator|substitution operator]] at the Frobenius factors, \(\mathcal{F}(l)=\mathcal{F}_{n,r,\ell}(l)\in M_{\mathcal{E}(N,k,n)}(O)\) is \(\mathcal{S}(r,\ell,n;\Psi)\) with \(\bigotimes_jl_j\) applied to every entry.
- **One copy left.** For \(g\in\mathrm{GL}_k(W)\), \(h\in O^{\mathcal{E}}\) and \(\beta\in\mathcal{E}\):
\[
\mathcal{C}_j(l;g,h)_\beta=\sum_\gamma(\rho_n(g)h)_\gamma\cdot\Bigl(\bigotimes_{i\ne j}l_i\Bigr)\bigl(\mathcal{S}(r,\ell,n;\Psi^{g})_{\beta,\gamma}\bigr)\in O[X],
\]
the substitution in the frame \(g\) applied to the translate \(\rho_n(g)h\), with the forms applied in all copies but \(j\).
- **Partial average.** Let \(c_0=k^{2}fN\) and \(\mathrm{ev}=p^{c_0}\cdot(\text{evaluation at }1)\). For linear forms \(I_j\) and a set \(J\subseteq\mathbb{Z}/N\): \(\mathrm{Av}_J=\mathcal{F}(l)\) with \(l_j=I_j\) for \(j\in J\) and \(l_j=\mathrm{ev}\) for \(j\notin J\).

## Properties

If all \(l_j=z\cdot(\text{evaluation at }1)\), then \(\mathcal{F}(l)=z^{N}\cdot1\): evaluating all copies at the identity matrix turns every Frobenius factor into \(1\) and the substitution operator into the identity. Hence \(\mathrm{Av}_\emptyset=p^{Nc_0}\cdot1\).

## References

1. Lean: `New.tensorDual`, `New.tensorDualExcept`, `New.FrobeniusCycle.frobContraction`, `New.FrobeniusCycle.contractOtherCopies`, `New.FrobeniusCycle.partialAverage`, `New.FrobeniusCycle.frobContraction_evalAtOne`, `New.FrobeniusCycle.partialAverage_empty`, `New.tensorDual_monomial`, `New.map_tensorDualExcept`, `New.tensorDual_evalAtOne` in `src/New/UpperBound/ElementaryDivisors/AveragingMap.lean`.
