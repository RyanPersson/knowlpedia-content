+++
id = "proofs/grh/upper-objects/jet-conjugation"
title = "Jet conjugation: a semilinear map conjugating Taylor coefficients of theta functions"
kind = "definition"
summary = "For an automorphism sigma of C over K, a sigma-semilinear map on the theta data of a space that scales finite translations by a finite adele b, is compatible with the additive character, and conjugates the jets of theta functions."
aliases = ["jet conjugation"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsJetConjugation"]
lean_files = ["src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(K=\mathbb Q(\sqrt{-d})\), \(E=E_s=K(\zeta)\) with \(\zeta\) a root of unity of order \(q_1(s)\), and \(V\) a [[?lean:New.Space|space]] over \(E\) with index set \(n\). Let \(\mathcal S(V)\) be the [[?lean:New.𝒮|space of theta data]] of \(V\), with the Heisenberg representation \(\varrho\) and the theta functional \(\theta\); \(\mathcal S(V)_{\mathrm{fin}}\) its [[?lean:New.Space.finitePart|finite part]] (the span of the finite Heisenberg translates of the vacuum); and for a finite adelic vector \(x\) let \(\hat x\) be the adelic vector with zero archimedean part and finite part \(\alpha x\) (\(\alpha\) the idele of the [[?lean:New.WeilData|Weil data]]). For a scale \(c\in\mathbb C\), \(\operatorname{Jet}_c(f)\) is the [[?lean:New.Space.jetSeries|jet series of \(f\) at scale \(c\)]], a formal power series in variables indexed by pairs (infinite place of \(E\), element of \(n\)): its coefficient at a multi-index \(\alpha\) is \(c^{\lvert\alpha\rvert}\,\theta\big(\text{integrated operator of the Fock monomial }v_\alpha\text{ applied to }f\big)/\alpha!\). For \(f\) in the finite part of a space with all signs \(+1\) this is the Taylor series at scale \(c\) of the theta function of \(f\) in the Fock coordinates; in general only the formal definition is used. Let \(\Omega\) be [[?lean:New.Parameters.bigOmega|the number \(\Omega\)]], \(c_0\) the [[?lean:New.Parameters.jetScale|jet scale]], and \(\psi\) the [[?lean:New.stdLattice.selfDualAddChar|additive character of the finite adeles]].

**Definition.** Let \(\sigma\in\operatorname{Aut}(\mathbb C/K)\), \(t\in\mathbb C\), \(b\) a finite adele of \(E\), and \(L\colon\mathcal S(V)\to\mathcal S(V)\) additive with \(L(zf)=\sigma(z)L(f)\). Then \(L\) is a **jet conjugation** for \((V,\sigma,t,b)\) if

1. \(\lvert t\rvert^2=\Omega^{-1}\);
2. \(L\) [[?lean:New.Space.ScalesTranslations|scales translations by \(b\)]]: \(L\) maps \(\mathcal S(V)_{\mathrm{fin}}\) into itself; \(L(\varrho(\hat x)f)=\varrho(\widehat{bx})L(f)\) for \(f\in\mathcal S(V)_{\mathrm{fin}}\) and all finite adelic vectors \(x\); and \(\sigma(\psi(z))=\psi(b\bar bz)\) for all finite adeles \(z\);
3. for every \(f\in\mathcal S(V)_{\mathrm{fin}}\), \(\operatorname{Jet}_t(Lf)\) is a [[?lean:New.Space.IsJetConjugate|jet conjugate]] of \(\operatorname{Jet}_{c_0}(f)\): applying \(\sigma\) to all coefficients of \(\operatorname{Jet}_{c_0}(f)\) gives \(\operatorname{Jet}_t(Lf)\) with the variable \((\tau,i)\) renamed to \((\pi_\sigma^{-1}\tau,i)\), where \(\pi_\sigma\) is the permutation of the infinite places of \(E\) induced by \(\sigma\).

## Remarks

Existence and the basic consequences are in [[proofs/grh/upper-objects/existence-of-jet-conjugation|existence of jet conjugations]].

## References

1. Lean: `New.Parameters.IsJetConjugation` in `src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean`.
