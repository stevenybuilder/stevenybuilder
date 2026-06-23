<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1220,45:2563EB,100:10B981&height=220&section=header&text=Steven%20Yang&fontSize=56&fontColor=FFFFFF&fontAlignY=38&desc=AI%2FML%20systems%20%7C%20agents%20%7C%20data%20science%20%7C%20cloud%20engineering&descSize=18&descColor=EAF2FF&descAlignY=60&animation=fadeIn" width="100%" />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-stevenyang99-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/stevenyang99)
[![Email](https://img.shields.io/badge/Email-stevenybusiness%40gmail.com-181717?style=for-the-badge&logo=gmail&logoColor=white)](mailto:stevenybusiness@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-stevenybuilder-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder)

</div>

<br/>

> **AI/ML systems builder | Python agents, LLM evals, RAG/MCP, GCP, Databricks, and statistically grounded decision systems**
>
> I build AI-native systems where models, data pipelines, cloud infrastructure, and production workflows meet. My work spans agent orchestration, explainable ML, calibrated decision systems, real-time WebSocket backends, LLM evaluation, and cloud-deployed data products.

<table><tbody>
<tr><td><b>Languages</b></td><td>Python, Kotlin, JavaScript, TypeScript, SQL, HTML/CSS, shell</td></tr>
<tr><td><b>ML/Data</b></td><td>CatBoost, scikit-learn, pandas, NumPy, calibration, conformal intervals, Bayesian scoring, survival/censoring, causal caution</td></tr>
<tr><td><b>AI Systems</b></td><td>LLM tool loops, MCP servers, RAG/retrieval, golden-dataset evals, deterministic gates, generated-code validation</td></tr>
<tr><td><b>Cloud/Infra</b></td><td>Google Cloud Run, BigQuery, Gemini, Vertex AI, Databricks Asset Bundles, Delta Lake, MLflow, Docker, FastAPI, React</td></tr>
</tbody></table>

<br/>

## Technical Throughline

Before enterprise AI product work, I did cognitive neuroscience research at UC Irvine's Center for Neurobiology of Learning and Memory / Stark Lab, using Python for fMRI image processing and analysis. That background still shapes how I build: define the measurement problem, separate signal from confounders, quantify uncertainty, and treat model outputs as evidence rather than magic.

<br/>

## What I'm Building

<div align="center">

### CareGap

**Healthcare access intelligence for finding and explaining medical deserts.**

[![Repo](https://img.shields.io/badge/caregap--medical--desert--map-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/caregap-medical-desert-map)
[![Cloud Run](https://img.shields.io/badge/live-Cloud%20Run-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://caregap-app-31043195041.us-central1.run.app/)
[![Devpost](https://img.shields.io/badge/devpost-project-003E54?style=for-the-badge&logo=devpost&logoColor=white)](https://devpost.com/software/databricks-copilot-medical-desert-map)

</div>

CareGap ranks likely medical deserts, estimates confidence, surfaces provider evidence, and recommends concrete deployment actions for healthcare planners. It combines lakehouse-style data workflows with statistical uncertainty layers so users can inspect not just where gaps exist, but why the system believes they exist.

<table><tbody>
<tr><td><b>Data pipeline</b></td><td>Bronze/silver/gold flow for facility records, geography, provider claims, district health indicators, and review queues; bundled as Databricks serverless jobs</td></tr>
<tr><td><b>Modeling</b></td><td>CatBoost capacity and doctor-count imputers, native categorical handling, log1p targets, 5-fold OOF validation, clipped predictions, MLflow logging</td></tr>
<tr><td><b>Uncertainty</b></td><td>Bayesian validity posterior, empirical-Bayes trust smoothing, Wilson intervals, split-conformal facility trust sets</td></tr>
<tr><td><b>Stack</b></td><td>Python, Databricks Apps, Databricks SQL connector, Delta Lake, Unity Catalog, MLflow, Streamlit, CatBoost, PyDeck/H3, Google Cloud Run, Docker</td></tr>
</tbody></table>

<div align="center">

---

### Guardia

**Deployment-risk copilot inside JetBrains IDEs.**

[![Repo](https://img.shields.io/badge/guardia-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/guardia)

</div>

Guardia brings production-risk analysis into the developer workflow before code ships. It reads touched services, Git context, incident patterns, and observability signals, then explains likely deployment risks with cited evidence and targeted remediation paths inside IntelliJ.

<table><tbody>
<tr><td><b>IDE engineering</b></td><td>Native IntelliJ plugin with PSI, Git4Idea diff extraction, PasswordSafe credentials, tool windows, editor highlights, and undoable WriteCommandAction patches</td></tr>
<tr><td><b>Risk engine</b></td><td>Sub-5ms deterministic Kotlin baseline plus bounded OpenAI/Codex Responses API override grounded in incident citations</td></tr>
<tr><td><b>Retrieval</b></td><td>Datadog incident context, BM25/structural matching, reciprocal-rank fusion, and offending-code snippet scans</td></tr>
<tr><td><b>Stack</b></td><td>Kotlin, IntelliJ Platform SDK, Gradle, JDK 21, OkHttp, Moshi, Python fixture generation, Datadog APIs, Supabase, OpenAI</td></tr>
<tr><td><b>Verification</b></td><td>28 Kotlin test files plus remote-robot UI smoke-test source set</td></tr>
</tbody></table>

<div align="center">

---

### Intuit SMB Underwriting

**Explainable ML system for small-business lending decisions.**

[![Team Repo](https://img.shields.io/badge/team%20repo-ron2k1%2Fintuit--techweek--smb--underwriting-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ron2k1/intuit-techweek-smb-underwriting)
[![Hackathon](https://img.shields.io/badge/Intuit%20TechWeek-NYC%202026-236CFF?style=for-the-badge)](https://github.com/intuit/intuit-techweek-nyc-hackathon-2026)

</div>

Team build for the Intuit TechWeek NYC 2026 Explainable ML hackathon. I owned modeling and calibration work for underwriting decisions: estimating probability of default, producing 90% intervals, and iterating on profit-aware approval logic under selection bias, leakage risk, censoring, and missing-not-at-random bank-feed data.

<table><tbody>
<tr><td><b>Decision problem</b></td><td>Approve or decline SMB loan applicants to maximize realized portfolio profit under APR, origination-fee, LGD, and default-definition constraints</td></tr>
<tr><td><b>ML depth</b></td><td>Calibrated PD modeling, uncertainty intervals, profit break-even thresholds, reject-inference awareness, leakage controls, MNAR missingness indicators</td></tr>
<tr><td><b>Challenge scope</b></td><td>Loan decisions, default trajectory forecasting, causal counterfactual PDs, monotonicity checks, and explainable methodology defense</td></tr>
<tr><td><b>Stack</b></td><td>Python, pandas, NumPy, scikit-learn, SciPy, statsmodels, HGB/value ensembles, calibration pipelines, CSV validators</td></tr>
<tr><td><b>Validation</b></td><td>Submission schema/ID/range/monotonicity gate with PASS status before upload</td></tr>
</tbody></table>

<div align="center">

---

### Sentinel

**Runtime security layer for autonomous AI agents.**

[![Repo](https://img.shields.io/badge/sentinel--agent--security-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/sentinel-agent-security)
[![Live Demo](https://img.shields.io/badge/demo-sentinelapp--delta.vercel.app-10B981?style=for-the-badge&logo=vercel&logoColor=white)](https://sentinelapp-delta.vercel.app)

</div>

Sentinel treats agent behavior as a security surface. Independent investigators verify payment-agent claims against ground truth, a deterministic safety gate blocks risky actions, and confirmed attacks generate new Python scoring rules that are AST-validated, regression-tested, and hot-deployed.

<table><tbody>
<tr><td><b>Core loop</b></td><td>Supervisor agent, payment agent, risk/compliance/forensics investigators, verdict board, deterministic policy gate</td></tr>
<tr><td><b>Concurrency</b></td><td>Python 3.11 asyncio.TaskGroup dispatch for parallel sub-agent investigations with structured cancellation</td></tr>
<tr><td><b>Learning system</b></td><td>Generated Python scoring functions validated by AST parse, attack/clean regression checks, forbidden-token scan, and RestrictedPython execution</td></tr>
<tr><td><b>Stack</b></td><td>Python, FastAPI, Pydantic, Anthropic async client, React, Vite, JavaScript, XYFlow, Zustand, Aerospike, RestrictedPython, Auth0, Docker</td></tr>
<tr><td><b>Verification</b></td><td>22 pytest files plus GitHub Actions backend deployment workflow to EC2</td></tr>
</tbody></table>

<div align="center">

---

### AI Meeting Autopilot

**Multimodal meeting agent with real-time audio, vision, memory, and action dispatch.**

[![Repo](https://img.shields.io/badge/ai--meeting--autopilot-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/ai-meeting-autopilot)
[![Cloud Run](https://img.shields.io/badge/live-Cloud%20Run-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://meeting-agent-ynzg64zhoa-uc.a.run.app/)

</div>

This system transcribes live browser audio, extracts commitments, checks sentiment, and dispatches actions across Slack, Calendar, Gmail, documents, and BigQuery reports. Sessions run through WebSockets and async background execution so follow-up work can happen while the meeting continues.

<table><tbody>
<tr><td><b>Realtime pipeline</b></td><td>Browser PCM at 16kHz, WebSocket transport, Cloud STT streaming, transcript buffering, Gemini extraction, deterministic sentiment gate</td></tr>
<tr><td><b>Reliability</b></td><td>Per-session dataclass registry, background task retention, proactive STT reconnect before streaming limits, async action fanout</td></tr>
<tr><td><b>Actions/data</b></td><td>Slack updates, Calendar events, Gmail summaries, document revision, BigQuery NL-to-SQL reports, DigitalOcean meeting memory</td></tr>
<tr><td><b>Stack</b></td><td>Python, FastAPI, JavaScript, HTML/Tailwind, WebSockets, Gemini, Google Cloud STT/Vision, BigQuery, Slack SDK, DigitalOcean inference/KB, Cloud Run, Terraform</td></tr>
<tr><td><b>Verification</b></td><td>8 regression/smoke tests with GitHub Actions install, smoke, and test workflow</td></tr>
</tbody></table>

<div align="center">

---

### Together

**Live translation and memory generation for cross-language presence.**

[![Repo](https://img.shields.io/badge/together--presence--agent-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/together-presence-agent)

</div>

Together is a real-time conversation system for people separated by distance and language. It translates speech bidirectionally, narrates the other person's environment on request, then turns call moments into a generated storybook and memory video.

<table><tbody>
<tr><td><b>Realtime mode</b></td><td>FastAPI/WebSocket rooms, per-participant streaming sessions, Gemini Live bidirectional speech translation, translated captions, session affinity on Cloud Run</td></tr>
<tr><td><b>Vision/memory</b></td><td>Vision scene analysis with semaphores, markdown transcript logging, storybook generation through Gemini interleaved output, memory video pipeline through Veo</td></tr>
<tr><td><b>Reliability</b></td><td>Deepgram STT sessions, ElevenLabs/Gradium TTS fallback path, billing monitor controls for demo safety</td></tr>
<tr><td><b>Stack</b></td><td>Python, FastAPI, WebSockets, Gemini Live, Google Cloud Vision, Deepgram, Veo, ElevenLabs, HTML/JavaScript, Docker, Cloud Run</td></tr>
</tbody></table>

<br/>

## Tech Stack

<div align="center">

**`Languages`**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**`Data / ML`**

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=flat-square&logo=googlebigquery&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

**`Cloud / Backend / Infra`**

![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Cloud Run](https://img.shields.io/badge/Cloud%20Run-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)

**`AI Systems`**

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat-square&logo=google&logoColor=white)
![Anthropic](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Datadog](https://img.shields.io/badge/Datadog-632CA6?style=flat-square&logo=datadog&logoColor=white)

</div>

<br/>

## Recent Wins

<table><tbody>
<tr><td><b>Intuit AI/ML Hackathon</b></td><td>2nd Place, June 2026 - calibrated underwriting PDs and profit-aware decision logic</td></tr>
<tr><td><b>Google DeepMind Hackathon</b></td><td>Best Use of DigitalOcean, March 2026 - multimodal meeting memory and agent workflow</td></tr>
<tr><td><b>Experian Global AI Hackathon</b></td><td>1st Place, November 2025 - AI-driven credit optimization MVP</td></tr>
<tr><td><b>AI Valley Robotics Hackathon</b></td><td>Best Use of Convex, November 2025</td></tr>
</tbody></table>

<br/>

## Operating Range

- Build production-shaped AI systems across backend, frontend, data, ML, and cloud infrastructure
- Design decision systems with calibration, uncertainty, evals, explainability, and data-quality guardrails
- Ship agentic workflows with MCP servers, tool use, RAG/retrieval, deterministic gates, and human review
- Translate ambiguous business problems into measurable systems while staying close to the code

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:10B981,50:2563EB,100:0B1220&height=110&section=footer" width="100%" />
