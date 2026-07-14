#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка PDF из русского перевода инструкции GP-180."""

from __future__ import annotations

import re
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from fpdf.fonts import FontFace

ROOT = Path(__file__).resolve().parents[1]
MANUAL_DIR = ROOT / "docs" / "manual-ru"
OUT_DIR = ROOT / "docs" / "pdf"
OUT_FILE = OUT_DIR / "GP-180_Instrukciya_RU.pdf"

FONT_REG = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")

MANUAL_ORDER = [
    "README.md",
    "12-pochemu-menshe-stranic.md",
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
    "13-akusticheskie-ir.md",
]

MODULES_DIR = ROOT / "docs" / "modules"
SNAP_DIR = ROOT / "docs" / "nam-snaptone"


class ManualPDF(FPDF):
    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("DocFont", size=9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Valeton GP-180 - RU  |  {self.page_no()}", align="C")

    def write_block(self, text: str, h: float = 6) -> None:
        text = sanitize(text)
        if not text:
            self.ln(h / 2)
            return
        self.set_x(self.l_margin)
        self.multi_cell(
            self.epw,
            h,
            text,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )


def sanitize(text: str) -> str:
    replacements = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u2192": "->",
        "\u2190": "<-",
        "\u00a0": " ",
        "\u2011": "-",
        "•": "-",
        "·": "-",
        "↔": "<->",
        "×": "x",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", text)
    return text


def strip_md_links(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return sanitize(text)


def is_md_separator_row(raw: str) -> bool:
    cells = [c.strip() for c in raw.strip().strip("|").split("|")]
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def parse_md_table_rows(raw_lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw in raw_lines:
        if is_md_separator_row(raw):
            continue
        cells = [strip_md_links(c.strip()) for c in raw.strip().strip("|").split("|")]
        while cells and cells[-1] == "":
            cells.pop()
        if cells:
            rows.append(cells)
    if not rows:
        return []
    width = max(len(r) for r in rows)
    return [r + [""] * (width - len(r)) for r in rows]


def draw_table(pdf: ManualPDF, rows: list[list[str]]) -> None:
    """Настоящая таблица с рамками и чередующейся заливкой строк."""
    if not rows:
        return

    pdf.ln(2)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("DocFont", size=9)
    pdf.set_text_color(25, 25, 25)

    col_count = len(rows[0])
    if col_count == 2:
        col_widths = (pdf.epw * 0.32, pdf.epw * 0.68)
    elif col_count == 3:
        col_widths = (pdf.epw * 0.22, pdf.epw * 0.28, pdf.epw * 0.50)
    elif col_count == 4:
        col_widths = tuple([pdf.epw / 4] * 4)
    else:
        col_widths = None

    heading = FontFace(
        emphasis="BOLD",
        color=(20, 20, 20),
        fill_color=(230, 230, 230),
    )

    with pdf.table(
        width=pdf.epw,
        col_widths=col_widths,
        text_align="LEFT",
        line_height=5,
        padding=2.5,
        borders_layout="ALL",
        cell_fill_mode="ROWS",
        cell_fill_color=(248, 248, 248),
        headings_style=heading,
        first_row_as_headings=True,
    ) as table:
        for data_row in rows:
            row = table.row()
            for cell in data_row:
                row.cell(cell or " ")

    pdf.set_font("DocFont", size=11)
    pdf.set_text_color(30, 30, 30)
    pdf.ln(3)


def render_markdown(pdf: ManualPDF, text: str, *, new_page_on_h1: bool = True) -> None:
    lines = text.replace("\r\n", "\n").split("\n")
    i = 0
    in_code = False
    table_buf: list[str] = []

    def flush_table() -> None:
        nonlocal table_buf
        rows = parse_md_table_rows(table_buf)
        table_buf = []
        if rows:
            draw_table(pdf, rows)

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
            pdf.multi_cell(
                pdf.epw,
                5,
                sanitize(line) if line else " ",
                fill=True,
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )
            i += 1
            continue

        if line.strip().startswith("|"):
            table_buf.append(line)
            i += 1
            continue

        flush_table()

        if not line.strip():
            pdf.ln(2)
            i += 1
            continue

        if line.startswith("# "):
            title = strip_md_links(line[2:].strip())
            if new_page_on_h1:
                pdf.add_page()
                pdf.set_font("DocFont", style="B", size=18)
                pdf.set_text_color(20, 20, 20)
                pdf.write_block(title, 10)
                pdf.ln(4)
            else:
                # плотная вёрстка каталога эффектов
                pdf.ln(3)
                pdf.set_draw_color(180, 180, 180)
                pdf.set_line_width(0.2)
                y = pdf.get_y()
                pdf.line(pdf.l_margin, y, pdf.l_margin + pdf.epw, y)
                pdf.ln(2)
                pdf.set_font("DocFont", style="B", size=12)
                pdf.set_text_color(20, 20, 20)
                pdf.write_block(title, 7)
                pdf.ln(1)
        elif line.startswith("## "):
            pdf.ln(2)
            pdf.set_font("DocFont", style="B", size=13 if new_page_on_h1 else 11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(strip_md_links(line[3:].strip()), 7 if new_page_on_h1 else 6)
            pdf.ln(1)
        elif line.startswith("### "):
            pdf.ln(1)
            pdf.set_font("DocFont", style="B", size=11 if new_page_on_h1 else 10)
            pdf.set_text_color(40, 40, 40)
            pdf.write_block(strip_md_links(line[4:].strip()), 6)
            pdf.ln(1)
        elif line.strip() == "---":
            pdf.ln(2)
        elif line.lstrip().startswith("- ") or line.lstrip().startswith("* "):
            content = strip_md_links(re.sub(r"^\s*[-*]\s+", "", line))
            pdf.set_font("DocFont", size=10 if not new_page_on_h1 else 11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(f"- {content}", 5 if not new_page_on_h1 else 6)
        elif re.match(r"^\d+\.\s+", line.lstrip()):
            content = strip_md_links(line.lstrip())
            pdf.set_font("DocFont", size=10 if not new_page_on_h1 else 11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(content, 5 if not new_page_on_h1 else 6)
        elif line.lstrip().startswith(">"):
            content = strip_md_links(line.lstrip()[1:].strip())
            pdf.set_font("DocFont", size=10)
            pdf.set_text_color(70, 70, 70)
            pdf.write_block(content, 5)
        else:
            pdf.set_font("DocFont", size=10 if not new_page_on_h1 else 11)
            pdf.set_text_color(30, 30, 30)
            pdf.write_block(strip_md_links(line), 5 if not new_page_on_h1 else 6)

        i += 1

    flush_table()


def append_effects_catalog(pdf: ManualPDF) -> None:
    """Приложение: полный каталог модулей/эффектов (закрывает «дыру» стр. 39–71 EN)."""
    print("add EFFECTS CATALOG ...", flush=True)
    pdf.add_page()
    pdf.set_font("DocFont", style="B", size=18)
    pdf.write_block(sanitize("Приложение A. Каталог эффектов (перевод)"), 10)
    pdf.ln(2)
    pdf.set_font("DocFont", size=11)
    pdf.write_block(
        sanitize(
            "Ниже — русские описания модулей и эффектов GP-180. "
            "В оригинальном EN-мануале этот блок занимает большую часть объёма (примерно страницы 39-71)."
        ),
        6,
    )

    index = MODULES_DIR / "README.md"
    if index.exists():
        render_markdown(pdf, index.read_text(encoding="utf-8"), new_page_on_h1=True)

    module_dirs = sorted(
        [p for p in MODULES_DIR.iterdir() if p.is_dir()],
        key=lambda p: p.name,
    )
    for mdir in module_dirs:
        m_readme = mdir / "README.md"
        print(f"  module {mdir.name} ...", flush=True)
        if m_readme.exists():
            render_markdown(pdf, m_readme.read_text(encoding="utf-8"), new_page_on_h1=True)

        effect_dirs = sorted([p for p in mdir.iterdir() if p.is_dir()], key=lambda p: p.name)
        for edir in effect_dirs:
            e_readme = edir / "README.md"
            if not e_readme.exists():
                continue
            render_markdown(
                pdf,
                e_readme.read_text(encoding="utf-8"),
                new_page_on_h1=False,
            )


def append_snaptone(pdf: ManualPDF) -> None:
    print("add SnapTone ...", flush=True)
    pdf.add_page()
    pdf.set_font("DocFont", style="B", size=18)
    pdf.write_block(sanitize("Приложение B. SnapTone / NAM"), 10)
    pdf.ln(2)
    for name in ("README.md", "kak-importirovat.md", "istochniki-modeley.md", "zavodskie-snaptone.md"):
        path = SNAP_DIR / name
        if path.exists():
            print(f"  {name} ...", flush=True)
            render_markdown(pdf, path.read_text(encoding="utf-8"), new_page_on_h1=True)


def build() -> Path:
    if not FONT_REG.exists() or not FONT_BOLD.exists():
        raise SystemExit("Не найдены Arial TTF в C:\\Windows\\Fonts")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf = ManualPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("DocFont", fname=str(FONT_REG))
    pdf.add_font("DocFont", style="B", fname=str(FONT_BOLD))
    pdf.set_margins(18, 18, 18)

    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("DocFont", style="B", size=24)
    pdf.multi_cell(pdf.epw, 12, "Valeton GP-180", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)
    pdf.set_font("DocFont", style="B", size=16)
    pdf.multi_cell(
        pdf.epw,
        9,
        sanitize("Инструкция по эксплуатации"),
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(2)
    pdf.set_font("DocFont", size=12)
    pdf.multi_cell(
        pdf.epw,
        7,
        sanitize("Русский перевод (на основе Firmware V1.0.0)"),
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(8)
    pdf.set_font("DocFont", size=10)
    pdf.set_text_color(90, 90, 90)
    pdf.multi_cell(
        pdf.epw,
        6,
        sanitize(
            "Неофициальный перевод документации проекта gp-180.\n"
            "Оригинал: GP-180 Online Manual EN Firmware V1.0.0."
        ),
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    for name in MANUAL_ORDER:
        path = MANUAL_DIR / name
        if not path.exists():
            print(f"skip missing: {path}")
            continue
        print(f"add {name} ...", flush=True)
        render_markdown(pdf, path.read_text(encoding="utf-8"))

    append_effects_catalog(pdf)
    append_snaptone(pdf)

    pdf.output(OUT_FILE)
    return OUT_FILE


if __name__ == "__main__":
    out = build()
    print(f"PDF written: {out} ({out.stat().st_size} bytes)", flush=True)
