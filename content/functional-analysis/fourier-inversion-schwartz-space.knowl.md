+++
id = "functional-analysis/fourier-inversion-schwartz-space"
title = "Fourier inversion on Schwartz space"
kind = "theorem"
summary = "Every Schwartz function is recovered pointwise and in the Schwartz topology from its Fourier transform."
aliases = ["Schwartz Fourier inversion"]
domains = ["functional-analysis", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/fourier-transform-schwartz-space", "functional-analysis/schwartz-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f\in\mathcal S(\mathbb R^n)\), and define its
[[functional-analysis/fourier-transform-schwartz-space|Fourier transform]] by
\[
\widehat f(\xi)=\int_{\mathbb R^n}e^{-2\pi i x\cdot\xi}f(x)\,dx.
\]
The **Fourier inversion theorem on Schwartz space** states that
\[
f(x)=\int_{\mathbb R^n}e^{2\pi i x\cdot\xi}\widehat f(\xi)\,d\xi
\]
for every \(x\in\mathbb R^n\). Equivalently,
\(\widehat{\widehat f}(x)=f(-x)\). Thus the inverse Fourier transform is
\(\mathcal F^{-1}g(x)=\widehat g(-x)\), and inversion holds both pointwise and
in the [[functional-analysis/schwartz-space|Schwartz topology]].

## Proof mechanism

One regularizes the inverse integral by a Gaussian factor, interchanges the
resulting absolutely convergent integrals using
[[measure-theory/fubinis-theorem|Fubini's theorem]], and evaluates the
Gaussian Fourier transform. As the regularization parameter tends to zero,
the Gaussian approximate identity converges to \(f\). Rapid decay controls
the limiting passage and permits differentiation, yielding convergence in
every Schwartz seminorm.

## Consequences

Inversion proves that the Fourier transform is injective and surjective on
\(\mathcal S(\mathbb R^n)\). Together with the continuity estimates for
weighted derivatives, it makes the transform a topological automorphism. The
reflection formula also determines the fourth-power identity
\(\mathcal F^4=\mathrm{id}\) under this normalization.

## Conventions and scope

**Warning.** The inverse formula depends on normalization. If the forward
kernel is \(e^{-ix\cdot\xi}\), the inverse carries a factor
\((2\pi)^{-n}\). Inversion for \(L^1\) or \(L^2\) functions requires
different hypotheses or modes of convergence; the statement here is
specifically the Schwartz-space theorem.

## References

1. Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton University Press, 2003. [DOI record](https://doi.org/10.1515/9781400831234). Relevant: Chapters 5–6, Fourier inversion for Schwartz functions.
2. Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999. [Publisher record](https://www.wiley.com/en-us/Real%2BAnalysis%3A%2BModern%2BTechniques%2Band%2BTheir%2BApplications%2C%2B2nd%2BEdition-p-9780471317166). Relevant: Chapter 8 on Fourier analysis.
