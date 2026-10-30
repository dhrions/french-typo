# TODO

Backlog technique du dépôt (voir `conventions-suivi-taches.adoc` de `repos-meta` pour la distinction avec `ROADMAP.md`). Issu de la full-review du 2026-07-27, traité intégralement le 2026-07-27.

## Notes de suivi (hors items d'origine, découverts pendant le traitement)

- `tests/conftest.py` créé : stub léger du module `aqt` (absent de pip, propre au dev Anki) pour que la suite se collecte et s'exécute en CI sans dépendance lourde. `pytest-mock` ajouté à l'extra `dev` (requis par les tests réécrits, absent jusqu'ici).
- README.adoc : la section « Profils disponibles » documentait une API `format_text(text, profile=TypoProfile.ANKI)` inexistante (aucune trace dans le code réel) — retirée, remplacée par l'exemple correct (`add_nbsp_enabled=`).
- Suite de tests vérifiée verte (53 tests) dans deux environnements : avec le vrai Anki installé (`env/` local) et sans (stub `aqt` de CI).

## 📝 Documentation

- [ ] README.adoc : l'en-tête (`Version 1.0.0, 27/07/2026`) et le badge `version-1.0.0` sont figés alors que le paquet en est à `1.6.1` (`pyproject.toml`, PyPI) — les retirer ou les faire suivre par semantic-release (repéré le 2026-10-30, migration des TL;DR)
