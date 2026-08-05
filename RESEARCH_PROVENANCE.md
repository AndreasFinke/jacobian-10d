# Research provenance and AI assistance

This repository is a **human-directed, AI-assisted research artifact**.

## Roles

- **Andreas Finke** set the research goals and acceptance criteria, selected
  which results were suitable for public release, reviewed the mathematical
  claims, and is responsible for the contents of this repository.
- **AI systems**, principally OpenAI GPT-5.6 Pro and coding agents, assisted
  with candidate generation, symbolic manipulation, exact-verifier code,
  adversarial checking, literature and priority searches, and drafting.

AI systems are acknowledged as research tools rather than listed as authors.
The human maintainer remains accountable for every public claim.

## Verification policy

No mathematical claim in this repository depends on trusting model output.
Public claims are retained only when they have exact, rerunnable certificates.
The repository therefore includes:

- explicit polynomial formulas;
- exact rational collision points;
- symbolic determinant checks;
- independent checks in more than one computer-algebra system where practical;
- machine-readable representations of the principal maps;
- continuous integration for the canonical Python certificates.

Speculative candidates, numerical near-solutions, and unsuccessful exploratory
searches are not presented here as results. The private research process was
substantially broader than this release repository.

## Reproducibility and attribution

The commit history records the public evolution of the constructions and
certificates. For scholarly use, cite the repository metadata in
[`CITATION.cff`](CITATION.cff) and identify the exact commit or release used.

The underlying three-dimensional counterexample is prior work. The claim
boundaries in [`README.md`](README.md), [`CONSTRUCTIONS.md`](CONSTRUCTIONS.md),
and [`CUBIC_HOMOGENEOUS.md`](CUBIC_HOMOGENEOUS.md) distinguish that source
result from the stable reductions and verification artifacts developed here.
