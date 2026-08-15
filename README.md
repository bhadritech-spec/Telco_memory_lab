# MemoryLab

A small assistant you build in five milestones to learn three things by hand:

- **Context engineering** — deciding exactly what text goes into each model request.
- **Semantic memory** — storing text as vectors and retrieving by meaning.
- **Context sharing between agents** — how multiple agents coordinate what each one sees.

Streamlit is used so the invisible stuff (the exact context sent, retrieved memories
and their scores, what each agent saw) is visible on screen. That visibility is the point.

## Milestones

- **M1 — Context by hand.** One agent. You assemble the request yourself and display it. ← you are here
- **M2 — History + budget.** Multi-turn history, then a size limit you have to curate.
- **M3 — Semantic memory.** Embed each turn, store vectors, retrieve top-k, inject only those.
- **M4 — Two agents, shared memory.** A Notetaker writes facts, a Responder reads them.
- **M5 — Consolidation (stretch).** Summarize / dedupe old memories so the store doesn't rot.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...   # your key from console.anthropic.com
```

`export` only lasts for the current terminal session. Re-run it in a new terminal,
or switch to a `.env` file later (already git-ignored).

## Run

Streamlit apps launch through the `streamlit` command — not `python app.py`:

```bash
streamlit run app.py
```

It opens a browser tab at http://localhost:8501. If `streamlit` isn't found:

```bash
python -m streamlit run app.py
```

## M1 — two things to actually do

1. Send two messages in a row. Notice the model has completely forgotten the first —
   there's no history because you didn't put any in. That "amnesia by default" is what
   every later milestone fights against.
2. Hand-inject a fake fact: in `build_context`, prepend
   `{"role": "user", "content": "Known fact: the user's name is Bhadri."}`
   before the real message and watch the answer change. You've just done manually what
   M3 will automate.

## Git

Version this from the start so you can diff between milestones.

```bash
git init
git add .
git commit -m "M1: context by hand"
git log --oneline
```

Daily loop: **edit → `git status` → `git add` → `git commit`.** Commit at each milestone.
