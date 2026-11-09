<a href="https://github.com/stevenybuilder"><img src="contributions.svg" alt="Steven Yang's GitHub contribution graph, March 2026 onward" width="100%"/></a>

# Steven Yang

Creating more efficient robot foundation models for continual learning.

[Writing](https://stevenybuilder.github.io) · [LinkedIn](https://www.linkedin.com/in/stevenyang99) · [X](https://x.com/stevenytechs) · [Email](mailto:stevenybusiness@gmail.com)

## Now

<img src="https://stevenybuilder.github.io/assets/media/about-steven-yang-headshot.webp" alt="Portrait of Steven Yang" align="right" width="150"/>

- More efficient robot foundation models for continual learning: models that keep learning from new experience after deployment, without forgetting old skills or being retrained from scratch.
- Learning and memory mechanisms for recurrent state-space models in JEPA, during pretraining and at inference time, with compute efficiency as a constraint.
- Looking for a scaling law for JEPA world models on robotics tasks: how planning success moves with model size, data and compute.
- Paper accepted at the CoRL 2026 Workshop on Memory for Robot Foundation Models: *MemJEPA: Learning What a Latent World-Model Planner Must Remember*. A recurrent state lets a latent world-model planner act with the controlled entity hidden, but only when it is trained on erased inputs with clean prediction targets.
- Paper accepted at the NeurIPS 2026 Workshop on Long-Context Foundation Models (LCFM): *Second-Read Divergence: Context Reuse in JEPA-WM*. An action patch in a JEPA world model matches the changed-input forecast at first, then diverges when the edited action returns as history. [Code and results](https://github.com/stevenybuilder/jepa_steering).
- Latest write-up: [Reading and steering motion in V-JEPA 2](https://github.com/stevenybuilder/jepa_physics). Layer-wise probing, nullspace erasure and manifold steering of direction, speed and acceleration in the frozen encoder, judged by the model's own predictor.
- Before that: [instruction following in π0.5](https://stevenybuilder.github.io/pick-it-up/), a causal pathway for instruction control in a vision-language-action model.

<br clear="right"/>

## Background

**Research.** Two single-author workshop papers in 2026 on memory and context reuse in JEPA world-model planners: MemJEPA at the CoRL 2026 Workshop on Memory for Robot Foundation Models, with the full-length version under review, and Second-Read Divergence at the NeurIPS 2026 Workshop on Long-Context Foundation Models. The experiments run on rented multi-GPU fleets with pre-registered reads, sealed held-out sets and three seeds per cell; every number in the papers traces to a per-episode record. Earlier in 2026: reproduced Meta FAIR's *Interpreting Physics in Video World Models* on V-JEPA 2 in 36 hours and extended it from reading motion to steering it (commissioned by Sonia Joseph, World Mechanics), and traced instruction following in π0.5 with K/V-cache activation patching scored by closed-loop success in LIBERO.

**Neuroscience.** Student researcher at UC Irvine's Center for the Neurobiology of Learning and Memory (Stark Lab), 2017 to 2020: computer-vision and deep-learning pipelines in Python for fMRI studies of spatial navigation and hippocampal pattern separation, and memory experiments with human participants. Proposed and secured funding for the lab's first study beyond its hippocampus focus, collected and analysed data from 150+ participants, and presented it at the UCI research symposium; its use of the Mnemonic Similarity Task was taken up by the lab's postdocs. Led a team of five undergraduates. This work is the origin of the current research on memory in world-model planners.

**Industry.** Technical product manager for AI and data products at Experian, New York, 2021 to 2026. Designed and built the evaluation harness for Experian's first AI dispute assistant (7M+ consumers): golden datasets, automated regression tests and open-source vision-LLM OCR intake. Led three engineering teams building the MCP servers and tool integrations for Experian's 0-to-1 Google Gemini integration (projected 1.2M users). Re-architected the API layer of a 100K-user financial product, removing 99% of customer-visible errors (Experian Excellence Award). Built an LLM agent that triages data-breach reports, adopted across business units, cutting response time from about five days to hours. Earlier, co-authored a report to the U.S. Congress on AI and innovation policy at the USPTO Office of the Chief Economist.

**Teaching.** Section leader and teaching assistant for Stanford's first open offering of Probability for AI (Professor Chris Piech; 10,000 students), selected from 2,700+ applicants. Designed and led hands-on Codex and Claude Code summits for 30 engineers and product managers at Experian, including safeguards for LLM systems.

**Education.** Computer science and mathematics coursework at UC San Diego and UCLA, 2026 to present (GPA 4.0): deep learning for computer vision, linear algebra for machine learning, probability and statistics for AI, embedded machine learning. B.A., UC Irvine, 2021, Phi Beta Kappa.

## Skills

| | |
|---|---|
| **Programming** | Python, C/C++, CUDA, SQL, JavaScript/TypeScript, Kotlin, Bash |
| **Deep learning** | PyTorch, JAX, distributed training (DDP), Triton kernels, vLLM, MLflow, NumPy, pandas, scikit-learn, XGBoost |
| **Computer vision** | OpenCV, Vision Transformers, DINO, VideoMAE, V-JEPA, Gaussian splatting, MONAI, 3D MRI volumes |
| **Robotics and world models** | MuJoCo, Isaac Sim, LIBERO, LeRobot, pi0.5, OpenVLA, JEPA-WM, LeWorldModel, DreamerV3, MPC/CEM planning, PPO and reinforcement learning |
| **Systems** | Docker, Git, Bash, multi-host GPU orchestration, AWS/GCP, FastAPI, Airflow, SQL, Databricks |

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

