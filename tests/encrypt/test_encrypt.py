from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("senha", 2) == "ahn_es"
    assert encrypt_message("senha", 3) == "nes_ah"
    assert encrypt_message("senha", 9) == "ahnes"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("senha", "s")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)
