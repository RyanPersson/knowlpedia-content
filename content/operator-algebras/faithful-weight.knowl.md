+++
id = "operator-algebras/faithful-weight"
title = "Faithful weight"
kind = "definition"
summary = "A weight whose zero set on the positive cone contains only the zero element."
aliases = ["faithfulness of a weight"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/weight-on-von-neumann-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let
\(\varphi:M_+\to[0,+\infty]\) be a
[[operator-algebras/weight-on-von-neumann-algebra|weight]]. The weight
\(\varphi\) is **faithful** if
\[
x\in M_+,\quad \varphi(x)=0\quad\Longrightarrow\quad x=0.
\]
Equivalently, \(\varphi(a^*a)=0\) implies \(a=0\) for every \(a\in M\).
Faithfulness is a nondegeneracy condition only: it neither requires
\(\varphi(x)<\infty\) for nonzero \(x\) nor asserts normality or semifiniteness.
In particular, an extended-valued weight can be faithful even when its finite
domain is small. The ambient positive cone is essential because a weight is
not generally a complex-valued functional on all of \(M\).

## Null ideal

The set
\[
\mathfrak n_\varphi^0=\{a\in M:\varphi(a^*a)=0\}
\]
is the null left ideal used when constructing the [[linear-algebra/hilbert-space|Hilbert space]] associated
with a weight. Faithfulness is exactly the assertion
\(\mathfrak n_\varphi^0=\{0\}\). For a nonfaithful weight, quotienting by this
ideal removes directions invisible to \(\varphi\), just as the null space is
removed in the [[operator-algebras/gns-construction|GNS construction]] for a [[operator-algebras/positive-linear-functional|positive functional]].

## Support

For a [[operator-algebras/normal-weight|normal weight]], there is a support
projection \(s(\varphi)\) such that \(\varphi\) is faithful on the corner
\(s(\varphi)Ms(\varphi)\). Faithfulness is equivalent to
\(s(\varphi)=1\). This support formulation depends on normality; it should not
be used as the definition for an arbitrary weight without first establishing
that the relevant support projection exists.

## Examples and independence

The [[operator-algebras/operator-trace|canonical operator trace]] on \(B(H)\)
is faithful: a positive operator with zero trace is zero. A
[[operator-algebras/vector-state|vector state]] on \(B(H)\) is generally not
faithful, because any nonzero positive operator annihilating the chosen vector
has value zero. The weight that is \(0\) at \(0\) and \(+\infty\) on every
nonzero positive element is faithful but not semifinite, demonstrating that
the two conditions are logically independent.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VII, §1 on faithful weights and their null ideals.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: the opening chapters on faithful normal semifinite weights and support.
