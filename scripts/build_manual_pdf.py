#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка PDF из русского перевода инструкции GP-180."""

from __future__ import annotations

import re
from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
MANUAL_DIR = ROOT / "docs" / "manual-ru"
OUT_DIR = ROOT / "docs" / "pdf"
OUT_FILE = OUT_DIR / "GP-180_Instrukciya_RU.pdf"

FONT_REG = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")

MANUAL_ORDER = [
    "README.md",
    "01-privetstvie-i-bezopasnost.md",
    "02-obzor.md",
    "03-panel.md",
    "04-nachalo-raboty.md",
    "05-ekrany.md",
    "06-redaktirovanie-patcha.md",
    "07-globalnye-nastroyki.md",
    "08-soft-i-scenarii.md",
    "09-midi.md",
    "10-ustranenie-neispravnostey.md",
    "11-specifikacii.md",
]


class ManualPDF(FPDF):
    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("DocFont", size=9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Valeton GP-180 — инструкция (RU)  |  {self.page_no()}", align="C")

    def write_block(self, text: str, h: float = 6) -> None:
        """Печать абзаца с гарантированным левым краем."""
        if not text:
            self.ln(h / 2)
            return
        self.set_x(self.l_margin)
        # fpdf иногда оставляет слишком узкую оставшуюся ширину
        usable = self.epw
        if usable < 20:
            self.ln(h)
            self.set_x(self.l_margin)
        self.multi_cell(self.epw, h, text)


def strip_md_links(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return text


def render_markdown(pdf: ManualPDF, text: str) -> None:
    lines = text.replace("\r\n", "\n").split("\n")
    i = 0
    in_code = False
    table_buf: list[str] = []

    def flush_table() -> None:
        nonlocal table_buf
        if not table_buf:
            return
        rows = []
        for raw in table_buf:
            if re.match(r"^\s*\|?\s*:-+", raw):
                continue
            cells = [strip_md_links(c.strip()) for c in raw.strip().strip("|").split("|")]
            if cells:
                rows.append(cells)
        table_buf = []
        if not rows:
            return
        pdf.set_font("DocFont", size=10)
        pdf.set_text_color(30, 30, 30)
        for row in rows:
            line = " — ".join(row) if len(row) > 1 else row[0]
            pdf.write_block(line, 5.5)
        pdf.ln(2)

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("```"):
            flush_table()
            in_code = not in_code
            i += 1
            continue

        if in_code:
            flush_table()
            pdf.set_font("DocFont", size=9)
            pdf.set_text_color(40, 40, 40)
            pdf.set_fill_color(245, 245, 245)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(pdf.epw, 5, line if line else " ", fill=True)
            i += 1
            continue

        if line.strip().startswith("|"):
            table_buf.append(line)
            i += 1
            continue
        else:
            flush_table()

        if not line.strip():
            pdf.ln(3)
            i += 1
            continue

        if line.startswith("# "):
            pdf.add_page()
            pdf.set_font("DocFont", style="B", size=18)
            pdf.set_text_color(20, 20, 20)
            pdf.write_block(strip_md_links(line[2:].strip()), 10)
            pdf.ln(4)
        elif line.startswith("## "):
            pdf.ln(3)
            pdf.set_font("DocFont", style="B", size=14)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(strip_md_links(line[3:].strip()), 8)
            pdf.ln(2)
        elif line.startswith("### "):
            pdf.ln(2)
            pdf.set_font("DocFont", style="B", size=12)
            pdf.set_text_color(40, 40, 40)
            pdf.write_block(strip_md_links(line[4:].strip()), 7)
            pdf.ln(1)
        elif line.strip() == "---":
            pdf.ln(2)
        elif line.lstrip().startswith("- ") or line.lstrip().startswith("* "):
            content = strip_md_links(re.sub(r"^\s*[-*]\s+", "", line))
            pdf.set_font("DocFont", size=11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(f"• {content}", 6)
        elif re.match(r"^\d+\.\s+", line.lstrip()):
            content = strip_md_links(line.lstrip())
            pdf.set_font("DocFont", size=11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(content, 6)
        elif line.lstrip().startswith(">"):
            content = strip_md_links(line.lstrip()[1:].strip())
            pdf.set_font("DocFont", size=10)
            pdf.set_text_color(70, 70, 70)
            pdf.write_block(content, 6)
        else:
            pdf.set_font("DocFont", size=11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(strip_md_links(line), 6)

        i += 1

    flush_table()


def build() -> Path:
    if not FONT_REG.exists() or not FONT_BOLD.exists():
        raise SystemExit("Не найдены Arial TTF в C:\\Windows\\Fonts")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf = ManualPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("DocFont", fname=str(FONT_REG))
    pdf.add_font("DocFont", style="B", fname=str(FONT_BOLD))
    pdf.set_margins(18, 18, 18)

    # Title page
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("DocFont", style="B", size=24)
    pdf.multi_cell(0, 12, "Valeton GP-180", align="C")
    pdf.ln(4)
    pdf.set_font("DocFont", style="B", size=16)
    pdf.multi_cell(0, 9, "Инструкция по эксплуатации", align="C")
    pdf.ln(2)
    pdf.set_font("DocFont", size=12)
    pdf.multi_cell(0, 7, "Русский перевод (на основе Firmware V1.0.0)", align="C")
    pdf.ln(8)
    pdf.set_font("DocFont", size=10)
    pdf.set_text_color(90, 90, 90)
    pdf.multi_cell(
        0,
        6,
        "Неофициальный перевод документации проекта gp-180.\n"
        "Оригинал: GP-180 Online Manual EN Firmware V1.0.0.",
        align="C",
    )

    for name in MANUAL_ORDER:
        path = MANUAL_DIR / name
        if not path.exists():
            print(f"skip missing: {path}")
            continue
        render_markdown(pdf, path.read_text(encoding="utf-8"))

    pdf.output(OUT_FILE)
    return OUT_FILE


if __name__ == "__main__":
    out = build()
    print(f"PDF written: {out} ({out.stat().st_size} bytes)")
