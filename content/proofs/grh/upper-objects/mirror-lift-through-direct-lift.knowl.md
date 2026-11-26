+++
id = "proofs/grh/upper-objects/mirror-lift-through-direct-lift"
title = "A mirror lift is Up after a direct lift"
kind = "lemma"
summary = "On ramified vectors the mirror lift, moved by diag(1,...,1,1/N), is Up of the direct lift, and equals gamma times the direct lift of Up; so Up passes through a direct lift at the cost gamma."
aliases = ["mirror data through direct data"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.LiftLaw.mirror_eq_upOperator_direct", "New.IsSplitLevel.LiftLaw.mirror_eq_direct_upOperator", "New.IsSplitLevel.LiftLaw.upOperator_direct"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
proof_status = "full"
+++

**Lemma.** Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\), let \(L\colon\Psi\mapsto L(\Psi)\in\operatorname{Hom}(\pi,\pi')\) obey the [[proofs/grh/upper-objects/lift-law|lift law]] with factor \(\gamma\), and let \(\varphi\in\pi\) be a [[proofs/grh/upper-objects/ramified-vector-at-split-level|ramified vector]]. With the direct and mirror [[proofs/grh/upper-objects/data-modulo-n|data]] and the [[proofs/grh/upper-objects/up-operator|operator Up]] (on \(\pi\) and on \(\pi'\)):

1. \(\pi'(D_N)\,L(\operatorname{mirror})\varphi=\mathrm{Up}\big(L(\operatorname{direct})\varphi\big)\);
2. \(\pi'(D_N)\,L(\operatorname{mirror})\varphi=\gamma\cdot L(\operatorname{direct})\big(\mathrm{Up}\,\varphi\big)\);
3. \(\mathrm{Up}\big(L(\operatorname{direct})\varphi\big)=\gamma\cdot L(\operatorname{direct})\big(\mathrm{Up}\,\varphi\big)\).

## Proof

By the [[proofs/grh/upper-objects/lift-law-vanishing-on-ramified-vectors|vanishing lemma]], \(L(\operatorname{mirror})\varphi=L(f^\sharp)\varphi\) with \(f(T)=\psi_N(T_{\ast\ast})\mathbf 1[T_{\ast\ast}\text{ unit}]\).

*1.* The function \(f\) depends only on the last column \(y=Te_\ast\) of \(T\), so by linearity in the datum
\[
L(\operatorname{mirror})\varphi=\sum_{y\,:\,y_\ast\ \mathrm{unit}}\psi_N(y_\ast)\,L(\operatorname{lastcol}_y)\varphi ,
\]
the sum over \(y\in((\mathbb Z/N)^P)^{n'^+}\). By property 2 of the lift law and \(\bar k_ye_\ast=y\), \(L(\operatorname{lastcol}_y)\varphi=\pi'(k_y)L(\operatorname{direct})\varphi\). Applying \(\pi'(D_N)\) gives exactly the definition of \(\mathrm{Up}\) on \(\pi'\) applied to \(L(\operatorname{direct})\varphi\).

*2.* The function \(f\) also depends only on the last row \(y\) of \(T\), so
\[
L(\operatorname{mirror})\varphi=\sum_{y\,:\,y_\ast\ \mathrm{unit}}\psi_N(y_\ast)\,L(\mathbf 1[\text{last row}=y]^\sharp)\varphi ,
\]
the sum over \(y\in((\mathbb Z/N)^P)^{n^+}\). Since the last row of \(\bar k_y\) is \(y\), i.e. \(e_\ast^{\mathsf T}\bar k_y=y^{\mathsf T}\), and right multiplication by \(\bar k_y\) is injective on rows, the last row of \(T\bar k_y\) is \(y\) iff the last row of \(T\) is \(e_\ast\). Integral equivariance with \(a=k_y\), \(b=1\) therefore gives
\(L(\mathbf 1[\text{last row}=y]^\sharp)\varphi=L(\operatorname{lastrow})(\pi(k_y)\varphi)\). Applying \(\pi'(D_N)\) and the change-of-lattice rule,
\[
\pi'(D_N)L(\operatorname{mirror})\varphi=\gamma\sum_y\psi_N(y_\ast)L(\operatorname{direct})\big(\pi(D_N)\pi(k_y)\varphi\big)=\gamma\,L(\operatorname{direct})(\mathrm{Up}\,\varphi).
\]

*3.* Compare 1 and 2. \(\square\)

## References

1. Lean: `New.IsSplitLevel.LiftLaw.mirror_eq_upOperator_direct`, `mirror_eq_direct_upOperator`, `upOperator_direct` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
