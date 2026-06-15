# Evidence Collection Sheet

## Student
- Name: Lê Văn Khoa
- Student ID: 2A202600603
- Repository: [vkhoa2110/2A202600603_LeVanKhoa_Day13](https://github.com/vkhoa2110/2A202600603_LeVanKhoa_Day13)

## Auto-Verification
- Validate logs score: 100/100
- Total traces tracked in Langfuse: 62
- PII leaks found: 0
- Metrics snapshot: `screenshot/metrics_endpoint_snapshot.png`
- Validate logs screenshot: `screenshot/validate_logs_score_100.png`

## Required screenshots
- Langfuse trace list with >= 10 traces: `screenshot/evidence_langfuse_trace_list_ge10.png`
- One full trace waterfall: `screenshot/evidence_trace_waterfall_preview.png`
- JSON logs showing correlation_id: `screenshot/evidence_correlation_id_logs.png`
- Log line with PII redaction: `screenshot/evidence_pii_redaction_logs.png`
- Dashboard with 6 panels: `screenshot/dashboard_6_panels.png`
- Alert rules with runbook link: `screenshot/alert_rules_with_runbook.png`

## Optional screenshots
- Langfuse home trace count overview: `screenshot/langfuse_home_trace_count_overview.png`
- Langfuse trace list page 2: `screenshot/langfuse_trace_list_page_2.png`
- Trace tags and metadata: `screenshot/trace_waterfall_tags_and_metadata.png`

## Incident Evidence
- Scenario: `rag_slow`
- Observed symptom: latency increased from about 150ms to about 9038ms, 15772ms, and 23953ms during load testing.
- Root cause: injected retrieval/RAG latency spike.
- Fix action: disabled `rag_slow` and verified the incident toggle returned to false.
