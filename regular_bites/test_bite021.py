import bite021


CARS = bite021.CARS


def test_get_all_jeeps():
    assert (
        bite021.get_all_jeeps(CARS) == "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
    )
    assert "Fairlane" not in bite021.get_all_jeeps(CARS)


def test_get_first_model_each_manufacturer():
    assert bite021.get_first_model_each_manufacturer() == [
        "Falcon",
        "Commodore",
        "Maxima",
        "Civic",
        "Grand Cherokee",
    ]


def test_get_all_matching_models():
    assert bite021.get_all_matching_models() == ["Trailblazer", "Trailhawk"]
    assert bite021.get_all_matching_models(grep="F") == [
        "Falcon",
        "Focus",
        "Festiva",
        "Fairlane",
    ]
    assert bite021.get_all_matching_models(grep="z") == ["Trailblazer", "350Z", "Jazz"]
    assert bite021.get_all_matching_models(grep="CO") == [
        "Falcon",
        "Commodore",
        "Accord",
    ]


def test_sort_car_models():
    assert bite021.sort_car_models() == {
        "Ford": ["Fairlane", "Falcon", "Festiva", "Focus"],
        "Holden": ["Barina", "Captiva", "Commodore", "Trailblazer"],
        "Nissan": ["350Z", "Maxima", "Navara", "Pulsar"],
        "Honda": ["Accord", "Civic", "Jazz", "Odyssey"],
        "Jeep": ["Cherokee", "Grand Cherokee", "Trailhawk", "Trackhawk"],
    }
