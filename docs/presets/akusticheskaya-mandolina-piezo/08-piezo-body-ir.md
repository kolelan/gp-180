# Piezo + Body IR

**Инструмент:** мандолина · пьезо.  
**Стиль:** окраска **User IR** инструмента в CAB + лёгкие примочки.  
**AMP/NAM** не обязательны.

Полный сценарий: [../../ir-acoustic/scenarii/piezo-body-ir-plus-fx.md](../../ir-acoustic/scenarii/piezo-body-ir-plus-fx.md).  
Профили: [`../../ir-acoustic/mandolina/`](../../ir-acoustic/mandolina/).

---

## Цепь

```
NR Gate3 → PRE COMP → AMP OFF (или AC Pre мягко) → N→S OFF
→ CAB User IR → EQ Guitar EQ2
→ DLY Slapback тихо → RVB Room → VOL
```

---

## Параметры — что крутить

### COMP
Sustain **25–40**.

### AMP
**OFF** — база сценария. Если quack/howl: AC Pre, EQ Gain ниже 50 на ~1.5–2 kHz.

### CAB User IR
| Параметр | Значение |
|----------|----------|
| Слот | ваш WAV 1024/2048 |
| Low Cut | **~120 Hz** |
| High Cut | **7.5–8.5 kHz** |
| Volume | под патч |
| Precision | regular / high по DSP |

Лучше **мандо-IR**; гитарный dreadnought — эксперимент.

### Guitar EQ 2
| 1k | 3k | 6k |
|----|----|-----|
| −2 | −2 | **−4** |

### Slapback
Mix низкий, Time ~80–110 ms — [термин](../../terminy/slapback.md).

### Room
Mix **12–20**.

Можно добавить G-Chorus Depth низкий / Digital 1/8 как в Celtic Sparkle.

---

## Минимум крутить

Выбор IR → Low/High Cut → EQ 6k → Room Mix  

**CTRL:** на припев/лид — Delay Mix↑ и/или лёгкий Plate.

---

## Когда пресет не подходит

- Нет подходящего **User IR** корпуса — вернитесь к [Natural DI](./01-natural-di.md) с заводским CAB Bird/OM/AC.  
- Нужен **жёсткий anti-FB приоритет** — [Stage Anti-FB](./05-stage-anti-feedback.md) (IR может усилить howl на мониторах).  
- Нужен **чоп без тела IR** — [Bluegrass Chop](./02-bluegrass-chop.md).
