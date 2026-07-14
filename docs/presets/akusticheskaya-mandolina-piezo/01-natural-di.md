# Natural DI

**Инструмент:** акустическая мандолина · **пьезо**.  
**Стиль:** основной сценический/студийный clean.  
**Цель:** «дерево в воздух», не пластик датчика.

Сценарий IR (вариант): [08-piezo-body-ir.md](./08-piezo-body-ir.md).

---

## Зачем

Основной патч дня. Не чоп, не anti-FB, не ambient.

**В одном PRE** — один эффект: рабочая цепь = **COMP + AC Pre** (Saturate — отдельный патч или вместо COMP).

---

## Цепь

```
NR Gate3 → PRE COMP → AMP AC Pre → CAB Bird (или OM)
→ EQ Guitar EQ1 → RVB Room → VOL
```

---

## Параметры — что крутить

### Gate 3
Threshold **20–35**; Attack/Release средние.

### COMP
| Параметр | Значение |
|----------|----------|
| Sustain | **25–40** |
| Volume | **~55** |

### AC Pre ([карточка](../../modules/06-amp/ac-pre/))
| Параметр | Значение | Смысл |
|----------|----------|--------|
| Volume | 50–60 | |
| Tone | 40–50 | яркость |
| Balance | 30–50 (0 = tone off) | включает tone-цепочку |
| **EQ Freq** | **~1.2–1.8 kHz** | зона quack |
| EQ Q | средний | |
| **EQ Gain** | **45–48** (нейтраль ≈50) | лёгкий вырез quack |

### CAB Bird
| Параметр | Значение |
|----------|----------|
| Low Cut | **~120 Hz** |
| High Cut | **~8 kHz** |

### Guitar EQ 1
| 125 | 400 | 800 | 1.6k | 4k |
|-----|-----|-----|------|-----|
| −2 | +2 | 0 | −2 | −3 |

### Room
Mix **15–25**, Decay короткий. Delay обычно OFF.

---

## Минимум
AC Pre EQ Freq/Gain → Low/High Cut → EQ 4k / 400 → Room Mix  

**CTRL:** Plate Mix↑ / Detune слабо.  
**Варианты:** CAB OM/AC; Saturate Mix 20; CAB OFF для голого [DI](../../terminy/di.md).
