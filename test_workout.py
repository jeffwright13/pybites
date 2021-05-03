import workout


def test_workout_invalid():
    assert workout.get_workout_motd("krebS") == workout.INVALID_DAY
    assert workout.get_workout_motd("") == workout.INVALID_DAY
    assert workout.get_workout_motd("Mondayy") == workout.INVALID_DAY


def test_workout_weekday():
    assert workout.get_workout_motd("mOndAy") == "Go train " + workout.WORKOUT_SCHEDULE["Monday"]
    assert workout.get_workout_motd("FRIDAy") == "Go train " + workout.WORKOUT_SCHEDULE["Friday"]


def test_workout_weekend():
    assert workout.get_workout_motd("Saturday") == workout.CHILL_OUT
