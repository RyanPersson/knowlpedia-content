+++
id = "operator-algebras/cstar-identity"
title = "C*-identity"
kind = "definition"
summary = "The norm identity equating the squared norm of an element with the norm of its adjoint product."
aliases = ["C*-norm identity"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a complex
[[operator-algebras/involutive-algebra|involutive algebra]] with a
submultiplicative norm. The norm satisfies the
**\(C^*\)-identity** when
\[
\lVert a^*a\rVert=\lVert a\rVert^2
\qquad\text{for every }a\in A.
\]
This is an identity for all elements, not merely an inequality or a condition
on self-adjoint elements. If \(A\) is complete, so that its underlying normed
algebra is a [[functional-analysis/banach-algebra|Banach algebra]], this axiom
makes \(A\) a \(C^*\)-algebra. Unitality is not part of the identity, and no
separate compatibility constant between the involution and norm is allowed.

## Immediate consequences

Submultiplicativity and the \(C^*\)-identity force the involution to be
isometric:
\[
\lVert a^*\rVert=\lVert a\rVert.
\]
Indeed, applying the identity to \(a\) and \(a^*\) gives the two inequalities
needed for equality. In the unital case the same identity gives
\(\lVert 1\rVert=1\) unless the algebra is zero. These consequences explain
why the involution need not be declared continuous as a separate
\(C^*\)-algebra axiom.

## Spectral rigidity

For every \(a\) in a \(C^*\)-algebra,
\[
\lVert a\rVert^2=r(a^*a),
\]
where \(r\) denotes spectral radius. Thus the algebraic operations and spectrum
determine the norm far more rigidly than in a general Banach
\(*\)-algebra. In particular, an injective \(*\)-homomorphism between
\(C^*\)-algebras is automatically isometric.

## Examples and non-examples

The [[linear-algebra/operator-norm|operator norm]] on \(\mathcal B(H)\)
satisfies the identity because
\(\lVert T^*T\rVert=\lVert T\rVert^2\). A Banach \(*\)-algebra whose norm only
satisfies \(\lVert a^*\rVert=\lVert a\rVert\) is a near-miss: isometric
involution does not by itself imply the \(C^*\)-identity.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Definition 2.1.1 and the norm consequences immediately following it.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.1 on the defining norm identity.
