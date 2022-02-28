from utils.header import setup_header


def test_header_contents():
    """
    Check Contents in request header

    """
    header = setup_header()
    
    assert "user-agent" in header

def test_header_value_UA():
    """
    Check 'User Agent' value in request header

    """

    # Expected Value Setting
    HEADER =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    # Actual Value
    header = setup_header()

    # Test
    assert header["user-agent"] == HEADER
    
    
    