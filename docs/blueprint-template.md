# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: 2A202600603_LeVanKhoa_Day13
- [REPO_URL]: [vkhoa2110/2A202600603_LeVanKhoa_Day13](https://github.com/vkhoa2110/2A202600603_LeVanKhoa_Day13)
- [MEMBERS]:
  - Member A: Lê Văn Khoa | Student ID: 2A202600603 | Role: Individual lab - all roles

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 62
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: screenshot/evidence_correlation_id_logs.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: screenshot/evidence_pii_redaction_logs.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: screenshot/evidence_trace_waterfall_preview.png
- [TRACE_WATERFALL_EXPLANATION]: The selected Langfuse trace shows a `/chat` request flowing through the agent `run` span. The trace includes user/session context, feature tag, model tag, request input, output, latency, tokens, cost, and quality score. This evidence shows how the request can be debugged from trace metadata and correlated with structured JSON logs through `correlation_id`, `session_id`, and hashed user context.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: screenshot/dashboard_6_panels.png
- [METRICS_ENDPOINT_EVIDENCE]: screenshot/metrics_endpoint_snapshot.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 2651ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.1276 test total |

Dashboard panels required by the lab:
- Latency P50/P95/P99
- Traffic
- Error rate
- Cost over time
- Tokens in/out
- Quality proxy

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: screenshot/alert_rules_with_runbook.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

Configured alert rules:
- `high_latency_p95`: `latency_p95_ms > 5000 for 30m`, severity P2, runbook `docs/alerts.md#1-high-latency-p95`
- `high_error_rate`: `error_rate_pct > 5 for 5m`, severity P1, runbook `docs/alerts.md#2-high-error-rate`
- `cost_budget_spike`: `hourly_cost_usd > 2x_baseline for 15m`, severity P2, runbook `docs/alerts.md#3-cost-budget-spike`

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: After enabling the `rag_slow` incident, the load test showed severe latency regression. Normal requests were around 150ms, while incident requests increased to approximately 9038ms, 15772ms, and 23953ms. This breached the latency SLO target of P95 < 3000ms.
- [ROOT_CAUSE_PROVED_BY]: The `rag_slow` incident toggle was enabled and Langfuse traces showed the agent `run` span becoming slow during affected requests. The related API logs can be correlated with the same request flow using `correlation_id`, `session_id`, and hashed user context in `data/logs.jsonl`.
- [FIX_ACTION]: Disabled the `rag_slow` incident toggle and verified the service returned to normal behavior through `/health`, `/metrics`, structured logs, and subsequent request traces.
- [PREVENTIVE_MEASURE]: Keep a high-latency P95 alert, inspect slow traces by RAG vs LLM span, set timeout/fallback behavior for retrieval, and keep structured JSON logs with correlation IDs for fast incident debugging.

---

## 5. Individual Contributions & Evidence

### Lê Văn Khoa
- [TASKS_COMPLETED]: Completed the individual lab implementation end to end: correlation ID middleware, structured JSON log enrichment, PII scrubbing, Langfuse SDK v3 tracing, trace flushing, configurable load-test base URL, configurable incident-injection base URL, validation evidence, incident debugging, and report preparation.
- [EVIDENCE_LINK]: [GitHub repository](https://github.com/vkhoa2110/2A202600603_LeVanKhoa_Day13)

Code files changed:
- `app/middleware.py`: implemented request correlation ID propagation and response headers.
- `app/main.py`: added log context enrichment and Langfuse trace flush after successful requests.
- `app/logging_config.py`: enabled PII scrubbing in the structlog processor chain.
- `app/pii.py`: extended PII patterns.
- `app/tracing.py`: migrated tracing integration to Langfuse SDK v3.
- `scripts/load_test.py`: added configurable `--base-url`.
- `scripts/inject_incident.py`: added configurable `--base-url`.

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: N/A
- [BONUS_AUDIT_LOGS]: N/A
- [BONUS_CUSTOM_METRIC]: N/A
