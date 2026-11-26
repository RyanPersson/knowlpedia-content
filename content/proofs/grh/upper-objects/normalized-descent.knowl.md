+++
id = "proofs/grh/upper-objects/normalized-descent"
title = "Fock polynomial, conjugate kernel and normalized descent of a descent pair"
kind = "definition"
summary = "For a descent pair: the polynomial attached to a weight vector, the Schwartz datum built from it and the block datum, the conjugate theta kernel as a linear form on weight vectors, and the normalized descent, a class sum from forms on V to functions on U(W)."
aliases = ["normalized descent", "Fock polynomial of a weight vector", "conjugate kernel", "Fock datum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.tensorPoly", "New.DescentPair.tensorPoly_vecMulVec", "New.DescentPair.fockPoly", "New.DescentPair.fockDatum", "New.DescentPair.conjKernel", "New.DescentPair.normalizedDescent"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]] with signs \(s\), numbering \(\nu\), column numbers \(k^\pm\), and forms \(\mathcal F_V(O)\) on \(V\) with values in the Weyl module \(\mathcal V\) of the weight of \(O\) (with its [[?lean:New.WeylIndex|basis of standard fillings]]). The Fock variables are \(X_{\tau,i,c}\) for \(\tau\) an infinite place, \(i\in n\), \(c\in r\).

**Definition.**

1. For \(a\in\mathcal V_{k^+}\) and \(b\in\mathcal V_{k^-}\) (Weyl modules of the column numbers \(k^+\), \(k^-\)), the polynomial of \(a\otimes b\) is \(P^+_a\cdot P^-_b\), where \(P^\pm\) is the [[?lean:New.letterPoly|letter polynomial]] in the variables of sign \(\pm1\): the letter \(h\) of a filling stands for the sum of the variables \(X_{\tau,i,c}\) over the \(c\) with \(s_c=\pm1\) and \(\nu(c)=h\). This extends linearly to \(\mathcal V_{k^+}\otimes\mathcal V_{k^-}\).
2. The **Fock polynomial** \(\xi\mapsto P_\xi\) on \(\mathcal V\) is the composite of the [[?lean:New.mixedCartan|chosen integral embedding]] \(\mathcal V\hookrightarrow\mathcal V_{k^+}\otimes\mathcal V_{k^-}\) with the map of 1.
3. The **Fock datum** of \(\xi\) is \(v_{P_\xi}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\): the Fock vector of \(P_\xi\) at the infinite places tensored with the [[proofs/grh/upper-objects/block-datum|block datum]].
4. The **conjugate kernel** at \(g\in U(W)(\mathbb A)\) and \(h\in U(V)(\mathbb A_f)\) is the linear form on \(\mathcal V\)
\[
\xi\longmapsto\overline{\theta\big(\omega_{\nu_W,\nu_V}(g,(1,h))\,(v_{P_{\bar\xi}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac})\big)},
\]
where \(\theta\) is the theta functional of the theta kernel of \(O\) and \(\bar\xi\) is the coordinatewise conjugate.
5. The **normalized descent** is the linear map \(\mathcal F_V(O)\to\{U(W)(\mathbb A)\to\mathbb C\}\),
\[
(\theta\Xi)(g)=\sum_{h}\ \text{(conjugate kernel at }(g,h))\big(\Xi(h)\big),
\]
the [[?lean:New.classSum|class sum]] for the rational points \(\Gamma\) of \(U(V)\) and the level group \(K_O\): the sum over the double cosets \(c\in\Gamma\backslash U(V)(\mathbb A_f)/K_O\), with chosen representatives \(h_c\), of the summand at \(h_c\) divided by \(\lvert\Gamma\cap h_cK_Oh_c^{-1}\rvert\).

## Remarks

By [[proofs/grh/upper-objects/normalized-descent-is-a-transposed-lift|the comparison theorem]] the normalized descent is a multiple of the conjugate of the transposed theta lift of the conjugate form.

## References

1. Lean: `New.DescentPair.fockPoly`, `New.DescentPair.conjKernel`, `New.DescentPair.normalizedDescent` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
