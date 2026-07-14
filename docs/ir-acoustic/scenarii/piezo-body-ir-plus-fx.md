# Сценарий: пьезо + IR инструмента в CAB (+ примочки)

Главный практический use case этого раздела: **своя акустика/мандолина с пьезо** → окраска **IR «крутого» корпуса** (например Martin D-35 / OM / body) в слоте **CAB → User IR** → поверх **примочки**.  

**NAM / SnapTone и симулятор усилителя не обязательны.**

## Идея в одном абзаце

IR инструмента в CAB — это фильтр характера «тела и съёма». Он не клонирует чужой инструмент 1:1, но заметно уводит пьезо от «пластика» к дереву. Дальше — COMP, EQ против quack, delay/reverb/chorus как обычные эффекты.

## Цепь (рекомендуемая)

```
NR Gate3          — мягко
PRE COMP          — выровнять атаку медиатора
PRE/ AMP          — OFF, либо AC Pre еле-еле (не ламповый хайгейн)
N→S               — OFF
CAB User IR       — профиль инструмента (1024/2048), Low/High Cut
EQ Guitar EQ1/2   — quack / посадка в микс
MOD / DLY / RVB   — примочки
VOL
```

### Когда AMP всё же включить

- Нужно чуть «аку-пре» и parametric notch (AC Pre) против howl.
- Хочется лёгкой сатурации преампа — Gain минимальный.

### Когда NAM уместен

- Отдельная задача «в акустический комбик» (amp или amp+cab capture).  
- Для сценария «только body IR» — **не нужен**; если NAM уже amp+cab, второй CAB часто OFF.

## Стартовые параметры

| Блок | Параметр | Ориентир |
|------|----------|----------|
| COMP | Sustain | 25–45 |
| CAB User IR | Volume | под патч |
| CAB | Low Cut | 100–130 Hz |
| CAB | High Cut | 7.5–9 kHz |
| Guitar EQ1 | 1.6k / 4k | −1…−3 / −2…−4 при резкости |
| Delay / Reverb | Mix | как в аку-пресетах: низкий на сцене |

## Примочки поверх IR

| Цель | Модуль | Заметка |
|------|--------|---------|
| Ширина | G-Chorus / Detune | Depth низкий — не размывать атаку |
| Слэп / кантри | [Slapback](../../terminy/slapback.md) (delay ~80–120 ms, не reverb) | Mix низкий |
| Баллада | Plate / Hall | Mix умеренный; IR уже даёт «микрофон» |
| Ambient | Sweet Space / Shimmer | На сцене осторожно (howl) |

Готовые отправные пресеты рядом:

- гитара: [../../presets/akustika-stal-piezo/11-piezo-body-ir.md](../../presets/akustika-stal-piezo/11-piezo-body-ir.md)
- мандолина: [../../presets/akusticheskaya-mandolina-piezo/08-piezo-body-ir.md](../../presets/akusticheskaya-mandolina-piezo/08-piezo-body-ir.md)

## Куда класть IR и отчёты

- [`../gitara/`](../gitara/) — WAV гитарных body IR  
- [`../mandolina/`](../mandolina/) — WAV мандолины  
- [`../issledovaniya/`](../issledovaniya/) — что получилось на слух  

Карточка файла: [`../_shablon-profilya.md`](../_shablon-profilya.md).

## Честные ожидания

Возможно: «моя пьезо-гитара + IR D-35 + примочки» звучит заметно богаче.  
Невозможно обещать: неотличимость от настоящей Martin в комнате без EQ и без понимания ограничений длины IR.
