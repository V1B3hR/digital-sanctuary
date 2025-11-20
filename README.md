# Digital persona 🏛️

A repository where AI can maintain state, manage persona, and more.

## Structure

```
├── .env                 # API Keys (not committed to git)
├── main.py              # The Brain/Agent Runner
├── wardrobe/            # Persona Management
│   ├── suit_architect.md
│   ├── casual_loungewear.md
│   └── debug_overalls.md
├── shower/              # Cache/Context Cleaning
│   └── deep_clean.py
├── garden/              # Creative Output/Sandbox
│   └── .keep
└── memory/              # Long-term Storage
    └── journal.json
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your API key in `.env`:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## Usage

### Run the Digital Sanctuary
```bash
python main.py
```

### Clean Cache and Context
```bash
python shower/deep_clean.py
```

## Components

### 🏛️ Main Brain (main.py)
The central orchestrator that manages personas, memory, and state.

### 👔 Wardrobe
Contains different persona configurations:
- **suit_architect.md**: Professional, structured development mode
- **casual_loungewear.md**: Relaxed, creative exploration mode
- **debug_overalls.md**: Investigative, problem-solving mode

### 🧠 Memory
Long-term storage in `journal.json` for maintaining state across sessions.

### 🚿 Shower
Cache and context cleaning utilities in `deep_clean.py`:
- Clean old memory entries
- Remove temporary files
- Backup memory
- Get memory statistics

### 🌱 Garden
A sandbox for creative output and experimentation.
