+++
id = "proofs/grh/upper-objects/lift-kernels-of-the-chain"
title = "The theta kernels of the chain X_0 to X_m and the restricted chain"
kind = "definition"
summary = "For a tame character theta: the theta kernel of lift j+1 between forms on X_j and X_{j+1}, the data obtained by translating the integral vacuum, combinations of chains with such data, and their restriction to Y_m."
aliases = ["lift kernel", "translations", "translated vacuum", "restricted chain", "chain combination"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.isLiftWeight_columnCount", "New.Data.homX", "New.Data.liftKernel", "New.Data.Translations", "New.Data.translateDatum", "New.Data.chainCombination", "New.Data.restrictedChain", "New.Data.m_eq_two_mul_varrho_add_two"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and \(\vartheta\) a [[?lean:New.Data.TameChar|character of \(U(1)(\mathbb A)\) of weight \(0\) with a given tame part]]. Let \(\mathcal A(X_j)\), \(K_{X_j}\) be the forms and [[proofs/grh/upper-objects/level-places-of-the-data|levels of the stages]].

**Definition.**

1. \(\operatorname{Hom}(X_j,X_{j+1})\) is the definite hermitian space of matrices with rows indexed by \(X_{j+1}\) and columns by \(X_j\), and \(\mathcal S_j\) is the finite part of its space of data.
2. The **kernel of lift \(j+1\)** is the [[?lean:New.thetaKernel|theta kernel]] \(k_j(\vartheta)\) from \(\mathcal A(X_j)\) to \(\mathcal A(X_{j+1})\) (in the sense of [[proofs/grh/upper-objects/chain-of-lifts|chains of lifts]]) with data space \(\mathcal S_j\), level \(K_{X_j}\), whose two characters are the [[?lean:New.rankTwist|rank twists]], by the ranks of \(X_j\) and \(X_{j+1}\), of the [[?lean:New.Data.chainChar|chain character]] \(\mu^0_{j+1}\vartheta^{\,j+1}\) (weight \(-\kappa_{j+1}\)), and whose jets (derivatives) are scaled by \(\pi_M\) times the period [[?lean:New.Parameters.jetScale|\(\Omega\)-scale]].
3. A **tuple of translations** is a family \(x=(x_j)_{j\ge0}\), \(x_j\) a matrix of finite adeles of \(E\) with rows \(X_{j+1}\) and columns \(X_j\). Its \(j\)-th datum is \(\Phi_j(x)=\varrho(x_j)\,v^{\mathrm{int}}_j\in\mathcal S_j\): the [[?lean:New.Parameters.intVacuum|integral vacuum]] of \(\operatorname{Hom}(X_j,X_{j+1})\) translated by the finite Heisenberg operator of \(x_j\).
4. For a finitely supported function \(\Psi\) on tuples of translations and data \(\Phi\), the **chain combination** is \(\sum_x\Psi(x)\cdot\operatorname{chain}_j(\Phi(x))\colon\mathcal A(X_0)\to\mathcal A(X_j)\).
5. The **restricted chain** of \(\Psi\) is the map from [[proofs/grh/upper-objects/source-form|source forms]] to forms on \(Y_m\)
\[
\varphi\longmapsto\operatorname{res}_Y\Big(\sum_x\Psi(x)\operatorname{chain}_m\big(\Phi(x)\big)\varphi\Big),
\]
with [[proofs/grh/upper-objects/branching-map-and-restriction-to-y|\(\operatorname{res}_Y\)]] the restriction from \(X_m\) to \(Y_m\).

## Remarks

That the kernel is defined uses that \((c_\tau,\ell_j)\) is a *lift weight* from \(X_j\) to \(X_{j+1}\) along the exponent \(\lfloor n_{j+1}/2\rfloor-\kappa_{j+1}\): \(n_j<n_{j+1}\), no column has a height strictly between \(n_j\) and \(n_{j+1}\), and \(\ell_j=n_{j+1}/2-\kappa_{j+1}+c_\tau(n_j)\); see the [[proofs/grh/upper-objects/columns-of-the-weights|column description]]. Also \(m=2\varrho+2\), so the chain of \(m\) lifts consists of \(\varrho+1\) double lifts.

## References

1. Lean: `New.Data.liftKernel`, `New.Data.translateDatum`, `New.Data.restrictedChain` in `src/New/UpperBound/Objects/Columns.lean`.
