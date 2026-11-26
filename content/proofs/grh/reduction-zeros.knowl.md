+++
id = "proofs/grh/reduction-zeros"
title = "From a one-sided prime-sum bound to the zeros: the final theorems"
kind = "page"
summary = "The five final theorems, the passage from the half-plane to the critical line, the one-sided criterion that turns an upper bound for a weighted prime sum into a zero-free half-plane, and the classical analytic number theory behind it."
aliases = ["reduction to zeros", "one-sided criterion chapter"]
domains = ["proofs"]
section_mode = "continuous"
prerequisites = []
lean_files = ["src/Statements.lean", "src/Main.lean", "src/New/Main.lean", "src/New/Reduction/Zeros/Criterion.lean", "src/New/Reduction/Zeros/PrimeError.lean", "src/New/Reduction/Zeros/PrimeNumberTheorem.lean", "src/Lib/Analytic/EntireLFunction.lean", "src/Lib/Analytic/Landau.lean", "src/Lib/Analytic/ZeroSymmetry.lean", "src/Lib/Analytic/PolyaVinogradov.lean", "src/Lib/Analytic/DirichletTheta.lean", "src/Lib/Analytic/QuadraticTwist.lean", "src/Lib/Analytic/Primes.lean", "src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean", "src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean", "src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean"]
+++

This chapter is the top of the proof. It states the [[proofs/grh/reduction-zeros/main-theorems|five final theorems]] and derives them from one statement, the half-plane theorem, and it proves the criterion by which that theorem follows from a one-sided bound for a weighted sum over primes. Everything here is analytic number theory in one complex variable; the bound itself is the work of the other chapters.

## The statements

Three propositions are formulated: the [[proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line|Riemann hypothesis]], the [[proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half|half-plane form]] of the generalized Riemann hypothesis (no Dirichlet \(L\)-function vanishes in \(\operatorname{Re}s>\tfrac12\), the pole excepted), and the [[proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line|critical-line form]] (zeros in \(0<\operatorname{Re}s<1\) have real part \(\tfrac12\)), with its restriction to primitive characters. Characters are not assumed primitive.

## From the half-plane to the line

The half-plane form is the [[?lean:New.grh|half-plane theorem]]. The other forms follow by the reflection \(s\mapsto1-s\): the [[proofs/grh/reduction-zeros/zero-symmetry|symmetry of the zeros]], a consequence of the functional equation of the primitive character inducing \(\chi\) (with the [[proofs/grh/reduction-zeros/euler-factors-nonvanishing|non-vanishing of the Euler factors]] off the imaginary axis), sends a zero \(s\) of \(L(\cdot,\chi)\) in the strip to the zero \(1-s\) of \(L(\cdot,\chi^{-1})\); neither can lie to the right of \(\tfrac12\). This gives [[proofs/grh/reduction-zeros/zeros-on-line-from-half-plane|the critical-line form]] and, for the modulus \(1\), [[proofs/grh/reduction-zeros/zeta-zeros-on-line-from-half-plane|the Riemann hypothesis]].

## Notation for the criterion

Throughout, \(d\) is a prime, \(\chi_K=(\cdot/d)\) the Legendre symbol (the character of \(K=\mathbb{Q}(\sqrt{-d})\) when \(d\equiv3\bmod4\)), \(q\ge1\) a modulus, \(E_\chi\) [[?lean:New.entireL|the \(L\)-function of \(\chi\) with the pole removed]] and \(\psi\chi_K\) the [[?lean:New.quadTwist|quadratic twist]] modulo \(qd\). The objects are

* the [[proofs/grh/reduction-zeros/weight-lambda-k|weight]] \(\lambda(n)=\Lambda(n)(1-\chi_K(n))\) on \(n\equiv1\bmod q\), which is \(\ge0\);
* the function [[proofs/grh/reduction-zeros/log-deriv-mean|\(G_q\)]], the mean over \(\psi\bmod q\) of \(E_{\psi\chi_K}'/E_{\psi\chi_K}-E_\psi'/E_\psi\), less \(1/\varphi(q)\);
* the [[proofs/grh/reduction-zeros/prime-remainder|remainder]] \(R_q(x)=\sum_{n\le x}\lambda(n)(1/n-1/x)-\log x/\varphi(q)-c_q\), \(c_q=\operatorname{Re}G_q(1)\).

