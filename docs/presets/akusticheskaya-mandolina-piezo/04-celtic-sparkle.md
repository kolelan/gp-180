# Celtic Sparkle

**Инструмент:** мандолина · пьезо.  
**Стиль:** кельт-лид, орнаменты (аналог [mandocaster Celtic Lead](../mandocaster/03-celtic-lead.md), но через AC Pre, не Foxy).  
**Характер:** блеск под контролем, delay в темп.

---

## Цепь

```
NR Gate3 → PRE COMP → AMP AC Pre → CAB OM
→ EQ Guitar EQ2 → MOD G-Chorus → DLY Digital → RVB Plate → VOL
```

---

## Параметры — что крутить

### COMP
Sustain **25–40**.

### AC Pre
| Параметр | Значение |
|----------|----------|
| Tone | **48–55** |
| EQ Freq | **~2 kHz** |
| EQ Gain | **46–49** |

Не крутите Tone «в пол» — пьезо уже яркий.

### CAB OM
Low **~110 Hz**, High **~8.5 kHz**.

### Guitar EQ 2
| 1k | 3k | 6k |
|----|----|-----|
| **+2** | 0 | **−4** |

### G-Chorus
| Параметр | Значение |
|----------|----------|
| Depth | **15–25** |
| Rate | средний |
| Volume | не громче dry |

### Digital Delay
| Параметр | Значение |
|----------|----------|
| Mix | **15–22** |
| Time | **1/8**, Sync **ON** |
| Feedback | низкий–средний |
| Trail | ON для CTRL |

Delay ≠ reverb; ≠ [Slapback](../../terminy/slapback.md).

### Plate
Mix **15–22**, Decay короткий–средний, High Damp чуть вверх.

---

## Сначала крутите это

Если патч не сел сразу — меняйте **только эти** параметры, в указанном порядке. Остальное можно не трогать.

AC Pre notch → EQ 6k → Chorus Depth → Delay Mix/Sync → Plate Mix  

**CTRL:** на соло — Delay Mix↑; в куплет — Chorus OFF (суше рядом с вокалом).  
**EXP:** VOL до delay для свэллов.

---

## Когда пресет не подходит

- Нужен **ритм-чоп** — слишком мокро; [Bluegrass Chop](./02-bluegrass-chop.md).  
- Нужна **тёплая баллада без chime** — [Ballad Body](./03-ballad-body.md) / [Natural DI](./01-natural-di.md).  
- Сильный **howl** — сначала [Stage Anti-FB](./05-stage-anti-feedback.md), потом лид.
