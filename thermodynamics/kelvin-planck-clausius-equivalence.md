---
title: "Kelvin–Planck–Clausius equivalence"
description: "The Kelvin–Planck and Clausius formulations of the second law are logically equivalent: violating either implies a violation of the other."
---

## Statement

Two standard formulations of the {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law of thermodynamics" >}} are:

- **Kelvin–Planck statement.** No cyclic device can extract heat from a single thermal reservoir and convert it entirely into work (i.e., no 100% efficient single-reservoir heat engine).

- **Clausius statement.** No cyclic device can transfer heat from a colder reservoir to a hotter reservoir without net work input (i.e., no “spontaneous” pumping of heat uphill for free).

**Equivalence theorem.** The Kelvin–Planck statement holds if and only if the Clausius statement holds.

## Key hypotheses and conclusions

**Hypotheses**
- Standard macroscopic bookkeeping consistent with the {{< knowl id="first-law-thermodynamics" section="thermodynamics" text="first law of thermodynamics" >}} (energy conservation over cycles).
- Reservoirs are idealized as bodies at fixed {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} that can supply/absorb heat without changing temperature.

**Conclusions**
- Either statement may be taken as the second law without loss of generality.
- Carnot-type bounds and entropy inequalities can be derived from either formulation:
  - {{< knowl id="carnot-theorem" section="stat-mech" text="Carnot theorem" >}}
  - {{< knowl id="clausius-theorem-entropy" text="Clausius theorem (entropy)" >}}
  - {{< knowl id="clausius-inequality" section="thermodynamics" text="Clausius inequality" >}}

## Cross-links to definitions

- Second law: {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law of thermodynamics" >}}.
- Energy conservation over cycles: {{< knowl id="first-law-thermodynamics" section="thermodynamics" text="first law" >}}.
- Temperature and reservoirs: {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.

## Proof idea / significance

**Clausius ⇒ Kelvin–Planck (contradiction).** Suppose the Clausius statement were false: there exists a device that moves heat from cold to hot with no work. Couple it to an ordinary heat engine so that the engine’s rejected heat is pumped back to the hot reservoir for free. The composite device then converts heat drawn from a single reservoir entirely into work, contradicting Kelvin–Planck.

**Kelvin–Planck ⇒ Clausius (contradiction).** Suppose Kelvin–Planck were false: there exists a device producing work while extracting heat only from one reservoir. Use that work to drive a refrigerator that pumps heat from cold to hot. If the engine supplies all the needed work, the net effect is heat transferred from cold to hot with no external work, contradicting Clausius.

**Significance.** This equivalence justifies treating “the second law” as a robust principle independent of which operational impossibility statement one starts from, and it underpins both {{< knowl id="carnot-theorem" section="stat-mech" text="Carnot’s theorem" >}} and entropy-based formulations.
