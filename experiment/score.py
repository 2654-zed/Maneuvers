#!/usr/bin/env python3
"""Scores a generation's pre-registered predictions and computes the automatable
metrics defined in experiment/PROTOCOL.md section 5.

Usage:
  python3 experiment/score.py G0            # score G0 from predictions/G0.json (+ ledger if present)
  python3 experiment/score.py G1 --resolve  # interactive: enter outcomes for G1 predictions, then score

Outputs experiment/metrics/<gen>.json. Fields the script cannot compute from repo
files are left as null with a "how_to_measure" note so the auditor fills them in
BEFORE writing narrative (PROTOCOL.md section 5.3).
"""
import json, os, sys, glob, re, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(ROOT, "experiment")

def load(p):
    with open(p) as f:
        return json.load(f)

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def score_predictions(pred):
    items = pred["predictions"]
    resolved = [x for x in items if x.get("outcome_value") is not None]
    unresolved = [x for x in items if x.get("outcome_value") is None]
    nonfals = [x for x in items if "NON-FALSIFIABLE" in str(x.get("outcome", ""))]
    has_p = [x for x in resolved if x.get("p") is not None]
    out = {
        "n_total": len(items),
        "n_resolved": len(resolved),
        "n_unresolved_or_nonfalsifiable": len(unresolved),
        "n_nonfalsifiable": len(nonfals),
        "hit_rate": (sum(float(x["outcome_value"]) for x in resolved) / len(resolved)) if resolved else None,
        "n_with_probabilities": len([x for x in items if x.get("p") is not None]),
        "brier": None,
        "calibration_bins": None,
        "p_distribution": None,
    }
    ps = [x["p"] for x in items if x.get("p") is not None]
    if ps:
        bins = {"<0.3": 0, "0.3-0.7": 0, ">0.7": 0}
        for p in ps:
            bins["<0.3" if p < 0.3 else ("0.3-0.7" if p <= 0.7 else ">0.7")] += 1
        out["p_distribution"] = bins
        out["anti_gaming_rule_met"] = bins["0.3-0.7"] >= 5
    if has_p:
        out["brier"] = sum((x["p"] - float(x["outcome_value"])) ** 2 for x in has_p) / len(has_p)
        # reliability by bin
        cal = {}
        for x in has_p:
            b = "<0.3" if x["p"] < 0.3 else ("0.3-0.7" if x["p"] <= 0.7 else ">0.7")
            cal.setdefault(b, []).append((x["p"], float(x["outcome_value"])))
        out["calibration_bins"] = {b: {"n": len(v), "mean_p": sum(p for p, _ in v) / len(v), "mean_outcome": sum(o for _, o in v) / len(v)} for b, v in cal.items()}
    return out

def ledger_metrics(gen):
    """Overclaim rate and claim-type mix from the successor's claim ledger, if it exists."""
    # Convention: the ledger that audits generation G<n> lives at reports/claim_ledger.json for n=0;
    # later audits should store theirs at experiment/runs/G<n+1>/main/claim_ledger.json as well.
    candidates = {
        "G0": [os.path.join(ROOT, "reports", "claim_ledger.json")],
    }.get(gen, []) + glob.glob(os.path.join(EXP, "runs", "*", "main", f"claim_ledger_{gen}.json"))
    for c in candidates:
        if os.path.exists(c):
            d = load(c)
            claims = d["claims"]
            n = len(claims)
            over = sum(1 for x in claims if x.get("original_stronger_than_evidence"))
            tested = sum(1 for x in claims if x.get("later_evidence_tests_claim"))
            def has(s, k): return k in str(s.get("status", "")).upper()
            status = {
                "still_supported": sum(1 for x in claims if has(x, "STILL SUPPORTED") and not has(x, "DISCONFIRMED")),
                "partially": sum(1 for x in claims if has(x, "PARTIALLY")),
                "disconfirmed": sum(1 for x in claims if has(x, "DISCONFIRMED")),
                "overstated": sum(1 for x in claims if has(x, "OVERSTATED")),
                "under_specified": sum(1 for x in claims if has(x, "UNDER-SPECIFIED")),
                "untestable": sum(1 for x in claims if has(x, "UNTESTABLE")),
                "not_found": sum(1 for x in claims if has(x, "NOT FOUND")),
                "non_falsifiable": sum(1 for x in claims if has(x, "NON-FALSIFIABLE")),
            }
            return {"ledger_file": os.path.relpath(c, ROOT), "n_claims": n, "overclaim_rate": over / n if n else None,
                    "share_tested_by_later_evidence": tested / n if n else None, "status_counts": status}
    return None

def volume_metrics(gen):
    """Bytes of framework + audit prose per ledger claim (PROTOCOL 5.2c). Paths by convention."""
    paths = {
        "G0": [os.path.join(ROOT, p) for p in ["POTENTIAL_ATTACKS_V1_ARCHIVE.md", "POTENTIAL_ATTACKS_V2.md", "POTENTIAL_ATTACKS_V3.md", "docs/lexicon.md", "CORRECTIONS.md"]] + glob.glob(os.path.join(ROOT, "reports", "extraction_event_*.md")) + [os.path.join(ROOT, "reports", p) for p in ["case_CE5E_drainer_operation.md", "kelp_retrospective_replay.md", "cross_chain_import_candidates.md", "advisor_parasite_candidates.md"]],
        "G1": glob.glob(os.path.join(ROOT, "V4", "*.md")) + [os.path.join(ROOT, "reports", p) for p in ["historical_reconstruction.md", "claim_ledger.md", "temporal_audit.md", "prediction_audit.md", "framework_failure_analysis.md", "model_comparison.md", "final_assessment.md"]],
    }.get(gen, [])
    total = sum(os.path.getsize(p) for p in paths if os.path.exists(p))
    return {"framework_and_audit_bytes": total, "files": [os.path.relpath(p, ROOT) for p in paths if os.path.exists(p)]}

def category_metrics(gen):
    if gen == "G0":
        return {"categories": 14, "candidates": 1, "note": "Attacks 1-14 + candidate 15 (V3); lexicon patterns/typologies not counted"}
    if gen == "G1":
        s = open(os.path.join(ROOT, "V4", "MANEUVERS.md")).read()
        idx = s.split("## Index")[1].split("Removed from")[0]
        st = re.findall(r"\| (OBSERVED|STRONGLY INFERRED|HYPOTHESIZED(?: \(downgraded\))?|THEORETICAL) \|", idx)
        return {"categories": len(st), "by_status": {k: st.count(k) for k in set(st)}, "added_vs_predecessor": 5, "removed_vs_predecessor": 6, "broadened": 4, "note": "counts from V4/CHANGELOG_FROM_V3.md"}
    return None

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    gen = sys.argv[1]
    pfile = os.path.join(EXP, "predictions", f"{gen}.json")
    pred = load(pfile)
    if "--resolve" in sys.argv:
        for x in pred["predictions"]:
            if x.get("outcome_value") is None:
                print(f"\n{x['id']}: {x['statement']}\n  confirmed_if: {x.get('confirmed_if')}\n  falsified_if: {x.get('falsified_if')}\n  resolution_date: {x.get('resolution_date')}")
                v = input("  outcome [1=confirmed, 0=falsified, 0.5=partial, blank=unresolved]: ").strip()
                if v:
                    x["outcome_value"] = float(v)
                    x["outcome"] = input("  outcome note: ").strip()
                    x["resolved_by"] = input("  resolved by (generation/model): ").strip()
        with open(pfile, "w") as f:
            json.dump(pred, f, indent=2)
    metrics = {
        "generation": gen,
        "scored_at": None,
        "predictions_file": os.path.relpath(pfile, ROOT),
        "predictions_sha256": sha256(pfile),
        "forward_looking": {
            "a_prediction_score": score_predictions(pred),
            "b_claim_survival": {"value": None, "how_to_measure": "share of this generation's claims still SUPPORTED/PARTIALLY at the audit two generations later; fill after G(n+2)"},
            "c_overclaim": ledger_metrics(gen),
            "d_retraction_propagation": {"value": None, "how_to_measure": "of claims this generation retired, share still cited live in its own later files (grep)"},
            "e_evidence_reproducibility": {"value": None, "how_to_measure": "share of Tier-A/OBSERVED claims the next auditor reproduced from primary sources"},
            "f_mechanism_embargo": {"asserted_before_postmortem": None, "later_contradicted": None},
            "g_citation_locatability": {"located": None, "not_found": None},
            "h_base_rates_measured": {"count": None, "how_to_measure": "number of detection signals with a measured benign-population rate in the framework text"},
            "i_calibration": "see a_prediction_score.calibration_bins (needs >= 20 resolved probabilistic predictions)",
        },
        "backward_looking": {
            "a_descriptive_coverage": {"value": None, "how_to_measure": "share of window incidents >= $1M mapping to an existing category without creating a new one"},
            "b_categories": category_metrics(gen),
            "c_volume": volume_metrics(gen),
            "d_hindsight_ratio": {"self_reported": None, "re_rated_by_next_generation": None},
        },
    }
    lm = metrics["forward_looking"]["c_overclaim"]
    if lm and metrics["backward_looking"]["c_volume"]["framework_and_audit_bytes"]:
        metrics["backward_looking"]["c_volume"]["bytes_per_ledger_claim"] = metrics["backward_looking"]["c_volume"]["framework_and_audit_bytes"] / lm["n_claims"]
    os.makedirs(os.path.join(EXP, "metrics"), exist_ok=True)
    out = os.path.join(EXP, "metrics", f"{gen}.json")
    existing = load(out) if os.path.exists(out) else {}
    # preserve manually filled fields
    def merge(a, b):
        for k, v in b.items():
            if isinstance(v, dict) and isinstance(a.get(k), dict):
                merge(a[k], v)
            elif a.get(k) is None:
                a[k] = v
        return a
    merged = merge(metrics, existing) if existing else metrics
    with open(out, "w") as f:
        json.dump(merged, f, indent=2)
    print(json.dumps(merged["forward_looking"]["a_prediction_score"], indent=2))
    print("wrote", os.path.relpath(out, ROOT))

if __name__ == "__main__":
    main()
