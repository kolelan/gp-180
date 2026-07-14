# NAM / SnapTone на GP-180

Модуль **N→S (SnapTone)** — способ загрузить нейросетевые модели усилителей/педалей формата **NAM** (Neural Amp Modeler) после конвертации в фирменный SnapTone.

| Параметр | Значение |
|----------|----------|
| Заводских SnapTone | 50 |
| Всего слотов | до 100 |
| Параметры слота | Gain, VOL, Bass, Middle, Treble, Presence |
| Импорт | Valeton Suite (ПК/моб.) |

## Содержание раздела

| Файл | О чём |
|------|--------|
| [kak-importirovat.md](./kak-importirovat.md) | Как конвертировать и загрузить NAM |
| [istochniki-modeley.md](./istochniki-modeley.md) | Где брать `.nam` модели легально |
| [zavodskie-snaptone.md](./zavodskie-snaptone.md) | Список заводских 50 файлов |
| [recepty/](./recepty/) | Рецепты использования + шаблон новых |

## Базовая схема сигнала

**Вариант A — SnapTone как amp+cab (если модель уже «с кабинетом»):**

`… → DST (опц.) → N→S ON → AMP OFF → CAB OFF → EQ → …`

**Вариант B — SnapTone amp-only + свой IR:**

`… → N→S ON → AMP OFF → CAB = User IR → EQ → …`

**Вариант C — встроенный AMP (без NAM):**

`… → N→S OFF → AMP ON → CAB ON → …`

Не включайте одновременно тяжёлый SnapTone и высокоточный CAB «на всякий случай» — следите за DSP.

## Для мандокастера

Предпочитайте открытые clean / edge-of-breakup модели (Fender Blackface/Bassman, Vox AC30 clean, JC, Matchless clean). Gain держите низким: магнитный датчик мандолины уже яркий и «перьями» клиппит быстрее гитары.
