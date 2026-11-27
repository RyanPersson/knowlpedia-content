+++
id = "proofs/grh/reduction-main"
title = "The reduction: data, heights, twisted lattices, three theorems and the main inequality"
kind = "page"
summary = "The top-level argument: the data, heights and twisted lattices, Theorems A, B and C as statements with their assembly, the main inequality, the one-sided bound and the theorem in half-plane form."
aliases = ["reduction-main"]
domains = ["proofs"]
section_mode = "continuous"
prerequisites = []
lean_files = ["src/New/Reduction/Lattices/Colength.lean", "src/New/Reduction/Lattices/Heights.lean", "src/New/Reduction/Lattices/TwistedLattice.lean", "src/New/Reduction/Data/FieldsAndPlaces.lean", "src/New/Reduction/Data/AdmissibleData.lean", "src/New/Reduction/Data/Magnitudes.lean", "src/New/Reduction/Data/LevelAndTwists.lean", "src/New/Reduction/Data/Sizes.lean", "src/New/Reduction/Data/Existence.lean", "src/New/Reduction/PrimeSums.lean", "src/New/Reduction/IntegralTargetForms.lean", "src/New/Reduction/ShortAndEnough.lean", "src/New/Determinant/Twist/FitTwists.lean", "src/New/Determinant/Twist/LongForms.lean", "src/New/Reduction/MainInequality.lean", "src/New/Reduction/OneSidedBound.lean"]
+++

This chapter contains the skeleton of the proof. It fixes the data on which every other chapter depends, sets up the abstract machinery (heights, twisted lattices) in which a size is played against a divisibility, states the three main theorems A, B, C in the form in which they are combined, and carries out the combination: the main inequality, the one-sided bound for a sum over primes, and the non-vanishing of Dirichlet \(L\)-functions for \(\operatorname{Re}s>\tfrac12\). Theorems A, B, C are proved here *relative to* results of the other chapters, which are quoted with their exact statements.

## 1. Result and strategy

The end result is the [[proofs/grh/reduction-main/grh|main theorem in half-plane form]]: \(L(\rho,\chi)\ne0\) for every Dirichlet character \(\chi\) and \(\operatorname{Re}\rho>\tfrac12\) (\(\rho\ne1\) if \(\chi\) is trivial).

By the one-sided criterion of the chapter on zeros ([[?lean:New.LFunction_ne_zero_of_primeRemainder_le|criterion]]), it suffices to prove, for \(q_0\) a multiple of \(18480\) and primes \(d\equiv q_0/2-1\pmod{q_0}\), the [[proofs/grh/reduction-main/one-sided-bound|one-sided bound]]
\[
R_{q_0}(y)=\sum_{n\le y,\ n\equiv1\,(q_0)}\Lambda(n)\bigl(1-(\tfrac nd)\bigr)\Bigl(\frac1n-\frac1y\Bigr)-\frac{\log y}{\varphi(q_0)}-c_{q_0}\ \le\ y^{-1/2+\varepsilon}\qquad(y\to\infty).
\]
Only an upper bound is needed. It is obtained from a single inequality, the [[proofs/grh/reduction-main/star-inequality|main inequality]] \(m\cdot\mathrm{rem}\le fa\log^5b\), in which \(\mathrm{rem}\) is a combination of values of \(R_{q_0}\) and \(R_1\) and \(m\approx\sqrt x\). The main inequality compares an upper and a lower bound for one quantity: the covolume, corrected by an index, of a family of automorphic forms in a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]].

## 2. The parameters and the data

The [[proofs/grh/reduction-main/parameters|parameters]] \(P=(q_0,d)\) are fixed; they give \(K=\mathbb Q(\sqrt{-d})\) and, for a tower exponent \(s\), the moduli \(q_1(s)\), \(q_2(s)\) and the [[proofs/grh/reduction-main/field-e-and-its-places|CM field \(E=K(\zeta_{q_1})\) with its group \(\Phi\cong(\mathbb Z/q_1)^\times\) of infinite places]]; the facts about \(E\) needed later are collected in [[proofs/grh/reduction-main/field-e-properties|properties of \(E\)]].

