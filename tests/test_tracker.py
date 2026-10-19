"""Tests de Fase 5: lógica de rachas y persistencia JSON."""
from datetime import date, timedelta
from pathlib import Path

from storage import load_habits
from tracker import HabitTracker


def _tracker(tmp_path: Path) -> HabitTracker:
    return HabitTracker(
        str(tmp_path / "habits.json"),
        str(tmp_path / "habits_log.json"),
    )


def test_nuevo_habito_racha_cero(tmp_path: Path) -> None:
    tracker = _tracker(tmp_path)
    tracker.add_habit("Leer", "diario")
    assert tracker.get_streak("Leer") == 0


def test_tres_dias_seguidos_racha_tres(tmp_path: Path) -> None:
    tracker = _tracker(tmp_path)
    tracker.add_habit("Leer", "diario")
    hoy = date.today()
    for dias_atras in range(3):
        tracker.mark_done("Leer", (hoy - timedelta(days=dias_atras)).isoformat())
    assert tracker.get_streak("Leer") == 3


def test_dia_saltado_reinicia_racha(tmp_path: Path) -> None:
    tracker = _tracker(tmp_path)
    tracker.add_habit("Leer", "diario")
    hoy = date.today()
    tracker.mark_done("Leer", (hoy - timedelta(days=2)).isoformat())
    tracker.mark_done("Leer", hoy.isoformat())
    assert tracker.get_streak("Leer") == 1


def test_fechas_duplicadas_no_inflan_racha(tmp_path: Path) -> None:
    tracker = _tracker(tmp_path)
    tracker.add_habit("Leer", "diario")
    hoy = date.today().isoformat()
    tracker.mark_done("Leer", hoy)
    tracker.mark_done("Leer", hoy)
    assert tracker.get_streak("Leer") == 1
    assert len(tracker.habits_historial) == 1


def test_mark_done_habito_inexistente_no_crea_log(tmp_path: Path) -> None:
    tracker = _tracker(tmp_path)
    tracker.mark_done("No existe")
    assert tracker.get_streak("No existe") == 0
    assert tracker.habits_historial == []


def test_load_habits_archivo_inexistente(tmp_path: Path) -> None:
    assert load_habits(str(tmp_path / "no_existe.json")) == []
