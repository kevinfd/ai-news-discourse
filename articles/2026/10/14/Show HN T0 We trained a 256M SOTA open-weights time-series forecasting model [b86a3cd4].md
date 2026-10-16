---
id: "b86a3cd450630e30"
title: "Show HN: T0: We trained a 256M SOTA open-weights time-series forecasting model"
url: "https://github.com/theforecastingcompany/tfc-t0"
link: "https://github.com/theforecastingcompany/tfc-t0"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-14T14:51:04Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["LTMeyer"]
language: "en"
summary: "Hi everyone, we are excited to share t0-gamma, the latest model in our t0 family. It is a 256M parameter open-weights foundation model for time series (TSFM). It runs on CPU, GPU or Apple chips. https://huggingface.co/theforecastingcompany/t0-gamma t0 leverages historical data to forecast the likely outcomes over a given horizon. It does so zero-shot. It works on almost any time series, as it…"
tags: []
orgs: ["Apple"]
topics: ["models & research", "chips & infrastructure", "health & science"]
content_source: "fulltext"
word_count: 1098
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50088582"
score: 14
comments: 0
community: "Hacker News"
---

# Show HN: T0: We trained a 256M SOTA open-weights time-series forecasting model

GitHub · LTMeyer · 2026-10-14

This repository contains the code to run t0, an open-weights time-series forecasting foundation model from The Forecasting Company that produces probabilistic forecasts using historical and known-future covariates.
t0 forecasting French national electricity demand in Retrocast. Data:
Enedis open data.
t0 can use past and known-future covariates to improve its forecasts:
Data: Medic'AM, monthly drug reimbursements from the French national health insurance.
For a complete worked example, the European day-ahead electricity prices notebook forecasts hourly prices in four bidding zones with load, renewable, holiday and weather covariates, and backtests the result.
pip install "tfc-t0[torch]>=0.6.0"
t0-gamma declares the conventions it was trained under in config.json:
its rotary position-scale layout (xpos_scale_layout) and how cells without an
observation are scaled (scaler_zero_no_value). Releases before 0.6.0 do not
read those fields: they load these weights without error and run them under
other conventions, which silently degrades the forecast. Pin the floor.
The simplest path is a univariate forecast through predict:
import torch
from t0 import T0Forecaster
model = T0Forecaster.from_pretrained("theforecastingcompany/t0-gamma").eval()
context = torch.randn(4, 512)  # 4 series, 512 past timesteps
out = model.predict(context, horizon=64, quantile_levels=[0.1, 0.5, 0.9])
out.quantiles  # (4, 64, 3)
out.median     # (4, 64)
predict accepts numpy arrays. 1-D contexts are auto-promoted to a
single-row batch. NaN in the context is read as a missing observation. To
say that some cells are padding instead, pass a mask. See
batched inference.
t0-alpha, t0-beta and t0-gamma are public and download without authentication.
Four optional predict settings produce t0-gamma's published scores. Each
uses only the series' own history:
- trim_leading_missing: ignore missing values before the first observation;
- symmetric_averaging: average the forecast with the mirrored forecast of the negated
series (two forward passes; skipped when the history's minimum is exactly zero);
- clip_nonnegative: clip at zero when the history is non-negative;
- snap_integers: round when the history is integer-valued.
out = model.predict(
    context,
    horizon=64,
    quantile_levels=[0.1, 0.5, 0.9],
    trim_leading_missing=True,
    symmetric_averaging=True,
    clip_nonnegative=True,
    snap_integers=True,
)
Anything you know over the past goes in context — alongside the
target, extra variates attend to it and are forecast together. Anything
you know over the future (calendar features, planned promotions,
weather forecasts) goes in future_covariates, shaped
[B, F, context + horizon]. The model conditions on it but does not
forecast it.
import torch
from t0 import T0Forecaster
model = T0Forecaster.from_pretrained("theforecastingcompany/t0-gamma").eval()
context = torch.randn(2, 512)                    # 2 series, 512 past timesteps
future_covariates = torch.randn(2, 3, 512 + 64)  # 3 covariates known over context + horizon
out = model.predict(
    context,
    horizon=64,
    quantile_levels=[0.1, 0.5, 0.9],
    future_covariates=future_covariates,
)
out.quantiles  # (2, 64, 3)
out.median     # (2, 64)import numpy as np
from t0 import T0Forecaster, batch_series
model = T0Forecaster.from_pretrained("theforecastingcompany/t0-gamma").eval()
daily = np.random.randn(180)    # one series, 180 past timesteps
store = np.random.randn(2, 96)  # one series of 2 variates, 96 past timesteps
hourly = np.random.randn(1024)  # one series, 1024 past timesteps
context, mask, group_ids = batch_series([daily, store, hourly])
context.shape  # (4, 1024) — variates stacked, right-aligned to the longest
group_ids      # [0, 1, 1, 2] — `store`'s two variates are forecast jointly
out = model.predict(
    context,
    horizon=24,
    quantile_levels=[0.1, 0.5, 0.9],
    mask=mask,
    group_ids=group_ids,
)
out.quantiles  # (4, 24, 3)
out.median[0]  # the 24-step median forecast for `daily`
Integrations that prepare complete T0 inputs, including known-future covariates, can batch the native representation directly:
from t0 import TimeSeries
first = TimeSeries.from_array(context_1, future_covariates_1)
second = TimeSeries.from_array(context_2, future_covariates_2)
batch = TimeSeries.batch([first, second])
out = model.predict(
    batch,
    horizon=64,
    context_length=max(context_1.shape[-1], context_2.shape[-1]),
)
Here each context includes its batch axis, for example [1, V, T], and each
known-future input is [1, F, T + horizon]. The output is ordered by the
flattened target rows in batch.
TimeSeries is the model's native input. It holds target rows, known-future
covariate rows, a mask and group ids, all on one width. predict builds one for
you from a raw array. You only need to construct one yourself to batch inputs of
different widths, or to call forward directly.
from t0 import TimeSeries
# context only, with `horizon` marking the region to predict
model_input = TimeSeries.from_array(context, horizon=24)          # context: [B, V, T]
# with known-future covariates, whose width sets the horizon
model_input = TimeSeries.from_array(context, future_covariates)   # covariates: [B, F, T + 24]
out = model.predict(model_input, horizon=24, quantile_levels=[0.1, 0.5, 0.9])
predict infers context_length from where the forecast region starts. Pass it
explicitly when batching series of different widths. forward takes the same
TimeSeries and runs a single differentiable pass over it, with no rollout. That
is the entry point for fine-tuning.
For efficient inference at scale, look at Retrocast.
Model family: t0-gamma (PyTorch/MLX) · t0-beta · t0-alpha · Collection
The tfc-t0 package provides PyTorch and MLX runtimes as separate extras.
ONNX artifacts and our managed API cover other deployment targets:
The ONNX artifacts are built from t0-alpha; there is no t0-beta or
t0-gamma ONNX export yet.
You can also use t0 on Retrocast to forecast on your own data and compare open-weight models.
t0.mlx is a first-party, inference-only runtime built on
MLX. It needs Apple silicon, macOS 14 or
newer, and a native arm64 Python 3.10 or newer, and it does not install
PyTorch:
pip install "tfc-t0[mlx]>=0.6.0"
It loads the same checkpoints as the PyTorch runtime. MLX uses the Apple GPU
automatically; there is no device selection or .to("mps") step. predict
takes NumPy or MLX arrays:
import numpy as np
from t0.mlx import T0Forecaster
model = T0Forecaster.from_pretrained("theforecastingcompany/t0-alpha").eval()
context = np.random.randn(4, 512).astype(np.float32)  # 4 series, 512 past timesteps
out = model.predict(context, horizon=64, quantile_levels=[0.1, 0.5, 0.9])
out.quantiles.shape  # (4, 64, 3)
out.median.shape     # (4, 64)
t0 is a decoder-style patch transformer that alternates time and
covariate attention layers. It decodes multiple horizons in parallel — up
to 1024 timesteps in one forward pass — and falls back on autoregressive
rollout for longer horizons. Quantile levels between the trained ones are
interpolated, and levels beyond them extrapolated on exponential tails.
t0 builds on ideas — and in places, code — from open-source forecasting
models. We gratefully acknowledge:
- Toto by Datadog (repo) & Chronos-2 by Amazon (repo) — factorizing attention in the time and variates dimension.
- TiRex by NXAI (repo) — contiguous patch masking.
- rotary-embedding-torch by Phil Wang (repo) — rotary position embeddings, used by the PyTorch runtime and followed by the MLX one.
Code-level attributions are listed in NOTICE, under their
respective open-source licenses.
If our model is useful, please cite our paper and star our repo!
@article{meyer2026t0,
  title   = {$t_0$: A Time-Series Foundation Model for Forecasting with Context},
  author  = {Meyer, Lucas and Sole, Claudio and Xiang, Huikan and Li, Nicolas and Franceschino, Lucas and Quera-Bofarull, Arnau and Scholl, Maarten P. and Fainberg, Joachim and N{\'e}giar, Geoffrey},
  journal = {arXiv preprint arXiv:2609.24559},
  year    = {2026},
  url     = {https://arxiv.org/abs/2609.24559},
}
