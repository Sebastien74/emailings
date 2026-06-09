# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Nature du projet

Campagne d'**emailing HTML** pour Nespresso — une série d'onboarding « Le Guide Nespresso » envoyée aux nouveaux inscrits. Ce n'est pas une application : il n'y a ni build, ni dépendances, ni tests, ni gestionnaire de paquets. Le livrable final est constitué de fichiers HTML autonomes et de templates Outlook (`.oft`).

Chaque email de la série est un dossier `guide_N/` :
- `guide_1` — « Bienvenue chez Nespresso » (présentation du concept, étapes de prise en main)
- `guide_2` — « Connaissez-vous les machines à café Nespresso ? »
- `guide_3` — réservé (vide pour l'instant)

## Le pattern à deux variantes (point d'architecture central)

Chaque `guide_N/` contient **deux sous-dossiers qui doivent rester synchronisés** :

| Dossier | Usage | Différence |
|---|---|---|
| `fontAbsolute/` | **Production / envoi** | `@font-face` pointe vers le CDN `https://www.nespresso.com/emailing/NespressoVisuals/common/fonts/...` |
| `fontLocale/`   | **Prévisualisation locale** | `@font-face` pointe vers `fonts/...` (police embarquée) + dossier `fonts/` présent |

**La SEULE différence légitime entre les deux variantes est l'URL des `@font-face`.** Les chemins d'images restent relatifs (`images/...`) dans les deux cas. Toute modification du contenu, de la structure ou du style HTML doit être répliquée à l'identique dans les deux variantes du même guide. (Attention : des écarts involontaires existent déjà — ex. `font-weight: 900` vs `800` dans `guide_1` — à harmoniser lors d'une édition.)

Contenu de chaque variante :
- `guide_N.html` — l'email (source de vérité à éditer)
- `guide_N.txt` — version texte / référence de contenu, structurée par marqueurs `<!-- Start of BLOCK n -->`
- `guide_N.oft` — template Outlook (ancien Outlook)
- `guide_N_new_outlook.oft` — template pour le nouvel Outlook
- `images/` — visuels de l'email (relatifs)

## Conventions de l'HTML email (impératives)

Le HTML email obéit à des règles différentes du web moderne. Respecter scrupuleusement l'existant :

- **XHTML 1.0 Transitional**, mise en page **100 % par tables** imbriquées (`<table>/<tr>/<td>`). Pas de flexbox, pas de grid, pas de div de layout.
- **Charset `iso-8859-1` (latin-1)** — déclaré dans `<head>`. Les caractères accentués sont encodés en entités HTML (`&eacute;`, `&agrave;`...). **Préserver l'encodage du fichier** : ne pas réenregistrer en UTF-8, ne pas remplacer les entités par des accents bruts.
- **Styles** : combinaison de styles inline sur les `<td>`/`<img>` et d'un bloc `<style>` dans le `<head>`. Les classes du `<style>` (`.dn`, `.db`, `.w100p`, `.pt-30m`...) ne servent que dans la `@media only screen and (max-width: 480px)` pour le rendu mobile.
- **Conditionnels MSO** : blocs `<!--[if mso]> ... <![endif]-->` pour le rendu Outlook (ex. `.fallback-text` en Arial). Les conserver et les tester séparément.
- Police de marque : `'Nespresso Lucas'` (Regular/Light/Bold/XtraBd), avec fallback Arial sous Outlook.

## Prévisualisation

Le projet est servi par **WAMP** (`C:\wamp64\www\...`). Ouvrir la variante `fontLocale` dans un navigateur via `http://localhost/PRM_journees_Nespresso_mars/guide_N/fontLocale/guide_N.html` pour un rendu fidèle avec les polices embarquées. Le test final du rendu email se fait dans les clients réels (Outlook ancien/nouveau, mobile) via les `.oft`.

## Avertissements

- À la racine : `*.psd` (~940 Mo) et `*.pptx` — sources de design lourdes, non versionnées de fait. Ne pas les lire/manipuler sans raison.
- Toute modification de contenu destinée à l'envoi relève d'une **validation humaine** avant diffusion (relecture client Nespresso).
