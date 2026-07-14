# MIDI

Управление патчами и параметрами по USB, BT и TRS MIDI IN/OUT.

Основные сообщения (по мануалу firmware 1.0.0; сверяйте с актуальной таблицей в PDF при смене FW):

| CC / PC | Диапазон | Назначение |
|---------|----------|------------|
| PC + Bank | см. мануал | Смена патча (1–200 через MSB/PC) |
| CC7 | 0–100 | Patch Volume |
| CC11 | 0–100 | EXP Parameter |
| CC13 | 0–127 | EXP A/B состояние |
| CC16–21 | — | Quick Access параметры / шаги |
| и др. | — | Модули on/off, TAP и пр. |

Полная таблица: страницы «MIDI Control Information List» в оригинальном PDF (`source/…`).

Практика: назначайте PC на контроллер для смены «clean / chop / lead» мандокастера; CC — на Mix Delay и Volume.
