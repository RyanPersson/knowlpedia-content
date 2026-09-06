+++
id = "algebra-rings/eisensteins-criterion"
title = "Eisenstein's criterion"
kind = "knowl"
summary = "A divisibility criterion implying that a polynomial is irreducible over the fraction field of a UFD."
aliases = ["eisensteins-criterion", "Eisenstein's criterion"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ufd", "algebra-rings/prime-element", "algebra-rings/polynomial-ring", "algebra-rings/irreducible-polynomial", "algebra-rings/fraction-field"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/eisensteins-criterion.md"
+++

**Eisenstein's criterion**: Let \(R\) be a [[algebra-rings/ufd|UFD]] and let \(p\in R\) be a [[algebra-rings/prime-element|prime element]]. Consider \(f(x)=a_nx^n+\cdots+a_0\in R[x]\) in the [[algebra-rings/polynomial-ring|polynomial ring]] \(R[x]\). If
- \(p\mid a_i\) for all \(i<n\),
- \(p\nmid a_n\), and
- \(p^2\nmid a_0\),
then \(f\) is [[algebra-rings/irreducible-polynomial|irreducible]] in \(\mathrm{Frac}(R)[x]\), where \(\mathrm{Frac}(R)\) is the [[algebra-rings/fraction-field|fraction field]] of \(R\). If \(f\) is primitive, Gauss's lemma also makes it irreducible in \(R[x]\).
