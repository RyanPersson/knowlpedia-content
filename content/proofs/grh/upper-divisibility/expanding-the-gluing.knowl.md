+++
id = "proofs/grh/upper-divisibility/expanding-the-gluing"
title = "Expanding the gluing of a chain datum"
kind = "theorem"
summary = "The glued tensor of a chain datum is the double sum, over the support and over the gluing classes, of unglued tensors of vacua translated by x plus the gluing tuple of the class."
aliases = ["gluing classes", "gluing tuple", "unglued vacuum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsChainDatum.gluedTensor_eq_sum_translates", "New.Data.GluingClasses", "New.Data.gluingTuple", "New.Data.ungluedVacuum", "New.Data.gluedVacuum_eq_sum_translates", "New.Data.gluedDoubleLiftDatum_translateDatum", "New.Data.heisenbergFinPart_translateDatum_of_disjoint", "New.Data.card_gluingClasses_le", "New.Data.gluingTuple_mem_supportedTranslations", "New.Data.TameChar.M_mul_normQ_notMem_of_N_mem", "New.Data.plainTensor_eq_sum_ungluedVacuum"]
lean_files = ["src/New/UpperBound/Divisibility/ChainDatumExpansion.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]; \(m=2(\varrho+1)\) lifts are grouped in \(\varrho+1\) double lifts \(X_{2i}\to X_{2i+1}\to X_{2i+2}\). For a tuple of translations \(t=(t_j)\) let \(\Phi^{0}_{t,j}\) be the [[?lean:New.Data.translateDatum|integral vacuum of \(\operatorname{Hom}(X_j,X_{j+1})\) translated by \(t_j\)]].

- A **gluing class** is a family \(y=(y_i)_{i\le\varrho}\), where \(y_i\) assigns to each basis index of the middle space \(X_{2i+1}\) and each prime \(w\mid\pi_N\) a residue modulo \(N\).
- The **gluing tuple** \(z(y)\) is the tuple of translations with \(z(y)_{2i}\) the matrix with last column \(-y_i/N\) at the places \(w\mid\pi_N\) and zero elsewhere ([[?lean:New.poleColumn|pole column]]), \(z(y)_{2i+1}\) the matrix with last row \(-\bar y_i/N\) at the conjugate places ([[?lean:New.poleRow|pole row]]), and all other entries \(0\).
- The **unglued vacuum** of \(t\) is \(\Omega(t)=\bigotimes_{i\le\varrho}\bigl(\Phi^{0}_{t,2i}\otimes\Phi^{0}_{t,2i+1}\bigr)\).
- The [[?lean:New.Data.gluedDoubleLiftDatum|gluing of the \(i\)-th double lift]] replaces \(v_{2i}\otimes v_{2i+1}\) by the sum over \(y_i\) of its Heisenberg translates by the pole column and the pole row of \(y_i\); the [[?lean:New.Data.gluedTensor|glued tensor]] of a coefficient function \(\Psi\) is \(\sum_x\Psi(x)\cdot\mathrm{Glue}\,\Omega(x)\), and the [[?lean:New.Data.plainTensor|plain tensor]] is \(\sum_x\Psi(x)\,\Omega(x)\).

**Theorem.** Let \(\vartheta\) be a twist and \(\Psi\) a [[?lean:New.Data.IsChainDatum|chain datum]] for \(\vartheta\). Then
\[
\mathrm{Glue}\Bigl(\sum_x\Psi(x)\Omega(x)\Bigr)=\sum_x\Psi(x)\sum_{y}\Omega\bigl(x+z(y)\bigr),
\]
the inner sum over all gluing classes. There are at most \(N^{fmn_m/2}\) gluing classes, and every \(z(y)\) vanishes at the places not above \(N\).

## Proof

A tuple \(x\) in the support of a chain datum vanishes at the places prime to \(M\cdot\mathrm N\vartheta\), in particular at the places above \(N\): such a place contains neither \(M\) (it is not chosen, nor is its conjugate) nor the norm \(\mathrm N\vartheta\) of the modulus (prime to \(N\)).

*One double lift.* Let \(t\) vanish above \(N\) and let \(c\) be a matrix supported at the primes dividing \(\pi_N\) and their conjugates. Translating the vacuum first by \(t_j\) and then by \(c\) equals translating it by \(c+t_j\): the composition of Heisenberg translations has a phase depending on the pairing \(\bar t_j\cdot c\), which vanishes because the supports are disjoint. Hence the glued datum of the \(i\)-th double lift of \(\Phi^{0}_{t,\cdot}\) is \(\sum_{y_i}\Phi^{0}_{t+z,2i}\otimes\Phi^{0}_{t+z,2i+1}\) with \(z\) the pole column and pole row of \(y_i\).

*All double lifts.* A tensor product of sums is the sum over the families \(y=(y_i)\) of the tensor products, which gives \(\mathrm{Glue}\,\Omega(t)=\sum_y\Omega(t+z(y))\); apply this to each \(x\) in the support.

*Count.* The \(i\)-th double lift has \(N^{f n_{2i+1}}\le N^{fn_m}\) classes (there are \(f\) primes dividing \(\pi_N\)), and there are \(\varrho+1=m/2\) double lifts. The support statement is clear from the definition of pole columns and rows. \(\blacksquare\)

*Status.* The composition law of finite Heisenberg operators ([[?lean:New.finHeisenbergOp_finHeisenbergOp|`finHeisenbergOp_finHeisenbergOp`]]) and the support condition in the definition of a chain datum are quoted.

## References

1. Lean: `New.Data.IsChainDatum.gluedTensor_eq_sum_translates` and the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/ChainDatumExpansion.lean`.
