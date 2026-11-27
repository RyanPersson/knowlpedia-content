+++
id = "proofs/grh/upper-objects/mirabolic-subgroup-at-split-level"
title = "Mirabolic subgroup at a split level"
kind = "definition"
summary = "The integral invertible matrices at a split level whose last column is the last basis vector modulo N; it fixes the direct datum and the mirror datum shifted by diag(1,...,1,N)."
aliases = ["mirabolic subgroup modulo N", "stabiliser of a marked lattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.mirabolic", "New.IsSplitLevel.mem_mirabolic", "New.IsSplitLevel.exists_inclGL_eq", "New.IsSplitLevel.directDatum_ne_zero_of_mem_mirabolic", "New.IsSplitLevel.exists_inclGL_eq_conj_diagNInv", "New.IsSplitLevel.directDatum_mul_mul_of_mem_mirabolic", "New.IsSplitLevel.mirrorDatum_mul_mul_of_mem_mirabolic"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\), with the notation \(E_P,\mathcal O_P,\bar{\ },n^+,e_\ast,D_N\) of that page.

**Definition.** The **mirabolic subgroup** \(\mathrm{Mir}_n\subseteq\mathrm{GL}_{n^+}(E_P)\) is the group of matrices \(g\in\mathrm{GL}_{n^+}(\mathcal O_P)\) with \(\bar g\,e_\ast=e_\ast\), i.e. whose last column is \(e_\ast\) modulo \(N\). It is the preimage under reduction of the [[algebra-groups/stabilizer|stabiliser]] of \(e_\ast\) in \(\mathrm{GL}_{n^+}((\mathbb Z/N)^P)\).

## Properties

Let \(g\in\mathrm{Mir}_n\), \(h\in\mathrm{Mir}_{n'}\) and let \(T\) be an \(n'^+\times n^+\) matrix over \(E_P\). With the [[proofs/grh/upper-objects/data-modulo-n|direct and mirror data]]:

1. \(D_N^{-1}gD_N\) is an integral invertible matrix whose *last row* is \(e_\ast\) modulo \(N\).
2. \(\operatorname{direct}(h^{-1}Tg)=\operatorname{direct}(T)\).
3. \(\operatorname{mirror}(D_N^{-1}h^{-1}Tg)=\operatorname{mirror}(D_N^{-1}T)\).

## Proof

*Preliminary.* If \(f^\sharp\) is the extension of a function \(f\) of square matrices modulo \(N\) and \(f^\sharp(g)\ne0\ne f^\sharp(g^{-1})\) for some \(g\in\mathrm{GL}_n(E_P)\), then \(g\) and \(g^{-1}\) are integral, so \(g\in\mathrm{GL}_n(\mathcal O_P)\) and \(f(\bar g)\neq0\). Also, for integral invertible \(a,b\) the extension of \(T\mapsto f(\bar bT\bar a)\) is \(T\mapsto f^\sharp(bTa)\), because \(bTa\) is integral iff \(T\) is.

*1.* The direct datum is \(1\) on \(\mathrm{Mir}_n\) by definition. By the change-of-lattice identity \(\operatorname{lastrow}(D_N^{-1}aD_N)=\operatorname{direct}(a)=1\) for \(a=g\) and \(a=g^{-1}\). By the preliminary, applied to the last-row datum and the matrix \(D_N^{-1}gD_N\), this matrix is integral invertible with last row \(e_\ast\) modulo \(N\).

*2.* Write \(a=g\), \(b=h^{-1}\); both are integral with \(\bar ae_\ast=e_\ast=\bar be_\ast\). For a matrix \(T'\) modulo \(N\), \(\bar bT'\bar a e_\ast=\bar b(T'e_\ast)\), and since \(\bar b\) is injective and fixes \(e_\ast\), this is \(e_\ast\) iff \(T'e_\ast=e_\ast\). Hence the indicator defining the direct datum is unchanged under \(T'\mapsto\bar bT'\bar a\), and the preliminary gives 2.

*3.* By 1 applied to \(h^{-1}\), \(b:=D_N^{-1}h^{-1}D_N\) is integral invertible with last row \(e_\ast\) modulo \(N\), and \(D_N^{-1}h^{-1}Tg=b\,(D_N^{-1}T)\,g\). For \(T'\) modulo \(N\) the corner entry of \(\bar bT'\bar g\) is \((e_\ast^{\mathsf T}\bar b)\,T'\,(\bar ge_\ast)=e_\ast^{\mathsf T}T'e_\ast=T'_{\ast\ast}\). So \(\psi_N\) of the corner is unchanged, and the preliminary gives 3. \(\square\)

## References

1. Lean: `New.IsSplitLevel.mirabolic`, `exists_inclGL_eq_conj_diagNInv`, `directDatum_mul_mul_of_mem_mirabolic`, `mirrorDatum_mul_mul_of_mem_mirabolic` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
