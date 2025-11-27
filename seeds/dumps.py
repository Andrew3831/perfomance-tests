import json
from pathlib import Path

from seeds.schema.result import SeedsResult
from tools.logger import get_logger

# Создаём логгер один раз
logger = get_logger("SEEDS_DUMPS")

DUMPS_DIR = Path("./dumps")
DUMPS_DIR.mkdir(exist_ok=True)


def save_seeds_result(result: SeedsResult, scenario: str) -> None:
    """
    Сохраняет результат сидинга в JSON-файл.
    """
    seeds_file = DUMPS_DIR / f"{scenario}_seeds.json"

    with open(seeds_file, "w", encoding="utf-8") as f:
        json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)

    # Логирование после успешного сохранения
    logger.debug(f"Seeding result saved to file: {seeds_file}")


def load_seeds_result(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из JSON-файла.
    """
    seeds_file = DUMPS_DIR / f"{scenario}_seeds.json"

    with open(seeds_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = SeedsResult(**data)

    # Логирование после успешной загрузки
    logger.debug(f"Seeding result loaded from file: {seeds_file}")

    return result
