# Creepvale - Horror / Spooky Video Style Lock

Sister pipeline to dark-fantasy, pallowyn, and the other niches -- same
architecture (Higgsfield still -> Minimax Hailuo 2.3 animate -> ffmpeg
music mux -> Buffer schedule) but a distinct visual identity.

## Tone: atmospheric dread, NOT gore

This is the crucial distinction from pallowyn (the cozy-spooky Halloween
niche). Creepvale is genuine unease -- abandoned places, uncanny stillness,
a sense of being watched -- built through atmosphere and composition, not
through graphic or shocking content.

- Abandoned buildings, empty corridors, flickering lights, deep shadow
- Distant or silhouetted figures -- never close-up faces, never gore
- Fog, decay, dust, stillness that feels wrong
- NO gore, NO jump-scare framing, NO graphic violence or disturbing imagery
- NO on-screen text, no captions (silent visual page, same as the other niches)

## Visual rules

- Wide establishing shots, not close-up portraits
- Camera always locked static -- only ambient elements move (flickering
  light, drifting dust/fog, a single swaying object)
- Palette: desaturated, cold blues and greys against pools of sickly warm
  light (a single bulb, a distant window)
- 9:16 vertical, 1080p stills, 6s animated clips (Minimax Hailuo 2.3)
- Roughly half the scene bank has a distant/silhouetted figure, half is
  pure environment/object shots

## Prompt templates

Still image prompt pattern:
"[scene description], cold desaturated color grade, single source of dim
light, thick atmospheric fog or dust, unsettling stillness, dark horror
illustration style, wide cinematic composition, 9:16 vertical, highly
detailed, no text, no watermark"

Animate prompt pattern:
"Camera completely locked and static, only [ambient element -- flickering
light / drifting dust / drifting fog / a single swaying object] moves
gently, unsettling atmospheric horror mood, subtle ambient motion only,
no camera movement, no zoom, no pan"

## Music

An eerie, sparse instrumental horror-ambient track -- slow, dread-building,
minimal percussion, distinct from pallowyn's playful "Carnival of the
Macabre" and dark-fantasy's "Creaking Hallways". Needs sourcing separately
(see repo README) -- do not reuse pallowyn's track, wrong tone entirely.
