+++
id = "posts/chojecki-riemann-hypothesis"
title = "Przemek Chojecki on Alpöge’s Riemann hypothesis announcement"
kind = "document"
summary = "An annotated transcript of @prz_chojecki’s post on prime sums, CM points and theta lifts. Select a term to unfold its meaning."
aliases = ["Chojecki tweet", "annotated Riemann hypothesis tweet"]
domains = ["posts"]
section_mode = "continuous"
prerequisites = []
+++

**Przemek Chojecki | PC** (@prz_chojecki), transcribed from the supplied screenshot.

> I had some fun fleshing out more details in [[posts/alpoge-riemann-announcement|Alpoge's]]
> [[analytic-number-theory/riemann-hypothesis|Riemann Hypothesis]] proof.
>
> Mostly I wanted to see how [[langlands|Langlands program]] plays into the proof (my PhD area of research).
> Basically the full argument can be summarized as follows (thanks
> [[posts/alpoge-riemann-announcement|Fable+Astra]]):
>
> To prove [[analytic-number-theory/dirichlet-grh|GRH]], it's proven by
> [[analytic-number-theory/landau-singularity-theorem|Landau]] that it's enough to establish a certain
> [[shared-foundations/upper-bound|upper bound]] on a [[analytic-number-theory/weighted-prime-sum|prime sum]].
>
> That [[shared-foundations/upper-bound|upper bound]] comes from a
> [[arithmetic-geometry/diophantine-inequality|Diophantine inequality]] in the style of
> [[arithmetic-geometry/stepanov-method|Stepanov's proof]] for
> [[algebraic-geometry-foundations/algebraic-curve|curves]], carried out with
> [[arithmetic-geometry/arakelov-slope|Arakelov slopes]] instead of
> [[arithmetic-geometry/degree-of-a-divisor|degrees]]. One builds
> [[arithmetic-geometry/integral-automorphic-form|integral automorphic forms]] on
> [[arithmetic-geometry/unitary-shimura-variety|unitary Shimura varieties]] over an
> [[arithmetic-geometry/abelian-cm-field|auxiliary abelian CM field]] and
> [[arithmetic-geometry/evaluation-at-a-cm-point|evaluates them]] at [[arithmetic-geometry/cm-point|CM points]]
> that are, [[arithmetic-geometry/isogeny|up to isogeny]],
> [[arithmetic-geometry/power-of-an-elliptic-curve|powers]] of an
> [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] with
> [[arithmetic-geometry/complex-multiplication|CM]] by [[algebra-fields-galois/imaginary-quadratic-field|Q(√−d)]].
> At [[arithmetic-geometry/inert-prime|primes inert]] in that
> [[algebra-fields-galois/imaginary-quadratic-field|quadratic field]], the
> [[arithmetic-geometry/evaluation-at-a-cm-point|evaluations]] are forced to be
> [[shared-foundations/p-adic-valuation|p-adically divisible]], and the
> [[arithmetic-geometry/inert-prime-divisibility|total forced divisibility]] is a
> [[analytic-number-theory/weighted-prime-sum|truncated sum]] of
> [[analytic-number-theory/von-mangoldt-function|log p]] over [[analytic-number-theory/prime-power|prime powers]].
> Their [[arithmetic-geometry/archimedean-size|archimedean size]] is a
> [[asymptotics/stirlings-approximation|Stirling term]] plus a
> [[arithmetic-geometry/chowla-selberg-period|Chowla-Selberg period]], which carries
> [[analytic-number-theory/l-logarithmic-derivative-at-one|L’/L(1)]]. The
> [[arithmetic-geometry/slope-inequality|slope inequality]] says
> [[arithmetic-geometry/slope-inequality|divisibility cannot exceed size]]. A
> [[analytic-number-theory/finite-fourier-inversion|finite Fourier identity]] on the
> [[algebra-fields-galois/galois-group|Galois group]] shows that
> "[[analytic-number-theory/prime-sum-balance|divisibility minus size]]" is exactly a sum of
> [[analytic-number-theory/centered-prime-sum|regularised prime sums]] over all
> [[analytic-number-theory/galois-character|characters of the field]], and a
> [[analytic-number-theory/character-projection|choice of weights]] isolates the
> [[analytic-number-theory/dirichlet-character|target characters]]. A
> [[arithmetic-geometry/iterated-theta-lifts|chain of about √x]] [[arithmetic-geometry/theta-lift|theta lifts]]
> plays the role of [[arithmetic-geometry/order-of-vanishing|vanishing to order √x]], which is where the
> [[analytic-number-theory/square-root-bound|exponent 1/2]] comes from. The
> [[arithmetic-geometry/integral-lattice-comparison|integral comparison]] needs
> [[shared-foundations/upper-bound|bounds]] on certain
> [[arithmetic-geometry/galois-cohomology|Galois cohomology groups]]
> ([[algebra-fields-galois/ideal-class-group|class-group-like]], of
> [[arithmetic-geometry/vandiver-type-bound|Vandiver type]]), which are proved only on
> [[analytic-number-theory/scale-window|windows]]; that is why
> [[analytic-number-theory/landau-singularity-theorem|Landau's theorem]] had to be
> [[analytic-number-theory/windowed-landau-criterion|windowed]].

## Reading the argument

Read the last paragraph in two directions. Starting with a zero of an \(L\)-function, the [[analytic-number-theory/windowed-landau-criterion|window criterion]] explains which prime-sum bound would rule it out. Starting with an integral value at a CM point, [[arithmetic-geometry/slope-inequality|the slope inequality]] limits how much prime divisibility it can carry. The [[analytic-number-theory/prime-sum-balance|character identity]] translates between these two kinds of information. In this post GRH concerns Dirichlet \(L\)-functions.

The Langlands connection is easiest to see at the two ends of a [[arithmetic-geometry/theta-lift|theta lift]]. Both ends carry automorphic forms on unitary groups. Farther along, the [[langlands/automorphic-galois-correspondence|automorphic–Galois correspondence]] attaches Galois representations to suitable automorphic representations. These enter the argument for the cohomological bounds in the last sentence.

For the terms in reading order, open the [analytic number theory index](/analytic-number-theory/) or the [arithmetic geometry index](/arithmetic-geometry/).

## References

- Przemek Chojecki (@prz_chojecki), post reproduced from the supplied screenshot.
- Levent Alpöge, [announcement, pp. 1 and 3–4](https://alpo.ge/remark.pdf).
- Manvir Jaswal, [reading of the released formalization, §§3–5](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
- Siniša Slijepčević, [outline, §§9–10, the cohomological estimates and their automorphic inputs](https://hexagonmath.org/pdf/2611.00812).
