+++
id = "functional-analysis/rigged-hilbert-space"
title = "Rigged Hilbert space"
kind = "definition"
summary = "A dense nuclear test space inside a Hilbert space, together with its continuous anti-dual."
aliases = ["Gelfand triple"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/nuclear-space", "functional-analysis/strong-dual", "linear-algebra/inner-product", "functional-analysis/densely-defined-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **rigged Hilbert space**, or **Gelfand triple**, is a chain
\[
\Phi\hookrightarrow H\hookrightarrow\Phi^\times
\]
in which \(H\) is a [[linear-algebra/hilbert-space|Hilbert space]], \(\Phi\) is a Hausdorff [[functional-analysis/nuclear-space|nuclear locally convex space]] continuously and densely embedded in \(H\), and \(\Phi^\times\) is its continuous anti-dual with the [[functional-analysis/strong-dual|strong dual topology]]. Taking the [[linear-algebra/inner-product|inner product]] on \(H\) linear in its first variable, the second embedding sends \(h\) to the conjugate-linear functional \(\phi\mapsto\langle h,\phi\rangle_H\). Density makes this embedding injective.

## Test vectors and generalized vectors

The space \(\Phi\) carries a topology finer than the Hilbert norm topology, encoding regularity or decay. Elements of \(\Phi^\times\) act as generalized vectors, including [[functional-analysis/distribution|distributions]] that do not belong to \(H\). The Hilbert space lies between these two scales and identifies ordinary vectors with continuous anti-linear functionals on the test space.

## Operators and spectral analysis

If a [[functional-analysis/densely-defined-operator|densely defined operator]] on \(H\) preserves \(\Phi\) and acts continuously on its locally convex topology, duality extends it to \(\Phi^\times\). Generalized eigenvectors may then live in \(\Phi^\times\) even when the operator has no eigenvectors in \(H\). Nuclearity supplies the compactness and kernel-theorem structure used in generalized spectral expansions.

## Example and convention

The canonical example is
\[
\mathcal S(\mathbb R^n)\hookrightarrow L^2(\mathbb R^n)\hookrightarrow\mathcal S'(\mathbb R^n),
\]
with [[functional-analysis/schwartz-space|Schwartz functions]] as test vectors and [[functional-analysis/tempered-distribution|tempered distributions]] as generalized vectors. Some authors use **rigged Hilbert space** for any continuous dense embedding \(\Phi\hookrightarrow H\), without requiring \(\Phi\) to be nuclear, and reserve **nuclear Gelfand triple** for the definition above. The nuclear convention is used here.

## References

1. I. M. Gel′fand and N. Ya. Vilenkin, *Generalized Functions, Volume 4: Applications of Harmonic Analysis*, Academic Press, 1964; AMS Chelsea reprint. [AMS publisher record](https://bookstore.ams.org/CHEL/380.H). Relevant: Chapter I on nuclear spaces, rigged Hilbert spaces, and spectral analysis.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics, Volume I: Functional Analysis*, Academic Press, 1972. [Elsevier DOI record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter V on locally convex spaces and distributions.
