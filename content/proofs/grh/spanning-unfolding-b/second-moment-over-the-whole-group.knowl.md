+++
id = "proofs/grh/spanning-unfolding-b/second-moment-over-the-whole-group"
title = "The second moment over the whole residue group"
kind = "theorem"
summary = "If the second moments of the blocks form a function of positive type on the residue group and the one at the identity is at most twice the source dimension, their sum over the group is at most (1 + 9 b^(-4)) times the main second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.sum_secondMoment_le", "New.Filling.le_one_add_nine_mul_of_le_add"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a CM field with [[?lean:New.WeilData|Weil data]] and \(S\) an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). For \(s\in\bar G\) let \(\beta(s)=\mathsf{E}(A_{G(E)},\{s\})=\nu^{-2}\sum_{c,c'}\lVert A_{G(E)}(c,s,c')\rVert^2\), with the [[proofs/grh/spanning-unfolding-b/filling-amplitude|amplitude sums]] of all terms for the full side. Suppose that

* \(\beta\) is of positive type: there are vectors \(u_a\) (\(a\in\bar G\)) in a complex inner product space with \(\langle u_a,u_b\rangle=\beta(a^{-1}b)\);
* \(\beta(1)\le2\dim_S\).

Then
\[
\sum_{s\in\bar G}\beta(s)\le\bigl(1+9b^{-4}\bigr)\,\mathcal{M}_{\mathrm{main}} .
\]

## Proof

Write \(F=b^{6k}\) and, for \(Q\subset C_0\) and a family \(d=(d_w)_{w\in C_0}\) of frame vectors, \(m(Q,d)=\sum_{s\in\operatorname{Fix}(Q,d)}\beta(s)\), with the fixer subgroups of [[proofs/grh/spanning-unfolding-b/second-moment-over-a-full-fixer|the lemma on a full fixer]]. Note \(\beta\ge0\) and \(m(\varnothing,d)=\sum_{s\in\bar G}\beta(s)\).

*Maximal choice.* There are finitely many pairs \((Q,d)\); choose one maximising \(F^{\lvert Q\rvert}m(Q,d)\). Comparing with \(Q=\varnothing\),
\[
\sum_{s}\beta(s)\le F^{\lvert Q\rvert}m(Q,d),
\]
so it suffices to prove \(m(Q,d)\le(1+9b^{-4})F^{-\lvert Q\rvert}\mathcal{M}_{\mathrm{main}}\).

*Case \(Q=C_0\).* By [[proofs/grh/spanning-unfolding-b/positive-type-function-is-largest-at-the-identity|the bound for functions of positive type]], \(\beta(s)\le\beta(1)\le2\dim_S\) for all \(s\); the lemma on a full fixer gives \(m(C_0,d)\le F^{-f}\mathcal{M}_{\mathrm{main}}\).

*Case \(Q\ne C_0\).* Pick \(w\in C_0\setminus Q\) and let \(\Gamma=\operatorname{Fix}(Q,d)\). For a frame vector \(d'\) at \(w\), the elements of \(\Gamma\) fixing \(d'\) form \(\operatorname{Fix}(Q\cup\{w\},d[w\mapsto d'])\), so by maximality \(F^{\lvert Q\rvert+1}\sum_{s\in\Gamma,\,s\text{ fixes }d'}\beta(s)\le F^{\lvert Q\rvert}m(Q,d)\), i.e. each such stabiliser carries at most \(F^{-1}m(Q,d)\). By [[proofs/grh/spanning-unfolding-b/non-open-elements-carry-little|the lemma on non-open elements]], the non-open elements of \(\Gamma\) carry at most \(b^{-4}m(Q,d)\). By [[proofs/grh/spanning-unfolding-b/second-moment-over-open-elements-of-a-fixer|the lemma on open elements]] and [[proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group|additivity over elements]], the open elements of \(\Gamma\) carry at most \((1+4b^{-4})F^{-\lvert Q\rvert}\mathcal{M}_{\mathrm{main}}\). Hence, with \(x=b^{-4}\le1/10\) and \(C=F^{-\lvert Q\rvert}\mathcal{M}_{\mathrm{main}}\ge0\),
\[
m\le(1+4x)C+x\,m,\qquad m=m(Q,d).
\]
Then \((1-x)m\le(1+4x)C\le(1-x)(1+9x)C\), because \((1-x)(1+9x)-(1+4x)=x(4-9x)\ge0\); dividing by \(1-x>0\) gives \(m\le(1+9x)C\).

## Remarks

The hypotheses are verified for the blocks of the operators \(P^*sP\) in [[proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators|the second moment theorem]]: positivity of type comes from \(\lVert P^*a^{-1}bP\rVert^2\) being a matrix coefficient of the representation of \(\bar G\) on Hilbert–Schmidt operators.

## References

1. Lean: `New.Filling.sum_secondMoment_le` in `src/New/Spanning/Unfolding/MomentBounds.lean`.
