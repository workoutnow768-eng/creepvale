"""
Scene bank for the creepvale (Horror/Spooky) video pipeline. Follows
CREEPVALE_VIDEO_STYLE.md exactly -- atmospheric dread, NOT gore or
jump-scares. 12 scenes, alternating has_people true/false 6/6 (same
pattern as dark-fantasy's and pallowyn's scene_bank.py).

Revised for more specific, unsettling detail per feedback that plain
"figure in a doorway" imagery reads as flat rather than scary -- every
scene now carries at least one concrete "wrongness" detail (an object
out of place, an impossible shadow, a trace with no explanation) instead
of relying on the silhouette alone to carry the scene.
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
            "reaching hands, a door standing open at the far end onto "
            "pure blackness, cold desaturated color grade, thick dust "
            "hanging in the air, dark horror illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "fluorescent light flickers and dust drifts slowly through the "
            "air, unsettling atmospheric horror mood, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "figure at the end of the hall",
        "has_people": True,
        "still_prompt": "A distant motionless silhouette standing at the "
            "far end of a dim empty hallway exactly where it bends out of "
            "sight, proportions subtly too tall and too thin, head tilted "
            "at an unnatural angle, its shadow stretching toward the "
            "camera far longer than the faint light behind it could "
            "explain, cold desaturated color grade, thick atmospheric fog "
            "low to the floor, dark horror illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figure remains perfectly still, only the fog drifts faintly "
            "near the floor and the impossible shadow flickers slightly, "
            "unsettling atmospheric horror mood, subtle ambient motion "
            "only, no camera movement, no zoom, no pan",
    },
    {
        "title": "dead forest at night",
        "has_people": False,
        "still_prompt": "A dense forest of bare twisted dead trees at "
            "night, bark peeling from the trunks in sheets like shed skin, "
            "a small child's single shoe half-sunk in wet blackened "
            "leaves in the foreground, thick fog weaving between the "
            "trunks, a single dim unexplained light glowing far in the "
            "distance down a narrow deer path, cold desaturated blue-grey "
            "color grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "fog drifts slowly between the tree trunks and the distant "
            "light flickers faintly, unsettling atmospheric horror mood, "
            "subtle ambient motion only, no camera movement, no zoom, no "
            "pan",
    },
    {
        "title": "empty swing in overgrown yard",
        "has_people": False,
        "still_prompt": "A rusted metal swing set standing alone in an "
            "overgrown weed-choked yard at dusk, one swing hanging "
            "crooked with its second chain snapped and dragging in the "
            "dirt, a faded chalk hopscotch grid barely visible on a "
            "cracked path nearby, a derelict boarded-up house looming in "
            "the background with one single upstairs window glowing warm "
            "light, cold desaturated color grade, thin mist at ground "
            "level, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "crooked swing sways very slightly on its remaining chain with "
            "no visible cause, unsettling atmospheric horror mood, subtle "
            "ambient motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "watcher in the doorway",
        "has_people": True,
        "still_prompt": "A tall shadowy figure standing completely still "
            "in an open doorway at the end of a dark room, only a "
            "paper-thin sliver of its face catching light, a muddy "
            "handprint pressed into the door frame at head height, this "
            "doorway the only one in the house without boards over its "
            "window, dust suspended in the air, cold desaturated color "
            "grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figure does not move, only dust motes drift slowly through "
            "the light behind it, unsettling atmospheric horror mood, "
            "subtle ambient motion only, no camera movement, no zoom, no "
            "pan",
    },
    {
        "title": "porcelain doll on a dusty shelf",
        "has_people": False,
        "still_prompt": "A cracked antique porcelain doll sitting alone on "
            "a dusty shelf in an abandoned room, one eye socket empty and "
            "hollow, a perfectly clean circle in the thick dust around its "
            "base as if it had just been set down, faded child's height "
            "marks pencilled on the wall behind it that stop abruptly at a "
            "single date, faded wallpaper peeling behind it, a single beam "
            "of dim light crossing the shelf, cold desaturated color "
            "grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only "
            "dust motes drift through the beam of light, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "figure in the attic window",
        "has_people": True,
        "still_prompt": "A decrepit house seen from outside at night, "
            "every window boarded and dark except the single attic window "
            "where a faint silhouette stands motionless with one hand "
            "pressed flat against the inside of the glass, a rusted "
            "weathervane above turning slowly though the air is still, "
            "bare twisted trees framing the house, cold desaturated color "
            "grade, thin fog drifting at ground level, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figure in the window does not move, only the weathervane "
            "turns slightly and fog drifts near the ground, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "flooded basement stairs",
        "has_people": False,
        "still_prompt": "A narrow staircase descending into a dark "
            "flooded basement, a single bare bulb swaying faintly "
            "overhead, a child's small toy sailboat drifting in a slow "
            "circle on the black water with no draft to explain it, one "
            "dry footprint on the stairs leading up out of the flood with "
            "no wet trail connecting to it, water reflecting the dim "
            "light below, cold desaturated color grade, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "bare bulb sways gently, its reflection ripples faintly on the "
            "water below, and the toy boat drifts in its slow circle, "
            "unsettling atmospheric horror mood, subtle ambient motion "
            "only, no camera movement, no zoom, no pan",
    },
    {
        "title": "rows of empty hospital beds",
        "has_people": False,
        "still_prompt": "A long abandoned hospital ward lined with rows of "
            "rusted bed frames, all stripped bare except one still made "
            "with a deep body-shaped impression pressed into the sheets, "
            "a nurse call-button light blinking red and unanswered far "
            "down the ward, a clipboard hanging open on a bed rail "
            "covered in illegible scrawled handwriting, torn curtains "
            "hanging motionless, faint grey light through boarded "
            "windows, cold desaturated color grade, dust hanging in the "
            "air, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only dust "
            "drifts through the grey light, the call light blinks steadily "
            "red, and one torn curtain shifts faintly, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "child silhouette at the tree line",
        "has_people": True,
        "still_prompt": "A small motionless silhouette standing at the "
            "edge of a dark tree line at dusk, facing away toward the "
            "trees, clutching something indistinct at its side, no "
            "footprints crossing the dew-soaked field to explain how it "
            "got there, a single warm porch light glowing small and "
            "distant on the opposite side of the field, cold desaturated "
            "color grade, thin mist drifting low, dark horror illustration "
            "style, wide cinematic composition, 9:16 vertical, highly "
            "detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "silhouette remains perfectly still, only the mist drifts "
            "faintly across the field and the distant porch light flickers "
            "once, unsettling atmospheric horror mood, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "cracked mirror in a dark room",
        "has_people": False,
        "still_prompt": "An old cracked full-length mirror standing alone "
            "in a dim dust-covered room, a spider-web crack radiating from "
            "a single point at exactly head height, the reflection faintly "
            "showing a second chair that does not exist anywhere in the "
            "actual room, a candle nearby burned down to a stub yet still "
            "guttering, peeling wallpaper around the frame, cold "
            "desaturated color grade, dark horror illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only dust "
            "motes drift past the mirror, the candle flame gutters, and "
            "the light catching the crack shifts very faintly, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "congregation of candles in a cellar",
        "has_people": True,
        "still_prompt": "Several robed figures standing perfectly still in "
            "a wide circle of lit candles on a stone cellar floor, backs "
            "entirely to camera, thick old wax rivulets on the floor "
            "suggesting decades of the same ritual repeated, a single "
            "empty high-backed chair at the center of the circle facing "
            "away from camera, the cellar stairs above swallowed entirely "
            "in blackness, heavy shadow obscuring detail, cold desaturated "
            "color grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figures remain motionless, only the candle flames flicker "
            "gently and shadows shift faintly along the stone walls, "
            "unsettling atmospheric horror mood, subtle ambient motion "
            "only, no camera movement, no zoom, no pan",
    },
]
