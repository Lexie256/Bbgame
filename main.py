#!/usr/bin/env python3
# Baby Steps: Vocab Quest
# A text-based, respectful simulation about the challenges of a single mom raising a newborn —
# where baby care effectiveness is tied to how well you answer cell biology questions.
# Paste into Replit (Python 3.10+) and click Run. No external libraries required.

import random
import sys
import textwrap
from dataclasses import dataclass, field

WRAP = 88

def say(msg=""):
    print(textwrap.fill(str(msg), WRAP))

def rule(char="-"):
    print(char * WRAP)

# -----------------------------
# Cell Biology Question Bank
# -----------------------------
# Each question: prompt, choices (A-D), correct ("A".."D"), an explanation

Question = dict

QUESTIONS: list[Question] = [
    {
        "q": "Which organelle is known as the powerhouse of the cell?",
        "opts": ["Ribosome", "Mitochondrion", "Golgi apparatus", "Lysosome"],
        "ans": "B",
        "why": "Mitochondria generate most of the cell's ATP via cellular respiration.",
    },
    {
        "q": "What is the primary function of ribosomes?",
        "opts": ["Lipid synthesis", "Protein synthesis", "DNA replication", "Cell movement"],
        "ans": "B",
        "why": "Ribosomes translate mRNA to build polypeptides (proteins).",
    },
    {
        "q": "Which macromolecule are enzymes mostly made of?",
        "opts": ["Carbohydrates", "Lipids", "Proteins", "Nucleic acids"],
        "ans": "C",
        "why": "Most enzymes are proteins that catalyze biochemical reactions.",
    },
    {
        "q": "Which structure controls what enters and leaves the cell?",
        "opts": ["Cell wall", "Plasma membrane", "Cytoskeleton", "Nucleus"],
        "ans": "B",
        "why": "The plasma membrane is selectively permeable and regulates transport.",
    },
    {
        "q": "DNA is replicated during which cell cycle phase?",
        "opts": ["G1", "S", "G2", "M"],
        "ans": "B",
        "why": "S phase (Synthesis) is when DNA replication occurs.",
    },
    {
        "q": "What carries amino acids to the ribosome during translation?",
        "opts": ["mRNA", "tRNA", "rRNA", "snRNA"],
        "ans": "B",
        "why": "tRNA molecules deliver specific amino acids to the ribosome.",
    },
    {
        "q": "Which term describes diffusion of water across a semi-permeable membrane?",
        "opts": ["Osmosis", "Active transport", "Endocytosis", "Facilitated diffusion"],
        "ans": "A",
        "why": "Osmosis is water's passive movement across membranes.",
    },
    {
        "q": "Where in eukaryotic cells does glycolysis occur?",
        "opts": ["Mitochondrial matrix", "Cytosol", "Nucleus", "Golgi"],
        "ans": "B",
        "why": "Glycolysis occurs in the cytosol and does not require oxygen.",
    },
    {
        "q": "Which organelle modifies, sorts, and packages proteins?",
        "opts": ["Golgi apparatus", "Smooth ER", "Rough ER", "Peroxisome"],
        "ans": "A",
        "why": "The Golgi receives proteins and lipids, processes them, and ships them.",
    },
    {
        "q": "Which base pairs with adenine in DNA?",
        "opts": ["Uracil", "Cytosine", "Guanine", "Thymine"],
        "ans": "D",
        "why": "In DNA, A pairs with T; in RNA, A pairs with U.",
    },
    {
        "q": "What is the central dogma of molecular biology?",
        "opts": [
            "Protein → DNA → RNA",
            "DNA → RNA → Protein",
            "RNA → DNA → Protein",
            "DNA → Protein → RNA",
        ],
        "ans": "B",
        "why": "Information flows from DNA to RNA (transcription) to protein (translation).",
    },
    {
        "q": "Which process produces gametes with half the number of chromosomes?",
        "opts": ["Mitosis", "Meiosis", "Binary fission", "Budding"],
        "ans": "B",
        "why": "Meiosis reduces ploidy and increases genetic diversity via recombination.",
    },
    {
        "q": "Phospholipids are described as amphipathic because they have:",
        "opts": [
            "Only hydrophobic parts",
            "Only hydrophilic parts",
            "Both hydrophobic and hydrophilic parts",
            "Neither hydrophobic nor hydrophilic parts",
        ],
        "ans": "C",
        "why": "They have hydrophilic heads and hydrophobic tails — essential for membranes.",
    },
    {
        "q": "Which organelle contains digestive enzymes for intracellular digestion?",
        "opts": ["Peroxisome", "Lysosome", "Nucleolus", "Chloroplast"],
        "ans": "B",
        "why": "Lysosomes contain hydrolytic enzymes to break down biomolecules.",
    },
    {
        "q": "Transcription occurs in the ____ and translation occurs in the ____.",
        "opts": ["cytosol; nucleus", "nucleus; cytosol", "Golgi; ER", "ER; Golgi"],
        "ans": "B",
        "why": "mRNA is transcribed in the nucleus and translated by ribosomes in the cytosol.",
    },
    {
        "q": "What is a codon?",
        "opts": [
            "A three-nucleotide sequence in mRNA",
            "A protein folding motif",
            "A DNA replication origin",
            "A lipid raft",
        ],
        "ans": "A",
        "why": "Each codon encodes an amino acid or start/stop signal during translation.",
    },
    {
        "q": "Which bond links amino acids in a polypeptide?",
        "opts": ["Glycosidic", "Phosphodiester", "Peptide", "Ionic"],
        "ans": "C",
        "why": "Peptide bonds connect amino acids in proteins.",
    },
    {
        "q": "Which component of the cytoskeleton provides tracks for vesicle transport?",
        "opts": ["Intermediate filaments", "Microtubules", "Actin filaments", "Centrioles"],
        "ans": "B",
        "why": "Motor proteins like kinesin move along microtubules.",
    },
    {
        "q": "Which step directly consumes oxygen in cellular respiration?",
        "opts": ["Glycolysis", "Citric acid cycle", "Electron transport chain", "Fermentation"],
        "ans": "C",
        "why": "Oxygen is the terminal electron acceptor in the ETC.",
    },
    {
        "q": "Which term describes movement of molecules from high to low concentration?",
        "opts": ["Active transport", "Diffusion", "Phagocytosis", "Pinocytosis"],
        "ans": "B",
        "why": "Diffusion is passive movement down a concentration gradient.",
    },
    {
        "q": "Which polymer stores genetic information in most organisms?",
        "opts": ["Protein", "DNA", "RNA", "Glycogen"],
        "ans": "B",
        "why": "DNA is the hereditary material in nearly all organisms.",
    },
    {
        "q": "Which structure synthesizes lipids and detoxifies certain chemicals?",
        "opts": ["Rough ER", "Smooth ER", "Golgi", "Ribosome"],
        "ans": "B",
        "why": "Smooth ER is involved in lipid synthesis and detoxification.",
    },
    {
        "q": "What is the fluid-filled interior of the cell (minus organelles) called?",
        "opts": ["Cytoplasm", "Cytosol", "Matrix", "Stroma"],
        "ans": "B",
        "why": "Cytosol is the aqueous component of the cytoplasm where many reactions occur.",
    },
    {
        "q": "What type of bond links nucleotides in a DNA strand?",
        "opts": ["Peptide", "Phosphodiester", "Hydrogen", "Disulfide"],
        "ans": "B",
        "why": "Adjacent nucleotides are joined by phosphodiester bonds in the backbone.",
    },
    {
        "q": "Which process converts glucose to pyruvate?",
        "opts": ["Glycolysis", "Gluconeogenesis", "Beta-oxidation", "Translation"],
        "ans": "A",
        "why": "Glycolysis breaks down glucose into pyruvate, producing ATP and NADH.",
    },
]

