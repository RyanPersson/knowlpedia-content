+++
id = "differential-geometry/maslov-class-lagrangian-grassmannian"
title = "Maslov class of the Lagrangian Grassmannian"
kind = "definition"
summary = "The canonical generator of the first integral cohomology of the real Lagrangian Grassmannian."
aliases = ["universal Maslov class"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For \(n\geq1\), identify the real [[differential-geometry/lagrangian-grassmannian|Lagrangian Grassmannian]] with \(\Lambda(n)=U(n)/O(n)\). Since \(\det(AQ)^2=\det(A)^2\) for \(Q\in O(n)\), the map
\[
\det^2:\Lambda(n)\longrightarrow S^1,\qquad [A]\longmapsto\det(A)^2
\]
is well defined. The **Maslov class of the Lagrangian Grassmannian** is
\[
\mu_\Lambda=(\det^2)^*\eta\in H^1(\Lambda(n);\mathbb Z),
\]
where \(\eta\) is the positively oriented generator of \(H^1(S^1;\mathbb Z)\). The map \(\det^2\) induces an isomorphism on [[topology/fundamental-group|fundamental groups]], so \(\mu_\Lambda\) is a generator of \(H^1(\Lambda(n);\mathbb Z)\) [Arnol'd, 1967](https://doi.org/10.1007/BF01079201). The sign is fixed by declaring counterclockwise rotation of a Lagrangian line through a half-turn to have value \(+1\).

## Evaluation on loops

If \(\ell:S^1\to\Lambda(n)\) is a loop and \(A(t)\) is a path of unitary representatives, then
\[
\langle\mu_\Lambda,[\ell]\rangle
=\operatorname{wind}\bigl(\det(A(t))^2\bigr).
\]
Although \(A(1)\) may differ from \(A(0)\) by an orthogonal matrix, squaring the determinant makes the phase close. Robbin and Salamon give the equivalent formula using a unitary frame and its determinant phase [Robbin–Salamon, Remark 2.6](https://doi.org/10.1016/0040-9383%2893%2990052-W).

## Duality with the Maslov cycle

Fix a reference Lagrangian \(L_0\). With its standard coorientation, the [[differential-geometry/maslov-cycle|Maslov cycle]] \(\Sigma(L_0)\) represents the Poincaré dual of \(\mu_\Lambda\) in the intersection-theoretic sense. Therefore a generic loop evaluates on \(\mu_\Lambda\) by its signed number of crossings with \(\Sigma(L_0)\). Changing \(L_0\) changes the representative cycle but not the cohomology class [Arnol'd, 1967](https://doi.org/10.1007/BF01079201).

## Normalization in dimension one

For \(\Lambda(1)=U(1)/O(1)\cong\mathbb RP^1\), write a line as \(e^{i\theta}\mathbb R\), with \(\theta\) defined modulo \(\pi\). Then \(\det^2\) sends it to \(e^{2i\theta}\). The loop \(\theta:0\to\pi\) winds once around \(S^1\), so its Maslov number is \(1\). Conventions assigning \(2\) to this loop use twice the generator defined here.

## Conventions and scope

The generator of an infinite cyclic group is determined only up to sign until a positive rotation convention is chosen. Some symplectic-path indices use a doubled normalization, and some endpoint-inclusive path indices take half-integer values. Those choices do not alter the integral universal class defined here but do alter formulas that compare different index conventions.

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: construction of the characteristic class and its cycle.
2. Joel Robbin and Dietmar Salamon, “The Maslov index for paths,” *Topology* 32 (1993), 827–844. [DOI record](https://doi.org/10.1016/0040-9383%2893%2990052-W). Relevant: Remark 2.6 and §§2–3.
