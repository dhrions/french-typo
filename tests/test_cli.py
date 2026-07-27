from click.testing import CliRunner

from french_typo.cli import fix


def test_version_option():
    runner = CliRunner()
    result = runner.invoke(fix, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output


def test_fix_on_single_adoc_file(tmp_path):
    adoc_file = tmp_path / "sample.adoc"
    adoc_file.write_text("Voir 10 KM.\n", encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(fix, [str(adoc_file)])

    assert result.exit_code == 0
    assert adoc_file.read_text(encoding="utf-8") == "Voir 10 km.\n"


def test_fix_on_directory_processes_all_adoc_files(tmp_path):
    (tmp_path / "a.adoc").write_text("10 KM\n", encoding="utf-8")
    (tmp_path / "b.adoc").write_text("20 KG\n", encoding="utf-8")
    (tmp_path / "ignored.txt").write_text("30 KM\n", encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(fix, [str(tmp_path)])

    assert result.exit_code == 0
    assert (tmp_path / "a.adoc").read_text(encoding="utf-8") == "10 km\n"
    assert (tmp_path / "b.adoc").read_text(encoding="utf-8") == "20 kg\n"
    assert (tmp_path / "ignored.txt").read_text(encoding="utf-8") == "30 KM\n"


def test_fix_rejects_non_adoc_file(tmp_path):
    txt_file = tmp_path / "sample.txt"
    txt_file.write_text("contenu", encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(fix, [str(txt_file)])

    assert result.exit_code != 0
    assert "❌" in result.output
    assert "Chemin invalide" in result.output
