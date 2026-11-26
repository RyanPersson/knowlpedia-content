+++
id = "proofs/grh/upper-objects/glued-datum-in-the-schrodinger-model"
title = "The gluing of a double lift in the Schrödinger model above N"
kind = "theorem"
summary = "Read in the Schrödinger model at any split level P above N, the gluing sum of translates with simple poles applied to data that are vacuum above N is the glued datum: the sum over z of the last-column datum tensor the character datum, with no constant."
aliases = ["glued datum in any model"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.doubleLiftGluing_eq_sum_schrodingerOpAt", "New.IsSplitLevel.sum_translate_eq_gluedDatum", "New.IsSplitLevel.exists_sub_mem_and_sub_star_mem_iff", "New.IsSplitLevel.exists_sub_residueOverN_mem_iff", "New.IsSplitLevel.star_residueOverN_mul_self", "New.IsSplitLevel.idem_add_star_eq", "New.IsSplitLevel.schrodingerOpAt", "New.IsSplitLevel.embedGL", "New.IsSplitLevel.detCharAt", "New.IsSplitLevel.pairWeilFinite_schrodingerOpAt", "New.IsSplitLevel.detCharAt_inclGL", "New.IsSplitLevel.norm_detCharAt_diagN_anti", "New.IsSplitLevel.diagN_eq_sdiff_mul", "New.IsSplitLevel.liftFn_eq_residueDatum", "New.IsSplitLevel.exists_embedGL_scalar_eq_scalarFin", "New.IsSplitLevel.mem_integralAbove_of_inclGL_eq", "New.IsSplitLevel.reduction_eq_iff_idem_mul_mem", "New.Seesaw.pairWeilFinite_scalarFin", "New.Space.vacuumProjFinPart"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
proof_status = "outline"
+++

Let \(E\) be a CM field with Weil data, \(N\) a prime, and \(P\), \(S\) two [[proofs/grh/upper-objects/split-level|split levels]] for \(N\) (each contains one place of every conjugate pair above \(N\); neither need contain the other). For finite index sets \(n,n'\), the finite data of \(\operatorname{Hom}(I_n,I_{n'})\) are realised in the **Schrödinger model at \(P\)**: a function \(\Psi\) of \(n'\times n\) matrices over \(E_P\) defines an operator \(v\mapsto\Psi\otimes v\) on finite data (\(\Psi\) is read as a function of adelic matrices through their components at \(P\); Lean: `schrodingerOpAt`). An invertible matrix \(g\in\mathrm{GL}_n(E_P)\) defines the element \(\iota(g)\) of \(U(I_n)(\mathbb A_f)\) supported above \(N\) with component \(g\) at \(P\). Write \(D_{N,T}=\operatorname{diag}(1,\dots,1,N)\) at the places of \(P\cap T\) and \(1\) at the other places of \(P\).

**Theorem (the glued datum in any model).** Let \(v\), \(v'\) be finite data of \(\operatorname{Hom}(I_{n^+},I_{n'})\) and \(\operatorname{Hom}(I_{n'},I_{m^+})\), and let \(\mathrm{pr}_S\) denote the projection onto the vacuum at the places above \(N\) (the average over the Heisenberg operators of the integral vectors supported above \(N\)). Then, with the [[proofs/grh/upper-objects/chain-datum-and-composite-lift|gluing]] taken over \(y\) modulo \(N\) at \(S\),
\[
\mathrm{Glue}_S\big(\mathrm{pr}_Sv\otimes\mathrm{pr}_Sv'\big)=\sum_{z\in((\mathbb Z/N)^P)^{n'}}\Big(\operatorname{lastcol}_z(\,\cdot\,D_{N,S})\otimes v\Big)\otimes\Big(\operatorname{char}_z(D_{N,P\setminus S}\,\cdot\,)\otimes v'\Big),
\]
where \(\operatorname{lastcol}_z\) and \(\operatorname{char}_z\) are the [[proofs/grh/upper-objects/data-modulo-n|last-column and character data modulo \(N\)]] at \(P\).

Pointwise form: for adelic matrices \(T\) (\(n'\times n^+\)) and \(R\) (\(m^+\times n'\)), the sum over \(y\) of the products of the translates by the pole column and pole row of the indicators of the matrices integral at \(P\), evaluated at \(T\) and \(R\), equals the glued datum at \(\big(T_PD_{N,S},\ D_{N,P\setminus S}R_P\big)\).

Further statements of the same section:

1. *(Weil action in the model.)* For \(g\in\mathrm{GL}_n(E_P)\), \(k\in\mathrm{GL}_{n'}(E_P)\), characters \(a,b\) and \(f\) a function of matrices modulo \(N\):
\(\omega_{a,b}(\iota(g),\iota(k))(f^\sharp\otimes v)=\dfrac{\delta_{a,n}(k)}{\delta_{b,n'}(g)}\,\big(T\mapsto f^\sharp(k^{-1}Tg)\big)\otimes v\), where \(\delta_{c,l}(x)=\chi(\det x)\lvert\det x\rvert^{-l/2}\) for \(\chi\) the base change of \(c\) divided by \(\upsilon^l\).
2. \(\delta\) is trivial on \(\mathrm{GL}(\mathcal O_P)\) when the base change of the character is unramified at \(P\); and for an embedding \(\mathbb C\to\mathbb C_N\) and \(k\le k'\), the \(N\)-adic size of \(\delta_{\chi,k'}(D_{N,S})\) is at most that of \(\delta_{\chi,k}(D_{N,S})\).
3. A scalar \(\nu\) of norm one, integral and equal to \(1\) away from \(w\in P\) and \(\bar w\), is \(\iota(x\cdot1)\) for a unit \(x\in\mathcal O_P^\times\) with \(\bar x_{w'}=1\) for \(w'\ne w\).

## Proof

Notation: \(j_P\) is the idempotent adele that is \(1\) at \(P\) and \(0\) elsewhere; an adele \(x\) is *integral at \(P\)* if \(j_Px\) is integral.

*Counting classes.* (i) For an adele \(z\): there is \(b\in(\mathbb Z/N)^P\) such that \(z-y/N\) is integral at \(P\) iff \(Nz\) is integral at \(P\) and \(y=b\). Indeed if \(z-y/N\) is integral at \(P\) then so is \(Nz=N(z-y/N)+\tilde y\); and when \(Nz\) is integral at \(P\), with residue \(b\), the criterion for the reduction says \(\overline{Nz}=y\iff z-y/N\) integral at \(P\). (ii) \(\overline{(y/N)}\cdot(y/N)=0\), since \(y/N\) is supported on a set of places disjoint from its conjugate. (iii) The places above \(N\) are \(P\cup\bar P=S\cup\bar S\). (iv) Let \(p\) be the adele that is \(N\) at \(S\) and \(1\) elsewhere, so \(N+1-p\) is \(1\) at \(S\) and \(N\) elsewhere, and \(p(N+1-p)=N\). For adeles \(t,s\) there is \(b\in(\mathbb Z/N)^S\) such that: \(t-y/N\) and \(s-\overline{y/N}\) are both integral at \(P\) iff \(tp\) and \((N+1-p)s\) are integral at \(P\) and \(y=b\). (Apply (i) at the split level \(S\) to the adele \(z\) that is \(t\) on \(P\) and \(\bar s\) on \(\bar P\): integrality of an adele and of its conjugate at \(P\) is integrality at all places above \(N\), which by (iii) can be tested at \(S\) and \(\bar S\).)

*Pointwise form.* Let \(t_i=T_{i\ast}\) (last column) and \(r_i=R_{\ast i}\) (last row). In the Schrödinger model the translate by a vector \(a\) of the indicator of the integral box is a character value times the indicator of \(\{X: X-a\text{ integral at }P\}\) (Lean: `schrodingerAct`, definition cited). So the \(y\)-term of the sum is nonzero only if \(T\) and \(R\) are integral at \(P\) off the last column, resp. last row, and \(t_i-y_i/N\), \(r_i-\overline{y_i/N}\) are integral at \(P\) for all \(i\); by (iv) this happens for at most one \(y=b\), and exactly when \(TD_{N,S}\) and \(D_{N,P\setminus S}R\) are integral at \(P\) (multiplying the last column by \(p\), the last row by \(N+1-p\)). For \(y=b\) the two character values multiply to \(\psi\) of an adele which differs from \(-\big(\sum_ir_it_i-c/N\big)\) at \(P\) — where \(c\) is the residue at \(P\) of \(N\sum_ir_it_i\), i.e. of the corner entry of \((D_{N,P\setminus S}R)(TD_{N,S})\) — by the integral adele \(\sum_i(t_i-b_i/N)(r_i-\overline{b_i/N})\) and terms killed by (ii); as \(\psi\) is trivial on integral adeles the value is \(\psi(-c/N)=\psi_N(c)\). This is the glued datum.

*Theorem.* Both sides are images, under the map "apply the Schrödinger operators at \(P\) to \(v\otimes v'\)", of tensors of functions of adelic matrices: the left side of \(\sum_yF_y\otimes G_y\) with \(F_y,G_y\) the translated indicators (a translated indicator applied to a datum gives the translate of its projection on the vacuum above \(N\), and this projection is the same for \(P\) and \(S\) by (iii); Lean: `schrodingerOp_schrodingerAct_boxIndicator`, cited), the right side of \(\sum_zF'_z\otimes G'_z\). The two tensors of functions are equal because their values at every pair \((T,R)\) agree, by the pointwise form and \(\operatorname{glued}=\sum_z\operatorname{lastcol}_z\cdot\operatorname{char}_z\).

*Further statements.* 1 is the Lean lemma `pairWeil_schrodingerOp_of_mem_supportedOn` (cited) for points supported above \(N\). 2: for \(g\in\mathrm{GL}(\mathcal O_P)\) the determinant is a unit at each place of \(P\), where both the base change and \(\upsilon\) are unramified; for the monotonicity, the local determinant of \(D_{N,S}\) is \(N\) or \(1\), of norm \(N^{-1}\) or \(1\), and \(\delta_{\chi,l}\) contains the factor \(\lvert\det\rvert^{-l/2}\), whose \(N\)-adic size is \(\le1\) to the power \(l\) (the \(N\)-adic size of \(\sqrt{\lvert d_w\rvert}\) is \(\ge1\)). 3: \(x\) is the component of \(\nu\) at \(P\), with inverse the component of \(\bar\nu\); at \(v\in P\setminus\{w\}\), \(\nu_v=1\) because \(v\ne w\) and \(\bar v\ne w\). \(\square\)

## Remarks

Together with the [[proofs/grh/upper-objects/chain-of-glued-lifts-becomes-direct|theorem that all lifts become direct]], this is what allows the chain of glued double lifts to be compared with a chain of direct lifts after a power of Up; the lift law for these kernels is proved in the area of the seesaw.

## References

1. Lean: `New.IsSplitLevel.doubleLiftGluing_eq_sum_schrodingerOpAt`, `New.IsSplitLevel.sum_translate_eq_gluedDatum`, `New.IsSplitLevel.pairWeilFinite_schrodingerOpAt` in `src/New/UpperBound/Objects/Columns.lean`.
