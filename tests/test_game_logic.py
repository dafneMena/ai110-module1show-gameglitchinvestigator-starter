from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_too_high_with_string_secret():
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_with_string_secret():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_winning_guess_with_string_secret():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert "Correct" in message


class TestSecretRangeValidation:
    """Tests for secret number range validation when difficulty changes."""

    def test_easy_difficulty_range(self):
        """Easy difficulty should return range 1-20."""
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

    def test_normal_difficulty_range(self):
        """Normal difficulty should return range 1-100."""
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 100

    def test_hard_difficulty_range(self):
        """Hard difficulty should return range 1-50."""
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 50

    def test_invalid_difficulty_defaults_to_normal(self):
        """Invalid difficulty should default to Normal range (1-100)."""
        low, high = get_range_for_difficulty("InvalidDifficulty")
        assert low == 1
        assert high == 100

    def test_secret_outside_hard_range(self):
        """Secret of 62 should be outside Hard range (1-50)."""
        secret = 62
        low, high = get_range_for_difficulty("Hard")
        is_in_range = low <= secret <= high
        assert not is_in_range, "Secret 62 should be regenerated when switching to Hard"

    def test_secret_at_hard_upper_boundary(self):
        """Secret at 50 (upper boundary) should be in Hard range."""
        secret = 50
        low, high = get_range_for_difficulty("Hard")
        assert low <= secret <= high

    def test_secret_at_hard_lower_boundary(self):
        """Secret at 1 (lower boundary) should be in Hard range."""
        secret = 1
        low, high = get_range_for_difficulty("Hard")
        assert low <= secret <= high

    def test_secret_switching_normal_to_hard_valid(self):
        """Secret 25 valid in Normal (1-100) and Hard (1-50)."""
        secret = 25
        normal_low, normal_high = get_range_for_difficulty("Normal")
        hard_low, hard_high = get_range_for_difficulty("Hard")
        assert normal_low <= secret <= normal_high
        assert hard_low <= secret <= hard_high

    def test_secret_switching_normal_to_hard_invalid(self):
        """Secret 75 valid in Normal but invalid in Hard - needs regeneration."""
        secret = 75
        normal_low, normal_high = get_range_for_difficulty("Normal")
        hard_low, hard_high = get_range_for_difficulty("Hard")
        assert normal_low <= secret <= normal_high  # Valid in Normal
        assert not (hard_low <= secret <= hard_high)  # Invalid in Hard

    def test_secret_switching_hard_to_easy_invalid(self):
        """Secret 25 invalid in Easy range (1-20)."""
        secret = 25
        easy_low, easy_high = get_range_for_difficulty("Easy")
        assert not (easy_low <= secret <= easy_high)

    def test_secret_switching_easy_to_hard_valid(self):
        """Secret 15 in Easy range (1-20) is also in Hard range (1-50)."""
        secret = 15
        easy_low, easy_high = get_range_for_difficulty("Easy")
        hard_low, hard_high = get_range_for_difficulty("Hard")
        assert easy_low <= secret <= easy_high
        assert hard_low <= secret <= hard_high

    def test_secret_at_easy_upper_boundary_invalid_in_hard(self):
        """Secret 20 at Easy boundary should also be in Hard range."""
        secret = 20
        easy_low, easy_high = get_range_for_difficulty("Easy")
        hard_low, hard_high = get_range_for_difficulty("Hard")
        assert easy_low <= secret <= easy_high
        assert hard_low <= secret <= hard_high

    def test_secret_outside_easy_range_from_normal(self):
        """Secret 50 from Normal should be regenerated for Easy (requires < 21)."""
        secret = 50
        easy_low, easy_high = get_range_for_difficulty("Easy")
        assert not (easy_low <= secret <= easy_high)