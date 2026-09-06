+++
id = "operator-algebras/corona-algebra"
title = "Corona C*-algebra"
kind = "definition"
summary = "The quotient of the multiplier algebra of a C-star algebra by its canonical essential ideal."
aliases = ["corona algebra", "M(A)/A", "Calkin-type corona"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/essential-ideal", "operator-algebras/multiplier-algebra", "operator-algebras/quotient-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]],
canonically embedded as an
[[operator-algebras/essential-ideal|essential ideal]] in its
[[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(A)\). The
**corona algebra** of \(A\) is the
[[operator-algebras/quotient-cstar-algebra|quotient \(C^*\)-algebra]]
\[
Q(A)=M(A)/A.
\]
Its elements are multiplier classes modulo those implemented by elements of
\(A\). The definition applies to every \(C^*\)-algebra, but it is most useful
for nonunital \(A\): if \(A\) is unital, then \(M(A)=A\) and \(Q(A)=0\).
Some authors write \(\mathcal Q(A)\) or \(\mathcal C(A)\) instead of \(Q(A)\).

## Fundamental examples

For an infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]]
\(H\),
\[
Q(\mathcal K(H))\cong\mathcal B(H)/\mathcal K(H),
\]
the Calkin algebra, because
\(M(\mathcal K(H))\cong\mathcal B(H)\), with
[[operator-algebras/compact-operator-cstar-algebra|\(\mathcal K(H)\)]] the
[[linear-algebra/compact-operator|compact operators]] and
[[operator-algebras/bounded-operator-cstar-algebra|\(\mathcal B(H)\)]] the
bounded operators. In the commutative case \(A=C_0(X)\), where \(X\) is
[[topology/locally-compact-space|locally compact]] Hausdorff,
\(M(A)\cong C_b(X)\); after identifying \(C_b(X)\) with
\(C(\beta X)\), the corona is \(C(\beta X\setminus X)\). The topological
remainder motivates the name “corona.”

## Extension-theoretic role

An extension
\[
0\longrightarrow A\longrightarrow E\longrightarrow B\longrightarrow0
\]
whose copy of \(A\) is essential determines a \(*\)-homomorphism
\(\tau:B\to Q(A)\), called its Busby invariant. Conversely, a suitable
\(*\)-homomorphism into \(Q(A)\) reconstructs an extension by a pullback.
This correspondence is the reason corona algebras organize extension theory.

## Scope and cautions

The corona is not the [[operator-algebras/unitization|unitization]] of \(A\):
it is a quotient of the generally much larger multiplier algebra. Nor must
\(Q(A)\) be nonzero when \(A\ne0\), as the unital case shows. Structural
properties such as simplicity, separability, and exactness do not pass
automatically from \(A\) to its corona.

## References

1. Robert C. Busby, “Double Centralizers and Extensions of C*-Algebras,” *Transactions of the American Mathematical Society* 132 (1968), 79–99. [AMS DOI record](https://doi.org/10.1090/S0002-9947-1968-0225175-5). Relevant: §§3–4 on multiplier quotients, Busby invariants, and extensions.
2. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 2 on multiplier algebras and their quotients.
