+++
id = "differential-geometry/liouville-vector-field"
title = "Liouville vector field"
kind = "definition"
summary = "The unique vector field dual to a chosen primitive of an exact symplectic form."
aliases = ["symplectic dilation vector field"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/exact-symplectic-manifold", "fiber-bundles/vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be an [[differential-geometry/exact-symplectic-manifold|exact symplectic manifold]] with a specified primitive \(\lambda\), so \(\omega=d\lambda\). The **Liouville vector field** associated with \(\lambda\) is the unique smooth [[fiber-bundles/vector-field|vector field]] \(Z\) satisfying
\[
\iota_Z\omega=\lambda.
\]
Nondegeneracy of \(\omega\) gives existence and uniqueness. Cartan's formula then yields
\[
\mathcal L_Z\omega=d(\iota_Z\omega)+\iota_Zd\omega=d\lambda=\omega.
\]
Thus the local flow of \(Z\) dilates the symplectic form: wherever it is defined, \(\varphi_t^*\omega=e^t\omega\). The field depends on the chosen primitive, not only on \(\omega\).

## Equivalent characterization

A vector field \(Z\) on a [[differential-geometry/symplectic-manifold|symplectic manifold]] is Liouville precisely when
\[
\mathcal L_Z\omega=\omega.
\]
Indeed, this equation implies \(d(\iota_Z\omega)=\omega\), so \(\lambda=\iota_Z\omega\) is a primitive; the converse is the calculation in the core. Accordingly, the existence of a global Liouville vector field forces the symplectic form to be exact.

## Dependence on the primitive

If \(\lambda'=\lambda+\alpha\) is another primitive, then \(\alpha\) is closed and the corresponding field is \(Z'=Z+X\), where \(\iota_X\omega=\alpha\). When \(\alpha=dH\), the correction \(X\) is the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] \(X_H\) in the sign convention \(\iota_{X_H}\omega=dH\). Hence changing a primitive by an exact form changes the Liouville field by a Hamiltonian field.

## Canonical example

On \(T^*Q\) with coordinates \((q_i,p_i)\), take
\[
\lambda=\sum_i p_i\,dq_i,\qquad
\omega=d\lambda=\sum_i dp_i\wedge dq_i.
\]
The corresponding Liouville field is
\[
Z=\sum_i p_i\frac{\partial}{\partial p_i},
\]
whose flow multiplies cotangent vectors by \(e^t\). With the alternative convention \(\omega=-d\lambda=\sum_i dq_i\wedge dp_i\), one also changes the defining contraction sign if one wants the same radial field.

## Conventions and scope

**Warning.** Authors using \(\omega=-d\lambda\) commonly define \(Z\) by \(\iota_Z\omega=-\lambda\). The invariant content is \(\mathcal L_Z\omega=\omega\). A Hamiltonian vector field instead satisfies \(\mathcal L_X\omega=0\), so it preserves rather than dilates the symplectic form.

## References

1. Kai Cieliebak and Yakov Eliashberg, *From Stein to Weinstein and Back*, Colloquium Publications 59, American Mathematical Society, 2012. [AMS DOI record](https://doi.org/10.1090/coll/059). Relevant: §2, Liouville forms and vector fields.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: pp. 69–79, contact forms and Liouville dynamics.
