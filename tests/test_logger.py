from format_anki_notes.logger import get_logger

def test_get_logger_with_error(mocker):
    mocker.patch('os.makedirs', side_effect=PermissionError)
    logger = get_logger()
    assert len(logger.handlers) == 1  # Doit tomber sur le handler de secours (StreamHandler)
