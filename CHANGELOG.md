# CHANGELOG


## v1.2.0 (2026-07-27)

### Other

- ✅ test(anki): fiabiliser le point d'entrée format_anki_html
  ([`b218b83`](https://github.com/dhrions/french-typo/commit/b218b83ccea5afe3f69f9857cfa35bd86ab67638))

Troisième volet du jalon roadmap 'source unique des règles typographiques'. format_anki_html() — le
  point d'entrée censé être LE point de composition core + règles Anki — n'avait aucun test :
  impossible de vérifier que l'assemblage (core -> nettoyage core -> règles Anki -> dédoublonnage ->
  nettoyage HTML/cloze) ne produisait pas d'artefact.

Ajouté : - Cas bout-en-bout repris de anki_french_typo/tests/test_formatter.py - Test d'idempotence
  explicite (objectif ROADMAP.md 'Idempotence garantie'), sur guillemets, unités, ordinaux, cloze et
  balises HTML - Test de composition cloze + guillemets + ordinal ensemble

Confronté manuellement aux fixtures de anki-french-typo/tests/ (lecture seule) pour vérifier
  l'équivalence de comportement.

56 tests verts.

- 📚 docs: corriger convention émojis dans nav et pages, ajouter workflow déploiement
  ([`c6677cc`](https://github.com/dhrions/french-typo/commit/c6677cc9ba478df87018baf59004b5dda9e291fe))

- nav.adoc : déplacer émojis à l'intérieur des xref labels (Antora supprime orphelins) — pattern :
  xref:page.adoc[🏠 Label] au lieu de 🏠 xref:... - installation.adoc, usage.adoc, workflows.adoc,
  semantic-release.adoc : ajouter émojis aux titres H2 pour cohérence interne avec README -
  .gitea/workflows/docs.yml : créer le workflow de build + déploiement Antora sur docs.dhrions.fr,
  plus trigger cross-repo de régénération de l'index repos-meta (via REPOS_META_DISPATCH_TOKEN)

- 🔥 refactor: supprimer l'add-on Anki legacy format_anki_notes/
  ([`0d96468`](https://github.com/dhrions/french-typo/commit/0d964681089ebb57504a6c817f2db643135c4811))

Supplanté par le dépôt autonome anki-french-typo, qui consomme french-typo depuis PyPI et fournit
  une UI complète (éditeur, navigateur, réviseur). Le legacy n'avait plus de commit fonctionnel
  depuis le 2026-01-03, soit deux jours avant le premier commit d'anki-french-typo.

Supprimés : - format_anki_notes/ (add-on legacy et ses 10 modules) - tests/format_anki_notes/,
  tests/test_format_anki_notes.py, tests/test_logger.py - tests/conftest.py (stub aqt : plus aucun
  test ne dépend d'Anki) - meta.json (manifeste de l'add-on legacy)

Conservé : french_typo/adapters/anki/, l'adaptateur du moteur, consommé par anki-french-typo.

Le dépôt ne contient plus que le moteur et sa CLI — plus aucune dépendance à aqt, y compris en test.
  36 tests verts.

- 🗺️ docs: ajouter ROADMAP.md et les renvois depuis README et index Antora
  ([`892cf47`](https://github.com/dhrions/french-typo/commit/892cf47f9667440d1d2b79a38465c53637716e5e))

Feuille de route au niveau jalon (charte conventions-suivi-taches.adoc) : positionnement du moteur
  comme source unique des règles, complétion de la typographie française, élargissement des formats,
  extensibilité long terme.

README.adoc et docs/.../index.adoc y renvoient par un lien, sans recopier la feuille de route
  (source unique).

- 🗺️ docs: cocher le jalon 'source unique des règles typographiques'
  ([`3ad70c5`](https://github.com/dhrions/french-typo/commit/3ad70c58e21a8ce7d49a70fe6c14301c0b591b2d))

Atteint côté moteur : catégorie de nettoyage nbsp ajoutée, règles HTML manquantes complétées dans
  l'adaptateur Anki, point d'entrée format_anki_html testé et idempotent. Le moteur ne force plus
  aucun consommateur à réimplémenter ces règles localement — commits 8757b22, 9915112, b218b83.

### ✨

- ✨ feat(anki): compléter les règles HTML-spécifiques manquantes
  ([`9915112`](https://github.com/dhrions/french-typo/commit/991511210697ed55cdd6cda54ff417c4b171f0d2))

Deuxième volet du jalon roadmap 'source unique des règles typographiques'. Deux capacités manquaient
  dans l'adaptateur Anki, forçant une réimplémentation côté add-on (anki_french_typo/rules.py) :

- Ponctuation collée sans espace à une balise fermante (</b>: -> </b>&nbsp;:) — le core ne gère que
  le cas avec espace - Nettoyage des nbsp mal placés après une balise HTML fermante ou après une
  cloze }} — le moteur ne savait qu'ajouter du nbsp, jamais en corriger un mal placé dans ce
  contexte

nbsp_before_punctuation_after_tag, clean_nbsp_after_html_tags et clean_nbsp_after_cloze rejoignent
  format_anki_specific_rules(), dans l'ordre validé par l'add-on (ajout -> dédoublonnage ->
  nettoyage).

tests/adapters/anki/test_rules.py était vide malgré son nom — comblé.

- ✨ feat(core): ajouter une catégorie de règles de nettoyage nbsp
  ([`8757b22`](https://github.com/dhrions/french-typo/commit/8757b22d5bc73ebe2879e448843402e7f318db7a))

Le moteur ne savait qu'ajouter du nbsp (add_nbsp) ou tout supprimer (remove_all_nbsp) — rien pour
  corriger un nbsp mal placé après une virgule ou en début de ligne. C'était l'une des deux lacunes
  empêchant le jalon roadmap 'source unique des règles typographiques' : l'add-on Anki avait dû
  écrire cette catégorie lui-même (anki_french_typo/rules.py).

Ajouté : - french_typo/core/rules/nbsp_cleanup.py : clean_nbsp_after_comma, clean_leading_nbsp -
  Composées dans format_text(), après add_nbsp, sous le même flag add_nbsp_enabled

Corrigé au passage : add_nbsp() sur les guillemets n'était pas idempotent (ré-appliquer le formatage
  doublait le nbsp autour de « »). Ajout des gardes négatives déjà présentes côté add-on.


## v1.1.0 (2026-07-27)

### Other

- Ci: publish to PyPI via trusted publishing on release
  ([`3ed91e5`](https://github.com/dhrions/french-typo/commit/3ed91e5169cdb8ce76bbe5768b11f3754d3b1f06))

- Refactor: dedupe ordinal-suffix nbsp regex between core and anki adapter
  ([`d897eb1`](https://github.com/dhrions/french-typo/commit/d897eb15909b171f4be3150c7c636b883e4cdc8e))

- ♻️ refactor(core,anki): dédupliquer, supprimer le code mort, séparer l'I/O
  ([`8339a1d`](https://github.com/dhrions/french-typo/commit/8339a1daac3f723f552c8fa3e769646c20a39ab0))

- format_anki_notes/format_note.py : factorise la boucle de formatage de champs dupliquée entre
  editor/format.py et browser/format.py - supprime french_typo/core/profiles.py (TypoProfile),
  orphelin : importé nulle part, jamais utilisé par format_text() - supprime l'import mort 'from aqt
  import mw' dans editor/button.py - french_typo/adapters/asciidoc/formatter.py : extrait
  _format_lines(), fonction pure de transformation, de format_asciidoc_file() qui ne gère plus que
  la lecture/écriture fichier - french_typo/core/rules/units.py : factorise
  normalize_km/normalize_kg en une table UNITS itérée par normalize_simple_units()

- ✅ test: réécrire les tests obsolètes, ajouter cli/logger/core_formatter
  ([`b03d77f`](https://github.com/dhrions/french-typo/commit/b03d77fc46ee2527e4a29849de21f5addeca89dd))

- tests/conftest.py : stub léger du module aqt (MagicMock, mw=None comme le vrai module avant init
  Anki) quand l'add-on Anki n'est pas installé, pour que la suite se collecte en CI sans dépendance
  lourde à 'anki'/'aqt' - ajout de pytest-mock (dev extra) requis par les tests utilisant 'mocker' -
  réécriture complète des 5 fichiers de test entièrement commentés (test_browser_format.py,
  test_browser_menu.py, test_editor_button.py, test_editor_format.py, test_format_anki_notes.py),
  désynchronisés du code actuel (messages d'erreur, signatures) : plus de couverture fictive -
  tests/test_cli.py : --version, fichier unique, mode répertoire, chemin invalide (aucun test
  n'existait pour l'entrypoint packagé) - tests/test_logger.py : le mock PermissionError/os.makedirs
  ne pouvait jamais s'exécuter (mw valait None) ; réécrit en 3 tests couvrant StreamHandler (mw
  absent), FileHandler (mw disponible) et le fallback PermissionError réellement atteint -
  tests/core/test_core_formatter.py (vide) : couvre format_text() et le flag add_nbsp_enabled

Suite complète vérifiée verte (53 tests) avec et sans Anki réel installé (env/ local vs stub aqt).

- 💄 docs(readme): mettre à jour la version, ajouter TL;DR et émojis
  ([`462663d`](https://github.com/dhrions/french-typo/commit/462663d10ffe50f843bf4d795f3b13c32e4641c8))

- version 0.2.0 -> 1.0.0 (en-tête, ligne de révision, badge) - ajout du bloc ⚡ TL;DR après les
  badges - émoji sur chaque titre de section et chaque élément de liste - ✔️ -> ✅ (pool canon de la
  charte pour Fonctionnalités) - suppression de la section 'Profils disponibles' : documentait une
  API profile=TypoProfile.* qui n'existe pas dans format_text() (dead code, cf. suppression de
  l'import TypoProfile dans core/formatter.py) - exemple d'usage bibliothèque corrigé pour refléter
  la signature réelle de format_text(text, add_nbsp_enabled=...)

- 📋 Cocher les items traités du TODO.md (full-review 2026-07-27)
  ([`240ee12`](https://github.com/dhrions/french-typo/commit/240ee12373e2444d89daf9c6e2df5a2349b9e2f8))

- 📝 docs(antora): créer la structure de documentation Antora
  ([`abdc085`](https://github.com/dhrions/french-typo/commit/abdc085ea08b5b76e48b06b8cee24ae49ac9162e))

- .repo-meta.json (dépôt personnel maintenu, migration décentralisée) - docs/antora.yml,
  docs/antora-playbook.yml, docs/modules/ROOT/nav.adoc - socle obligatoire (archétype 🛠️ Projet
  applicatif) : index.adoc, installation.adoc, usage.adoc - pages conditionnelles : workflows.adoc,
  semantic-release.adoc

Le contenu usage.adoc corrige au passage un exemple obsolète du README (l'API
  'profile=TypoProfile.ANKI' documentée n'existe plus dans format_text ; TypoProfile n'est utilisé
  par aucun code du dépôt).

### ✨

- ✨ deps(dev): déclarer l'extra dev (pytest, python-semantic-release)
  ([`44d8248`](https://github.com/dhrions/french-typo/commit/44d82487d3292a2a68128fda5e5b48d068308af5))

- pyproject.toml n'exposait aucun extra dev alors que .github/workflows/tests.yml installe déjà 'pip
  install -e ".[dev]"' -> extra inexistant, install en échec - pytest était utilisé
  (tests/test_formatter.py) sans être déclaré nulle part - python-semantic-release borné >=9,<10,
  identique au workflow de release

pip-audit exécuté sur l'environnement du projet : aucune vulnérabilité actionnable sur les
  dépendances déclarées (click reste non borné en haut, les CVE trouvées concernent des versions
  anciennes déjà couvertes par la plage >=8.0 avec résolution vers une version patchée).

### 🐛

- 🐛 fix(release): corriger semantic-release et gater la release par les tests
  ([`4bc122b`](https://github.com/dhrions/french-typo/commit/4bc122b8c1a152f10113b83ccfb5bce89161bc45))

- commit_parser: angular -> emoji (les commits gitmoji n'étaient jamais détectés par le parser
  angular, releases vertes sans tag) - ajout de version_variables, commit_parser_options,
  commit_message [skip ci] - job release gaté par needs: test - python-semantic-release borné à
  >=9,<10 dans le workflow - ajout de __version__ et --version au CLI - préfixe ❌ sur le message
  d'erreur CLI


## v1.0.0 (2026-07-09)

### Other

- 1.0.0
  ([`dcc1c89`](https://github.com/dhrions/french-typo/commit/dcc1c89499e0327c61cea04cdd8ebff49bea623b))

Automatically generated by python-semantic-release

- Ci: add semantic-release configuration [skip ci]
  ([`7582cb1`](https://github.com/dhrions/french-typo/commit/7582cb10c161364e9482b7dfa2faec0a418f59e1))

- Fix: add package __init__.py exporting format_text
  ([`c43c1e8`](https://github.com/dhrions/french-typo/commit/c43c1e86b0924f70c4d384a6fa6ece88d528fc2a))

Le dossier french_typo/ n'avait pas de __init__.py racine : le paquet était donc résolu comme un
  namespace package (sans __file__), et `from french_typo import format_text` échouait avec
  "ImportError: cannot import name 'format_text' from 'french_typo' (unknown location)".

Ajoute le __init__.py racine qui ré-exporte format_text depuis french_typo.core.formatter.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

- 💩 Add code
  ([`07c4e06`](https://github.com/dhrions/french-typo/commit/07c4e06cb252f247147aebc90a52136e555b0fb7))

### ✨

- ✨ Add a rule
  ([`7ec6771`](https://github.com/dhrions/french-typo/commit/7ec677108833bc69a5ce9e31fdbfe7ebb5d8c88b))

- ✨ Add a rule
  ([`8eaaffb`](https://github.com/dhrions/french-typo/commit/8eaaffbca7ee8703592653b6a093cfcb0e1eeab2))

- ✨ Add rule for lists
  ([`b273b75`](https://github.com/dhrions/french-typo/commit/b273b752bbdd97885789405f00d5af0d0b40ddbd))

- ✨ Improve
  ([`e4ffd86`](https://github.com/dhrions/french-typo/commit/e4ffd86e15d060f5a9ad424bc1766c144b24e45e))

- ✨ Improve
  ([`c8a52f7`](https://github.com/dhrions/french-typo/commit/c8a52f708517aaaa665e9fbdc8cbbb8412058aec))

### 🐛

- 🐛 Fix
  ([`30b46a7`](https://github.com/dhrions/french-typo/commit/30b46a7884af5ce8e1ab1f47e6e2837ed1500fa6))


## v0.2.0 (2026-01-03)

### Other

- ✅ Add test
  ([`822b167`](https://github.com/dhrions/french-typo/commit/822b1670296b8c88b1910daca8788e780c0e804e))

- ✅ Add test
  ([`3661f36`](https://github.com/dhrions/french-typo/commit/3661f36ef8ba45d46fcb6828481a67258d2a0e9e))

- ✅ Add test for logger
  ([`338b019`](https://github.com/dhrions/french-typo/commit/338b0195240f724ecc71f2a20d95d7b12c8acaca))

- ✅ Add test for main
  ([`54e4c09`](https://github.com/dhrions/french-typo/commit/54e4c09a1736207a30f03a883c26ea5b8d04e551))

- ✅ Add tests
  ([`3449ac1`](https://github.com/dhrions/french-typo/commit/3449ac193a56e243ff0b852994028f9b9e223dbe))

- ✏️ Fix
  ([`4552889`](https://github.com/dhrions/french-typo/commit/4552889087e893547a534f00d95c0ede99d8048d))

- ✏️ Fix
  ([`0e42fc7`](https://github.com/dhrions/french-typo/commit/0e42fc75efc4ab846df9fb2941485847b10e7147))

- 🎨 Format code
  ([`3921f59`](https://github.com/dhrions/french-typo/commit/3921f597dbc0c3536073a22b43ba0143b84c49d4))

- 🎨 Format module
  ([`31d19b7`](https://github.com/dhrions/french-typo/commit/31d19b7671f5b6e30caf05cbf5a3a3b119bf0429))

- 💡 Improve docstring
  ([`0b06dbc`](https://github.com/dhrions/french-typo/commit/0b06dbc5e1281b15349b74fcebb046d4272894aa))

- 💩 ✅ Add tests to implement correctly
  ([`8ab86d4`](https://github.com/dhrions/french-typo/commit/8ab86d4ebcab2bbd5327e47a0b29669f517705f1))

- 📝 Update doc
  ([`89cb2c1`](https://github.com/dhrions/french-typo/commit/89cb2c12820de23d75cf746744f4a49a7fd9c164))

- 🔥 Remove bad rule
  ([`f84c7df`](https://github.com/dhrions/french-typo/commit/f84c7df2fce392bd971dbe7c67169ed3cabd725c))

- 🔥 Remove code
  ([`b9c1c77`](https://github.com/dhrions/french-typo/commit/b9c1c77a8651e63749f238d7d928ed849b9f1d1f))

- 🔥 Remove file
  ([`c1783f2`](https://github.com/dhrions/french-typo/commit/c1783f2f731d81dc78720f0229bc38977f702c6b))

- 🔥 Remove some rules
  ([`970d96c`](https://github.com/dhrions/french-typo/commit/970d96ca7c86e54b1e3557186cb827cc78c8ce30))

- 🔧 Update gitignore
  ([`91cd6d3`](https://github.com/dhrions/french-typo/commit/91cd6d33ce082e85dd774ba5d9ccedfb1eb8e65b))

### ✨

- ✨ Add management of Anki rules
  ([`5104877`](https://github.com/dhrions/french-typo/commit/510487758c5da7944f6f033a716acef0efd64ed9))

- ✨ Enhance to manage a case
  ([`521613b`](https://github.com/dhrions/french-typo/commit/521613bbaa52ca43f7111c85f25bca03fa7a2954))

- ✨ Enhance to manage a case
  ([`4f706ec`](https://github.com/dhrions/french-typo/commit/4f706ec68328020d24ba7699701cfd5d9758e763))

- ✨ Improve script
  ([`84fb286`](https://github.com/dhrions/french-typo/commit/84fb2866a1ce0f62c86e0a45b13120b8f393dfa0))

### 🐛

- 🐛 Fix
  ([`2fe4253`](https://github.com/dhrions/french-typo/commit/2fe4253c6295009e8b1187cc68961154dc4f901d))


## v0.1.0 (2025-08-26)

### Other

- Initial commit
  ([`fbfae6a`](https://github.com/dhrions/french-typo/commit/fbfae6a814d6ad0b67cec387b1dd44354af6d455))

- 🏗️ Improve architecture
  ([`64c98b9`](https://github.com/dhrions/french-typo/commit/64c98b98388816d387be78218d73366ca73297b2))

- 📝 Add changelog
  ([`72aacf9`](https://github.com/dhrions/french-typo/commit/72aacf9cfcaf4eb62b42e3268344b0a3e705f240))

- 📝 Add README.adoc
  ([`2b87faf`](https://github.com/dhrions/french-typo/commit/2b87fafb15d49553a8ab4c3782cd39fc55de41f0))

- 📝 Update
  ([`c031d1e`](https://github.com/dhrions/french-typo/commit/c031d1efea96946c63633bd07a6ddea321c5e11b))

- 📝 Update
  ([`a1c191d`](https://github.com/dhrions/french-typo/commit/a1c191d8080fc16f02e00957f0ef0081ff9f5edc))

- 📝 Update doc
  ([`55d776c`](https://github.com/dhrions/french-typo/commit/55d776ca10276cae01bf4118602e777e7039617e))

- 🔥 Remove file
  ([`0f7d942`](https://github.com/dhrions/french-typo/commit/0f7d94245ff0f4f14ce02f27ce86e94b79b60c93))

- 🔧 Add requirements.txt
  ([`3f9ed71`](https://github.com/dhrions/french-typo/commit/3f9ed711081d9a4496880197635f58460cb8ea61))

- 🔧 Update gitignore
  ([`7e3ba2e`](https://github.com/dhrions/french-typo/commit/7e3ba2edfebba9c7b55576c4f09893ba8ef50279))

- 🔧 Update gitignore
  ([`dbc5d06`](https://github.com/dhrions/french-typo/commit/dbc5d0673474c9198d8d949ff8fd0044c15553f5))

- 🔧 Update meta.json
  ([`ea0cb31`](https://github.com/dhrions/french-typo/commit/ea0cb31173bf75bf1e18471999c6be5e3eb9a361))

- 🚚 Copy code from other folder
  ([`41a8363`](https://github.com/dhrions/french-typo/commit/41a8363fe68928e6f5a7dc8f1a256051579880c8))

### ✨

- ✨ Enhance management of nbsps
  ([`72483ef`](https://github.com/dhrions/french-typo/commit/72483ef5511f44e9d39f05215b2facc4fe67c589))
