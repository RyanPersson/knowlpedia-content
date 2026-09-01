+++
id = "langlands/continuous-automorphic-spectrum"
title = "Continuous automorphic spectrum"
kind = "definition"
summary = "The non-discrete part of the automorphic L2 spectrum, assembled from Eisenstein series induced from proper Levi subgroups."
aliases = ["continuous spectrum of automorphic forms", "continuous automorphic L2 spectrum", "Eisenstein spectrum"]
domains = ["langlands", "harmonic-analysis"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/global-local-fields-completions", "algebra-representation-theory/central-character", "linear-algebra/hilbert-space", "langlands/discrete-automorphic-spectrum", "harmonic-analysis/direct-integral-unitary-representations", "algebraic-geometry-foundations/levi-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a [[langlands-letter/knowls/global-local-fields-completions|global field]] \(F\). After fixing a
[[algebra-representation-theory/central-character|central-character]] or
split-center convention, the right regular
representation on the automorphic
[[linear-algebra/hilbert-space|Hilbert space]] decomposes as

\[
L^2_{\mathrm{aut}}(G)=
L^2_{\mathrm{disc}}(G)\oplus L^2_{\mathrm{cont}}(G).
\]

The first summand is the
[[langlands/discrete-automorphic-spectrum|discrete automorphic spectrum]];
the second is the **continuous automorphic spectrum**. Spectrally, it is a
[[harmonic-analysis/direct-integral-unitary-representations|direct integral]]
of representations obtained by normalized adelic parabolic induction from
discrete automorphic data on proper
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroups]].

## Eisenstein construction

[[langlands-letter/knowls/eisenstein-series|Eisenstein series]] and their
meromorphic continuation provide generalized eigenfunctions for the
continuous spectrum. Their
[[langlands/automorphic-constant-term|constant terms]] and normalized
intertwining operators determine the
[[harmonic-analysis/plancherel-measure-nonabelian|Plancherel measure]] and
identify redundancies among
inducing data.

Poles of Eisenstein series can contribute square-integrable residues.  Those
belong to the [[langlands/residual-automorphic-spectrum|residual spectrum]],
which is discrete rather than continuous.

## Trace-formula role

The spectral side of the
[[langlands/arthur-selberg-trace-formula|Arthur–Selberg trace formula]]
includes integrals of
weighted characters arising from this continuous family.  It reduces to a
plain sum only when the relevant automorphic quotient is compact or when a
[[harmonic-analysis/test-function-space-local-group|test function]]
annihilates all proper-parabolic contributions.

## References

1. Robert P. Langlands, *On the Functional Equations Satisfied by Eisenstein
   Series*, Lecture Notes in Mathematics 544, Springer, 1976.
2. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics
   Proceedings 4, 2005, §§12–14 and 21.
   [Clay](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
