# well-agent

Агент для решения инженерной задачи. Шаблон репозитория проекта.

## Структура

- `agent.py` — `run(request, ctx) -> AgentResult`
- `project.yaml` — название, пара, точка входа
- `requirements.txt` — зависимости
- `.env.example` — имена переменных без значений
- `src/agent/` — `schemas.py`, `tools.py`, `loop.py`, `prompts.py`
- `tests/` — pytest
- `notebooks/demo.ipynb` — демо для Colab
- `docs/` — схема агента, слайды защиты
