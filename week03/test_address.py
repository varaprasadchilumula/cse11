from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])