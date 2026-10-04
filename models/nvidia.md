# NVIDIA NIM Free API — Verified Chat Models

Models verified as chat-compatible (OpenAI `/chat/completions`) and responding to free-tier requests on 2026-09-26.

## Working models

| Model ID | Notes |
|---|---|
| `nvidia/nemotron-3-super-120b-a12b` | **Default for Horizon** — MoE 120B, best quality |
| `nvidia/nemotron-3-ultra-550b-a55b` | MoE 550B, largest available |
| `openai/gpt-oss-20b` | OpenAI open-source 20B |
| `z-ai/glm-5.3` | Z.AI GLM-5.3 |
| `z-ai/glm-5.3-flash` | GLM-5.3 faster variant |
| `moonshotai/kimi-k3` | Moonshot Kimi K3 |
| `meta/llama-3.2-11b-vision-instruct` | Llama 3.2 11B multimodal |
| `google/gemma-4-31b-it` | Google Gemma 4 31B instruction-tuned |

## Not available (EOL / 404 / timed out)

These models appear in the NVIDIA catalog but returned 404 or timed out during testing:

- `meta/llama-3.1-8b-instruct` — EOL as of 2026-08-26
- `meta/llama-3.1-70b-instruct` — EOL
- `meta/llama-3.2-3b-instruct` — EOL
- `meta/llama-3.2-90b-vision-instruct` — timeout
- `mistralai/mistral-large` — 404
- `mistralai/mistral-large-2-instruct` — 404
- `mistralai/mistral-nemotron` — timeout
- `moonshotai/kimi-k2.6` — 404
- `deepseek-ai/deepseek-v4.1-flash` — timeout
- `databricks/dbrx-instruct` — 404
- `nvidia/nemotron-4-340b-instruct` — 404
- `nvidia/llama-3.1-nemotron-70b-instruct` — 404
- `writer/palmyra-creative-122b` — 404
- `writer/palmyra-fin-70b-32k` — 404
- `writer/palmyra-med-70b` — 404
- `google/gemma-3-12b-it` — 404
- `ibm/granite-3.0-8b-instruct` — 404

## Non-chat models (skipped)

These exist in the catalog but do not support the OpenAI `/chat/completions` API — they are embeddings, vision-only, or specialized safety models:

`nvidia/embed-qa-4`, `nvidia/nv-embedqa-mistral-7b-v2`, `nvidia/nvclip`, `nvidia/vila`,
`baai/bge-m3`, `snowflake/arctic-embed-l`, `google/deplot`, `microsoft/kosmos-2`,
`microsoft/phi-3-vision-128k-instruct`, `adept/fuyu-8b`, `google/diffusiongemma-26b-a4b-it`,
`meta/llama-guard-4-12b`, `nvidia/llama-3.1-nemoguard-*`, `nvidia/llama-3.1-nemotron-safety-guard-*`,
`nvidia/nemotron-3.5-content-safety`, `nvidia/ai-synthetic-video-detector`,
`nvidia/cosmos-reason2-8b`, `nvidia/ising-calibration-1.5-31b`,
`nvidia/nemoretriever-*`, `nvidia/nemotron-parse*`, `nvidia/nemotron-3-embed-*`,
`nvidia/riva-translate-*`, `nvidia/neva-22b`, `nvidia/nv-embed-v1`, `nvidia/nv-embedcode-*`,
`google/gemma-2b`, `google/gemma-3-4b-it`, `google/recurrentgemma-2b`,
`bigcode/starcoder2-15b`, `deepseek-ai/deepseek-coder-6.7b-instruct`,
`mistralai/codestral-22b-instruct-v0.1`, `ibm/granite-*-code-instruct` (code-only),
`meta/codellama-70b`, `meta/llama2-70b`, `ai21labs/jamba-1.5-large-instruct`,
`zyphra/zamba2-7b-instruct`, `poolside/laguna-xs-2.1`, `nvidia/nemotron-nano-*`.

> **Note**: NVIDIA periodically deprecates models. If a model returns 404 or EOL, check [build.nvidia.com](https://build.nvidia.com) for the latest available models, or query the live list via `GET https://integrate.api.nvidia.com/v1/models`.
