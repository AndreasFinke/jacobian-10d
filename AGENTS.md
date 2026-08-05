# Agent instructions

This is a public release repository, not a research scratchpad.

## Read first

1. `README.md`
2. `CONSTRUCTIONS.md`
3. `CUBIC_HOMOGENEOUS.md`
4. `RESEARCH_PROVENANCE.md`

## Required discipline

- Preserve the claim boundaries in the public documents.
- Do not add novelty, priority, minimality, or breakthrough claims without a
  separate evidence audit.
- Do not add a mathematical construction unless an exact verifier is committed
  with it.
- Regenerate machine-readable map files through their canonical verifier; do
  not edit generated formulas by hand.
- Run both canonical Python certificates before committing:

  ```bash
  python3 verify_all.py
  python3 verify_cubic_homogeneous18.py --output cubic_homogeneous18.json
  ```

- Run the independent Wolfram Language or Singular verifier when modifying the
  corresponding construction.
- Keep speculative candidates, numerical near-solutions, search ledgers,
  private prompts, and null-result audits out of this repository.
- Keep public documents self-contained. Do not refer readers to private
  branches or private research repositories.

## Public acceptance boundary

A result is ready for this repository only when the displayed polynomial map,
constant Jacobian determinant, and stated collision are all checked exactly.
AI-generated text or code is never evidence by itself.