Everything that grows with the length \(x\) of the prime sum is bundled in the [[proofs/grh/reduction-main/data|data]] \(D\): integer scales \(x\ll x_1\ll b\), the number \(m\in[\sqrt x,2\sqrt x]\) of lifts, the rank \(r\in[x^5,3x^5]\), the exponent \(s\) with \(2^s=m^{22}\), a [[proofs/grh/reduction-main/sparse-set-of-places|sparse]] set \(\Phi_b\) of places \(\equiv-1\bmod q_0\) with weight \(b\) (all other places have weight \(a/x_1\), \(a=xb\)), primes \(p_0,p_1\in[b^{10},b^{11}]\) and a prime level \(N\) in a prescribed window, all \(\equiv1\bmod q_2^2\), with integers of norm \(p_0p_1\) and \(N\). The [[proofs/grh/reduction-main/data-derived-quantities|derived quantities]] (\(k=r+1-m\), \(t=5r\), \(n_j\), \(\Delta=2r^8\), \(M=p_0p_1\), \(f\), the \(a\)-places \(\Phi_a\), the lift weights \(\kappa_j\)) and the [[proofs/grh/reduction-main/target-parameter|row parameter]] are read off. Sizes are compared by the [[proofs/grh/reduction-main/log-bound-calculus|calculus of logarithmic bounds]] and tabulated in [[proofs/grh/reduction-main/data-sizes|sizes of the data]]. The characters entering the lifts are the [[proofs/grh/reduction-main/lift-characters|characters \(\mu_j^0\)]], twisted by [[proofs/grh/reduction-main/twist|twists]] and [[proofs/grh/reduction-main/m-fold-twist|\(m\)-fold twists]].

