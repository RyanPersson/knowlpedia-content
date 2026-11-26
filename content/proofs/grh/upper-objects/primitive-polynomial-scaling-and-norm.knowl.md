+++
id = "proofs/grh/upper-objects/primitive-polynomial-scaling-and-norm"
title = "Primitive polynomials: scaling of roots, and the product of the roots"
kind = "lemma"
summary = "Primitive polynomials are stable under scaling the roots by an M-th root of unity when M squared divides q-1, and the product of their roots generates the units of the base field."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsPrimitivePolynomial.scaleRoots", "New.IsPrimitivePolynomial.pow_geom_sum_eq_prod_aroots", "New.IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots", "New.IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots_and_exists_pow_eq"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
proof_status = "full"
+++

**Lemma.** Let \(k\) be a finite field with \(q\) elements and \(c\in k[X]\) a [[proofs/grh/upper-objects/primitive-polynomial|primitive polynomial]] of degree \(r\).

1. Let \(M\ge0\) with \(M^2\mid q-1\) and let \(a\in k^\times\) with \(a^M=1\). Then the polynomial \(c_a\) whose roots are those of \(c\) multiplied by \(a\) (with multiplicity; \(c_a(X)=a^{r}c(X/a)\)) is again a primitive polynomial of degree \(r\).
2. For every root \(\xi\in\bar k\) of \(c\), \(\xi^{1+q+\dots+q^{r-1}}\) equals the product \(\nu\) of the roots of \(c\) in \(\bar k\).
3. \(\nu\) is a primitive root of unity of order \(q-1\), i.e. a generator of \(k^\times\).

## Proof

*1.* Scaling the roots by a unit preserves being monic, squarefree, of degree \(r\), with nonzero constant term, and irreducible (it is induced by the automorphism \(X\mapsto X/a\) of \(k[X]\) up to the unit \(a^r\)). Let \(\xi\) be a root of \(c\) of order \(n=q^r-1\); then \(a\xi\) is a root of \(c_a\), and we show it has order \(n\). Let \(o\) be the order of \(a\). Then \(o\mid M\), so \(o^2\mid M^2\mid q-1\mid n\). First \((a\xi)^n=1\) since \(o\mid n\). Conversely let \((a\xi)^e=1\). Then \(\xi^{eo}=a^{-eo}=1\), so \(n\mid eo\), hence \((n/o)\mid e\); as \(o^2\mid n\) we get \(o\mid n/o\mid e\), so \(a^e=1\), so \(\xi^e=1\) and \(n\mid e\).

*2.* Since \(c\) is irreducible of degree \(r\) over the finite field \(k\), its roots are the Frobenius conjugates \(\xi,\xi^q,\dots,\xi^{q^{r-1}}\) of any one root \(\xi\) ([[?c:roots of an irreducible polynomial over a finite field|roots of an irreducible polynomial over a finite field]]). Their product is \(\xi^{1+q+\dots+q^{r-1}}\).

*3.* Take the root \(\xi\) of order \(q^r-1\) and \(e=1+q+\dots+q^{r-1}\), so \(e(q-1)=q^r-1\) and \(q^r-1>0\). A power \(\xi^e\) of an element of order \(e(q-1)\) has order \(q-1\). \(\square\)

## Remarks

Statement 2 says that \(\nu\) is the norm of \(\xi\) from \(\mathbb F_{q^r}\) to \(k\), and that it is one and the same power of every root.

## References

1. Lean: `New.IsPrimitivePolynomial.scaleRoots`, `New.IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots_and_exists_pow_eq` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
