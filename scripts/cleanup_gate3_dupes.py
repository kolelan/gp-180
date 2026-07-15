# -*- coding: utf-8 -*-
"""Clean duplicate Gate3 tables; fix celtic starter columns."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"


def main() -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        orig = text

        # If detailed Gate 3 block exists, drop compact Gate3 table rows
        if "### Gate 3 ([описание]" in text or "### Gate 3 (" in text:
            text = re.sub(
                r"\| Gate3(?: \(\[карточка\]\([^)]+\)\))? \|[^\n]*\n",
                "",
                text,
            )

        # Fix celtic starter: if Gate3 lines lost and table jumps to COMP — insert pointer row
        if path.name == "03-celtic-lead.md":
            # ensure pointer after header if no Gate in starter table
            if (
                "| COMP | Sustain |" in text
                and "| Gate3" not in text.split("## Стартовые параметры")[1].split("## Параметры")[0]
            ):
                text = text.replace(
                    "|------|----------|----------|-------------|\n| COMP |",
                    "|------|----------|----------|-------------|\n"
                    "| Gate3 | см. ниже | — | [описание](../../modules/01-nr/gate-3/) |\n| COMP |",
                    1,
                )

        # nam recipe: drop trailing Gate section if table already has params
        if path.name == "01-mandolin-clean-fender.md":
            # restore gate rows in table if removed, then drop trailing section
            if "| Gate3" not in text and "### Gate 3" in text:
                # re-add compact rows into starter table then remove section — prefer keep section only
                pass
            # Remove duplicate trailing ### Gate 3 section if starter still has values elsewhere
            text = re.sub(
                r"\n### Gate 3 \(\[описание\]\([^)]+\)\)\n[\s\S]*$",
                "\n",
                text,
            )
            # If no gate params left, append compact into starter table
            if "Threshold**" not in text and "| Gate3" not in text:
                insert = (
                    "| Gate3 ([карточка](../../modules/01-nr/gate-3/)) | Threshold | 22–30 |\n"
                    "| Gate3 | Ratio | 40–50 |\n"
                    "| Gate3 | Attack ≈ ms | 8–15 |\n"
                    "| Gate3 | Release ≈ ms | 200–320 |\n"
                    "| Gate3 | Hold ≈ ms | 50–90 |\n"
                )
                text = text.replace(
                    "|------|----------|---------------------------|\n",
                    "|------|----------|---------------------------|\n" + insert,
                    1,
                )
            # link in chain
            text = text.replace(
                "NR(Gate3)",
                "NR([Gate3](../../modules/01-nr/gate-3/))",
                1,
            )

        if text != orig:
            path.write_text(text, encoding="utf-8", newline="\n")
            print("cleaned", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
