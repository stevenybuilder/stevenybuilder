# Steven Yang

Creating more efficient robot foundation models based on deployment data that can perform well on long horizon and complex planning tasks in spatial navigation.

[Writing](https://stevenybuilder.github.io) · [LinkedIn](https://www.linkedin.com/in/stevenyang99) · [X](https://x.com/stevenytechs) · [Email](mailto:stevenybusiness@gmail.com)

## What I'm Working On

<img src="https://stevenybuilder.github.io/assets/media/about-steven-yang-headshot.webp" alt="Portrait of Steven Yang" align="right" width="150"/>

- More efficient robot foundation models for continual learning: models that keep learning after deployment without forgetting old skills or retraining from scratch.
- Learning and memory mechanisms for recurrent state-space models in JEPA, and a scaling law for JEPA world models on robotics tasks.
- Papers: *MemJEPA: Learning What a Latent World-Model Planner Must Remember* (CoRL 2026 Workshop on Memory for Robot Foundation Models) and *Second-Read Divergence: Context Reuse in JEPA-WM* (NeurIPS 2026 Workshop on Long-Context Foundation Models, [code and results](https://github.com/stevenybuilder/jepa_steering)).
- Write-ups: [Reading and steering motion in V-JEPA 2](https://github.com/stevenybuilder/jepa_physics) and [instruction following in π0.5](https://stevenybuilder.github.io/pick-it-up/).

<br clear="right"/>

## Background

**Publications.** Two single-author workshop papers in 2026 (CoRL and NeurIPS) on memory and context reuse in JEPA world-model planners, with the CoRL paper's full-length version under review. Experiments run on rented multi-GPU fleets with pre-registered reads and sealed held-out sets. Earlier in 2026: interpretability studies of V-JEPA 2 (for World Mechanics) and of instruction following in π0.5.

**Spatial navigation and memory research.** Student researcher at UC Irvine's Center for the Neurobiology of Learning and Memory (Stark Lab), 2017 to 2020: fMRI pipelines and human memory experiments on spatial navigation and hippocampal pattern separation. Proposed and secured funding for a study of 150+ participants that the lab's postdocs carried forward, and led a team of five undergraduates. This is where the interest in memory in world-model planners started.

**Industry.** Technical product manager for AI and data products at Experian, 2021 to 2026: built the evaluation harness for its first AI dispute assistant (7M+ consumers) and led three engineering teams on its Google Gemini integration. Before that, as a summer 2019 intern in the Office of the Chief Economist at the U.S. Patent and Trademark Office, co-authored with four staff economists an economics report on AI, technology policy and innovation that Congress had commissioned from the office.

**Teaching.** Section leader for Stanford's first open offering of Probability for AI (Professor Chris Piech; 10,000 students), selected from 2,700+ applicants.

**Education.** Deep Learning for Computer Vision; Practicum for Deep Neural Networks; Linear Algebra for Machine Learning; Probability and Statistics for AI; Embedded Machine Learning; Multivariable Calculus; Discrete Math; Data Structures and Algorithms.

## Skills

| | |
|---|---|
| **Programming** | Python, C/C++, CUDA, SQL, JavaScript/TypeScript, Kotlin, Bash |
| **Deep learning** | PyTorch, JAX, distributed training (DDP), Triton kernels, vLLM, MLflow, NumPy, pandas, scikit-learn, XGBoost |
| **Computer vision** | OpenCV, Vision Transformers, DINO, VideoMAE, V-JEPA, Gaussian splatting, MONAI, 3D MRI volumes |
| **Robotics and world models** | MuJoCo, Isaac Sim, LIBERO, LeRobot, pi0.5, OpenVLA, JEPA-WM, LeWorldModel, DreamerV3, MPC/CEM planning, PPO and reinforcement learning |
| **Systems** | Docker, Git, Bash, multi-host GPU orchestration, AWS/GCP, FastAPI, Airflow, SQL, Databricks |

## Awards

| | |
|---|---|
| Intuit AI/ML Hackathon, June 2026 | 2nd place |
| Google DeepMind Hackathon, March 2026 | Best Use of DigitalOcean |
| Experian Global AI Hackathon, November 2025 | 1st of 91 teams |
| AI Valley Robotics Hackathon, November 2025 | Best Use of Convex |

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

## Activity

<img src="contributions.svg" alt="Steven Yang's GitHub contributions, last six months" width="420"/>