[[proofs/grh/reduction-main/data-exist|Data exist at every large integer \(x\)]], with \(\log b\approx x^{\varepsilon}\) and \(\log x_1\approx x^{\varepsilon/6}\); the \(b\)-places come from [[proofs/grh/reduction-main/sparse-places-exist|Behrend's construction]], the primes from the Siegel–Walfisz theorem in short logarithmic windows, the element of norm \(p_0p_1\) from a pigeonhole argument in the class group of \(K\), and the element of norm \(N\) from a sum of two squares.

## 3. The quantities compared

The [[proofs/grh/reduction-main/prime-sum|prime sum]] \(s_{\mathrm{fin}}(y,\sigma)=\sum_{\nu\le a}\Lambda_K(\nu)(y/\nu-\kappa(-\nu\sigma))_+\) measures the guaranteed divisibility of a derivative of order \(y\) at the place \(\sigma\); the jet size \(s_\infty(j)=\log j!+j\log(M/\Omega)\) its archimedean size. From them: the direction amount \(h_{\mathrm{dir}}\), the [[proofs/grh/reduction-main/main-amount-and-total-remainder|main amount \(h_{\mathrm{main}}=mk\,h_{\mathrm{dir}}\), the expected prime sum \(s_{\mathrm{main}}\) and the total remainder \(\mathrm{rem}\)]]. The key identity is the [[proofs/grh/reduction-main/total-remainder-formula|formula]]
\[
\mathrm{rem}=a\bigl(\#\Phi_b(R_{q_0}(x)-R_{q_0}(x_1))+\#\Phi_aR_1(x_1)\bigr),
\]
in which the main terms \(\log x,\log x_1,c_1\) and the constant \(c_{q_0}\) cancel; elementary [[proofs/grh/reduction-main/prime-sum-bounds|bounds]] give \(h_{\mathrm{main}}\ge x^4fa\ge0\).

## 4. Heights and twisted lattices

A [[proofs/grh/reduction-main/prime-padic-iso|finite place \(\iota\mid\ell\) of \(\mathbb C\)]] is a prime with an isomorphism \(\mathbb C\cong\overline{\mathbb Q}_\ell\). A family of complex numbers indexed by these places has a [[proofs/grh/reduction-main/height-bound|height bound]]; heights obey a [[proofs/grh/reduction-main/height-calculus|calculus]] and the [[proofs/grh/reduction-main/height-product-formula|product formula]] (a consequence of the [[proofs/grh/reduction-main/log-product-formula|product formula for \(\mathbb Q\)]]): a nonzero number cannot be small at all places at once.

A [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] is a family of maps \(\Theta_\xi:V\to S_\xi\) with integral structures. For a finite family in \(V\) one has the [[proofs/grh/reduction-main/index-bound|index]] (how far it is from integral, with its [[proofs/grh/reduction-main/index-calculus|calculus]], fed by [[proofs/grh/reduction-main/colength-divides|colengths]] and their [[proofs/grh/reduction-main/colength-calculus|calculus]]; see also [[proofs/grh/reduction-main/colength-of-matrix-image|images of matrices]], [[proofs/grh/reduction-main/colength-bounds-length|lengths]], [[proofs/grh/reduction-main/onto-up-to-colength|endomorphisms onto up to colength]] and their [[proofs/grh/reduction-main/onto-up-to-colength-product|products]], used in other chapters) and the [[proofs/grh/reduction-main/covolume-bound|covolume]] (Gram determinants of the untwisted lifts at all conjugates, with its [[proofs/grh/reduction-main/covolume-calculus|calculus]]). With the [[proofs/grh/reduction-main/twisted-lattice-volume|volumes \(Z(\xi)\)]] and the [[proofs/grh/reduction-main/gram-determinant-valuation|valuations of Gram determinants]], the abstract lower bound is the theorem [[proofs/grh/reduction-main/covolume-add-index-nonneg|a twist for each prime]]:
\[
c+2\delta+n'(b_{\mathrm{short}}+b_{\mathrm{denom}})+b_{\mathrm{volume}}\ge0 .
\]
Its point is that the twist \(\xi_\iota\) may depend on the place \(\iota\), since the multiplier of a height does not.

The instance is the [[proofs/grh/reduction-main/target-lattice|target lattice]]: \(V\) the target forms on \(\mathrm U(Y_0)\), twists the \(m\)-fold twists, \(\Theta_\vartheta\) the chain of \(m\) theta lifts to \(\mathrm U(Y_m)\).

## 5. Theorems A, B, C

Throughout this section the **source** \(\mathcal S\) is the space of *ramified* source forms, a subspace of the space \(\mathcal S_X\) of all source forms on \(\mathrm U(X_0)\); \(\dim\mathcal S\) always means the dimension of this subspace, and \(d_T\) is the dimension of the target. Ramified source forms are mapped to target forms by the translates \(s\mathfrak p\) of the [[proofs/grh/reduction-main/normalized-poincare|normalised Poincaré map]] \(\mathfrak p=c_B\,c_{ss}^{-1}\,\#\bar G\,e_0\,\mathcal P\), where \(c_B\) is the [[proofs/grh/reduction-main/gain-normalisation|product of \(\ell^{-g_\ell}\)]] that divides out the guaranteed divisibility.

- [[proofs/grh/reduction-main/theorem-a-short-forms|Theorem A (a)]]: the source is spanned by integral forms \(\varphi\) with \(\lVert\Theta_1s\mathfrak p\varphi\rVert_\sigma^2\le\exp(h_{\mathrm{main}}-m\,\mathrm{rem}+fa\log^4b)\). Inputs: the seesaw identity, the size of the composite lift, short source forms.
- [[proofs/grh/reduction-main/theorem-a-index|Theorem A (b)]]: such images, for \(s\) in a set \(t\), have index at most \(\#t\dim\mathcal S\cdot2fa\log^3b\). Input: the divisibility of the composite lift.
- [[proofs/grh/reduction-main/theorem-b-enough-forms|Theorem B]]: some \(t\) with \(\#t\dim\mathcal S\le5d_T\log(1+2b^2)\) has images spanning \((1-4/b^2)d_T\) dimensions. Input: the spanning theorem (second moment).
- [[proofs/grh/reduction-main/theorem-c-integral-forms-long|Theorem C]]: independent \(y_1,\dots,y_n\), \(n\ge(1-4/b^2)d_T\), of index \(\le\delta\) and covolume \(\le c\), satisfy \(c+2\delta\ge d_T(h_{\mathrm{main}}-3fa\log^4b)\). It is the abstract lower bound applied with [[proofs/grh/reduction-main/auxiliary-forms|auxiliary forms]] completing the family to a basis and a [[proofs/grh/reduction-main/regular-family-of-twists|regular family of twists]], for which [[proofs/grh/reduction-main/inverse-ratio-height|\(Z(1)/Z(\xi_\iota)\) has height at most \(d_T(b+fa\log^4b-h_{\mathrm{main}})\)]].

## 6. The main inequality and the conclusion

In the [[proofs/grh/reduction-main/star-inequality|main inequality]], Theorems A and B produce a linearly independent family with \((1-4/b^2)d_T\le n\le d_T\) members (the lower bound is what Theorem C requires), covolume \(\le n(h_{\mathrm{main}}-m\,\mathrm{rem}+F)\) and index \(\le d_T\cdot10\log(1+2b^2)fa\log^3b\); Theorem C bounds the same quantity below by \(d_T(h_{\mathrm{main}}-3F)\). Since \(n\le d_T\) and \(h_{\mathrm{main}}+F\ge0\), the main amount cancels, leaving \(n\,m\,\mathrm{rem}\le d_T(4F+2I)\); only then is \(n\ge d_T/2\) used, to divide by \(n\), and \(m\,\mathrm{rem}\le fa\log^5b\) remains.

Dividing by \(m\,a\,\#\Phi_b\) and using the formula for \(\mathrm{rem}\) gives [[proofs/grh/reduction-main/prime-remainder-bound-from-data|\(R_{q_0}(x)\le\varphi(q_0)\log^6b/m+\lvert R_{q_0}(x_1)\rvert+\log b\,\lvert R_1(x_1)\rvert\)]]. With \(\log b\le2x^\varepsilon\), \(m\ge\sqrt x\) and the prime number theorem at the much larger point \(x_1\), this is \(O(x^{-1/2+6\varepsilon})\) at integers \(x\); the slow variation \(\lvert R(z)-R(y)\rvert\le13(z-y)/y\) passes from integers to real arguments, giving the [[proofs/grh/reduction-main/one-sided-bound|one-sided bound]], and the criterion gives [[proofs/grh/reduction-main/grh|the theorem]].

## References

1. Lean: the files listed in the front matter, under `documents/grh-lean/grh/src/`; reading guide `GUIDE.md`, sections 1–3.
