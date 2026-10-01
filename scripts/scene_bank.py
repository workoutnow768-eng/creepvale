"""
Scene bank for the creepvale (Horror/Spooky) video pipeline. Follows
CREEPVALE_VIDEO_STYLE.md exactly -- atmospheric dread, NOT gore or
jump-scares. Uses Higgsfield Soul v2 for the still + Minimax Hailuo 2.3
image-to-video for the animate step, same as pallowyn/dark-fantasy.

Third revision (2026-10-01), two changes based on direct feedback that
the videos "look like a still image with a tiny bit of flame movement"
and that posts "keep almost repeating themselves":

  1. Hailuo 2.3 has NO structural camera_fixed parameter -- camera
     behavior is driven entirely by animate_prompt wording. Every scene
     previously said "camera completely locked... no camera movement
     whatsoever", which directly told the model to barely move. That
     phrasing is gone -- every animate_prompt below now asks for a real,
     deliberate camera move (push-in, pull-back, pan, tilt, orbit, or
     dolly), varied scene to scene, while keeping the figures/props in a
     scene themselves mostly still (per CREEPVALE_VIDEO_STYLE's "dread,
     not jump-scare" rule) so it's the camera that creates motion, not
     things leaping around.
  2. Bank grew from 12 to 16 scenes to stretch the rotation cycle at 3
     posts/day from 4 days to a bit over 5, and the 4 new scenes use
     different environments (root cellar, motel room, church pews) than
     the existing hospital/forest/house/doorway set so the cycle doesn't
     feel like reruns of the same few locations.

`has_people` is roughly half true/false across the bank by design so
consecutive posts don't repeat the same subject pattern.
"""

