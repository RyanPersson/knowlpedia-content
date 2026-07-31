+++
id = "lie-groups/parabolic-subgroup-real-reductive-group"
title = "Parabolic subgroup of a real reductive group"
kind = "definition"
summary = "A subgroup whose Lie algebra contains a minimal parabolic subalgebra of a real reductive Lie algebra."
aliases = ["real parabolic subgroup", "parabolic P"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a connected
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] with Lie
algebra \(\mathfrak g\). A **parabolic subgroup** of \(G\) is a closed
subgroup \(P\) whose [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak p\) is a real parabolic
subalgebra. Concretely, after choosing a Cartan decomposition, a maximal
abelian subspace \(\mathfrak a\) of its noncompact part, and positive
restricted roots, \(\mathfrak p\) must contain
\(\mathfrak p_0=\mathfrak m\oplus\mathfrak a\oplus\mathfrak n\), where
\(\mathfrak m=Z_{\mathfrak k}(\mathfrak a)\) and \(\mathfrak n\) is the sum
of the positive restricted-root spaces. In the standard linear real-reductive
setting, \(P=N_G(\mathfrak p)\). Those parabolics containing the chosen
\(\mathfrak p_0\) are the **standard parabolic subgroups**.

## Classification by simple restricted roots

Fix a positive [[lie-groups/restricted-root-system|restricted-root system]]
with [[lie-groups/simple-root|simple roots]] \(\Delta\). Subsets \(F\subseteq\Delta\) parametrize standard
parabolic subgroups \(P_F\);
inclusion of subsets gives inclusion of the corresponding parabolics. Every
parabolic subgroup is conjugate to a standard one. These statements, including
the passage between parabolic subalgebras and subgroups, are proved for the

## Internal structure and representation theory

Every parabolic has a
[[lie-groups/langlands-decomposition-of-a-parabolic|Langlands decomposition]]
\(P=MAN\). Its nilpotent factor \(N\) is assembled from positive restricted
[[lie-groups/root-space|root spaces]] not belonging to the Levi part, while \(MA\) is reductive. This
decomposition is the structural input for parabolic induction: a
representation of \(MA\), extended trivially across \(N\), can be induced to
\(G\).

## Examples and conventions

For \(G=\operatorname{SL}(n,\mathbb R)\), the subgroups of block upper
triangular matrices are parabolic; the upper triangular subgroup is minimal,
and \(G\) itself is the parabolic corresponding to all simple roots.

**Warning.** Some authors reserve “proper parabolic” for \(P\ne G\). For
disconnected or non-linear reductive groups, the subgroup attached to a
parabolic Lie algebra can differ by finite components, so the ambient class
and normalizer convention must be stated.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/beyond2.html). Relevant: Chapter VII, §7 on parabolic subgroups.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on parabolic subgroups and induced representations.
