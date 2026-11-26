+++
id = "proofs/grh/upper-objects/lift-law-vanishing-on-ramified-vectors"
title = "Lifts by scalar-invariant data kill ramified vectors"
kind = "lemma"
summary = "A lift obeying the lift law, with a datum invariant under unit scalars at one place, annihilates ramified vectors; so the mirror datum may be restricted to unit corner entries."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.LiftLaw.apply_liftFn_eq_zero_of_smul_invariant", "New.IsSplitLevel.LiftLaw.apply_liftFn_indicator_eq_zero", "New.IsSplitLevel.LiftLaw.mirrorDatum_eq_unitCorner"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
proof_status = "full"
+++

**Lemma.** Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\), let \(L\colon\Psi\mapsto L(\Psi)\in\operatorname{Hom}(\pi,\pi')\) obey the [[proofs/grh/upper-objects/lift-law|lift law]], and let \(\varphi\in\pi\) be a [[proofs/grh/upper-objects/ramified-vector-at-split-level|ramified vector]].

1. Let \(w\in P\) and let \(f\) be a function on \(n'^+\times n^+\) matrices modulo \(N\) with \(f(cT)=f(T)\) for every unit \(c\in(\mathbb Z/N)^P\) with \(c_{w'}=1\) for \(w'\ne w\). Then \(L(f^\sharp)\varphi=0\).
2. Let \(r\) be a map from matrices modulo \(N\) to vectors in \(((\mathbb Z/N)^P)^{\iota}\) (\(\iota\) any index set) with \(r(cT)=c\,r(T)\) for all \(c\in(\mathbb Z/N)^P\), and let \(y\) be a vector all of whose entries vanish at some place \(w\in P\). Then \(L(\mathbf 1[r=y]^\sharp)\varphi=0\).
3. \(L(\operatorname{mirror})\varphi=L(f^\sharp)\varphi\) where \(f(T)=\psi_N(T_{\ast\ast})\) if \(T_{\ast\ast}\) is a unit and \(f(T)=0\) otherwise.

## Proof

*1.* Write \(\varphi=\psi-\pi(x\cdot1)\psi\) with \(x\in\mathcal O_P^\times\), \(\bar x_{w'}=1\) for \(w'\neq w\). Integral equivariance with \(a=x\cdot1\), \(b=1\) gives \(L((T\mapsto f(T\bar x))^\sharp)(\pi(x\cdot 1)\psi)=L(f^\sharp)\psi\), and \(f(T\bar x)=f(\bar xT)=f(T)\) by hypothesis (\(\bar x\) is a unit). Hence \(L(f^\sharp)\pi(x\cdot1)\psi=L(f^\sharp)\psi\) and \(L(f^\sharp)\varphi=0\).

*2.* Let \(c\) be a unit with \(c_{w'}=1\) for \(w'\ne w\). Then \(cy=y\), since the entries of \(y\) vanish at \(w\). So \(r(cT)=y\iff c\,r(T)=cy\iff r(T)=y\), and 1 applies to \(f=\mathbf 1[r=y]\).

*3.* Sorting by the corner entry \(t=T_{\ast\ast}\) (property 4 of the lift law), \(L(\operatorname{mirror})\varphi=\sum_t\psi_N(t)L(\mathbf 1[T_{\ast\ast}=t]^\sharp)\varphi\) and likewise for \(f\) with the sum restricted to units \(t\). If \(t\) is not a unit then \(t_w=0\) for some \(w\in P\), and the term vanishes by 2 applied to \(r(T)=T_{\ast\ast}\). \(\square\)

## References

1. Lean: `New.IsSplitLevel.LiftLaw.apply_liftFn_eq_zero_of_smul_invariant`, `apply_liftFn_indicator_eq_zero`, `mirrorDatum_eq_unitCorner` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