# -----------------------------
# Data Models
# -----------------------------

@dataclass
class Item:
    name: str
    price: int
    uses_per_unit: int
    base_effect: int  # how much it improves a stat before multiplier

@dataclass
class Player:
    cash: int = 50
    inventory: dict = field(default_factory=lambda: {"formula": 2, "diapers": 6, "wipes": 10, "toy": 1, "blanket": 1, "lotion": 1})
    correct: int = 0
    total: int = 0

@dataclass
class Baby:
    hunger: int = 50
    hygiene: int = 50
    energy: int = 50
    happiness: int = 50
    health: int = 100

    def clamp(self):
        for k in ("hunger", "hygiene", "energy", "happiness", "health"):
            v = getattr(self, k)
            setattr(self, k, max(0, min(100, v)))

# -----------------------------
# Game Constants
# -----------------------------

STORE: dict[str, Item] = {
    "formula": Item("formula", price=6, uses_per_unit=3, base_effect=28),
    "diapers": Item("diapers", price=10, uses_per_unit=12, base_effect=22),
    "wipes": Item("wipes", price=4, uses_per_unit=15, base_effect=18),
    "toy": Item("toy", price=12, uses_per_unit=9999, base_effect=16),  # toy is durable
    "blanket": Item("blanket", price=8, uses_per_unit=9999, base_effect=14),
    "lotion": Item("lotion", price=7, uses_per_unit=6, base_effect=12),
}

