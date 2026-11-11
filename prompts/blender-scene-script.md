# Starter prompt: Blender scene from Python (no downloaded assets)

The pattern behind the Blender effort test, ballpoint and the fable5.2demo models: the scene is a set of Python scripts building from an empty file, so "how it was made" is readable and rerunnable. Needs Blender MCP attached locally (Blender 4.5/5.2+ on the machine), per the [benchmark's](../teardowns/fable-5-2-benchmark.md) local-prompt pattern.

```text
You are driving Blender [5.2] through its Python API. Machine: [GPU
model], Blender at [path], render device [OptiX/CUDA/METAL/CPU].

Goal: [one sentence — a lamp-lit still life / a rainy neon street /
a macro shot of X]. Mood and lens: [references, focal feel].

Hard constraints:
- Start from an empty file. Build EVERYTHING in Python: no downloaded
  or imported models, no image textures; procedural materials only.
- Split by physical cause, one script per layer, one-way data flow:
  [e.g. hand.py → paper.py → ink.py → rig.py →] build.py, render.py,
  finish.py. No layer reads another's internals — only its outputs.
- Render with Cycles; world units [mm/m]; name every object.
- A resumable renderer: interrupted renders continue from the last
  written frame.

Deliverables:
- The scripts, in order, with a one-line "run book" at the top.
- 3 stills at [1920×1080, N samples]: [wide / detail / hero angle].
- An honest gap list: what a viewer will find different from a fully
  hand-crafted scene.

Completion bar:
- The run book executes start-to-finish on this machine with zero
  errors (you ran it).
- Stills reviewed by you in the sequencer / image viewer; obvious
  artifacts (fireflies, z-fighting, floating geometry) fixed or listed.
- File sizes and per-frame render time reported.
```

Notes from the teardowns

- **Cheap pass first, then brief the expensive pass**: run v1 at medium effort, then hand v1's failures to a max-effort agent as the v2 brief — [blender-effort-test](../teardowns/blender-effort-test.md).
- **To show it on the web**, bridge deliberately: bake procedural materials to one atlas, export camera/lights to JSON, then publish the difference list — never claim parity ([blender-effort-test](../teardowns/blender-effort-test.md)).
- **Proving "not a video model"** = publishing the generator with layers separated by cause ([ballpoint](../teardowns/ballpoint.md)).
- State machine facts (GPU, Blender version, device) in the prompt itself — they materially change results and belong in your published method.
