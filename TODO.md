# TODO

Backlog technique du dépôt (voir `conventions-suivi-taches.adoc` de `repos-meta` pour la distinction avec `ROADMAP.md`). Issu de la full-review du 2026-07-27, traité intégralement le 2026-07-27.

## CI / Release

- [x] Corriger `commit_parser = "angular"` alors que l'historique utilise gitmoji — piège causant des releases vertes sans tag (pyproject.toml:24)
- [x] Gater le job `release` par `needs: test` — actuellement aucune dépendance aux tests avant publication PyPI (.github/workflows/release.yml:8-13)
- [x] Ajouter une borne `python-semantic-release>=9,<10` dans le workflow (`pip install python-semantic-release build` est non bornée) (.github/workflows/release.yml:20,24)
- [x] Déclarer `python-semantic-release` comme dev dependency dans `pyproject.toml` (installé à la volée dans le workflow uniquement, non versionné) (pyproject.toml)
- [x] Ajouter `version_variables` dans `[tool.semantic_release]` pour synchroniser `pyproject.toml`/`__init__.py` (pyproject.toml)
- [x] Ajouter `commit_parser_options` pour mapper les emojis (💥/✨/🐛…) sur les niveaux de bump (pyproject.toml)
- [x] Configurer `commit_message` avec `[skip ci]` en semantic-release (pyproject.toml)
- [x] Ajouter une option `--version` au CLI et un `__version__` dans le package (french_typo/cli.py:6-13, french_typo/__init__.py)
- [x] Ajouter le préfixe `❌` aux messages d'erreur CLI (french_typo/cli.py:25)
- [x] Vérifier si les workflows en `.github/workflows/` (plutôt que `.gitea/workflows/`) sont justifiés par le besoin d'OIDC GitHub pour la publication PyPI trusted publishing, sinon aligner sur la doctrine Gitea du parc (.github/workflows/release.yml:1) — vérifié : justifié, `CLI_STANDARDS.md` documente ce pattern GitHub Actions pour semantic-release + PyPI trusted publishing, pas de migration

## Dépendances

- [x] Créer `[project.optional-dependencies]` avec un extra `dev` incluant `pytest` — `tests.yml` exécute `pip install -e ".[dev]"` mais cet extra n'existe pas (.github/workflows/tests.yml:22, pyproject.toml)
- [x] Déclarer `pytest` comme dépendance (utilisé via `import pytest` mais absent de toute section de dépendances) (tests/test_formatter.py:2)
- [x] Vérifier l'absence de vulnérabilités connues via `pip-audit` — exécuté, aucune vulnérabilité actionnable sur les dépendances déclarées

## Documentation Antora

- [x] Créer `.repo-meta.json` (dépôt personnel maintenu) — requis par `repo-metadata.adoc` de repos-meta
- [x] Créer la structure Antora minimale : `docs/antora.yml`, `docs/antora-playbook.yml`, `docs/modules/ROOT/nav.adoc`
- [x] Créer les pages du socle obligatoire (archétype 🛠️ Projet applicatif) : `index.adoc` (🏠), `installation.adoc` (🚀), `usage.adoc` (💻)
- [x] Créer les pages conditionnelles justifiées par le contenu réel : `workflows.adoc` (🔄, CI présente) et `semantic-release.adoc` (📦, semantic-release utilisé)
- [x] Mettre à jour la référence du dépôt dans `REPOS_INDEX.md:141` vers la méthode décentralisée `.repo-meta.json` (retirée, commit séparé dans le dépôt repos-meta)

## README

- [x] Mettre à jour la version affichée (`0.2.0` → `1.0.0`) en en-tête et dans le badge, cohérente avec `pyproject.toml` et le tag git `v1.0.0` (README.adoc:3,13)
- [x] Corriger la ligne de révision au format canon « Version X.Y.Z, DD/MM/YYYY » (README.adoc:3)
- [x] Ajouter un bloc `⚡ TL;DR` juste après les badges (README.adoc)
- [x] Ajouter un émoji à chaque titre de section (Introduction, Fonctionnalités, Installation, Utilisation, Intégrations, Architecture du projet, Développement, Philosophie du projet, Licence) (README.adoc:18,38,49,60,109,134,149,172,181)
- [x] Ajouter un émoji en tête de chaque élément des listes à puces (README.adoc:25-29,31-34,78-80,116-118,128-130,174-177)
- [x] Remplacer l'émoji `✔️` par `✅` (pool canon de la catégorie Fonctionnalités) (README.adoc:40-45)

## Conception / Code

- [x] Factoriser la boucle dupliquée entre `format_current_note` et `format_selected_notes_in_browser` en un helper commun (format_anki_notes/editor/format.py:19-28, format_anki_notes/browser/format.py:44-50) — `format_anki_notes/format_note.py`
- [x] Supprimer l'import mort `TypoProfile` (french_typo/core/formatter.py:1) — le module `core/profiles.py` était lui-même orphelin (aucun importeur), supprimé entièrement
- [x] Supprimer l'import mort `mw` (format_anki_notes/editor/button.py:2)
- [x] Séparer la logique métier et l'I/O dans `format_asciidoc_file` pour la rendre testable indépendamment (french_typo/adapters/asciidoc/formatter.py:12-97) — extraction de `_format_lines()`
- [x] Factoriser `normalize_km`/`normalize_kg` via une table `{unit: variants}` itérée une fois (french_typo/core/rules/units.py:17-23)
- [x] Documenter (ou clarifier) le couplage implicite entre les deux arborescences top-level `format_anki_notes/` (add-on legacy) et `french_typo/` (package publié) (pyproject.toml:15-18) — précisé dans README.adoc, section Architecture

## Tests

- [x] Supprimer ou réactiver les 5 fichiers de test entièrement commentés (browser/format.py, browser/menu.py, editor/button.py, editor/format.py, format_anki_notes.py) — aucune couverture réelle actuellement (tests/format_anki_notes/) — réécrits pour matcher le code actuel (les anciens mocks étaient désynchronisés)
- [x] Créer des tests pour `french_typo/cli.py` (entrypoint packagé `french-typo`), notamment le chemin d'erreur `BadParameter` et le mode répertoire (french_typo/cli.py:24) — `tests/test_cli.py`
- [x] Corriger ou retirer le mock mort `os.makedirs`/`PermissionError` dans `test_get_logger_with_error` (code jamais atteint car `mw` vaut `None` en environnement de test) (tests/test_logger.py:4) — réécrit en 3 tests couvrant les 3 branches réelles
- [x] Compléter `tests/core/test_core_formatter.py` (actuellement vide) pour tester `format_text`, fonction d'assemblage centrale (french_typo/core/formatter.py:11-31)

## Notes de suivi (hors items d'origine, découverts pendant le traitement)

- `tests/conftest.py` créé : stub léger du module `aqt` (absent de pip, propre au dev Anki) pour que la suite se collecte et s'exécute en CI sans dépendance lourde. `pytest-mock` ajouté à l'extra `dev` (requis par les tests réécrits, absent jusqu'ici).
- README.adoc : la section « Profils disponibles » documentait une API `format_text(text, profile=TypoProfile.ANKI)` inexistante (aucune trace dans le code réel) — retirée, remplacée par l'exemple correct (`add_nbsp_enabled=`).
- Suite de tests vérifiée verte (53 tests) dans deux environnements : avec le vrai Anki installé (`env/` local) et sans (stub `aqt` de CI).
