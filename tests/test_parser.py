# 🚀 Unit Test for Parser

from Alpha_Modular_Autopilot.brain_module.parser import parse_input

def test_parse_input():
    result = parse_input("Distribusi promo ke facebook dan instagram")
    assert result["intent"] == "distribute_content"
    assert "facebook" in result["platforms"]
    assert "promo" in result["categories"]