ACTIONS = [
    ("Feed (uses formula)", "feed"),
    ("Change diaper (uses diaper + wipes)", "change"),
    ("Nap/Soothing (needs blanket)", "nap"),
    ("Playtime (needs toy)", "play"),
    ("Apply lotion (uses lotion)", "lotion"),
    ("Shop at the corner store", "shop"),
    ("Check baby & inventory", "check"),
    ("End the day", "end"),
    ("Quit game", "quit"),
]

# Question state
_unused_q_indices = list(range(len(QUESTIONS)))
random.shuffle(_unused_q_indices)

def draw_question():
    global _unused_q_indices
    if not _unused_q_indices:
        _unused_q_indices = list(range(len(QUESTIONS)))
        random.shuffle(_unused_q_indices)
    idx = _unused_q_indices.pop()
    return idx, QUESTIONS[idx]

def ask_question(player: Player):
    idx, q = draw_question()
    say(f"QUIZ — {q['q']}")
    options = q["opts"]
    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(options):
        print(f"  {letters[i]}. {opt}")
    while True:
        guess = input("Your answer (A/B/C/D): ").strip().upper()
        if guess in letters:
            break
        print("Please enter A, B, C, or D.")
    player.total += 1
    if guess == q["ans"]:
        player.correct += 1
        say("Nice! That's correct.")
        print(f"Explanation: {q['why']}")
        return True
    else:
        say("Not quite.")
        print(f"Correct answer: {q['ans']} — {options[letters.index(q['ans'])]}")
        print(f"Explanation: {q['why']}")
        return False

def apply_quiz_modifiers(correct: bool):
    # How well the item works & how many uses are spent depend on the answer
    if correct:
        effect_mult = 1.25
        uses_cost = 1
        happiness_delta = +4
        cash_bonus = 3  # reward knowledge with a tiny stipend (tutoring prize / scholarship vibe)
    else:
        effect_mult = 0.7
        uses_cost = 2
        happiness_delta = -5
        cash_bonus = 0
    return effect_mult, uses_cost, happiness_delta, cash_bonus

def degrade_stats(baby: Baby):
    # Base daily/turn decay
    baby.hunger -= random.randint(8, 12)
    baby.hygiene -= random.randint(5, 9)
    baby.energy -= random.randint(4, 8)
    baby.happiness -= random.randint(3, 6)

    # Health penalties if core needs are low
    penalty = 0
    for need, val in [("hunger", baby.hunger), ("hygiene", baby.hygiene), ("energy", baby.energy), ("happiness", baby.happiness)]:
        if val < 30:
            penalty += 2
        if val < 10:
            penalty += 3
    baby.health -= penalty

    # Random little events (both up and down)
    if random.random() < 0.12:
        event = random.choice([
            ("Spit-up! Hygiene drops a bit.", ("hygiene", -8)),
            ("Growth spurt hunger!", ("hunger", -10)),
            ("Catnap restored some energy.", ("energy", +7)),
            ("Giggle fit boosted happiness.", ("happiness", +6)),
        ])
        say(f"Event: {event[0]}")
        attr, delta = event[1]
        setattr(baby, attr, getattr(baby, attr) + delta)

    baby.clamp()

