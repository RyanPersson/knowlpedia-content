+++
id = "mathematical-physics/georgi-glashow-su5-embedding"
title = "Georgi–Glashow SU(5) embedding"
kind = "construction"
summary = "The Standard Model central quotient embedded block-diagonally in SU(5)."
aliases = ["SU(5) Standard Model embedding", "Georgi-Glashow embedding"]
domains = ["mathematical-physics", "lie-groups"]
prerequisites = ["lie-groups/special-block-unitary-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

The **Georgi–Glashow \(SU(5)\) homomorphism** is
\[
\Phi:U(1)\times SU(2)\times SU(3)\longrightarrow SU(5),
\qquad
\Phi(z,A,B)=
\begin{pmatrix}
z^3A&0\\
0&z^{-2}B
\end{pmatrix}.
\]
Its image is [[lie-groups/special-block-unitary-group|\(S(U(2)\times U(3))\)]], and its kernel is
\[
\{(z,z^{-3}I_2,z^2I_3):z^6=1\}\cong\mathbb Z_6.
\]
It therefore induces an embedding
\[
\overline\Phi:
\bigl(U(1)\times SU(2)\times SU(3)\bigr)/\mathbb Z_6
\hookrightarrow SU(5).
\]

## Why the exponents are \(3\) and \(-2\)

The scalar actions commute with \(SU(2)\times SU(3)\), while
\[
(z^3)^2(z^{-2})^3=1
\]
ensures determinant one. For \(z=e^{i\theta}\), differentiating the scalar
part gives the compact Lie-algebra element
\[
i\operatorname{diag}(3,3,-2,-2,-2).
\]
The associated Hermitian weight matrix is
\(\operatorname{diag}(3,3,-2,-2,-2)\); after dividing by \(3\), it is the
weak-hypercharge operator in the convention \(Q=T_3+Y/2\).

## Terminology

The direct product does **not** embed injectively by \(\Phi\). “The Standard Model embedding in \(SU(5)\)” means the induced embedding of its \(\mathbb Z_6\) quotient, equivalently the inclusion \(S(U(2)\times U(3))\subset SU(5)\).

## Representation-theoretic role

Restricting the natural \(SU(5)\)-action on \(\bigwedge\mathbb C^5\) along \(\Phi\) gives the [[mathematical-physics/standard-model-exterior-algebra-representation|exterior-algebra model of one Standard Model generation and its antiparticles]].

## Physics scope

Mathematically, this is a [[algebra-groups/group-homomorphism|group homomorphism]] and representation extension. The original Georgi–Glashow model additionally interprets \(SU(5)\) as a unified gauge symmetry and introduces dynamics and symmetry breaking; those claims are extra structure.

## References

1. Howard Georgi and Sheldon L. Glashow, “Unity of All Elementary-Particle Forces,” *Physical Review Letters* 32 (1974), 438–441. [DOI record](https://doi.org/10.1103/PhysRevLett.32.438).
2. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §3.1.
3. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§1 and 8.
