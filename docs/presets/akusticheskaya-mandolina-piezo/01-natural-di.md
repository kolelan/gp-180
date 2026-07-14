# Natural DI

**Роль:** основной сценический/студийный clean — «мандолина в воздух, а не в пьезо».

```
NR Gate3 → PRE Saturate → PRE/COMP в одном PRE: COMP
→ AMP AC Pre → CAB Bird (или OM)
→ EQ Guitar EQ1 → DLY off → RVB Room → VOL
```

> В одном слоте PRE одновременно один эффект: чередуйте **два патча** (с Saturate / с COMP) или поставьте COMP в PRE, а Saturate выключите — чаще хватает **COMP + AC Pre**. Ниже — рекомендуемая рабочая цепь без дубля PRE.

## Рабочая цепь

```
NR Gate3 → PRE COMP → AMP AC Pre → CAB Bird → EQ Guitar EQ1 → RVB Room → VOL
```

| Блок | Параметр | Значение |
|------|----------|----------|
| Gate3 | Threshold | 20–35 |
| COMP | Sustain / Volume | 25–40 / ~55 |
| AC Pre | Volume | 50–60 |
| AC Pre | Tone | 40–50 |
| AC Pre | Balance | 30–50 (подключить tone; 0 = tone off) |
| AC Pre | EQ Freq | ~1.2–1.8 kHz |
| AC Pre | EQ Q | средний |
| AC Pre | EQ Gain | 45–48 (чуть ниже нейтрали 50 — вырез quack) |
| CAB Bird | Low Cut | ~120 Hz |
| CAB Bird | High Cut | ~8 kHz |
| EQ1 | 125 / 400 / 800 / 1.6k / 4k | −2 / +2 / 0 / −2 / −3 |
| Room | Mix / Decay | 15–25 / короткий |

## Варианты

1. Больше «дерева»: CAB → **OM** или **AC**, EQ 400 Hz +1…+3.
2. Теплее без CAB-sim: добавьте PRE **Saturate** Mix 20 вместо сильного +Bass.
3. Запись DI без «колонки»: CAB OFF, режьте High Cut глобально / EQ 4k ↓.

## CTRL

Короткий Plate (Mix↑) на припев или лёгкий Detune Wet низкий.
