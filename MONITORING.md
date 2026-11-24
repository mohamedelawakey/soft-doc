# Usage and Cost Monitoring

This report shows model requests recorded by `scripts/monitor_usage.py`. The append-only `monitoring/usage.jsonl` file is the history. Each agent can submit one normalized JSON event after a provider returns usage data. The agent or integration must supply that data; this script cannot inspect another agent's private session or provider bill.

## Record a request

Run `python3 scripts/monitor_usage.py record event.json` from the project root, or pipe the same JSON to `record`. Use one stable `task_id` for all model calls belonging to a user request, and a distinct `request_id` for each provider call. The same provider and request ID cannot be recorded twice.

```json
{
  "timestamp": "2026-11-23T12:00:00+02:00",
  "task_id": "TASK-001",
  "request_id": "example-request-001",
  "agent": "example-agent",
  "provider": "example-provider",
  "model": "example-model",
  "usage_source": "provider response usage field",
  "tokens": {"input": 1000, "cached_input": 200, "cache_write": 0, "output": 300},
  "pricing": {
    "currency": "USD",
    "effective_date": "2026-11-23",
    "source": "provider pricing page URL or contract reference",
    "per_million": {"input": "1.00", "cached_input": "0.10", "cache_write": null, "output": "2.00"}
  }
}
```

The four token buckets are **mutually exclusive**. `input` means uncached input; subtract cached tokens from a provider's inclusive input count before recording. Use `cache_write` only when the provider reports it separately. The example numbers and rates above are illustrative, not a claim about any provider's current prices. Record rates as decimal strings per million tokens. Set an unused bucket to `0`; a required but unavailable rate is `null`. If usage or pricing is unavailable, set `tokens` or `pricing` to `null`; the cost remains `Unknown`. Keep the provider's raw response outside this ledger if it includes prompts or other sensitive data.

The script stores the rate snapshot and calculates an **estimate**, not the final bill. Other charges, discounts, taxes, subscription fees, and tool fees are outside this token calculation. Verify rates against the provider and reconcile billing separately. Never infer token counts from text length or assume an agent exposes them. Run `python3 scripts/monitor_usage.py report` to rebuild this view from the JSONL history.

Keep personal usage data private. The generated ledger is ignored by Git; this Markdown report is tracked only if you choose to commit it.

## Request history

<!-- usage-report:start -->

Recorded requests: 0. Estimated totals: None. Requests with unknown cost: 0.

### By task

| Task | Requests | Estimated cost | Unknown costs |
| --- | ---: | ---: | ---: |

### By model request

| Date | Task | Request | Agent | Provider / model | Input | Cached | Cache write | Output | Estimated cost |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |

<!-- usage-report:end -->
