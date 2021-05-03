from slice_and_dice import slice_and_dice

def test_slice_and_dice():
    text1 = """
            So, you se, the thing about
             joes' is that at Joes.
            you eat at Joe's. :-)!
             and navels.!
            """
    assert slice_and_dice(text1) == ["Joe's", ":-)", "navels"]