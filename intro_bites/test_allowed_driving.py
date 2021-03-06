from allowed_driving import allowed_driving

def test_not_allowed_to_drive1(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'


def test_allowed_to_drive1(capfd):
    allowed_driving('bob', 18)
    output = capfd.readouterr()[0].strip()
    print(output, type(output))
    assert output == 'bob is allowed to drive'


def test_allowed_to_drive_other_name1(capfd):
    allowed_driving('julian', 19)
    output = capfd.readouterr()[0].strip()
    assert output == 'julian is allowed to drive'
