+++
id = "proofs/grh/upper-objects/lift-law"
title = "Lift law modulo N"
kind = "definition"
summary = "Two rules for a lift between representations of GL at a split level that depends linearly on a datum: equivariance under integral matrices, and the cost gamma of the change of lattice."
aliases = ["lift law"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.LiftLaw", "New.IsSplitLevel.LiftLaw.mem_ramified", "New.IsSplitLevel.LiftLaw.inclGL_lastColDatum", "New.IsSplitLevel.LiftLaw.charDatum_inclGL", "New.IsSplitLevel.liftFn_comp_eq_sum_smul"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\), let \(\pi,\pi'\) be complex [[algebra-representation-theory/group-representation|representations]] of \(\mathrm{GL}_{n^+}(E_P)\) and \(\mathrm{GL}_{n'^+}(E_P)\), and let
\[
L\colon\{\text{functions } \Psi\colon M_{n'^+\times n^+}(E_P)\to\mathbb C\}\longrightarrow\operatorname{Hom}_{\mathbb C}(\pi,\pi')
\]
be a \(\mathbb C\)-linear map (a *lift depending linearly on its datum* \(\Psi\)). Let \(\gamma\in\mathbb C\). Recall the extension \(f\mapsto f^\sharp\) and the last-row and direct [[proofs/grh/upper-objects/data-modulo-n|data modulo \(N\)]].

**Definition.** \(L\) **obeys the lift law with factor \(\gamma\)** if

1. *(integral equivariance)* for all \(a\in\mathrm{GL}_{n^+}(\mathcal O_P)\), \(b\in\mathrm{GL}_{n'^+}(\mathcal O_P)\), all functions \(f\) on \(n'^+\times n^+\) matrices modulo \(N\) and all \(\varphi\in\pi\),
\[
\pi'(b)\,L\big((T\mapsto f(\bar b\,T\,\bar a))^\sharp\big)\big(\pi(a)\varphi\big)=L(f^\sharp)\,\varphi ;
\]
2. *(change of lattice)* for all \(\varphi\in\pi\),
\[
\pi'(D_N)\,L(\operatorname{lastrow})\,\varphi=\gamma\cdot L(\operatorname{direct})\big(\pi(D_N)\varphi\big).
\]

## Properties

Assume \(L\) obeys the lift law.

1. For every \(f\), \(L(f^\sharp)\) commutes with unit scalar matrices and hence maps [[proofs/grh/upper-objects/ramified-vector-at-split-level|ramified vectors]] to ramified vectors.
2. For \(k\in\mathrm{GL}_{n'^+}(\mathcal O_P)\) and \(y\in((\mathbb Z/N)^P)^{n'^+}\): \(\pi'(k)\,L(\operatorname{lastcol}_y)\varphi=L(\operatorname{lastcol}_{\bar ky})\varphi\).
3. For \(k\in\mathrm{GL}_{n^+}(\mathcal O_P)\) and \(y\in((\mathbb Z/N)^P)^{n^+}\): \(L(\operatorname{char}_{\bar ky})(\pi(k)\varphi)=L(\operatorname{char}_y)\varphi\).
4. If \(r\) is a map from matrices modulo \(N\) to a finite set and \(g\) a complex function on that set, then \(L((g\circ r)^\sharp)=\sum_y g(y)\,L(\mathbf 1[r=y]^\sharp)\).

## Proof

*1.* Apply integral equivariance with \(a=x^{-1}\cdot1\), \(b=x\cdot1\) to the vector \(\pi(x\cdot 1)\psi\): since \(\bar x\,T\,\bar x^{-1}=T\), we get \(\pi'(x\cdot1)L(f^\sharp)\psi=L(f^\sharp)\pi(x\cdot1)\psi\).

*2.* Apply integral equivariance with \(a=1\), \(b=k\) and \(f=\mathbf 1[\text{last column}=\bar ky]\): \(f(\bar kT)=\mathbf 1[\bar kTe_\ast=\bar ky]=\mathbf 1[Te_\ast=y]\).

*3.* Apply it with \(a=k\), \(b=1\) and \(f=\psi_N(T_\ast\cdot y)\): \((T\bar k)_\ast\cdot y=T_\ast\cdot\bar ky\).

*4.* \(g\circ r=\sum_yg(y)\mathbf 1[r=y]\), the extension is linear, and \(L\) is linear. \(\square\)

## Remarks

The lift law is verified for the theta lifts between the spaces \(X_j\) in the area of the seesaw; here it is an abstract hypothesis. The representations are of the abstract groups; no smoothness is used.

## References

1. Lean: `New.IsSplitLevel.LiftLaw` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
