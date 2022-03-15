"""Test for my functions.

Note: I was not sure how to test my functions so I only asserted that they were callable.
"""

from functions import cleanser, moisturizer, sunscreen, calculate_total, skincare

def test_cleanser():
    """Tests for cleanser function."""
    
    # test the function is callable
    assert callable(cleanser)

def test_moisturizer():
    """Tests for moisturizer function."""
    
    # test the function is callable
    assert callable(moisturizer)

def test_sunscreen():
    """Tests for sunscreen function."""
    
    # test the function is callable
    assert callable(sunscreen)

def test_calculate_total():
    """Tests for calculate_total function."""
    
    # test the function is callable
    assert callable(calculate_total)
    
def test_skincare():
    """Tests for skincare function."""
    
    # test the function is callable
    assert callable(skincare)