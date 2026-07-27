import logging

import format_anki_notes.logger as logger_module
from format_anki_notes.logger import get_logger


def _reset_logger():
    logger_module._LOGGER = None
    logging.getLogger("FormatAnkiNotes").handlers.clear()


def test_get_logger_falls_back_to_stream_handler_when_mw_unavailable(mocker):
    _reset_logger()
    mocker.patch.object(logger_module, "mw", None)

    logger = get_logger()

    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_get_logger_uses_file_handler_when_mw_available(mocker, tmp_path):
    _reset_logger()
    mock_mw = mocker.MagicMock()
    mock_mw.pm.profileFolder.return_value = str(tmp_path)
    mocker.patch.object(logger_module, "mw", mock_mw)

    logger = get_logger()

    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.FileHandler)
    assert (tmp_path / "addons" / "format_anki_notes_logs").is_dir()


def test_get_logger_with_error_falls_back_to_stream_handler(mocker, tmp_path):
    _reset_logger()
    mock_mw = mocker.MagicMock()
    mock_mw.pm.profileFolder.return_value = str(tmp_path)
    mocker.patch.object(logger_module, "mw", mock_mw)
    mocker.patch.object(logger_module.os, "makedirs", side_effect=PermissionError)

    logger = get_logger()

    assert len(logger.handlers) == 1  # tombe sur le handler de secours (StreamHandler)
    assert isinstance(logger.handlers[0], logging.StreamHandler)
