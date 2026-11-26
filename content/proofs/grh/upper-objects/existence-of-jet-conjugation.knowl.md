+++
id = "proofs/grh/upper-objects/existence-of-jet-conjugation"
title = "Existence and first properties of jet conjugations"
kind = "theorem"
summary = "On a standard space every automorphism of C over K has a jet conjugation; such a map is injective on the finite part, conjugates the values of theta functions at finite points, and sends the vacuum and the data Psi tensor vacuum to explicit Weil translates."
aliases = ["Galois conjugates of jets"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isJetConjugation", "New.Space.map_selfDualAddChar_of_isJetConjugate", "New.Parameters.norm_multiplierRatio", "New.Parameters.IsJetConjugation.eq_zero_of_map_eq_zero", "New.Parameters.IsJetConjugation.map_apply_finVec", "New.Parameters.IsJetConjugation.exists_map_schrodingerOp"]
lean_files = ["src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/upper-objects/jet-conjugation|jet conjugation]]. A space is *standard* if all its signs are \(+1\) and its point is the identity matrix.

**Theorem.** Let \(V\) be a standard space over \(E=E_s\) and \(\sigma\in\operatorname{Aut}(\mathbb C/K)\).

1. *(Existence.)* There are \(t\in\mathbb C\), a finite adele \(b\) and a \(\sigma\)-semilinear \(L\) such that \(L\) is a jet conjugation for \((V,\sigma,t,b)\).
2. *(Injectivity.)* If \(L\) is a jet conjugation, \(f\in\mathcal S(V)_{\mathrm{fin}}\) and \(Lf=0\), then \(f=0\).
3. *(Values.)* If \(L\) is a jet conjugation for a space \(V\) (not necessarily standard), \(f\in\mathcal S(V)_{\mathrm{fin}}\) and \(x\) is a finite adelic vector, then \(\sigma\big(f(\hat x)\big)=(Lf)(\widehat{bx})\).
4. *(Vacuum.)* Let \(L\) be a jet conjugation on the standard \(V\) and \(R\) a set of finite places disjoint from its conjugate. There are \(c\in\mathbb C\), \(c\ne0\), and a finite adele \(u\) with \(u\bar u=1\) such that \(L(\mathrm{vac})=c\,\omega(u)\mathrm{vac}\) and \(L(\Psi\otimes\mathrm{vac})=c\,\omega(u)\big((\sigma\circ\Psi)\otimes\mathrm{vac}\big)\) for every function \(\Psi\) that is Schwartz–Bruhat above \(R\); here \(\omega(u)\) is the Weil operator at the point with trivial archimedean part and finite part the scalar matrix \(u\), and \(\Psi\otimes\) is the [[?lean:New.Space.schrodingerOp|Schrödinger operator]] of \(\Psi\) at \(R\).

Auxiliary statement (*Galois law of the additive character*): let \(E\) be any CM field with Weil data, \(V_1\) the standard space of rank one, \(F,F'\in\mathcal S(V_1)_{\mathrm{fin}}\), \(F\ne0\), \(t\ne0\), \(\sigma\colon\mathbb C\to\mathbb C\) a ring homomorphism, \(e\) a permutation of the infinite places and \(b\) a finite adele. If for all \(x\) the series \(\operatorname{Jet}_{t'}(\varrho(\widehat{bx})F')\) is the \((\sigma,e)\)-jet conjugate of \(\operatorname{Jet}_{t}(\varrho(\hat x)F)\), then \(\sigma(\psi(z))=\psi(b\bar bz)\) for all finite adeles \(z\).

## Proof

*Auxiliary statement.* Translation is locally constant on the finite part, so there is an integer \(N\neq0\) with \(\varrho(\hat N)F=F\) and \(\varrho(\widehat{Nb})F'=F'\). Write \(z=Nx\) (every nonzero integer is a unit of the finite adeles). Apply the hypothesis at \(2x\) to \(F=\varrho(\hat N)F\) and \(F'=\varrho(\widehat{Nb})F'\), and at \(2x+N\). By the Heisenberg relation \(\varrho(\hat y)\varrho(\hat y')=\psi(\tfrac12\,\cdot)\)-multiple of \(\varrho(\widehat{y+y'})\), the jets of \(\varrho(\widehat{2x})\varrho(\hat N)F\) are \(\psi(\tfrac12\cdot x\cdot 2N)=\psi(Nx)\) times those of \(\varrho(\widehat{2x+N})F\), and on the other side the scalar is \(\psi(b\bar b Nx)\). The jets of \(\varrho(\widehat{2x+N})F\) are not zero because jets at a nonzero scale determine an element of the finite part (Lean: `eq_zero_of_jetSeries_eq_zero`, cited) and \(\varrho\) is isometric. Cancelling gives \(\sigma(\psi(Nx))=\psi(b\bar bNx)\).

*1.* The input is the Lean lemma `New.Parameters.exists_isJetConjugate_translates` (area on derivatives of theta functions; cited, not reproved): there is a map \(\sigma\mapsto B_\sigma\) to finite adeles such that every standard \(V\) has a vector \(F\in\mathcal S(V)_{\mathrm{fin}}\) with \(\theta F=1\) whose translates \(\varrho(\hat x)F\) span \(\mathcal S(V)_{\mathrm{fin}}\), and for each \(\sigma\) a \(t\) with \(\lvert t\rvert^2=\Omega^{-1}\) and \(F'\in\mathcal S(V)_{\mathrm{fin}}\) such that \(\operatorname{Jet}_t(\varrho(\widehat{B_\sigma x})F')\) is the jet conjugate of \(\operatorname{Jet}_{c_0}(\varrho(\hat x)F)\) for all \(x\). Since \(t\ne0\), the map \(J\colon f\mapsto\) (renamed \(\operatorname{Jet}_t(f)\)) is injective on \(\mathcal S(V)_{\mathrm{fin}}\). Define \(L=J^{-1}\circ(\sigma\circ\operatorname{Jet}_{c_0})\), where \(J^{-1}\) is a linear left inverse of \(J\); \(L\) is \(\sigma\)-semilinear with values in \(\mathcal S(V)_{\mathrm{fin}}\), and \(L(\varrho(\hat x)F)=\varrho(\widehat{B_\sigma x})F'\). The law for \(\psi\) follows from the auxiliary statement applied to the rank-one space (with its own \(F_1,F_1'\); \(F_1\neq0\) because \(\theta F_1=1\); the scale \(c_0\ne0\)). The translation law and the jet-conjugacy hold on the translates of \(F\) (using the Heisenberg relation and the law for \(\psi\) for the first), hence on their span by semilinearity.

