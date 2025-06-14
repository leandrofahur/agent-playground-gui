# 🧠 Agent Playground GUI

## Objective
A visual GUI to design, simulate, and debug autonomous LLM agents. The goal is to configure your custom agent goal, memory, toolset, and then watch it execute, retry, and adapt in real-time.

## Features

- Drag-and-drop agent builder (React Flow)
- Memory (short-term + long-term)
- Tool integration (Python shell, file reader, web browser)
- Retry & fallback logic
- Real-time execution visualization
- Save/load agent playgrounds
- Powered by FastAPI and LangChain + CrewAI

## Tech Stack

- **Frontend**: React, React Flow, Tailwind, Zustand, Shadcn/UI
- **Backend**: Python, FastAPI, LangChain + CrewAI
- **LLMs**: OpenAI, Ollama, or local models
- **Database**: SQLite / Postgres for configs, and ChromaDB

## The Architecture Structure

A bird's eye view of how we separate concerns in order to keep the code more maintainable

```bash
backend/
├── app/
│   ├── api/                        # API layer (routes)
│   │   ├── __init__.py
│   │   ├── v1/                     # API versioning
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/          # Route handlers
│   │   │   └── router.py           # Router configuration
│   ├── core/                       # Core application code
│   │   ├── __init__.py
│   │   ├── config.py               # Configuration management
│   │   └── security.py             # Security related code
│   ├── domain/                     # Domain layer
│   │   ├── __init__.py
│   │   ├── models/                 # Domain models
│   │   └── services/               # Business logic
│   ├── infrastructure/             # Infrastructure layer
│   │   ├── __init__.py
│   │   ├── database/               # Database related code
│   │   └── external/               # External service integrations
│   ├── schemas/                    # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── requests/
│   │   └── responses/
│   └── main.py                     # Application entry point
```

## Running The Environment
The environment is orchestrated by a docker compose file that lives on the root folder of the project.

```bash
$ docker compose up --build
```

**IMPORTANT**
If you're running this application locally, you should create a `.env` following the structure below:
```bash
OPENAI_API_KEY=<your_key_here>
``` 

## License 

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
