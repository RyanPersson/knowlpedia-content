+++
id = "proofs/grh/derivatives-vacuum/least-valuation-zero-when-forms-span"
title = "Least valuation at most zero when the forms span the coordinates"
kind = "lemma"
summary = "If every coordinate is, up to one common unit, an integral combination of the linear forms, then the least valuation over six copies is at most zero in every degree."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.leastValLE_zero_of_span"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-relation|the least valuation relation]]; \(d\) is a prime \(\equiv7\bmod8\).

**Lemma.** Suppose there are \(a_{x,i}\in\mathcal{O}_{\mathbb{C}_p}\) (\(x\in X\), \(i\in J\)) and \(s\in\mathbb{C}_p\) with \(\lvert s\rvert_p=1\) such that \(\sum_ia_{x,i}\mu_i(z)=s\,z_x\) for all \(x\). Then \(\operatorname{val}_6(\nu)\le0\) for every \(\nu\).

## Proof

The series \(y\) has \(y(0)=0\) and linear coefficient \(1\). So \(G_x=\sum_ia_{x,i}\,y(\mu_iz)\in\mathcal{O}[\![y(\mu z)]\!]\) has [[proofs/grh/derivatives-vacuum/lowest-term-of-a-power-series|lowest term]] \(s\,z_x\) for the total degree. By multiplicativity of lowest terms, and since \(\Theta\) has lowest term \(1\), the series \(\bigl(\prod_xG_x^{\nu_x}\bigr)\Theta\) has lowest term \(s^{\lvert\nu\rvert}z^\nu\); its coefficient at \(\nu\) is a unit. Hence \(\operatorname{val}_1(\nu)\le0\), and adding five copies in degree \(0\) ([[proofs/grh/derivatives-vacuum/least-valuation-rules|rule 1]]) gives \(\operatorname{val}_6(\nu)\le0\).

## References

1. Lean: `New.CMLattice.leastValLE_zero_of_span` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