## The transform of the remainder

For odd \(d\) prime to \(q\), orthogonality of characters and the [[proofs/grh/reduction-zeros/dirichlet-series-of-chi-lambda|series of \(\chi\Lambda\)]] give the [[proofs/grh/reduction-zeros/dirichlet-series-of-weight|Dirichlet series of the weight]], \(s/(\varphi(q)(s-1))+G_q(s)\); here it matters that [[proofs/grh/reduction-zeros/quad-twist-not-principal|no twist is principal]]. Partial summation and the [[proofs/grh/reduction-zeros/growth-of-prime-remainder|growth bounds]] turn this into the [[proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder|Laplace transform of \(R_q(e^{v})\)]], namely \((G_q(s)/s-c_q)/(s-1)\). Since the transform of a real function is real on the real axis, [[proofs/grh/reduction-zeros/g-q-at-one-is-real|\(G_q(1)\) is real]], so there is no pole at \(1\). The poles of \(G_q\) are simple with residues given by orders of vanishing ([[proofs/grh/reduction-zeros/residue-of-log-deriv-entire-l|one \(L\)-function]], [[proofs/grh/reduction-zeros/residues-of-log-deriv-mean|the mean]]; the functions \(E_\chi\) are entire, not zero, and zero-free on \(\operatorname{Re}s\ge1\) by the [[proofs/grh/reduction-zeros/entire-l-basic-properties|basic properties]]). The outcome is that \(v\mapsto R_q(e^{v})\) is a [[proofs/grh/reduction-zeros/polar-function|polar function]]: [[proofs/grh/reduction-zeros/prime-remainder-is-polar|its transform has at most simple poles in \(\operatorname{Re}s>0\)]] with residue
\[
\frac{n(s)-n'(s)}{\varphi(q)\,s(1-s)},
\]
where \(n(s)\) and \(n'(s)\) count the zeros at \(s\) of the \(E_\psi\) and of the twists \(E_{\psi\chi_K}\). For \(q=1\) the constant is [[proofs/grh/reduction-zeros/g-one-and-chowla-selberg-constant|\(c_1=-1-\gamma+\operatorname{Re}L'/L(1,\chi_K)\)]]. A [[proofs/grh/reduction-zeros/mertens-type-bound|bound of Mertens type]] is recorded for later use.

## Landau's lemma

