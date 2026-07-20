<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1220,45:2563EB,100:10B981&height=220&section=header&text=Steven%20Yang&fontSize=56&fontColor=FFFFFF&fontAlignY=38&desc=representation%20learning%20%7C%20evaluation%20design&descSize=22&descAlignY=60&animation=fadeIn" width="100%" />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-stevenyang99-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/stevenyang99)
[![Email](https://img.shields.io/badge/Email-stevenybusiness%40gmail.com-181717?style=for-the-badge&logo=gmail&logoColor=white)](mailto:stevenybusiness@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-stevenybuilder-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder)

</div>

<br/>

> **Research PM — representation learning, evaluation design, and computer vision on 3D volumetric data.**
>
> I probe frozen self-supervised encoders and build the evaluation layer that decides whether what they encode is signal or acquisition artifact. On 96 healthy brains with no disease signal, the frozen encoder I probed still predicted scanner field strength at AUC 0.931 — that kind of result is the product. Cognitive neuroscience background — hippocampal pattern separation and fMRI analysis at UC Irvine (Stark Lab / CNLM). Looking for research-adjacent product work at labs building learned representations and world models.

<table><tbody>
<tr><td width="22%"><b>Representation learning</b></td><td>JEPA-family predictive embeddings (third-party weights, frozen), frozen-encoder inference, linear and MLP probing, embedding-space evaluation, batch-effect and confound ablation, PCA under p&gt;&gt;n</td></tr>
<tr><td width="22%"><b>Computer vision</b></td><td>3D volumetric MRI (T1w), MONAI transform pipelines, MNI152 space, skull-stripping, DICOM→NIfTI, 3D ViT inference on GPU runtimes</td></tr>
<tr><td width="22%"><b>Evaluation / stats</b></td><td>Site-disjoint StratifiedGroupKFold, label-permutation nulls, bootstrap CIs, ComBat harmonization, split-conformal intervals, calibration, empirical-Bayes smoothing</td></tr>
<tr><td width="22%"><b>Languages</b></td><td>Python, Kotlin, JavaScript, TypeScript, SQL, HTML/CSS</td></tr>
<tr><td width="22%"><b>AI systems</b></td><td>LLM tool loops, enum-constrained routing, MCP servers, RAG/retrieval, golden-dataset evals, deterministic gates, generated-code validation</td></tr>
<tr><td width="22%"><b>Cloud / infra</b></td><td>Google Cloud Run, BigQuery, Vertex AI, Databricks Asset Bundles, Delta Lake, MLflow, Docker, FastAPI, React</td></tr>
</tbody></table>

<br/>

## Why Representations

Before product work I did cognitive neuroscience research at UC Irvine's Center for the Neurobiology of Learning and Memory, in Craig Stark's lab, writing Python for fMRI image processing and analysis.

The lab's core question is **pattern separation**: how the hippocampus keeps highly similar experiences from collapsing into the same memory. The circuit-level story is a dissociation — the DG/CA3 subregion, a joint ROI because fMRI cannot resolve the two, and a theoretically awkward one since CA3's recurrent collaterals are the classic *completion* circuit, shows a stepwise, separation-biased response where a small change in input is amplified into a large change in output, while CA1 responds in a graded, completion-biased way. The behavioral readout is **mnemonic discrimination**, measured with the Mnemonic Similarity Task (MST): an old/new/similar recognition task with parametrically graded lures, scored by the Lure Discrimination Index. I also worked on the spatial side of the lab's program — navigation experiments and simulations in virtual environments, where the constructs are place and grid coding, allocentric versus egocentric reference frames, and cognitive maps.

Two things in that work turned out to be the same problems I now care about in machine learning, and I want to be precise about the mapping rather than gesture at it.

**Pattern separation is a statement about representation geometry.** DG expansion recoding takes an overlapping entorhinal input and re-embeds it into a much larger, sparser, decorrelated code, so that near-duplicate experiences remain separately retrievable. That is the same problem a joint-embedding objective faces from the other side. A JEPA has no negatives — nothing in the loss pushes near-duplicate inputs apart; collapse is held off architecturally, by the asymmetry between an EMA target encoder and a predictor, not by a repulsion term. So separation is never guaranteed by the objective. It is an empirical property of the trained encoder that someone has to go measure, on inputs chosen to be as confusable as possible. That is what lure trials are for, and it is the instinct I carry into probing models.

**Latents should be judged by what they predict.** The successor-representation line (Stachenfeld, Botvinick & Gershman) argues place cells encode expected discounted future state occupancy under the current policy rather than geometry, and the Tolman-Eichenbaum Machine factorizes structural transition rules from sensory content. Both say the useful latent is a *predictive* one. That is the same commitment a JEPA makes by predicting in embedding space instead of pixel space and letting unpredictable detail go. I read this literature; I have not trained a world model, and NeuroAD has no actions, rollouts, or temporal dynamics. What I have done is the evaluation half — take a frozen predictive encoder and measure, adversarially, what its representation actually contains.

<br/>

## Things I've Built

<div align="center">

### NeuroAD Discovery Engine

**Latent-space forensics for a frozen 3D brain-MRI foundation model.**

[![Repo](https://img.shields.io/badge/NeuroAD-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/stevenybuilder/NeuroAD)
[![Hackathon](https://img.shields.io/badge/Claude%20Life%20Sciences-Gladstone%20Institutes-D97757?style=for-the-badge)](https://github.com/stevenybuilder/NeuroAD)

</div>

Built for the Claude Life Sciences hackathon with Gladstone Institutes. The premise: a foundation-model embedding separates Alzheimer's from control — but it separates scanners, sites, and field strengths just as well. NeuroAD is the referee that tells you which one the model is reading.

**Attribution, stated plainly.** The encoder is **Neuro-JEPA** (NYUMedML, [arXiv 2606.14957](https://arxiv.org/abs/2606.14957)) — a **third-party** model that extends V-JEPA 2 predictive-embedding to 3D brain MRI, pretrained by its authors on ~1.55M scans. **I did not train, fine-tune, adapt, or author it.** I ran frozen-encoder inference under its gated CC-BY-NC-ND terms — no gradients, no derivative weights, weights never written to the repo — and wrote the extraction, confound-ablation, probing, and evaluation layers on top. Frontend and MRI QC work was contributed by Siddharth Radhakrishnan.

**What the pipeline does.** 3D T1w volume → MONAI preprocessing (RAS reorientation, 1mm resampling, foreground crop, center crop) and deepbet skull-stripping → frozen ViT-MoE forward pass under `no_grad`, token mean-pool to a 768-d vector → one reused logistic probe → a five-test confound gauntlet → a verdict and a proposed next experiment. **1,787 subjects across four cohorts** (ADNI, OASIS-1, OASIS-2, OpenBHB) have real extracted embeddings on disk.

**The finding I care about most is a negative one about the encoder.** On 96 healthy OpenBHB brains with no disease signal, the frozen Neuro-JEPA representation predicts **scanner field strength at AUC 0.931 at PCA-10** — reduced to ten components specifically so it is not a p≫n artifact. At n=96 that point estimate carries a permutation p of 0.073, so I treat it as suggestive rather than significant; the same fixture recomputed under a different CV split gives 0.958 with p<sub>perm</sub>=0.001, and the honest read is the band, not either endpoint. Field strength is also partly nested within site in this cohort, so this probe cannot be cleanly site-disjoint — read it as a within-cohort acquisition probe, not a site-independent one. The raw 768-d number is ~0.998 and I report it labelled as inflated rather than quietly dropping it. Nuisance acquisition physics is linearly decodable from a self-supervised embedding and does not wash out under dimensionality reduction.

<table><tbody>
<tr><td width="22%"><b>Probing</b></td><td>One reused L2-logistic head pointed at either the outcome (<code>dx_binary</code>) or the confound (<code>scanner</code>/<code>site</code>), so the result and its own falsifier share an estimator. Site-disjoint StratifiedGroupKFold, bootstrap CIs, label-permutation nulls. PCA/whitening and covariate residualization fit <b>inside</b> each fold — <a href="https://github.com/stevenybuilder/NeuroAD/blob/main/src/neuroad/probe.py"><code>src/neuroad/probe.py</code></a></td></tr>
<tr><td width="22%"><b>Confound instrumentation</b></td><td>Leakage margin (outcome AUC − scanner AUC) and a double dissociation that scrubs the scanner-predicting direction from the embedding and re-measures the outcome — <a href="https://github.com/stevenybuilder/NeuroAD/blob/main/src/neuroad/leakage.py"><code>src/neuroad/leakage.py</code></a></td></tr>
<tr><td width="22%"><b>Harmonization</b></td><td>Hand-written parametric ComBat with empirical-Bayes shrinkage, deliberately label-blind: age and sex protected as covariates, diagnosis excluded from the design so the correction never sees the outcome — <a href="https://github.com/stevenybuilder/NeuroAD/blob/main/src/neuroad/data/harmonize.py"><code>src/neuroad/data/harmonize.py</code></a></td></tr>
<tr><td width="22%"><b>Batch-effect result</b></td><td>Raw embeddings separate ADNI from OASIS at AUC 0.9996. After label-blind ComBat, cohort drops to 0.5634 while AD-vs-CN survives at 0.8608 pooled and 0.8313 cross-cohort site-disjoint (n=835). The ComBat fit is whole-cohort, not fold-honest, so 0.5634 is an optimistic floor on residual cohort leakage — the AD-vs-CN figures are the leakage-free site-disjoint CV numbers</td></tr>
<tr><td width="22%"><b>Latent geometry</b></td><td>Within-ADNI AD-vs-CN 0.848 [0.805–0.888], n=590 (87 AD), p<sub>perm</sub>=0.001 (cross-cohort run). Not age-residualized: AD atrophy and accelerated aging load on overlapping directions, and separating them needs a brain-age-gap control I have not run cleanly, so read this as AD-vs-CN discriminability rather than AD-specific structure. In a separate repeated-CV probe run on the same n=590, a regularized MLP head scores 0.857 against that run's linear probe at 0.859 — a gap far inside the bootstrap CI, so the nonlinear head buys nothing at this n and the frozen embedding is already near-linearly separable</td></tr>
<tr><td width="22%"><b>Anchoring</b></td><td>The frozen structural embedding predicts <i>measured</i> plasma p-tau217 high-vs-low at 0.653 [0.609–0.697] (n=590) and amyloid status at 0.661 [0.608–0.710] (n=546) — modest, above the permutation null, and not adjusted for age, which drives both atrophy and p-tau217. I would want an age-and-sex-only baseline before reading this as molecular signal rather than shared age variance</td></tr>
<tr><td width="22%"><b>Stated limits</b></td><td>The extraction yields one pooled 768-d vector per subject, not per-patch tokens, so there are no spatial attention maps. The nonlinear head is a regularized MLP with leave-one-group-out attribution, labelled attribution and not attention — <a href="https://github.com/stevenybuilder/NeuroAD/blob/main/src/neuroad/attentive_probe.py"><code>src/neuroad/attentive_probe.py</code></a></td></tr>
<tr><td width="22%"><b>Honest negative</b></td><td>Unsupervised phenotype discovery on real OpenBHB returned <b>0 promotable phenotypes</b> — both recovered clusters were flagged as acquisition artifact and killed by the gauntlet. It is in the demo as-is</td></tr>
<tr><td width="22%"><b>Agentic layer</b></td><td>Claude Sonnet router with enum-constrained routing plus a per-scan Opus agent that reads the evidence and drafts the next experiment. Claude never produces a number — every figure comes from the probe</td></tr>
<tr><td width="22%"><b>Reproducibility</b></td><td><code>neuroad reproduce-finding</code> recomputes the scanner-leakage probe from a license-safe PCA-10 fixture — 0.958 [0.907–0.997], p<sub>perm</sub>=0.001, landing in the same PCA-10 band as the 0.931 headline; the gap is the different cross-validation split, not a different claim. The fixture is git-ignored alongside the 768-d embedding tables rather than redistributed, so the command runs from a local checkout, not a bare clone, and needs no gated weights</td></tr>
</tbody></table>

**What I got wrong.** I audited my own flagship result — an AD-vs-CN AUROC of 0.922 on FreeSurfer ROI morphometry, a different substrate from the Neuro-JEPA embedding — and found the de-confound evidence on display, a below-chance scanner AUC of 0.374, was an artifact of running ComBat across the whole cohort before the probe. Fold-honest, residual scanner leakage is 0.648, not below chance. I corrected the honest residual leakage upward and kept the claim only for the cell where the confound is impossible by construction: within a single field strength. The audit is in the repo.

**What I would do next.** The pooled 768-d vector throws away everything Neuro-JEPA's sparse-MoE structure encodes about *where* it is looking. Per-patch tokens plus expert-routing analysis would let the same confound gauntlet ask which experts fire on acquisition physics versus anatomy — that is the experiment I want to run.

<div align="center">

---

### Intuit SMB Underwriting

**Calibrated probability-of-default modeling for small-business lending decisions.**

[![Team Repo](https://img.shields.io/badge/team%20repo-ron2k1%2Fintuit--techweek--smb--underwriting-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ron2k1/intuit-techweek-smb-underwriting)
[![Hackathon](https://img.shields.io/badge/Intuit%20TechWeek-NYC%202026-236CFF?style=flat-square)](https://github.com/intuit/intuit-techweek-nyc-hackathon-2026)

</div>

Team build for the Intuit TechWeek NYC 2026 Explainable ML hackathon — 2nd place; I owned modeling and calibration. The objective was stated as an objective function rather than a metric: approve or decline to maximize realized portfolio profit under APR, origination-fee, LGD, and default-definition constraints — which makes the threshold a business decision and the calibration the thing that has to be right.

<table><tbody>
<tr><td width="22%"><b>ML depth</b></td><td>Calibrated PD modeling with 90% intervals, profit break-even thresholds, leakage controls, MNAR missingness indicators for bank-feed gaps, and selection-bias handling on an observed-approvals-only population. Calibration was checked on a held-out split at hackathon data scale — treat as directional, not a production calibration claim</td></tr>
<tr><td width="22%"><b>Enforced gate</b></td><td>A schema, ID-range, and monotonicity gate had to return PASS before any submission uploaded; a non-monotonic PD curve blocked the run</td></tr>
<tr><td width="22%"><b>Scoped out</b></td><td>Causal counterfactual PDs. The observational data could not identify the effect, and a confidently wrong counterfactual is worse than an absent one</td></tr>
</tbody></table>

<div align="center">

---

### CareGap

**Healthcare access intelligence for finding and explaining medical deserts.**

[![Repo](https://img.shields.io/badge/caregap--medical--desert--map-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/stevenybuilder/caregap-medical-desert-map)
[![Cloud Run](https://img.shields.io/badge/live-Cloud%20Run-4285F4?style=flat-square&logo=googlecloud&logoColor=white)](https://caregap-app-31043195041.us-central1.run.app/)
[![Devpost](https://img.shields.io/badge/devpost-project-003E54?style=flat-square&logo=devpost&logoColor=white)](https://devpost.com/software/databricks-copilot-medical-desert-map)

</div>

CareGap ranks likely medical deserts and attaches an uncertainty layer to every ranking, so a planner can inspect not just where the gaps are but how much the system should be believed about each one. The ranking is only worth acting on if the uncertainty is real, which made the interval machinery the load-bearing part rather than the model.

<table><tbody>
<tr><td width="22%"><b>Uncertainty</b></td><td>Bayesian validity posterior, empirical-Bayes trust smoothing across sparse facilities, Wilson intervals, split-conformal facility trust sets. Coverage was targeted but not empirically validated at demo scope — I would not quote a coverage number</td></tr>
<tr><td width="22%"><b>Modeling / data</b></td><td>CatBoost capacity and doctor-count imputers with native categorical handling and log1p targets, 5-fold OOF validation, MLflow logging, over a bronze/silver/gold Delta flow bundled as Databricks serverless jobs</td></tr>
</tbody></table>

<div align="center">

---

### Sentinel

**Runtime verification layer for autonomous AI agents.**

[![Repo](https://img.shields.io/badge/sentinel--agent--security-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/stevenybuilder/sentinel-agent-security)
[![Live Demo](https://img.shields.io/badge/demo-sentinelapp--delta.vercel.app-10B981?style=flat-square&logo=vercel&logoColor=white)](https://sentinelapp-delta.vercel.app)

</div>

Sentinel checks a payment agent's claims against ground truth before the action executes. Independent investigator agents run in parallel, a deterministic policy gate — not a model — makes the block/allow call, and confirmed attacks generate new Python scoring rules that are validated and hot-deployed.

<table><tbody>
<tr><td width="22%"><b>Learning loop</b></td><td>Generated scoring functions gated by AST parse, attack/clean regression checks, and a forbidden-token scan before hot-deploy. RestrictedPython narrows the execution surface but is not a sandbox — the real containment is the regression gate, and I would not ship this against a determined adversary without process isolation</td></tr>
<tr><td width="22%"><b>Concurrency</b></td><td>Python 3.11 <code>asyncio.TaskGroup</code> dispatch for parallel sub-agent investigations with structured cancellation</td></tr>
</tbody></table>

<br/>

**Also shipped**

<table><tbody>
<tr><td width="22%"><b><a href="https://github.com/stevenybuilder/guardia">Guardia</a></b></td><td>Deployment-risk analysis as a native IntelliJ plugin — deterministic Kotlin risk baseline with a bounded LLM override grounded in cited Datadog incidents; PSI, Git4Idea diff extraction, BM25 + reciprocal-rank fusion retrieval</td></tr>
<tr><td width="22%"><b><a href="https://github.com/stevenybuilder/ai-meeting-autopilot">AI Meeting Autopilot</a></b></td><td><a href="https://meeting-agent-ynzg64zhoa-uc.a.run.app/">Live</a> · realtime meeting agent: browser PCM at 16kHz over WebSockets, streaming STT with proactive reconnect, commitment extraction, async action fanout to Slack/Calendar/Gmail/BigQuery</td></tr>
<tr><td width="22%"><b><a href="https://github.com/stevenybuilder/together-presence-agent">Together</a></b></td><td>Bidirectional live speech translation with vision scene narration, then storybook and memory-video generation from call moments; FastAPI/WebSocket rooms with session affinity on Cloud Run</td></tr>
</tbody></table>

<br/>

## What I Look For

- **New model, no product yet.** Neuro-JEPA shipped in 2026 as a 3D brain-MRI extension of V-JEPA 2, benchmarked by its authors across 47 downstream tasks. Strong task-level benchmarks still leave open which of those gains survive site and acquisition confounds on a cohort the model has not seen — that gap is where the product was.
- **The eval is the deliverable.** If I cannot design the measurement that would falsify a capability, I do not think the capability is shippable yet — and I would rather say so than ship it behind a demo.

<br/>

*Hackathons: Claude Life Sciences, with Gladstone Institutes (Jul 2026) · Google DeepMind, Best Use of DigitalOcean (Mar 2026) · Experian Global AI, 1st place (Nov 2025) · AI Valley Robotics, Best Use of Convex (Nov 2025).*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:10B981,50:2563EB,100:0B1220&height=110&section=footer" width="100%" />
