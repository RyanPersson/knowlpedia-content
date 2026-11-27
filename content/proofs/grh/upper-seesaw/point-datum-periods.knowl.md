+++
id = "proofs/grh/upper-seesaw/point-datum-periods"
title = "The point datum is fixed by translations by the modulus"
kind = "lemma"
summary = "The finite datum of a lift of the lower chain is fixed by the Heisenberg translations by the generator of the twist modulus times integral vectors."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.finHeisenbergOp_generator_smul_pointDatumY", "New.Data.twistIdele", "New.Data.valued_twistIdele"]
lean_files = ["src/New/UpperBound/Seesaw/UnfoldingStages.lean"]
proof_status = "full"
+++

Let \(D\) be the [[?lean:New.Data|data]], \(\vartheta\) a tame character with chosen modulus \(Q\) (a finite set of places outside which its tame part is trivial; the tame part may also be trivial at places of \(Q\), and \(Q\) is the exact support only for a [[?lean:New.Data.Twist|twist]]), \(\mathfrak{m}\) the [[?lean:New.Data.twistModulus|modulus of the twist]] (the product of
the chosen places and the places of \(Q\)), \(\varpi_{\mathfrak m}\) its chosen idele generator, and
\(\Phi_k\) the [[?lean:New.Data.pointDatumY|point datum]] on
\(H_k=\operatorname{Hom}(Y_k,Y_{k+1})\).

**Lemma.**

1. For every integral vector \(x\) of \(H_k\):
   \(\varrho_f(\varpi_{\mathfrak m}x)\,\Phi_k=\Phi_k\).
2. The **twist idele** \(\mathfrak q=\varpi_{\mathfrak m}/\varpi\) (\(\varpi\) the
   [[?lean:New.Data.chosenIdele|chosen idele]]) is a uniformiser at the places of \(Q\) and a unit
   at all other finite places.

## Proof

(1) By [[proofs/grh/upper-seesaw/schrodinger-operator-admissible|the Schrödinger operator lemma]]
in its general form, with \(g=0\), \(q=1\) and \(d=\varpi_{\mathfrak m}\) (which reduces to \(0\)
modulo \(\mathfrak m\)), the point datum — the Schrödinger operator of the indicator of a residue
class applied to the vacuum — is a finite combination of translates \(\varrho_f(t)v_0\) with
\(\bar\varpi_{\mathfrak m}t\) integral at all places (for \(q=1\) no place is excluded). For such
\(t\), \(\psi\bigl(\varpi_{\mathfrak m}\,t^{*}x\bigr)=\psi\bigl((\bar\varpi_{\mathfrak m}t)^{*}x\bigr)=1\)
by self-duality of the standard lattice, so by the
[[?lean:New.Space.finHeisenbergOp_comm|commutation law]] \(\varrho_f(\varpi_{\mathfrak m}x)\)
commutes with \(\varrho_f(t)\); and it fixes \(v_0\) because \(\varpi_{\mathfrak m}x\) is integral.

(2) The ideal of \(\mathfrak m\) is \((\pi_M)\) times the product of the distinct primes of \(Q\),
so its multiplicity at \(w\) is that of \((\pi_M)\) plus \(1\) if \(w\in Q\) and plus \(0\)
otherwise; \(\varpi_{\mathfrak m}\) has the valuations of \(\mathfrak m\) and \(\varpi\) those of
\(\pi_M\) ([[proofs/grh/upper-seesaw/tower-lattice-data|lattice data of the tower]]).
\(\blacksquare\)

## References

1. Lean: `New.Data.finHeisenbergOp_generator_smul_pointDatumY`, `New.Data.valued_twistIdele` in `src/New/UpperBound/Seesaw/UnfoldingStages.lean`.
