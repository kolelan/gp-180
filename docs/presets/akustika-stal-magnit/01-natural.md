# Natural Acoustic Mag

**Роль:** основной чистый тон акустики с магнитным датчиком.

```
NR Gate3 → PRE COMP → AMP AC Pre → CAB OM → EQ Guitar EQ1 → RVB Room → VOL
```

### Gate 3 ([описание](../../modules/01-nr/gate-3/))

Мягкий сустейн / clean. Единицы и логика ручек — в карточке.

| Параметр | Ориентир | Зачем |
|----------|----------|--------|
| **Threshold** | **22–30** | порог по паузе без игры |
| **Ratio** | **40–50** | жёсткость глушения |
| **Attack** | **8–15** ≈ ms | открытие под атаку |
| **Release** | **200–320** ≈ ms | хвост ноты / тишина |
| **Hold** | **50–90** ≈ ms | стабильность на тремоло |


| Блок | Параметр | Значение |
|------|----------|----------|
| COMP | Sustain / Volume | 25–40 / ~55 |
| AC Pre | Volume | 50–60 |
| AC Pre | Tone | 48–56 |
| AC Pre | Balance | 35–50 |
| AC Pre | EQ Freq | ~320–450 Hz |
| AC Pre | EQ Gain | 46–49 |
| CAB OM | Low / High Cut | 90–110 Hz / 9–10 kHz |
| EQ1 | 125 / 400 / 800 / 1.6k / 4k | −2 / −2 / +1 / +1 / 0…−1 |
| Room | Mix / Decay | 15–25 / короткий |

**Варианты:** ярче → CAB Bird; крупнее корпус → CAB AC; без AC Pre → Dark Twin Gain низкий, Bright OFF + CAB OM.
