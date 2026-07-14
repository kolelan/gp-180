# Bluegrass Chop (пьезо)

**Инструмент:** мандолина · пьезо.  
**Стиль:** ритм-чоп.  
**Характер:** атака, анти-quack, почти без реверба.

Аналог магнитного: [../mandocaster/02-bluegrass-chop.md](../mandocaster/02-bluegrass-chop.md).

---

## Цепь

```
NR Gate2 → PRE COMP4 → AMP AC Pre → CAB AC
→ EQ Guitar EQ2 → RVB Room Mix минимальный → VOL
```

MOD/DLY — **OFF**.

---

## Параметры — что крутить

### Gate 2
**Threshold 40–55**, Attack короткий.

### COMP4
| Параметр | Значение |
|----------|----------|
| Sustain | 35–45 |
| Attack | **быстрый** |

### AC Pre
| Параметр | Значение |
|----------|----------|
| Tone | **35–45** (темнее Natural) |
| EQ Freq | **~1.5–2.0 kHz** |
| EQ Gain | **40–46** — заметный вырез quack |

### CAB AC
Low Cut **~130 Hz**, High Cut **~7 kHz**.

### Guitar EQ 2
| 100 | 500 | 1k | 3k | 6k |
|-----|-----|----|----|-----|
| −4 | −1 | −2 | −2 | **−5** |

### Room
Mix **5–10** только.

---

## Сначала крутите это

Если патч не сел сразу — меняйте **только эти** параметры, в указанном порядке. Остальное можно не трогать.

Gate → AC Pre notch → EQ 6k → Room ≈0  

**CTRL:** на fill чуть поднять Volume и ослабить Gate, чтобы не срезать концы фраз.

---

## Когда пресет не подходит

- Нужен **лид с delay / plate** — [Celtic Sparkle](./04-celtic-sparkle.md).  
- Нужна **баллада / тёплое пространство** — [Ballad Body](./03-ballad-body.md).  
- Нужен **пад / эмбиент** — [Ambient Acoustic](./07-ambient-acoustic.md).
