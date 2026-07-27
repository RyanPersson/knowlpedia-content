+++
id = "lie-groups/harish-chandra-regularity-theorem"
title = "Harish–Chandra regularity theorem"
kind = "theorem"
summary = "The theorem representing invariant eigendistributions by locally integrable functions analytic on regular semisimple elements."
aliases = ["regularity of invariant eigendistributions", "character regularity theorem"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected real reductive [[fiber-bundles/lie-group|Lie group]]. Suppose \(\Theta\) is a conjugation-invariant [[functional-analysis/distribution|distribution]] on \(G\) and a joint eigendistribution for the invariant differential operators coming from \(Z(U(\mathfrak g_\mathbb C))\). The **Harish–Chandra regularity theorem** states that there is a locally integrable function \(F_\Theta\) whose associated distribution is \(\Theta\), and that \(F_\Theta\) is real analytic on the regular semisimple set \(G_{\mathrm{reg}}\). Here an element is regular semisimple when its [[algebra-groups/centralizer|centralizer]] has the minimal possible dimension. Equality with \(\Theta\) is distributional; values of \(F_\Theta\) on measure-zero singular sets are not determined.

## Application to characters

An admissible representation with [[lie-groups/infinitesimal-character|infinitesimal character]] has a [[lie-groups/global-character-of-an-admissible-representation|global character]] satisfying the theorem's hypotheses. Its distribution character can therefore be studied through an analytic class function on \(G_{\mathrm{reg}}\), even though the operators \(\pi(g)\) are generally not trace class. This is the rigorous meaning of the Harish–Chandra character function.

## Strength and limitations

Local integrability across the singular set is an essential part of the theorem; analyticity is asserted only on the regular semisimple set. The result does not say that the representing function extends continuously, smoothly, or analytically across singular elements. Related Lie-algebra and group versions require hypotheses appropriate to the chosen real reductive or semisimple setting [Harish-Chandra, 1965](https://doi.org/10.1090/S0002-9947-1965-0180631-0).

## Proof architecture

The proof reduces invariant differential equations to Cartan subgroups and controls their singularities near root hyperplanes. Elliptic regularity supplies analyticity on regular elements, while delicate descent and estimates establish local integrability across the singular locus. These steps are substantially stronger than the formal observation that a character is an eigendistribution.

## References

1. Harish-Chandra, “Invariant Eigendistributions on a Semisimple Lie Group,” *Transactions of the American Mathematical Society* 119 (1965), 457–508. [DOI record](https://doi.org/10.1090/S0002-9947-1965-0180631-0). Relevant: the group regularity theorem.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986; reprint 2001. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter X on invariant eigendistributions and global characters.
