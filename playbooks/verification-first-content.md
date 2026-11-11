# Playbook: verification-first content and honest artifacts

How projects in this directory let agents write 67k events, ship galleries and claim "it's all code" — without asking you to trust them.

**Evidence:** [earth-whole-story](../teardowns/earth-whole-story.md) · [Sumi OS](../teardowns/sumi-os.md) · [fable5.2demo](../teardowns/fable5.2demo.md) · [fable-five](../teardowns/fable-five.md) · [html-files-gallery](../teardowns/html-files-gallery.md) · [ballpoint](../teardowns/ballpoint.md)

## Mechanical provenance, not good intentions

earth-whole-story's rule: **"write only what the source says" — enforced by the build.** Every content record names the retrieved source it was written from; a record whose source wasn't retrieved *cannot enter the build*. The audits behind it are a copyable triad:

- **Sample audit**: 200 curated claims re-checked against re-retrieved sources; 300 random links checked.
- **Full offline sweep**: every claim re-verified against the already-fetched source text (no network).
- **Placeholder scan**: no filler words, no empty fields — the "agent left a TODO" detector.

## Pre-register the checks, then let the artifact speak

Sumi OS defined **9 acceptance items before the run**, executed them in QEMU afterward with screenshots, and noted plainly: *the model produced no completion report* — the checks settled "done", not a claim. For integrity, `SHA256SUMS.txt` preserves the run's exact bytes; the two publication edits are itemized against it. "Untouched as the run left it" becomes a checkable statement.

## The "what was faked" section

fable5.2demo ships a report per project: implementation, verification, and **做了假的地方 — where corners were cut or things faked** (and it labels its one generated-texture exception honestly). fable-five's Limits section is the specific kind: "rays that circle the hole many times come out black", "malloc never frees". Vague humility convinces no one; enumerated limits do. Make it a standing section in every agent-built README:

```text
## Limits & honest gaps
- Checked: [what, and how — including what was NOT checked]
- Faked / simplified: [each with why]
- Single-run? [n=1 means n=1]
```

## Publish the generator, not the claim

ballpoint proves "no video model" by open-sourcing the pipeline: handwriting dynamics, cellulose fibres, ink deposition as separate scripts with one-way data flow — you can read exactly where the ragged ink edge comes from. html-files-gallery makes its derived artifacts honest by **hash-gating**: a screenshot is reused only when both the HTML and image hashes match the manifest; changed content forces re-capture, and a failed check blocks deployment. Derived artifacts should never be able to silently disagree with their sources.

## Untouched model output as evidence

fable-5-2-benchmark publishes each job's `TESLIM.md` — the model's own delivery note, unedited — beside the human evaluation. The contrast between the two is the review. (Sumi OS does the same with the model-written in-repo README, gaps and all.)

## Checklist

- [ ] Every agent-written factual record names a retrievable source
- [ ] "Done" defined by pre-registered checks, executed after the run
- [ ] A Limits / what-was-faked section with specifics
- [ ] Derived artifacts hash-gated to their sources; deploy blocked on failure
- [ ] Hashes published for anything claimed "as the run left it"
- [ ] Model self-reports published untouched next to your evaluation