[[proofs/grh/reduction-zeros/landau-lemma|Landau's lemma]] says that the Laplace transform of a nonnegative measure is not analytic at its abscissa of convergence; a variant allows [[proofs/grh/reduction-zeros/landau-lemma-with-simple-pole|a simple pole whose residue has real part \(\le0\)]]. A one-sided bound \(E(v)\le e^{(\beta-1)v}\) produces such a [[proofs/grh/reduction-zeros/measure-for-one-sided-bound|measure]], and the conclusion is that a polar function with this bound, whose residues at real points \(x>\beta\) have real part \(\ge0\), has [[proofs/grh/reduction-zeros/no-pole-right-of-beta|no pole in \(\operatorname{Re}s>\beta\)]].

## The criterion

The [[proofs/grh/reduction-zeros/one-sided-criterion|one-sided criterion]]: if \(8\mid q_0\), \(d_0\equiv7\bmod8\) is prime to \(q_0\), \(\beta>\tfrac12\), and \(R_{q_0}(x)\le x^{\beta-1}\) for large \(x\) for every prime \(d\equiv d_0\bmod q_0\), then no \(L(s,\psi)\), \(\psi\bmod q_0\), vanishes in \(\operatorname{Re}s>\beta\) (\(s\ne1\)). At real points \(\beta<x<1\) the residue \(n(x)/(\varphi x(1-x))\) has the right sign provided the twists contribute nothing, and this is arranged by the choice of \(d\).

## Choosing the prime: zero density for quadratic twists

The [[proofs/grh/reduction-zeros/choice-of-prime|choice of the prime]] rests on a count: [[proofs/grh/reduction-zeros/bad-primes-are-rare|bad primes are rare]], that is, the primes \(d\le X\) of the class for which some \(L(s,\xi\chi_K)\) has a zero in a box \(\operatorname{Re}s\ge\tfrac12+9\delta\), \(\lvert\operatorname{Im}s\rvert\le H\) number \(O(X^{1-\delta/2})\), while \(\sum\log p/p\) over the class diverges. The count uses [[proofs/grh/reduction-zeros/theta-series-of-coefficients|theta series with a Gaussian weight]]: their [[proofs/grh/reduction-zeros/mellin-of-theta-series|Mellin transforms]] are \(\Gamma_jL\) and \(\Gamma_j/L\); [[proofs/grh/reduction-zeros/poisson-summation-for-character-theta|Poisson summation]] and the [[proofs/grh/reduction-zeros/gauss-sum-modulus|modulus of the Gauss sum]] give [[proofs/grh/reduction-zeros/riemann-formula-for-character|Riemann's formula in \(\operatorname{Re}s>0\) and the symmetry \(u\mapsto1/(qu)\)]]. With the [[proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier|tail integral \(J\) and the mollifier]], the three-lines theorem shows that [[proofs/grh/reduction-zeros/zero-forces-large-tail-integral|a zero in the box forces \(J>T^{2\delta}\)]]. On the other side, [[proofs/grh/reduction-zeros/legendre-as-jacobi-of-odd-part|reciprocity]] writes the twisted coefficients as \(\psi(n)(-d/n^{\circ})\), and the [[proofs/grh/reduction-zeros/mean-value-theta-jacobi|mean value estimate]] bounds the sum of \(J\) over all \(v\le T^2\) by \(O(T^{2+\delta})\), using only the [[proofs/grh/reduction-zeros/polya-vinogradov|Pólya–Vinogradov inequality]] for [[proofs/grh/reduction-zeros/jacobi-symbol-sums|Jacobi symbol sums]]. A [[proofs/grh/reduction-zeros/twist-of-primitive-is-primitive|twist of a primitive character is primitive]], which lets the count pass through primitive characters.

## The prime number theorem for the remainder

Independently of the criterion, \(R_q(y)\to0\), which identifies \(c_q\): the [[proofs/grh/reduction-zeros/pnt-for-prime-remainder|prime number theorem for \(R_q\)]] gives \(\lvert R_q(y)\rvert\le(\log y)^{-B}\). The remainder is [[proofs/grh/reduction-zeros/prime-remainder-as-integral|an integral of the counting error]] and so [[proofs/grh/reduction-zeros/prime-remainder-varies-slowly|varies slowly]]; a [[proofs/grh/reduction-zeros/tauberian-theorem|Tauberian theorem]] (built on [[proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean|Gamma means]] and a [[proofs/grh/reduction-zeros/cauchy-estimate-for-slope|Cauchy estimate]]) converts the [[proofs/grh/reduction-zeros/bound-for-log-deriv-mean-near-one|bound for \(G_q(s)/s\)]] left of the line \(\operatorname{Re}s=1\) into the decay. That bound comes from the [[proofs/grh/reduction-zeros/zero-free-region|zero-free region]], proved from the [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-function]] by a [[proofs/grh/reduction-zeros/linear-bound-regular-l|linear bound]], a [[proofs/grh/reduction-zeros/bound-regular-l-near-one-line|three-lines bound near the line]] and the [[proofs/grh/reduction-zeros/lower-bound-right-of-one|3-4-1 lower bound]].

## Primes in a logarithmic window

Finally the library supplies, for the choice of auxiliary primes elsewhere, [[proofs/grh/reduction-zeros/prime-in-log-window|a prime \(p\equiv1\bmod M^{k}\) with \(\log p\) in a prescribed window]], by Newman's method ([[proofs/grh/reduction-zeros/newman-circle-bound|bound on the circle]]) on a [[proofs/grh/reduction-zeros/zero-free-disc-uniform|zero-free disc about \(1\) that is uniform in \(k\)]], and the [[proofs/grh/reduction-zeros/totient-lower-bound|totient bound]] \(n\le\varphi(n)(2\log n+1)\).

## References

1. Lean: the files listed in the front matter, under `documents/grh-lean/grh/src/`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, Cambridge University Press, 2007 (the source named in most of the Lean file heads).
