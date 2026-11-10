# Ren'Py 8.x starter source — illustrations must be packaged separately.
define intel = Character("Intel")
define amd = Character("AMD")
define narrator = Character(None)
image bg citadel = Solid("#182b4d")
label start:
    scene bg citadel
    "At the gates of the x86 Citadel, an old software banner still flies."
    intel "The old code stays. Compatibility is the gate."
    amd "Then I'll build around it. A chiplet bridge could do more than a wall."
    menu:
        "Protect the legacy path":
            jump legacy
        "Build the modular bridge":
            jump bridge
label legacy:
    intel "We keep yesterday's applications alive. The citadel opens slowly, but safely."
    "ENDING: The Compatibility Pact. Old programs remain the kingdom's first promise."
    return
label bridge:
    amd "A modular bridge goes up beside the gate. New pieces can now join the design."
    "ENDING: The Chiplet Accord. The factions agree to collaborate on a new architecture."
    return
