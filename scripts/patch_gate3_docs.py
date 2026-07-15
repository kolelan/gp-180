# -*- coding: utf-8 -*-
"""Add Gate 3 links + full param tables across presets."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"

PROFILES = {
    "soft": ("22–30", "40–50", "8–15", "200–320", "50–90", "мягкий сустейн / clean"),
    "lead": ("20–32", "40–50", "8–15", "220–350", "50–100", "лид: не рубить орнаменты"),
    "edge": ("25–40", "45–60", "5–15", "120–250", "30–70", "edge/OD: паузы чуть суше"),
    "stage": ("35–50", "50–70", "5–15", "100–200", "20–50", "сцена / anti-FB: суше паузы"),
    "ambient": ("15–28", "25–45", "10–40", "400–1200", "80–200", "длинные ноты / pad"),
    "call": ("28–40", "45–60", "5–15", "120–220", "30–70", "паузы между репликами"),
    "synth": ("15–28", "25–45", "10–40", "400–1200", "80–200", "synth bed / swell"),
}

MAP = {
    "presets/mandocaster/03-celtic-lead.md": "lead",
    "presets/mandocaster/04-rock-crossover.md": "edge",
    "presets/mandocaster/05-ambient-pad.md": "ambient",
    "presets/mandocaster/06-bright-lead.md": "lead",
    "presets/mandocaster/07-synth-bed.md": "synth",
    "presets/mandocaster/08-call-response.md": "call",
    "presets/akusticheskaya-mandolina-piezo/01-natural-di.md": "soft",
    "presets/akusticheskaya-mandolina-piezo/03-ballad-body.md": "soft",
    "presets/akusticheskaya-mandolina-piezo/04-celtic-sparkle.md": "lead",
    "presets/akusticheskaya-mandolina-piezo/05-stage-anti-feedback.md": "stage",
    "presets/akusticheskaya-mandolina-piezo/06-warm-jazz.md": "soft",
    "presets/akusticheskaya-mandolina-piezo/07-ambient-acoustic.md": "ambient",
    "presets/akusticheskaya-mandolina-piezo/08-piezo-body-ir.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/magnitnyy/01-natural-mag.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/magnitnyy/03-fingerstyle.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/magnitnyy/04-singer-edge.md": "edge",
    "presets/akusticheskaya-gitara-sredniy-korpus/piezo/01-natural-piezo.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/piezo/03-fingerstyle-piezo.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/piezo/04-ballad-warm.md": "soft",
    "presets/akusticheskaya-gitara-sredniy-korpus/piezo/05-stage-anti-feedback.md": "stage",
    "presets/akustika-stal-magnit/01-natural.md": "soft",
    "presets/akustika-stal-magnit/03-fingerstyle.md": "soft",
    "presets/akustika-stal-magnit/04-flatpick.md": "soft",
    "presets/akustika-stal-magnit/05-ballad-chorus.md": "soft",
    "presets/akustika-stal-magnit/06-singer-edge.md": "edge",
    "presets/akustika-stal-magnit/07-stage-clear.md": "stage",
    "presets/akustika-stal-magnit/08-soft-jazz.md": "soft",
    "presets/akustika-stal-magnit/10-capo-bright.md": "soft",
    "presets/akustika-stal-piezo/01-natural.md": "soft",
    "presets/akustika-stal-piezo/03-fingerstyle.md": "soft",
    "presets/akustika-stal-piezo/04-flatpick.md": "soft",
    "presets/akustika-stal-piezo/05-ballad-body.md": "soft",
    "presets/akustika-stal-piezo/06-singer-soft.md": "soft",
    "presets/akustika-stal-piezo/07-stage-anti-feedback.md": "stage",
    "presets/akustika-stal-piezo/08-warm-hall.md": "ambient",
    "presets/akustika-stal-piezo/10-capo-control.md": "soft",
    "presets/akustika-stal-piezo/11-piezo-body-ir.md": "soft",
    "presets/elektro-ansambl/01-folk-clean.md": "soft",
    "presets/elektro-ansambl/02-folk-edge.md": "edge",
    "presets/elektro-ansambl/05-dark-americana-clean.md": "soft",
    "presets/elektro-ansambl/06-dark-americana-edge.md": "edge",
    "nam-snaptone/recepty/01-mandolin-clean-fender.md": "soft",
    "ir-acoustic/scenarii/piezo-body-ir-plus-fx.md": "soft",
}


def link_for(rel: str) -> str:
    depth = len(Path(rel).parts) - 1
    return "../" * depth + "modules/01-nr/gate-3/"


def detailed_block(link: str, profile: str) -> str:
    T, R, A, Rel, H, note = PROFILES[profile]
    return (
        f"### Gate 3 ([описание]({link}))\n\n"
        f"{note[0].upper() + note[1:]}. Единицы и логика ручек — в карточке.\n\n"
        f"| Параметр | Ориентир | Зачем |\n"
        f"|----------|----------|--------|\n"
        f"| **Threshold** | **{T}** | порог по паузе без игры |\n"
        f"| **Ratio** | **{R}** | жёсткость глушения |\n"
        f"| **Attack** | **{A}** ≈ ms | открытие под атаку |\n"
        f"| **Release** | **{Rel}** ≈ ms | хвост ноты / тишина |\n"
        f"| **Hold** | **{H}** ≈ ms | стабильность на тремоло |\n"
    )


def table_rows(profile: str, link: str) -> str:
    T, R, A, Rel, H, _ = PROFILES[profile]
    return (
        f"| Gate3 ([карточка]({link})) | Threshold | {T} |\n"
        f"| Gate3 | Ratio | {R} |\n"
        f"| Gate3 | Attack ≈ ms | {A} |\n"
        f"| Gate3 | Release ≈ ms | {Rel} |\n"
        f"| Gate3 | Hold ≈ ms | {H} |\n"
    )


def patch_file(rel: str, profile: str) -> str:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    orig = text
    link = link_for(rel)
    block = detailed_block(link, profile)

    # Replace existing Gate 3 sections (greedy until next ### or --- at line start after content)
    for pat in (
        r"### NR — Gate 3\n.*?(?=\n### |\n---\n)",
        r"### Gate 3\n.*?(?=\n### |\n---\n)",
    ):
        m = re.search(pat, text, flags=re.S)
        if m:
            text = text[: m.start()] + block + "\n" + text[m.end() :]
            break
    else:
        # No ### Gate section: after first chain fence, or before first param table
        if "### Gate 3" not in text and "Gate 3 ([" not in text:
            m = re.search(r"```[\s\S]*?```\n", text)
            if m:
                text = text[: m.end()] + "\n" + block + "\n" + text[m.end() :]
            else:
                text = text.rstrip() + "\n\n" + block + "\n"

    # Compact tables: replace/remove old Gate3 lines and insert full set
    if re.search(r"\| Gate3", text):
        text = re.sub(r"\| Gate3[^\n]*\n", "", text)
        m2 = re.search(r"(\| Блок \|[^\n]*\n\|[-| :]+\|\n)", text)
        if m2:
            text = text[: m2.end()] + table_rows(profile, link) + text[m2.end() :]
        else:
            # starter tables without Блок
            m3 = re.search(
                r"(\| (?:Блок|Параметр)[^\n]*\n\|[-| :]+\|\n)", text
            )
            if m3:
                text = text[: m3.end()] + table_rows(profile, link) + text[m3.end() :]
            elif "|------|" in text or "|----------|" in text:
                m4 = re.search(r"(\|[-\s|]+\|\n)", text)
                if m4:
                    text = text[: m4.end()] + table_rows(profile, link) + text[m4.end() :]

    # Celtic-style starter still may say Gate3 only threshold in a different table
    # Ensure link somewhere
    if "modules/01-nr/gate-3" not in text:
        text = text.replace("NR Gate3", f"NR [Gate3]({link})", 1)

    # nam recipe table style without Блок header word in Russian sometimes uses different cols
    if rel.startswith("nam-snaptone/") and "| Gate3 |" not in text and "Threshold" in PROFILES[profile][0]:
        # recipe already may have Gate3 Threshold line removed — re-check
        if "Gate3 ([карточка]" not in text and "| Gate3 |" not in text:
            # after block insert ok
            pass

    if text == orig:
        return "unchanged"
    path.write_text(text, encoding="utf-8", newline="\n")
    return "updated"


def patch_import_doc() -> None:
    rel = "nam-snaptone/kak-importirovat.md"
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if "modules/01-nr/gate-3" in text:
        return
    text2 = text.replace(
        "**NR Gate 3** перед N→S",
        "**[NR Gate 3](../modules/01-nr/gate-3/)** перед N→S",
    )
    if text2 == text:
        text2 = text.replace(
            "NR Gate 3",
            "[NR Gate 3](../modules/01-nr/gate-3/)",
            1,
        )
    if text2 != text:
        path.write_text(text2, encoding="utf-8", newline="\n")
        print(" +", rel)


def main() -> None:
    patch_import_doc()
    for rel, profile in MAP.items():
        status = patch_file(rel, profile)
        print(status, rel)


if __name__ == "__main__":
    main()
