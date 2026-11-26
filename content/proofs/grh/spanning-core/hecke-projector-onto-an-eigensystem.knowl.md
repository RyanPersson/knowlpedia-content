+++
id = "proofs/grh/spanning-core/hecke-projector-onto-an-eigensystem"
title = "A Hecke operator projecting onto one eigensystem"
kind = "lemma"
summary = "For an eigensystem q and finitely many others, one member of the Hecke algebra is the identity on the q-part and zero on the other parts, on all spaces at once."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_hecke_proj_eigenPart", "New.Data.smul_mul_heckeOperator_sub_smul_apply"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be admissible data, \(q\) an eigensystem and \(F\) a finite set of eigensystems. There is \(T\) in the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from \(M\)]] such that for every hermitian space \(V\) of rank \(r\) over \(E\), every \(d\in F\cup\{q\}\) and every \(y\) in the [[proofs/grh/spanning-core/hecke-eigensystem-part|\(d\)-part]] \(\mathcal F_V[d]\),
\[
T_V\,y=\begin{cases}y,& d=q,\\ 0,& d\neq q.\end{cases}
\]

## Proof

Induction on \(F\). For \(F=\emptyset\) take \(T=1\). Let \(T\) work for \(F\) and let \(e\) be a further eigensystem. If \(e=q\), \(T\) works. Otherwise choose \(x\) with \(q(x)\ne e(x)\) and put
\[
T'=\frac{1}{q(x)-e(x)}\,\bigl(T\,T_x-e(x)\,T\bigr)\in\mathcal H ,
\]
with \(T_x\) the [[proofs/grh/spanning-core/hecke-operators-at-split-places|Hecke operator]]. For \(y\in\mathcal F_V[d]\) we have \(T_xy=d(x)y\), so \(T'_Vy=\dfrac{d(x)-e(x)}{q(x)-e(x)}\,T_Vy\). For \(d=e\) this is \(0\); for \(d=q\) it is \(T_Vy=y\); for \(d\in F\), \(d\neq q\), it is a multiple of \(T_Vy=0\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_hecke_proj_eigenPart` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
