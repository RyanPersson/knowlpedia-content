+++
id = "algebra-fields-galois/finite-field-existence-uniqueness"
title = "Existence and uniqueness of finite fields"
kind = "knowl"
summary = "For each prime power q=p^n there is a unique (up to isomorphism) field with q elements."
aliases = ["finite-field-existence-uniqueness", "Existence and uniqueness of finite fields"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/finite-field-existence-uniqueness.md"
prerequisites = ["algebra-fields-galois/finite-field", "algebra-rings/characteristic"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[algebra-fields-galois/finite-field|finite field]] is a field with finitely many elements.

**Theorem (Existence and uniqueness).** Let \(q=p^n\) where \(p\) is prime and \(n\ge1\).
1. (**Existence**) There exists a field \(\mathbb{F}_q\) with exactly \(q\) elements. It has [[algebra-rings/characteristic|characteristic]] \(p\).
2. (**Uniqueness up to isomorphism**) Any two fields with \(q\) elements are isomorphic.

For existence, choose an irreducible polynomial \(f(x)\in\mathbb F_p[x]\) of degree \(n\). Then \(\mathbb F_p[x]/(f)\) is a field of order \(p^n\).

## Remarks

Every field of order \(q\) is a [[algebra-fields-galois/splitting-field|splitting field]] of \(x^q-x\) over \(\mathbb F_p\), so uniqueness follows from uniqueness of splitting fields up to \(\mathbb F_p\)-isomorphism. The isomorphism itself need not be unique: \(\mathbb F_{p^n}\) has \(n\) automorphisms over \(\mathbb F_p\).

### Examples
1. \(q=p\). Then \(\mathbb{F}_p\cong \mathbb{Z}/p\mathbb{Z}\) is the unique field of order \(p\).

2. \(q=4=2^2\). Take \(f(x)=x^2+x+1\in\mathbb{F}_2[x]\), which has no root in \(\mathbb{F}_2\) and hence is irreducible.
   Then \(\mathbb{F}_4\cong \mathbb{F}_2[x]/(x^2+x+1)\).

3. \(q=9=3^2\). The polynomial \(f(x)=x^2+1\in\mathbb{F}_3[x]\) has no root in \(\mathbb{F}_3\) (since \(0^2+1=1\), \(1^2+1=2\), \(2^2+1=2\)), so it is irreducible.
   Then \(\mathbb{F}_9\cong \mathbb{F}_3[x]/(x^2+1)\).
