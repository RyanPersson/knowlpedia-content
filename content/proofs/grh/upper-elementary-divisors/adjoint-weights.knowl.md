+++
id = "proofs/grh/upper-elementary-divisors/adjoint-weights"
title = "Adjoint weights from multinomial coefficients"
kind = "lemma"
summary = "Over a valuation domain where p is not a unit, the quotients of a power of p by multinomial coefficients make substitution by a matrix and by its transpose adjoint."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.IsAdjointWeight", "New.Average.exists_isAdjointWeight", "New.Average.cast_choose_dvd_pow", "New.Average.cast_multinomial_dvd_pow", "New.Average.prod_factorial_mul_coeff_linSubst"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

Let \(O\) be a commutative ring and \(\sigma\) a finite set of variables. For a matrix \(A\in M_\sigma(O)\) let \(L_A\) be the \(O\)-algebra endomorphism of \(O[x_i:i\in\sigma]\) with \(L_A(x_b)=\sum_t A_{t,b}x_t\) ([[?lean:New.linSubst|linear substitution]]). A function \(\eta\colon\mathbb{N}^{\sigma}\to O\) is a system of **adjoint weights** if for all \(A\) and all exponents \(\alpha,\beta\)
\[
[x^{\alpha}]\,L_A(x^{\beta})\cdot\eta(\alpha)=\eta(\beta)\cdot[x^{\beta}]\,L_{{}^{t}A}(x^{\alpha}),
\]
i.e. \(L_A\) and \(L_{{}^tA}\) are adjoint for the symmetric bilinear form with \(\langle x^{\alpha},x^{\beta}\rangle=\delta_{\alpha\beta}\,\eta(\alpha)\).

**Lemma.** Let \(O\) be a [[?c:Valuation ring|valuation ring]] that is an [[algebra-rings/integral-domain|integral domain]] of characteristic \(0\), \(p\) a prime number that is not a unit of \(O\), and \(f\ge0\). Then there are adjoint weights \(\eta\) such that
\[
p^{\lvert\sigma\rvert f}=\binom{\lvert\gamma\rvert}{\gamma}\,\eta(\gamma)\qquad\text{for every exponent }\gamma\text{ of total degree }\lvert\gamma\rvert<p^{f},
\]
where \(\binom{\lvert\gamma\rvert}{\gamma}=\lvert\gamma\rvert!/\prod_i\gamma_i!\) is the [[?c:Multinomial coefficient|multinomial coefficient]].

## Proof

*Divisibility.* Let \(n+m<p^{f}\). If \(n+m=0\) the binomial coefficient is \(1\). If \(n+m\ge1\), the \(p\)-adic valuation of \(\binom{n+m}{n}\) is at most \(\lfloor\log_p(n+m)\rfloor\le f\) (Kummer's bound, [[?c:Kummer's theorem on binomial coefficients|Kummer's theorem]]). Write \(\binom{n+m}{n}=p^{v}u\) with \(p\nmid u\). Since \(O\) is local and \(p\) lies in its maximal ideal, the integer \(u\), being coprime to \(p\), is a unit of \(O\). Hence \(\binom{n+m}{n}\mid p^{f}\) in \(O\). A multinomial coefficient of degree \(<p^{f}\) over a set of \(m\) indices is a product of \(m\) binomial coefficients with upper index \(<p^{f}\), so it divides \(p^{mf}\).

*Definition of \(\eta\).* For \(\lvert\gamma\rvert<p^{f}\) choose \(\eta(\gamma)\) with \(p^{\lvert\sigma\rvert f}=\binom{\lvert\gamma\rvert}{\gamma}\eta(\gamma)\); for \(\lvert\gamma\rvert\ge p^{f}\) choose \(\eta(\gamma)\) with \(0=\binom{\lvert\gamma\rvert}{\gamma}\eta(\gamma)\), i.e. \(\eta(\gamma)=0\) (characteristic \(0\), domain). In both cases \(\binom{\lvert\gamma\rvert}{\gamma}\eta(\gamma)=c_{\lvert\gamma\rvert}\) depends only on the degree.

*Adjointness.* For the form \(\langle x^{\alpha},x^{\beta}\rangle=\delta_{\alpha\beta}\alpha!\) with \(\alpha!=\prod_i\alpha_i!\) (the [[?lean:New.fockPairing|Fock pairing]]), \(L_A\) and \(L_{{}^tA}\) are adjoint ([[?lean:New.fockPairing_linSubst|adjointness for the Fock pairing]]): \(\alpha!\,[x^{\alpha}]L_A(x^{\beta})=\beta!\,[x^{\beta}]L_{{}^tA}(x^{\alpha})\). If \(\lvert\alpha\rvert\ne\lvert\beta\rvert\), both coefficients vanish because linear substitutions preserve degree. If \(\lvert\alpha\rvert=\lvert\beta\rvert=d\), multiply the desired identity by \(d!\ne0\): since \(d!\,\eta(\alpha)=\alpha!\binom{d}{\alpha}\eta(\alpha)=\alpha!\,c_d\) and likewise for \(\beta\), it becomes \(c_d\) times the Fock adjointness. Cancel \(d!\) in the domain \(O\). \(\square\)

## References

1. Lean: `New.Average.IsAdjointWeight`, `New.Average.exists_isAdjointWeight`, `New.Average.cast_choose_dvd_pow`, `New.Average.cast_multinomial_dvd_pow`, `New.Average.prod_factorial_mul_coeff_linSubst` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
