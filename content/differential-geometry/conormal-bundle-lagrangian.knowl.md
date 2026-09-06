+++
id = "differential-geometry/conormal-bundle-lagrangian"
title = "Conormal bundle is Lagrangian"
kind = "theorem"
summary = "The conormal bundle of an embedded submanifold is Lagrangian in the ambient cotangent bundle."
aliases = ["Lagrangian conormal theorem"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/cotangent-bundle", "differential-geometry/canonical-symplectic-form-cotangent", "differential-geometry/lagrangian-submanifold", "fiber-bundles/zero-section"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(S\subseteq Q\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]] of a smooth \(n\)-manifold. Its conormal bundle
\[
N^*S=\{\alpha_q\in T^*Q:q\in S,\ \alpha_q(v)=0\text{ for every }v\in T_qS\}
\]
is an embedded \(n\)-dimensional submanifold of the [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*Q\). With the [[differential-geometry/canonical-symplectic-form-cotangent|canonical symplectic form]] on \(T^*Q\), the submanifold \(N^*S\) is [[differential-geometry/lagrangian-submanifold|Lagrangian]]. This includes the [[fiber-bundles/zero-section|zero section]] as the case \(S=Q\). The statement uses the full conormal bundle over \(S\), including its zero covectors; deleting the zero section gives another, nonclosed Lagrangian submanifold.

## Proof mechanism

Let \(\lambda\) denote the tautological one-form on \(T^*Q\), so that at \(\alpha_q\),
\[
\lambda_{\alpha_q}(\xi)=\alpha_q(d\pi(\xi)).
\]
If \(\xi\in T_{\alpha_q}N^*S\), then \(d\pi(\xi)\in T_qS\), while \(\alpha_q\) annihilates \(T_qS\). Hence \(\lambda|_{N^*S}=0\), and therefore the canonical symplectic form, whether defined as \(d\lambda\) or \(-d\lambda\), restricts to zero on \(N^*S\). The conormal bundle has rank \(\operatorname{codim}_Q S\) over \(S\), so
\[
\dim N^*S=\dim S+\operatorname{codim}_Q S=n=\tfrac12\dim T^*Q.
\]
Isotropy plus this dimension count proves the theorem.

## Examples and local coordinates

If local coordinates \((x^1,\ldots,x^k,y^1,\ldots,y^{n-k})\) make \(S\) the locus \(y=0\), then
\[
N^*S=\{y=0,\ p_x=0\}
\]
in the induced cotangent coordinates \((x,y,p_x,p_y)\). The free coordinates are \(x\) and \(p_y\), visibly giving dimension \(n\), and the canonical form restricts to zero.

For a point \(q\in Q\), the conormal bundle is the entire cotangent fiber \(T_q^*Q\), which is Lagrangian. For an open submanifold \(S\subseteq Q\), it is the zero section over \(S\). The [[differential-geometry/normal-bundle|normal bundle]] of a Riemannian embedding is not the same object until a metric identifies tangent and cotangent vectors.

## Geometric significance

Conormal bundles are the basic Lagrangians attached functorially to submanifolds. Their punctured versions are conic Lagrangians and provide the phase-space geometry used to record singular directions of distributions and kernels in microlocal analysis. The theorem depends only on the embedding \(S\hookrightarrow Q\), whereas identifying \(N^*S\) with a normal bundle requires auxiliary metric data.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, 2nd ed., Springer, 1990. [DOI record](https://doi.org/10.1007/978-3-642-96750-4). Relevant: §21.2, conormal bundles as canonical Lagrangian submanifolds.
2. Victor Guillemin and Shlomo Sternberg, *Geometric Asymptotics*, revised ed., Mathematical Surveys and Monographs 14, American Mathematical Society, 1977. [DOI record](https://doi.org/10.1090/surv/014). Relevant: Chapter IV, cotangent symplectic geometry and conormal examples.
