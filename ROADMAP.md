# Roadmap

Feuille de route de **French Typo**
(jalons organisés par priorité — le détail d'implémentation vit dans `TODO.md`)

---

## 🔴 Priorité très haute

### Positionnement du moteur
- [x] **Moteur autonome** : cœur typographique pur, sans dépendance à une interface ou à un environnement hôte
- [x] **Périmètre clarifié** : le dépôt ne porte que le moteur et sa CLI, les intégrations applicatives vivent dans leurs propres dépôts
- [ ] **Source unique des règles typographiques** : toute règle appliquée par un consommateur provient du moteur, aucun consommateur n'a besoin de réimplémenter ou de figer une copie

### Distribution
- [x] **Publication PyPI automatisée** : release déclenchée par les commits, gatée par les tests

---

## 🟠 Priorité haute

### Couverture typographique française
- [x] **Ponctuations doubles et unités** : espaces insécables, normalisation des unités, ordinaux en exposant
- [x] **Guillemets français** : espaces insécables autour de « et »
- [ ] **Guillemets simples** : prise en charge de ‹ et ›
- [ ] **Abréviations courantes** : traitement des formes usuelles (M., Mme, Dr, etc.)

### Contrôle par l'appelant
- [ ] **Sélection des règles** : permettre d'activer ou désactiver individuellement les règles appliquées, condition préalable à toute interface de préférences côté consommateur

---

## 🟡 Priorité moyenne

### Élargissement des formats
- [x] **AsciiDoc** : adaptateur gérant blocs littéraux, commentaires et ponctuation des listes
- [x] **Anki** : adaptateur gérant le HTML et les clozes
- [ ] **Markdown** : adaptateur respectant les blocs de code et la syntaxe inline

### Fiabilité
- [x] **Suite de tests automatisée** : couverture du cœur, des adaptateurs et de la CLI, exécutée sur plusieurs versions de Python
- [ ] **Idempotence garantie** : appliquer le formatage deux fois produit le même résultat, sur tous les adaptateurs

---

## 🟢 Priorité basse

### Élargissement des formats
- [ ] **LaTeX** : adaptateur respectant les commandes et environnements

### Structure du dépôt
- [x] **Documentation publiée** : documentation Antora construite et déployée automatiquement
- [ ] **Gouvernance de contribution** : conditions d'accueil de contributions externes définies

---

## 🔵 Long terme

### Au-delà du français
- [ ] **Autres langues** : jeux de règles typographiques pour d'autres langues (italien, espagnol)

### Extensibilité
- [ ] **Règles définies par l'utilisateur** : possibilité de déclarer ses propres règles sans modifier le moteur
