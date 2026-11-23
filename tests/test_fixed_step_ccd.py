import pytest
import gameplay.fixed_step_ccd as mod

CASES = [
    ("accumulate", (1)),
    ("sub_step", (1)),
    ("ccd_sweep", (1)),
    ("reentry_guard", (1)),
    ("wake_cache", (1)),
    ("integrate_order", (1)),
    ("contact_refresh", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("clamp_dt", (1)),
    ("metrics", (1)),
    ("replay", (1)),
    ("sleep_state", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
