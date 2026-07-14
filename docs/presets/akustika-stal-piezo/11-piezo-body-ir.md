# Piezo + Body IR

**Роль:** пьезо-гитара через **User IR инструмента** (например dreadnought / «Martin-like»), AMP/NAM по возможности OFF; примочки сверху.

Подробный разбор сценария: [../../ir-acoustic/scenarii/piezo-body-ir-plus-fx.md](../../ir-acoustic/scenarii/piezo-body-ir-plus-fx.md).

```
NR Gate3 → PRE COMP → AMP OFF → N→S OFF
→ CAB User IR (body) → EQ Guitar EQ1
→ MOD Detune еле / G-Chorus опц.
→ DLY Slapback или Sweet Echo тихо
→ RVB Room или Plate → VOL
```

| Блок | Параметр | Значение |
|------|----------|----------|
| COMP | Sustain | 30–45 |
| CAB | User IR слот | ваш профиль из `docs/ir-acoustic/gitara/` |
| CAB | Low / High Cut | 110 Hz / 8–9 kHz |
| EQ1 | 125 / 400 / 800 / 1.6k / 4k | −2 / +1…+2 / 0 / −2 / −3 |
| Detune или Chorus | Wet/Depth | низкий |
| Slapback / Plate | Mix | 10–20 / 12–22 |

Если quack сильный — вместо полного OFF на AMP поставьте **AC Pre** с вырезом ~1.5–2 kHz, Gain нейтральный.
