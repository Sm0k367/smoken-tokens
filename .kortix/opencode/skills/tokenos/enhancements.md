# TokenOS Enhancements

## Usage Metering
- Every MCP call, model inference, and local tool run is metered
- Granular per-agent, per-session, per-project tokens/compute minutes

## Burn Forecasting
- TimesFM integration for zero-shot token burn prediction
- Daily/weekly/monthly projections with confidence intervals

## Budget Guardrails
- Hard and soft limits per workspace
- Auto-pause or human-approval workflows when approaching limits

## Billing Modes
- Token-native (pay with compute credits)
- Fiat via Stripe (kortix-executor)
- Hybrid

## Reporting
- Quarterly "compute P&L" for teams and enterprises
- Exportable CSV + PDF dashboards

**Status**: Core TokenOS skill exists. Full implementation pending MCP + dashboard work.
