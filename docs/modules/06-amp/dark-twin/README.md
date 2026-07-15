# Dark Twin

**Тип:** Clean (AMP)  
**Модуль:** [AMP](../)

## Описание

По Effect List GP-180: **Dark Twin** — симуляция **Fender® ’65 Twin Reverb®\*** (blackface Twin). Классический американский clean: широкий, «воздушный», хорошо садится в кантри / джаз / мягкий рок.

Для **мандокастера** (магнит уже яркий) обычно держат **Bright OFF** и **Treble** невысоко — иначе быстро появляется [шип](../../../terminy/ship.md).

Имена брендов — только для описания характера звука.

---

## Параметры

| Параметр | UI (типично) | Смысл (мануал) | На практике |
|----------|--------------|----------------|-------------|
| **Gain** | 0–100 | Pre-gain — насколько «горячий» преамп | Громкость искажения преампа. Низкий = clean; чуть выше = [edge-of-breakup](../../../terminy/edge-of-breakup.md). Не путать с **Volume** |
| **Volume** | 0–100 | Post-gain — выход комбика после Gain | Общая громкость amp-блока **без** существенного добавления грязи. Громче сцена → Volume↑, не Gain↑ |
| **Bass** | 0–100 | Низ 3-полосного EQ amp | Тело / гул. На мандо часто нейтраль или чуть ниже + [Low Cut](../../../terminy/low-cut-high-cut.md) в CAB |
| **Middle** | 0–100 | Середина | Читаемость в бэнде; для folk можно чуть выше Treble |
| **Treble** | 0–100 | Верх | Атака и «стекло». На мандокастере легко даёт шип — держать скромно |
| **Bright** | ON / OFF | Доп. яркость (как bright-switch на Twin) | **OFF** почти всегда для мандо/аку; ON — только если тон глухой на тёмном CAB/мониторе |

> **Presence** у **AMP Dark Twin нет**. Presence бывает у части **N→S / SnapTone**. Не ищите Bright и Presence на одном блоке.

---

## Gain vs Volume

| | **Gain** | **Volume** |
|--|----------|------------|
| Что делает | Насыщение / характер clean↔breakup | Уровень на выходе amp |
| Если тихо | Сначала Volume | — |
| Если мало «искры» | Чуть Gain | Не Volume |
| Если орёт верх | Gain и Treble вниз, Bright OFF | Volume можно оставить |

---

## Примеры настроек

### Folk / баллада / мандокастер (как [Folk Clean](../../../presets/mandocaster/01-folk-clean.md))

| Параметр | Ориентир |
|----------|----------|
| Gain | **20–30** (старт **25**) |
| Volume | **50–60** (под уровень патча / unity с N→S-вариантом) |
| Bass | **40–50** |
| Middle | **50–58** |
| Treble | **35–45** |
| Bright | **OFF** |

### Ярче «country sparkle» (осторожно на мандо)

Treble **48–55**, Bright всё равно чаще **OFF**; яркость лучше EQ **1.6 kHz**, не Bright.

### Edge рядом с электро

Gain **30–40**, Treble не выше 45, Bright OFF; дальше уже [Rock Crossover](../../../presets/mandocaster/04-rock-crossover.md) / OD, не разгон Twin.

---

## CAB рядом с Dark Twin

Обычно **CAB Twin 2x12**. На [FRFR](../../../terminy/frfr.md)/наушниках CAB ON; в INPUT гитарного комбика — часто CAB OFF.

Low Cut ~90–110 Hz, High Cut ~9–10 kHz для folk-мандо.

---

## Dark Twin (AMP) vs N→S Dark CL

В пресетах часто пишут «N→S Dark CL **или** AMP Dark Twin» — это **разные** модели:

| | AMP **Dark Twin** | N→S **Dark CL** (заводской) |
|--|-------------------|------------------------------|
| Характер | Twin Reverb '65 | чаще Bassman-like clean (см. список SnapTone) |
| Ручки | Gain, Volume, Bass, Middle, Treble, **Bright** | Gain, EQ, часто **Presence**, VOL; Bright может отсутствовать |
| Когда | Нужен именно Twin + Bright OFF | Удобный SnapTone-clean, cab иногда уже в модели |

Не копируйте Presence с SnapTone в блок Dark Twin — его там нет.

---

## Заметки

- DSP: amp лёгкий; тяжесть обычно SnapTone + Precision CAB + FX.  
- Англ. мануал: *Gain (pre); Volume (post); Bass/Middle/Treble; Bright on/off.*