*2.* By condition 3 of the definition the conjugates of all coefficients of \(\operatorname{Jet}_{c_0}(f)\) vanish, so \(\operatorname{Jet}_{c_0}(f)=0\) and \(f=0\) since \(c_0\ne0\).

*3.* \(f(\hat x)\) is the constant term of \(\operatorname{Jet}_{c_0}(\varrho(\hat x)f)\), and \(L(\varrho(\hat x)f)=\varrho(\widehat{bx})Lf\); compare constant terms of the conjugate jets.

*4.* For maps that scale translations the Lean lemma `New.Space.ScalesTranslations.exists_map_schrodingerOp` (the Galois law of the finite Weil representation, in `Lib`; cited) gives \(c\) and \(u\) with the two formulas. If \(c=0\) then \(L(\mathrm{vac})=0\), so \(\mathrm{vac}=0\) by 2, contradicting that the vacuum is a unit vector. \(\square\)

## Remarks

Also used later: for \(\sigma\in\operatorname{Aut}(\mathbb C/K)\) and a finite unitary point \(g\), the ratio \(\sigma(\Delta(g))/\Delta(g)\) of the finite multiplier of the Weil representation has absolute value \(1\) (its square is a quotient of two numbers of absolute value \(1\)). The Lean file head lists as related work Bannai–Kobayashi (2010), Kings–Sprang (2019) and Katz (1978).

## References

1. Lean: `New.Parameters.exists_isJetConjugation`, `New.Parameters.IsJetConjugation.map_apply_finVec`, `New.Parameters.IsJetConjugation.exists_map_schrodingerOp` in `src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean`; `New.Parameters.exists_isJetConjugate_translates` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
