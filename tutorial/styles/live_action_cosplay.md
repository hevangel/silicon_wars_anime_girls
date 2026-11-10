# Practical cosplay and studio photo workflow (#63)

**Delivery status:** Build briefs and prompts only; no fabric, pattern, photo, approved actor or budget figures are claimed complete.

## Construction-first steps

1. **Continuity trace:** compare [AMD](../../characters/amd/character_sheet.png) and [Intel](../../characters/intel/character_sheet.png) against the individual cosplay overrides. Identify the minimum recognizable logo-free silhouette before detailing embroidery or props.
2. **Choose maker/showpiece tier:** maker uses sewable/stick-on upgrades, EVA/craft foam and accessible patterns; showpiece can use tailored heavy twill, thermoplastic or careful 3D printed parts. Keep a sourced bill of materials rather than guessing costs.
3. **Pattern and attachment board:** sketch front/side/back and mark each seam, zip, snap, wig anchoring, crown fastening, shoulder armor and trim; document how each piece can be taken on/off and how arms/legs move.
4. **Safe prop test:** ensure Intel's wafer disc has a rounded edge and secure hand grip; AMD's chiplet gauntlets have flexible elbow and wrist zones. Avoid sharp edges, snagging wires and heavy headpieces.
5. **Photograph separate references:** 3-view full-body costume turnaround, hair/wig/makeup closeup, swatch/closure/material construction board, neutral portrait, at least two expressions and two camera angles per character.
6. **Matched two-character comparison:** neutral editorial studio full-body shot of AMD vs Intel; confirm braided hair and headset versus crown/epaulettes are easily distinguishable without text labels. No fake spectacle effects.
7. **Review:** costume designer certifies feasibility, performer/rights clearance documented, art director verifies identity and natural age-appropriate presentation, source list records actual fabrics and pattern licensing. Only then mark `human_approved` true.

## Maker vs showpiece checklist

| Category | Maker | Showpiece |
| --- | --- | --- |
| Intel crown | supported flexible foam and simple gem | sculpted lightweight crown with stable mount |
| Intel coat | altered blue coat and sewn cream panels | drafted/fit double-breasted coat and lined epaulettes |
| AMD jacket | modified black jacket with stitch-on crimson sections | fitted red/black garment with articulated faux-metal segments |
| AMD headset | off-the-shelf lightweight headset | custom-styled but still safe wearable headphones |
| Documentation | maker pattern and materials | detailed pattern, exploded joins, repair and transport plan |

All pricing must come from specific sourced shops/receipts and be dated; **no estimates are currently provided**.

## Material/physical QA and provenance

Store `costume_id`, pattern/source license, maker or supplier, material, weight, fastener, safe prop dimensions, actor/model release, camera/lens, photo version, source hashes, build notes and approval in a separate workflow manifest. Save approved source photography under `characters/<id>/references/live_action_cosplay/`; use Git LFS for large RAW files, ordinary-Git JPG thumbnails when authorized. Do not create fictitious source paths or mark a reference accepted before it exists.

**Troubleshooting:** loose wig → add hidden anchors; heavy armor → switch to lightweight foam and move straps to fabric lining; disconnected visual logo → apply to the canonical lower skirt/garment location; image looks CGI → remove speculative lighting and display real seams/fit; silhouette not recognizable → restore hair/crown/headphones before adding ornament.

Resources: [Krita](https://krita.org/) for paintovers; [Blender](https://www.blender.org/) for safe blocking. Photographed cosplay is a *style*, not lip-sync or animation technique.