SCENES = [
    {
        "title": "flickering asylum corridor",
        "has_people": False,
        "still_prompt": "A long abandoned hospital corridor, peeling paint "
            "walls, a single flickering fluorescent light at the far end, "
            "an overturned wheelchair blocking part of the hallway, torn "
            "restraint straps dangling from a rusted gurney against the "
            "wall, water stains on the ceiling forming shapes like "
            "reaching hands, a trail of small muddy footprints leading "
            "toward the open door and abruptly stopping halfway down the "
            "hall, a fallen clipboard with a chart still clipped inside "
            "it, a door standing open at the far end onto pure blackness, "
            "cold desaturated color grade, thick dust hanging in the air, "
            "dark horror illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow dolly "
            "forward down the corridor toward the dark open doorway at "
            "the far end. The fluorescent light keeps flickering, dust "
            "drifts through the air, the stopped footprints stay exactly "
            "as they are. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "figure at the end of the hall",
        "has_people": True,
        "still_prompt": "A distant motionless silhouette standing at the "
            "far end of a dim empty hallway exactly where it bends out of "
            "sight, proportions subtly too tall and too thin, head tilted "
            "at an unnatural angle, its shadow stretching toward the "
            "camera far longer than the faint light behind it could "
            "explain, a row of closed doors along the hallway all slightly "
            "ajar except the one nearest the figure, faint scratch marks "
            "at hand height along the wall closest to camera, cold "
            "desaturated color grade, thick atmospheric fog low to the "
            "floor, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow push-in "
            "toward the distant figure, the hallway appearing to slowly "
            "lengthen as the camera approaches. The figure itself remains "
            "perfectly still, only the fog drifts near the floor and the "
            "impossible shadow flickers. Unsettling atmospheric horror "
            "mood, not a jump-scare, no text",
    },
    {
        "title": "dead forest at night",
        "has_people": False,
        "still_prompt": "A dense forest of bare twisted dead trees at "
            "night, bark peeling from the trunks in sheets like shed skin, "
            "a small child's single shoe half-sunk in wet blackened "
            "leaves in the foreground, deep gouges raked into the bark of "
            "the nearest trunk at roughly shoulder height, thick fog "
            "weaving between the trunks, a single dim unexplained light "
            "glowing far in the distance down a narrow deer path, "
            "something pale just barely visible at the treeline where the "
            "path vanishes, cold desaturated blue-grey color grade, dark "
            "horror illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow pan right, "
            "sweeping across the dead trees toward the narrow deer path "
            "and its distant light. Fog drifts slowly between the "
            "trunks, the light flickers faintly, the pale shape at the "
            "treeline does not move. Unsettling atmospheric horror mood, "
            "not a jump-scare, no text",
    },
    {
        "title": "empty swing in overgrown yard",
        "has_people": False,
        "still_prompt": "A rusted metal swing set standing alone in an "
            "overgrown weed-choked yard at dusk, one swing hanging "
            "crooked with its second chain snapped and dragging in the "
            "dirt, a faded chalk hopscotch grid barely visible on a "
            "cracked path nearby with the numbers scratched out past "
            "square six, a child's rain boot standing upright and alone "
            "in the tall grass, a derelict boarded-up house looming in "
            "the background with one single upstairs window glowing warm "
            "light, cold desaturated color grade, thin mist at ground "
            "level, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow pull-back, "
            "widening from the crooked swing to reveal the full yard and "
            "the glowing upstairs window. The swing sways very slightly "
            "on its remaining chain with no visible cause, mist drifts "
            "low. Unsettling atmospheric horror mood, not a jump-scare, "
            "no text",
    },
    {
        "title": "watcher in the doorway",
        "has_people": True,
        "still_prompt": "A tall shadowy figure standing completely still "
            "in an open doorway at the end of a dark room, only a "
            "paper-thin sliver of its face catching light, a muddy "
            "handprint pressed into the door frame at head height, this "
            "doorway the only one in the house without boards over its "
            "window, an overturned chair a few feet in front of the "
            "figure as if someone backed away from it in a hurry, a thin "
            "line of dark liquid seeping from beneath the door threshold, "
            "dust suspended in the air, cold desaturated color grade, dark "
            "horror illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow tilt "
            "downward, starting on the figure's face and lowering to the "
            "overturned chair and the seeping line of liquid. The figure "
            "does not move, only dust motes drift through the light "
            "behind it. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "porcelain doll on a dusty shelf",
        "has_people": False,
        "still_prompt": "A cracked antique porcelain doll sitting alone on "
            "a dusty shelf in an abandoned room, one eye socket empty and "
            "hollow, its head turned slightly further than the last time "
            "anyone could have posed it, a perfectly clean circle in the "
            "thick dust around its base as if it had just been set down, "
            "faded child's height marks pencilled on the wall behind it "
            "that stop abruptly at a single date, a music box lying open "
            "and silent beside it with its dancer figure snapped off, "
            "faded wallpaper peeling behind it, a single beam of dim light "
            "crossing the shelf, cold desaturated color grade, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow push-in on "
            "the doll's face, the height marks on the wall passing out of "
            "frame as the camera closes in. Dust motes drift through the "
            "beam of light. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "figure in the attic window",
        "has_people": True,
        "still_prompt": "A decrepit house seen from outside at night, "
            "every window boarded and dark except the single attic window "
            "where a faint silhouette stands motionless with one hand "
            "pressed flat against the inside of the glass, breath fog "
            "faintly visible on the glass around where its face should "
            "be, a rusted weathervane above turning slowly though the air "
            "is still, a child's tricycle overturned and half-buried in "
            "dead leaves near the porch, bare twisted trees framing the "
            "house, cold desaturated color grade, thin fog drifting at "
            "ground level, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow rising "
            "camera movement, craning up from the tricycle on the ground "
            "to the attic window. The figure in the window does not move, "
            "only the weathervane turns slightly and fog drifts near the "
            "ground. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "flooded basement stairs",
        "has_people": False,
        "still_prompt": "A narrow staircase descending into a dark "
            "flooded basement, a single bare bulb swaying faintly "
            "overhead, a child's small toy sailboat drifting in a slow "
            "circle on the black water with no draft to explain it, one "
            "dry footprint on the stairs leading up out of the flood with "
            "no wet trail connecting to it, ripples spreading from a "
            "point in the water with nothing visible that could have "
            "caused them, shelves of drowned cardboard boxes sagging "
            "along the walls, water reflecting the dim light below, cold "
            "desaturated color grade, dark horror illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Bring this image to life with a slow dolly "
            "forward down the staircase toward the black water. The bare "
            "bulb sways, its reflection ripples on the water below, and "
            "the toy boat drifts in its slow circle. Unsettling "
            "atmospheric horror mood, not a jump-scare, no text",
    },
    {
        "title": "rows of empty hospital beds",
        "has_people": False,
        "still_prompt": "A long abandoned hospital ward lined with rows of "
            "rusted bed frames, all stripped bare except one still made "
            "with a deep body-shaped impression pressed into the sheets, "
            "a nurse call-button light blinking red and unanswered far "
            "down the ward, a clipboard hanging open on a bed rail "
            "covered in illegible scrawled handwriting that grows more "
            "erratic toward the bottom of the page, an IV stand tipped "
            "over with its tubing stretched taut toward the made bed, "
            "torn curtains hanging motionless, faint grey light through "
            "boarded windows, cold desaturated color grade, dust hanging "
            "in the air, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow pan left "
            "down the row of beds, ending on the one made bed with the "
            "body-shaped impression. Dust drifts through the grey light, "
            "the call light blinks steadily red, one torn curtain shifts. "
            "Unsettling atmospheric horror mood, not a jump-scare, no "
            "text",
    },
    {
        "title": "child silhouette at the tree line",
        "has_people": True,
        "still_prompt": "A small motionless silhouette standing at the "
            "edge of a dark tree line at dusk, facing away toward the "
            "trees, clutching something indistinct at its side, no "
            "footprints crossing the dew-soaked field to explain how it "
            "got there, a child's jump rope coiled neatly in the grass "
            "several feet behind it as if set down mid-game, a single "
            "warm porch light glowing small and distant on the opposite "
            "side of the field, cold desaturated color grade, thin mist "
            "drifting low, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow pull-back "
            "from the silhouette, widening to show the full field between "
            "it and the distant porch light. The silhouette remains "
            "perfectly still, only the mist drifts and the porch light "
            "flickers once. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "cracked mirror in a dark room",
        "has_people": False,
        "still_prompt": "An old cracked full-length mirror standing alone "
            "in a dim dust-covered room, a spider-web crack radiating from "
            "a single point at exactly head height, the reflection faintly "
            "showing a second chair that does not exist anywhere in the "
            "actual room, and a doorway open in the reflection that stands "
            "closed in the room itself, a candle nearby burned down to a "
            "stub yet still guttering, peeling wallpaper around the frame, "
            "cold desaturated color grade, dark horror illustration style, "
            "wide cinematic composition, 9:16 vertical, highly detailed, "
            "no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow orbital "
            "drift to the left around the mirror, briefly revealing more "
            "of the reflection's impossible second chair. Dust motes "
            "drift, the candle flame gutters, the light on the crack "
            "shifts. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "congregation of candles in a cellar",
        "has_people": True,
        "still_prompt": "Several robed figures standing perfectly still in "
            "a wide circle of lit candles on a stone cellar floor, backs "
            "entirely to camera, thick old wax rivulets on the floor "
            "suggesting decades of the same ritual repeated, a single "
            "empty high-backed chair at the center of the circle facing "
            "away from camera, a ring of small handwritten notes weighted "
            "down with stones just outside the candle circle, the cellar "
            "stairs above swallowed entirely in blackness, heavy shadow "
            "obscuring detail, cold desaturated color grade, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow push-in "
            "toward the empty high-backed chair at the center of the "
            "circle. The robed figures remain motionless, only the "
            "candle flames flicker and shadows shift along the stone "
            "walls. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "the root cellar door",
        "has_people": False,
        "still_prompt": "A heavy wooden root cellar door set at a steep "
            "angle into an overgrown hillside, its iron latch hanging "
            "open and a thick chain pooled uselessly in the weeds beside "
            "it, deep claw-like gouges dragged across the wood from "
            "inside out, a faint cold mist seeping from the gap at the "
            "door's edge even though the night air around it is still, "
            "dead sunflowers bowed over nearby, a single work boot left "
            "standing upright a few feet from the door, cold desaturated "
            "color grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow push-in "
            "toward the gap at the door's edge where the mist seeps out. "
            "The mist curls and thickens slightly, the dead sunflowers "
            "sway faintly. Unsettling atmospheric horror mood, not a "
            "jump-scare, no text",
    },
    {
        "title": "motel room 12",
        "has_people": True,
        "still_prompt": "A dated motel room lit only by a buzzing neon "
            "sign bleeding red light through the curtains, a figure "
            "sitting rigidly upright on the edge of the bed facing the "
            "wall instead of the door, the television on with no signal, "
            "static light flickering across the room, a room-service tray "
            "untouched on the dresser with a fork placed neatly across an "
            "empty plate, the number '12' visible upside down through the "
            "peephole view embedded faintly in the corner of the frame, "
            "cold desaturated color grade with red neon bleed, dark "
            "horror illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow pan right "
            "from the static-filled television to the motionless seated "
            "figure. The static flickers and shifts, the neon sign buzzes "
            "and pulses faintly through the curtains. Unsettling "
            "atmospheric horror mood, not a jump-scare, no text",
    },
    {
        "title": "the last pew",
        "has_people": False,
        "still_prompt": "The interior of an abandoned small-town church "
            "at night, rows of splintered wooden pews receding toward a "
            "collapsed altar, a single hymnal left open on the last pew "
            "to a page with no printed text at all, moonlight falling "
            "through a broken stained-glass window and scattering colored "
            "light across the dusty floor in a pattern that doesn't match "
            "the window's actual shape, cobwebs thick between the rafters, "
            "a rope from the bell tower dangling down through a hole in "
            "the ceiling, cold desaturated color grade, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow dolly "
            "forward up the center aisle toward the collapsed altar. The "
            "colored light shifts faintly as clouds pass outside the "
            "window, the bell rope sways almost imperceptibly, dust "
            "drifts in the moonlight. Unsettling atmospheric horror mood, "
            "not a jump-scare, no text",
    },
]
