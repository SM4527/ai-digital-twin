---
title: Siva Manickavasagam - AI Digital Twin
short_description: Ask my AI twin about my Oracle, cloud and AI career
thumbnail: https://huggingface.co/spaces/SM4527/ai-digital-twin/resolve/main/preview.png
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

A Gradio chat app that answers questions about my career, using my LinkedIn profile (`My_Linkedin_Profile.pdf`) and `summary.txt` as context. Runs `openai/gpt-oss-120b` on Groq. Contact requests and unanswered questions are sent to me via Pushover.

The twin only states facts from the profile and declines to discuss employer internals (rules in `context.py`). For LinkedIn, share the `huggingface.co/spaces/...` URL: its preview card uses `title`, `short_description` and `thumbnail` (`preview.png`) above.

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
