"""Basic tests for the template package.

Overview:
- Purpose: Verify example behavior and error handling.
- Used by: `pytest` via `make test` and CI.
- Adds: Confidence that core functionality works after changes.
- Learn more: https://docs.pytest.org/en/stable/getting-started.html

How to adapt this file to your own function:
1. Import your function at the top of the file.
2. Update one "known values" test with 3-5 concrete input/output examples.
3. Add at least one edge case (for example: empty input, zero, or one).
4. Add at least one invalid-input test using ``pytest.raises``.
5. Keep one regression test per bug you fix in the future.

Additional tutorials:
- Pytest examples: https://docs.pytest.org/en/stable/example/index.html
- Good test structure: https://docs.pytest.org/en/stable/explanation/goodpractices.html
- Python testing intro (Real Python): https://realpython.com/python-testing/
"""

import pytest

from territorial_inequality.example_sunderland import transportation_density

# Check for positive values in length, constituency area, and density variables

def test_length_positive() -> None:
    """Template: replace this with tests for your own function."""
    result = transportation_density("Zambia", "AFR_Infra_Transport_Road")
    
    assert (result["length_km"] >= 0).all()
 
def test_area_positive() -> None:
    """Template: replace this with tests for your own function."""
    result = transportation_density("Zambia", "AFR_Infra_Transport_Road")
    
    assert (result["const_area_km2"] >= 0).all()
    
def test_density_positive() -> None:
    """Template: replace this with tests for your own function."""
    result = transportation_density("Zambia", "AFR_Infra_Transport_Road")
    
    assert (result["density"] >= 0).all()   

    
    