def print_status(day, turn, player: Player, baby: Baby):
    rule("=")
    say(f"Day {day} — Turn {turn}")
    rule("-")
    say(f"Baby — Health:{baby.health:>3}  Hunger:{baby.hunger:>3}  Hygiene:{baby.hygiene:>3}  Energy:{baby.energy:>3}  Happiness:{baby.happiness:>3}")
    say(f"Mom — Cash: ${player.cash:>3} | Inventory: {player.inventory}")
    say(f"Study — Quiz Score: {player.correct}/{player.total} correct")
    rule("=")

def ensure_item(player: Player, key: str, min_needed: int = 1):
    return player.inventory.get(key, 0) >= min_needed

def spend_item(player: Player, key: str, amount: int):
    have = player.inventory.get(key, 0)
    player.inventory[key] = max(0, have - amount)

def add_item(player: Player, key: str, amount: int):
    player.inventory[key] = player.inventory.get(key, 0) + amount

def shop(player: Player):
    rule()
    say("Welcome to the corner store. What do you need?")
    say("Tip: Doing well on quizzes gives you a small cash bonus after actions.")
    print("Items:")
    for k, it in STORE.items():
        pack = it.uses_per_unit
        unit = "uses" if pack < 9999 else "durable"
        info = f"{pack} {unit}" if pack < 9999 else unit
        print(f"  - {it.name:8}  ${it.price:>2}  ({info})")
    say("Type the item name to buy, or press Enter to leave.")
    while True:
        choice = input("Buy what? ").strip().lower()
        if not choice:
            break
        if choice not in STORE:
            print("Sorry, we don't carry that.")
            continue
        item = STORE[choice]
        if player.cash < item.price:
            print("You can't afford that right now.")
            continue
        player.cash -= item.price
        if item.uses_per_unit >= 9999:
            add_item(player, choice, 1)  # durable items counted as quantity
        else:
            add_item(player, choice, item.uses_per_unit)
        print(f"Bought {choice}. Cash left: ${player.cash}")

def do_feed(player: Player, baby: Baby):
    if not ensure_item(player, "formula", 1):
        say("You need formula to feed the baby. Pick some up at the store.")
        return
    correct = ask_question(player)
    effect_mult, uses_cost, happiness_delta, cash_bonus = apply_quiz_modifiers(correct)
    spend_item(player, "formula", uses_cost)
    baby.hunger += int(STORE["formula"].base_effect * effect_mult)
    baby.happiness += happiness_delta
    player.cash += cash_bonus
    say(f"Feeding done. Formula used: {uses_cost}. Cash +${cash_bonus}.")
    baby.clamp()

def do_change(player: Player, baby: Baby):
    if not (ensure_item(player, "diapers", 1) and ensure_item(player, "wipes", 1)):
        say("You need both diapers and wipes to change the baby.")
        return
    correct = ask_question(player)
    effect_mult, uses_cost, happiness_delta, cash_bonus = apply_quiz_modifiers(correct)
    spend_item(player, "diapers", uses_cost)
    spend_item(player, "wipes", uses_cost)
    baby.hygiene += int(STORE["diapers"].base_effect * effect_mult)
    baby.happiness += happiness_delta
    player.cash += cash_bonus
    say(f"Fresh diaper! Diapers & wipes used: {uses_cost} each. Cash +${cash_bonus}.")
    baby.clamp()

def do_nap(player: Player, baby: Baby):
    if not ensure_item(player, "blanket", 1):
        say("A cozy blanket helps the baby nap. Buy one at the store.")
        return
    correct = ask_question(player)
    effect_mult, uses_cost, happiness_delta, cash_bonus = apply_quiz_modifiers(correct)
    # blanket is durable; uses_cost doesn't consume blanket, but bad answers reduce effect
    baby.energy += int(STORE["blanket"].base_effect * effect_mult)
    baby.happiness += happiness_delta
    if not correct:
        baby.hunger -= 3  # restless nap can make baby a bit hungrier
    player.cash += cash_bonus
    say(f"Nap time. Blanket tucked. Cash +${cash_bonus}.")
    baby.clamp()

