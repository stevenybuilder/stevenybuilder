<a href="https://github.com/stevenybuilder"><img src="https://ghchart.rshah.org/2f855a/stevenybuilder" alt="Steven Yang's GitHub contribution graph, last twelve months" width="100%"/></a>

# Steven Yang

Applied interpretability for world models and physical AI.

[Writing](https://stevenybuilder.github.io) · [LinkedIn](https://www.linkedin.com/in/stevenyang99) · [X](https://x.com/stevenytechs) · [Email](mailto:stevenybusiness@gmail.com)

## Now

<img src="https://stevenybuilder.github.io/assets/media/about-steven-yang-8937.webp" alt="Steven Yang beside a mountain lake" align="right" width="200"/>

- Fine-grained steering and applied interpretability for world models, to improve robotics task outcomes and scale physical AI safely.
- Learning and memory mechanisms for recurrent state-space models in JEPA, during pretraining and at inference time, with compute efficiency as a constraint.
- Paper accepted at the NeurIPS 2026 Workshop on Long-Context Foundation Models (LCFM): *Second-Read Divergence: Context Reuse in JEPA-WM*. An action patch in a JEPA world model matches the changed-input forecast at first, then diverges when the edited action returns as history. [Code and results](https://github.com/stevenybuilder/jepa_steering).
- Latest write-up: [Reading and steering motion in V-JEPA 2](https://github.com/stevenybuilder/jepa_physics). Layer-wise probing, nullspace erasure and manifold steering of direction, speed and acceleration in the frozen encoder, judged by the model's own predictor.
- Before that: [instruction following in π0.5](https://stevenybuilder.github.io/pick-it-up/), a causal pathway for instruction control in a vision-language-action model.

<br clear="right"/>

## Skills

| | |
|---|---|
| **Languages** | Python, C/C++ (embedded, ESP32), Kotlin, JavaScript, TypeScript, SQL |
| **Deep learning** | PyTorch, JAX, TensorFlow, Vision Transformers, JEPA-family predictive embeddings, frozen-encoder inference, linear and MLP probing, activation patching and steering |
| **ML and statistics** | scikit-learn, CatBoost, pandas, NumPy, SciPy, calibration, conformal intervals, bootstrap and permutation nulls, survival and censoring, confound ablation |
| **Robotics and embedded** | ESP32 / ESP-IDF firmware for real-time arm control and sensor tracking, computer-vision perception closing the loop with a physical actuator |
| **GPU and systems** | Matrix-multiply performance from first principles (arithmetic intensity, roofline, memory bandwidth, mixed precision), following the Hugging Face Ultra-Scale Playbook and DeepMind's *How to Scale Your Model* (JAX); managing fleets of rented GPU instances from a CPU-only machine with locked scheduling, checkpointed resumability and pinned CUDA and PyTorch stacks |
| **AI systems** | LLM tool loops, MCP servers, retrieval, golden-dataset evals, deterministic gates, generated-code validation |
| **Cloud and data** | Google Cloud Run, BigQuery, Vertex AI, Gemini, Databricks Asset Bundles, Delta Lake, MLflow, Docker, FastAPI, React |

## Projects

| | | |
|---|---|---|
| [**jepa_steering**](https://github.com/stevenybuilder/jepa_steering) | Activation steering inside the JEPA-WM predictor: second-read divergence of action patches, planner search effects and a precision-dependent geometry result. Paper accepted at the NeurIPS 2026 LCFM workshop. | PyTorch, scikit-learn |
| [**jepa_physics**](https://github.com/stevenybuilder/jepa_physics) | Reads and steers physical variables inside V-JEPA 2 and asks whether the predictor uses them. Spline versus straight edits at held-out values, token-level binding, position and contact through the forecast. | PyTorch, transformers, scikit-learn |
| [**NeuroAD**](https://github.com/stevenybuilder/NeuroAD) | Confound ablation for a frozen JEPA-style 3D imaging encoder. Shows the embedding decodes scanner field strength as readily as disease, then harmonizes it away label-blind. Built at the Claude Life Sciences hackathon with Gladstone Institutes. [Demo video](https://www.youtube.com/watch?v=Q1F49sy4BC0). | PyTorch, scikit-learn, FastAPI, Cloud Run |
| **TrueDose AI** | Robotic medication-safety cabinet: ESP32 firmware, vision-based medication identification, a real actuator delivering the dose. Best Use of Convex, AI Valley Robotics Hackathon. | C/C++, Python, Convex |
| [**SMB underwriting**](https://github.com/ron2k1/intuit-techweek-smb-underwriting) | Calibrated probability-of-default modeling with 90% intervals and profit-aware approval logic under selection bias and censoring. 2nd place, Intuit TechWeek NYC 2026. | Python, scikit-learn, statsmodels |
| [**CareGap**](https://github.com/stevenybuilder/caregap-medical-desert-map) | Ranks likely medical deserts with Bayesian trust posteriors, Wilson intervals and conformal sets over a lakehouse pipeline. [Live](https://caregap-app-31043195041.us-central1.run.app/). | Databricks, CatBoost, MLflow, Streamlit |
| [**Guardia**](https://github.com/stevenybuilder/guardia) | Deployment-risk copilot inside IntelliJ: deterministic Kotlin baseline plus an LLM override grounded in incident citations. | Kotlin, IntelliJ SDK, Datadog |
| [**Sentinel**](https://github.com/stevenybuilder/sentinel-agent-security) | Runtime security layer for autonomous agents: investigators verify claims, a policy gate blocks risky actions, confirmed attacks become AST-validated scoring rules. [Live](https://sentinelapp-delta.vercel.app). | Python, asyncio, FastAPI, React |
| [**AI Meeting Autopilot**](https://github.com/stevenybuilder/ai-meeting-autopilot) | Live transcription, commitment extraction and action dispatch across Slack, Calendar, Gmail and BigQuery over WebSockets. | Python, Gemini, Cloud STT, Terraform |
| [**Together**](https://github.com/stevenybuilder/together-presence-agent) | Bidirectional live speech translation with scene narration, then a generated storybook and memory video from the call. | Gemini Live, Deepgram, Veo |

## Awards

| | |
|---|---|
| Intuit AI/ML Hackathon, June 2026 | 2nd place |
| Google DeepMind Hackathon, March 2026 | Best Use of DigitalOcean |
| Experian Global AI Hackathon, November 2025 | 1st of 91 teams |
| AI Valley Robotics Hackathon, November 2025 | Best Use of Convex |

## Background

Cognitive neuroscience at UC Irvine's Center for the Neurobiology of Learning and Memory (Stark Lab): fMRI analysis in Python for studies of spatial navigation, hippocampal pattern separation and human memory, including a self-proposed, funded study later adopted by the lab's postdocs.
