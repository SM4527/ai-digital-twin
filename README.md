---
title: AI Digital Twin
short_description: My AI Digital Twin
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 6.31.0
python_version: "3.12"
app_file: app.py
pinned: false
license: mit
---

# AI Digital Twin

A Gradio chat app that answers questions about my career, using my LinkedIn profile (`My_Linkedin_Profile.pdf`) and `summary.txt` as context. Runs `openai/gpt-oss-20b` on Groq. Contact requests and unanswered questions are sent to me via Pushover.

## Setup

Create `.env` with:

```
GROQ_API_KEY=...
PUSHOVER_USER=...
PUSHOVER_TOKEN=...
```

## Run

```
uv run app.py
```