def do_play(player: Player, baby: Baby):
    if not ensure_item(player, "toy", 1):
        say("A simple toy goes a long way. Pick one up at the store.")
        return
    correct = ask_question(player)
    effect_mult, uses_cost, happiness_delta, cash_bonus = apply_quiz_modifiers(correct)
    baby.happiness += int(STORE["toy"].base_effect * effect_mult) + happiness_delta
    baby.energy -= 3  # playtime tires baby slightly
    player.cash += cash_bonus
    say(f"Playtime complete. Smiles all around. Cash +${cash_bonus}.")
    baby.clamp()

def do_lotion(player: Player, baby: Baby):
    if not ensure_item(player, "lotion", 1):
        say("You're out of lotion. Buy some to help with skin comfort/health.")
        return
    correct = ask_question(player)
    effect_mult, uses_cost, happiness_delta, cash_bonus = apply_quiz_modifiers(correct)
    spend_item(player, "lotion", uses_cost)
    baby.health += int(STORE["lotion"].base_effect * effect_mult)
    baby.hygiene += 4
    baby.happiness += happiness_delta
    player.cash += cash_bonus
    say(f"Lotion applied. Lotion used: {uses_cost}. Cash +${cash_bonus}.")
    baby.clamp()

def choose_action():
    print("\nWhat would you like to do?")
    for i, (label, key) in enumerate(ACTIONS, 1):
        print(f"  {i}. {label}")
    while True:
        try:
            pick = int(input("Choose an action (1-9): ").strip())
            if 1 <= pick <= len(ACTIONS):
                return ACTIONS[pick - 1][1]
        except ValueError:
            pass
        print("Please pick a valid number.")

def prologue():
    rule("=")
    say("BABY STEPS: VOCAB QUEST")
    rule("-")
    say("You're a new mom, doing your best while your co-parent isn't in the picture. "
        "Money is tight, sleep is scarce, and your tiny human has big needs. "
        "Fortunately, you've got grit — and your biology class. "
        "Answer quick cell-bio questions to make baby care more effective and stretch supplies.")
    rule("-")
    say("Your goal: keep baby healthy and happy through 10 tough turns. "
        "Do well on quizzes to save supplies and earn a few bucks. "
        "If Health hits 0, the run ends. You win by making it to the end!")
    rule("=")
    input("Press Enter to begin...")

def epilogue(player: Player, baby: Baby, day, turn):
    rule("=")
    say("RUN COMPLETE")
    rule("-")
    say(f"Final status — Health:{baby.health}  Hunger:{baby.hunger}  Hygiene:{baby.hygiene}  Energy:{baby.energy}  Happiness:{baby.happiness}")
    say(f"Cash: ${player.cash}  Inventory: {player.inventory}")
    acc = (player.correct / player.total * 100) if player.total else 0.0
    say(f"Quiz accuracy: {player.correct}/{player.total} ({acc:.1f}%)")
    if baby.health <= 0:
        say("It was a hard stretch. Consider reviewing key terms, shopping strategically, and trying again.")
    else:
        say("You made it through! Nice juggling — knowledge really helped stretch those supplies.")
    rule("=")

def main():
    random.seed()
    player = Player()
    baby = Baby()
    prologue()

    max_turns = 10
    day = 1
    for turn in range(1, max_turns + 1):
        degrade_stats(baby)
        if baby.health <= 0:
            say("Your baby's health has fallen to 0. The run ends here.")
            break
        print_status(day, turn, player, baby)
        act = choose_action()
        if act == "feed":
            do_feed(player, baby)
        elif act == "change":
            do_change(player, baby)
        elif act == "nap":
            do_nap(player, baby)
        elif act == "play":
            do_play(player, baby)
        elif act == "lotion":
            do_lotion(player, baby)
        elif act == "shop":
            shop(player)
        elif act == "check":
            print_status(day, turn, player, baby)
            input("Press Enter to continue...")
        elif act == "end":
            say("You take a breath, tidy up, and brace for the next stretch...")
        elif act == "quit":
            say("Thanks for playing. Take care out there.")
            break

    epilogue(player, baby, day, turn)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Take care!")