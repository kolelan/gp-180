# Ambient Pad

**Инструмент:** мандокастер (магнит).  
**Стиль:** вступления, подложки, лупы, эмбиент.  
**Характер:** мягкая атака, слои delay/reverb, опционально Freeze.

---

## Зачем этот патч

| Нужно | Не этот патч |
|-------|----------------|
| Дрон / пад под вокал | Ритм-чоп / читаемый лид в грид |
| Лупы Post | Сухой clean в бэнде → Folk Clean |

На сцене с бэндом **режьте Mix** Shimmer — иначе howl и каша с тарелками.

---

## Цепь

```
NR Gate3 → PRE Saturate → N→S Dark CL → CAB Twin
→ EQ Guitar EQ2 → MOD Auto Swell (+ Freeze по CTRL)
→ DLY Dual Echo → RVB Shimmer (или Sweet Space) → VOL
```

---

## Параметры эффектов — что крутить и зачем

### Gate 3
Threshold мягкий (20–35) — длинные ноты не резать.

### PRE — Saturate
| Параметр | Значение | Зачем |
|----------|----------|--------|
| **Mix** | **~20** | тепло, не кранч |
| High Cut | вниз | меньше цифрового песка |
| Volume | под уровень | |

Карточка: [Saturate](../../modules/02-pre/saturate/).

### N→S Dark CL + CAB Twin
| Параметр | Значение |
|----------|----------|
| Gain | 15–30 |
| Treble / Presence | сдержанно |
| Low / High Cut | ~100 Hz / 8–9 kHz |

### Guitar EQ 2
| Полоса | Значение |
|--------|----------|
| 100 Hz | −3…−4 |
| 6 kHz | **−3…−4** |
| 1 kHz | 0…+1 |

### MOD — Auto Swell
| Параметр | Значение | Зачем |
|----------|----------|--------|
| **Attack** | средний | скрипичное нарастание |
| Curve | Line / Exp | по вкусу |

Карточка: [Auto Swell](../../modules/09-mod/auto-swell/).

### MOD — Freeze (опц., CTRL)
| Параметр | Значение |
|----------|----------|
| Activate | CTRL / EXP |
| Volume | под слой |
| Attack / Release | плавные |

[Freeze](../../modules/09-mod/freeze/).

### DLY Dual Echo
| Параметр | Значение |
|----------|----------|
| Mix A / B | умеренный |
| Time A ≠ Time B | полиритмия повторов |
| Feedback | низкий–средний |
| Sync A/B | по вкусу |

[Dual Echo](../../modules/10-dly/dual-echo/).

### RVB Shimmer / Sweet Space
| Параметр | Значение |
|----------|----------|
| Mix | **~25** дома; на сцене с бэндом **≤12–15** |
| Decay | длинный ок в соло-эмбиенте |
| Low/High End | прибрать яркость хвоста |

---

## Looper

- **Post** — пишете уже «космос».  
- **Pre** — сухой bed, сверху другой патч.

---

## Минимум крутить

1. Saturate Mix → 2. Auto Swell Attack → 3. Dual Echo Mix/Time → 4. Shimmer Mix  

**CTRL:** Freeze Activate и/или Shimmer Mix↑ на текстурные куски.

---

## Когда пресет не подходит

- Нужен **плотный блюграсс / чоп** — [Bluegrass Chop](./02-bluegrass-chop.md).  
- **Громкие мониторы без anti-FB** — хвосты и shimmer раздуют howl; сначала сцена без пада или [Anti-FB](../akusticheskaya-mandolina-piezo/05-stage-anti-feedback.md) (пьезо) / жёстче Low Cut.  
- Нужен обычный **чистый / лид** в песне — Folk / Celtic, не этот пад.
