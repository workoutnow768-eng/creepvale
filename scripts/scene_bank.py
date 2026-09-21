"""
Scene bank for the creepvale (Horror/Spooky) video pipeline. Follows
CREEPVALE_VIDEO_STYLE.md exactly -- atmospheric dread, NOT gore or
jump-scares. 12 scenes, alternating has_people true/false 6/6 (same
pattern as dark-fantasy's and pallowyn's scene_bank.py).
"""

SCENES = [
    {
        "title": "flickering asylum corridor",
        "has_people": False,
        "still_prompt": "A long abandoned hospital corridor, peeling paint "
            "walls, a single flickering fluorescent light at the far end, "
            "rows of closed doors fading into darkness, cold desaturated "
            "color grade, thick dust hanging in the air, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "fluorescent light flickers and dust drifts slowly through the "
            "air, unsettling atmospheric horror mood, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "figure at the end of the hall",
        "has_people": True,
        "still_prompt": "A distant motionless silhouette standing at the "
            "far end of a dim empty hallway, back turned, faint cold light "
            "spilling from a doorway behind it, cold desaturated color "
            "grade, thick atmospheric fog low to the floor, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figure remains perfectly still, only the fog drifts faintly "
            "near the floor, unsettling atmospheric horror mood, subtle "
            "ambient motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "dead forest at night",
        "has_people": False,
        "still_prompt": "A dense forest of bare twisted dead trees at "
            "night, thick fog weaving between the trunks, a single dim "
            "unexplained light glowing far in the distance, cold "
            "desaturated blue-grey color grade, dark horror illustration "
            "style, wide cinematic composition, 9:16 vertical, highly "
            "detailed, no text, no watermark",
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
            "slightly crooked, a derelict house looming in the background, "
            "cold desaturated color grade, thin mist at ground level, dark "
            "horror illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "crooked swing sways very slightly on its chains with no "
            "visible cause, unsettling atmospheric horror mood, subtle "
            "ambient motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "watcher in the doorway",
        "has_people": True,
        "still_prompt": "A tall shadowy figure standing completely still "
            "in an open doorway at the end of a dark room, faint cold "
            "light outlining its silhouette from behind, dust suspended "
            "in the air, cold desaturated color grade, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
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
            "a dusty shelf in an abandoned room, faded wallpaper peeling "
            "behind it, a single beam of dim light crossing the shelf, "
            "cold desaturated color grade, dark horror illustration style, "
            "wide cinematic composition, 9:16 vertical, highly detailed, "
            "no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only "
            "dust motes drift through the beam of light, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "figure in the attic window",
        "has_people": True,
        "still_prompt": "A decrepit house seen from outside at night, a "
            "faint silhouette of a figure standing motionless in the "
            "single lit attic window, bare twisted trees framing the "
            "house, cold desaturated color grade, thin fog drifting at "
            "ground level, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figure in the window does not move, only the attic light "
            "flickers faintly and fog drifts near the ground, unsettling "
            "atmospheric horror mood, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "flooded basement stairs",
        "has_people": False,
        "still_prompt": "A narrow staircase descending into a dark "
            "flooded basement, a single bare bulb swaying faintly overhead, "
            "water reflecting the dim light below, cold desaturated color "
            "grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "bare bulb sways gently and its reflection ripples faintly on "
            "the water below, unsettling atmospheric horror mood, subtle "
            "ambient motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "rows of empty hospital beds",
        "has_people": False,
        "still_prompt": "A long abandoned hospital ward lined with rows of "
            "rusted empty bed frames, torn curtains hanging motionless, "
            "faint grey light through boarded windows, cold desaturated "
            "color grade, dust hanging in the air, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only dust "
            "drifts through the grey light and one torn curtain shifts "
            "faintly, unsettling atmospheric horror mood, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "child silhouette at the tree line",
        "has_people": True,
        "still_prompt": "A small motionless silhouette standing at the "
            "edge of a dark tree line at dusk, facing away toward the "
            "trees, an empty field of dead grass in the foreground, cold "
            "desaturated color grade, thin mist drifting low, dark horror "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "silhouette remains perfectly still, only the mist drifts "
            "faintly across the field, unsettling atmospheric horror "
            "mood, subtle ambient motion only, no camera movement, no "
            "zoom, no pan",
    },
    {
        "title": "cracked mirror in a dark room",
        "has_people": False,
        "still_prompt": "An old cracked full-length mirror standing alone "
            "in a dim dust-covered room, faint cold light catching the "
            "fractured glass, peeling wallpaper around it, cold "
            "desaturated color grade, dark horror illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only dust "
            "motes drift past the mirror and the light catching the crack "
            "shifts very faintly, unsettling atmospheric horror mood, "
            "subtle ambient motion only, no camera movement, no zoom, no "
            "pan",
    },
    {
        "title": "congregation of candles in a cellar",
        "has_people": True,
        "still_prompt": "Several robed figures standing perfectly still in "
            "a circle of lit candles in a stone cellar, backs mostly to "
            "camera, heavy shadow obscuring detail, cold desaturated color "
            "grade, dark horror illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, the "
            "figures remain motionless, only the candle flames flicker "
            "gently, unsettling atmospheric horror mood, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
]
