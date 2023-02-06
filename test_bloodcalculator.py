import pytest

#decorator
@pytest.mark.parametrize("HDL_input, expected", 
[(65, "Normal"), 
(45, "Borderline Low"), 
(20, "Low")])

def test_HDL_analysis(HDL_input, expected):
    from bloodcalculator import HDL_analysis
    # Arrange
    #HDL_input = 65
    #expected = "Normal"
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected

@pytest.mark.parametrize("LDL_input, expected", 
[(65, "Normal"), 
(140, "Borderline High"), 
(169, "High"),
(190, "Very High")])

def test_LDL_analysis(LDL_input, expected):
    from bloodcalculator import LDL_analysis
    # Arrange
    #HDL_input = 65
    #expected = "Normal"
    # Act
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected
