# Starter prompt: code-only 3D world / scene

For a walkable or flyable three.js scene with zero external assets — the pattern behind Portals' worlds, worm-rider's arena and the Grand Bazaar walk. One message, empty folder, budget ceiling recommended.

```text
Create an explorable 3D browser scene: [one sentence — place, mood,
time of day, what the visitor does]. It should feel [art-directed
adjective: e.g. like a woodblock print of a harbour at dusk].

Hard constraints:
- Single index.html; three.js [r170] from CDN is the only library.
- Everything generated in code at load: no model, texture, image or
  audio files. Tiling textures baked on the GPU; geometry procedural
  or instanced.
- One shared environment: sky, sun/image-based light, fog and grade
  chosen to serve the mood; light changes only with a visible cause.
- Runs at [60] fps on a laptop iGPU; instance instead of duplicating;
  distance fade or baked far detail where cheap.
- Quiet synthesized ambience ([wind/water/hum]) with a mute toggle.

Scene requirements:
- A readable centerpiece: [the lighthouse / the market street / the
  ship] readable from the spawn point.
- [2–3 set pieces that reward approaching or circling]
- A gentle default camera path that shows the scene hands-off
  (autoplay / cinematic mode), plus manual look controls.

Completion bar:
- Zero console errors at load and after 60 seconds of the camera path.
- Screenshots at spawn, mid-path and the far end reviewed by you in a
  real browser; broken pixels and z-fighting fixed or listed.
- A 20-second hands-off run completed; frame rate reported.
- Limits listed honestly (what is simplified or faked).
```

Notes from the teardowns

- **World = `build()` returning scene + camera path + duration** is the whole Portals interface; if you plan many worlds, make each a file exporting that and share a kit (skies, water, terrain, buildings) — see [ai-portals](../teardowns/ai-portals.md).
- **Asset-lab first**: if the scene has hero assets (a vehicle, a creature), build each alone under neutral light before composing — [worm-rider](../teardowns/worm-rider.md).
- Keep texture baking and displacement in their own files (`tex.js`, `wormskin.js` in worm-rider) so surfaces are debuggable layer by layer.
