# Préconisations d'intégration — Série emailing « Le Guide Nespresso »

> Document de cadrage technique pour l'intégration de la série d'emails à partir de
> la maquette `PRM_journees_Nespresso_mars_V7 2.psd`, en s'appuyant sur les emails
> déjà produits (`guide_1`, `guide_2`) comme gabarits de référence.
>
> Distinction des niveaux d'information (norme agence) :
> **[Fait]** vérifié dans le code/la maquette · **[Hypothèse]** à confirmer · **[Préco]** recommandation.

---

## 1. Contexte & objectif

- **[Fait]** La maquette est une planche unique de **13 620 × 3 490 px** (72 dpi, RVB) regroupant
  l'ensemble des emails de la série alignés horizontalement.
- **[Fait]** La série est numérotée **#01 → #14** (badge « #NN — Votre guide Nespresso » en tête
  de chaque email).
- **[Fait]** `guide_1` (#01 « Bienvenue ») et `guide_2` (#02 « Les machines ») sont **intégrés** et
  servent de référence technique.
- **Objectif** : intégrer les emails restants (#03 → #14) en réutilisant une **base commune**
  identique, sans réintégrer le squelette à chaque fois.

> **Règle impérative : `guide_2` est la base de travail.** Tout nouvel email part d'une
> copie de `guide_2` (le plus complet structurellement) ; on n'invente pas de nouvelle
> structure, on adapte. En cas de doute, c'est `guide_2` qui fait foi.

Les visuels de la maquette s'extraient du PSD avec ImageMagick (`magick "fichier.psd[0]" -flatten`)
puis crop par artboard ; chaque email occupe ~646 px de large dans la planche aplatie.

---

## 2. Cartographie de la série

| #  | Objet / accroche principale (lecture maquette) | Statut |
|----|------------------------------------------------|--------|
| 01 | Bienvenue chez Nespresso — Merci pour votre inscription | ✅ intégré (`guide_1`) |
| 02 | Connaissez-vous les machines ? Original / Vertuo | ✅ intégré (`guide_2`) |
| 03 | Le premier avantage d'une longue lignée | à produire |
| 04 | Il est temps de commencer votre voyage avec Nespresso | à produire |
| 05 | Un café au goût inoubliable dans une capsule à base de papier compostable | à produire |
| 06 | Explorez les gammes de café Nespresso (offre 30% + Original / Vertuo) | ✅ intégré (`guide_6`) |
| 07 | Votre avantage pour explorer l'univers Nespresso | à produire |
| 08 | Votre avantage pour explorer… (gamme Original / professionnel) | à produire |
| 09 | -10 % sur vos cafés, sans lever le petit doigt (abonnement / app) | à produire |
| 10 | Votre offre exclusive : 0,31 € la capsule | à produire |
| 11 | Dernière chance — offre de remise | à produire |
| 12-13 | « Une offre pour vous » (variantes d'offre) | à produire |
| 14 | Dernière chance | à produire |

> **[Hypothèse]** Le libellé exact, l'objet/pré-header et l'ordre définitif des emails #12-#13
> doivent être **confirmés sur les calques du PSD** (les accroches ci-dessus sont relevées
> visuellement). Certains emails sont des variantes d'offre proches — vérifier s'il s'agit
> d'envois distincts ou d'un A/B.

---

## 3. La base commune (squelette réutilisable)

**[Fait]** Tous les emails partagent la même ossature. Seuls les **blocs centraux de contenu**
changent. À industrialiser comme un gabarit unique :

### En-tête (identique partout)
1. Pré-header : ligne d'objet grise + texte de pré-en-tête (12-13 px, `#434343`, Light 300).
2. Espaceur, puis **logo Nespresso centré** (`logo.png`, largeur 59 px, lien vers `nespresso.com/fr/fr`).
3. Badge **« #NN »** aligné à droite (numéro 40 px `#aa896a` Light + libellé « Votre guide Nespresso » 16 px noir).
4. **Bannière hero** pleine largeur (640 px, cliquable, `height:auto`).

### Pied de page & modules récurrents (identiques partout)
- **« Téléchargez l'application »** + icônes Android / Apple.
- **Bloc 4 services** (icônes) : livraison offerte · Boutique & Click&Collect · recyclage capsules · abonnement café — séparés par filets `#d0bfa8` (1 px).
- **Barre sociale** : « Rejoignez-nous #Nespressomoments » + Facebook / Instagram / LinkedIn.
- **Bloc B Corp** : visuel certificat + texte « mouvement mondial… » + lien.
- **Footer légal** : « Visuels non contractuels. » + mentions livraison (astérisque), texte 10 px `#1e2326`.

### Modules de contenu réutilisables (apparaissent sur plusieurs emails)
- **« PROFITEZ DE VOTRE OFFRE EN X ÉTAPES »** — pastilles numérotées brun.
- **« BIENVENUE DANS LE NESPRESSO CLUB »** — 3 colonnes circulaires (Services / Exclusivités / Privilèges).
- **« RENDEZ-VOUS VITE ! »** — 4 cartes (en boutiques / concept store / site / application).
- **Bloc CTA bandeau couleur** (ex. « La gamme des cafés professionnels » sur fond `#aa896a`).

> **[Préco]** Constituer une **bibliothèque de partials** (en-tête, chaque module, footer) copiables
> tels quels. Tout email = en-tête + sélection de modules + footer. Voir §6.

### Charte technique (relevée dans `guide_1`/`guide_2`)
| Élément | Valeur |
|---|---|
| Largeur contenu / conteneur | **640 px** / 800 px |
| Breakpoint mobile | `@media (max-width:480px)` → `.w100p` passe à 100 % |
| Police | **Nespresso Lucas** (Light 300 / Regular / Bold / XtraBd 900), fallback Arial |
| Brun principal (CTA, accents) | `#aa896a` |
| Beige clair (fonds blocs) | `#f3eee6` |
| Filets / séparateurs | `#d0bfa8` |
| Taupe (titres « À la une ») | `#8e8373` |
| Texte courant / pré-header | `#000000` / `#434343` |
| Footer | `#1e2326` |
| Boutons | brun plein texte blanc **ou** contour noir, hauteur 36 px, `letter-spacing:2px` |

---

## 4. Préconisations techniques d'intégration

1. **[Préco] Partir d'une copie de `guide_2`** (le plus complet : hero, blocs texte, bloc image+texte
   gauche/droite, bandeau couleur, club, services, footer) plutôt que de repartir de zéro.
2. **[Préco] Tables only / XHTML 1.0 Transitional.** Pas de flex/grid, pas de `<div>` de mise en page.
   Conserver `border-collapse`, `cellpadding/cellspacing=0`, `role` implicite des tables.
3. **[Préco] Encodage `iso-8859-1` à préserver.** Caractères accentués en **entités HTML**
   (`&eacute;`, `&agrave;`…). Ne jamais réenregistrer en UTF-8.
   ⚠️ `guide_2` contient déjà des accents bruts mal encodés (« Banni�re », « JE D�COUVRE ») —
   **à corriger en entités** et à ne pas reproduire.
4. **[Préco] Le double dossier `fontAbsolute` / `fontLocale`.** Voir `CLAUDE.md` : la **seule**
   différence légitime = l'URL des `@font-face` (CDN vs local). Tout le reste doit être **identique**.
   Maintenir les deux variantes synchronisées (harmoniser au passage l'écart `font-weight 900/800`
   présent sur `guide_1`).
5. **[Préco] Images — respecter les tailles de `guide_2`.** Chemins relatifs `images/`,
   `display:block`, `border=0`, `width` en dur + `height:auto`, **`alt` renseigné systématiquement**.
   Tailles réelles relevées dans `guide_2` (à reproduire) :

   | Type d'image | Fichier source réel | Largeur d'affichage (HTML) | Densité |
   |---|---|---|---|
   | Bannière hero | `img_banner.jpg` **640×286** | `width="640"` | **~1x** |
   | Bannière secondaire | `img_banner_2.jpg` **640×240** | `width="640"` | ~1x |
   | Visuel bloc produit | `img_bloc3_a/b.jpg` **386×458** | `width="320"` | ~1.2x |
   | Logo | `logo.png` **118×118** | `width="59"` | **2x** |
   | Icônes (services, social, B Corp, app) | `ico_*.png` ~**80–94 px** | `width=22–46` | **2x** |

   → **Photos en ~1x à la largeur d'affichage** (640 hero, 320 blocs) ; **logo + icônes en 2x**.
   Mutualiser les visuels communs (logo, icônes, social, B Corp, étapes) en les **copiant** depuis
   `guide_2`/`guide_1` plutôt qu'en les ré-exportant.
   ⚠️ Les photos extraites du PSD aplati sont en ~1x (≈646 px/email). Pour un rendu retina parfait,
   ré-exporter les photos depuis les calques du PSD ; les visuels actuels de `guide_6` sont en 1x.

   #### Méthode fiable de récupération des images depuis le PSD (par calques)

   > **[Préco] Ne PAS découper l'image aplatie « à l'œil » par coordonnées estimées** : cela laisse
   > des liserés blancs (fond de la maquette capté sur les bords) et des cadrages irréguliers.
   > **Se caler sur la géométrie exacte des calques.**

   1. **Lister les calques** (index, taille, offset, nom) pour repérer les bornes exactes de chaque photo :
      ```bash
      magick identify -format "%p: %wx%h %g\n" "PRM_XXX.psd"
      ```
      Chaque photo visible correspond à un **calque-cadre** aux dimensions/position précises
      (ex. cartes uniformes `292x170`, hero `646x250`). Il peut exister un second calque « photo »
      légèrement plus grand (image sous masque) — se fier au **cadre visible**, pas au calque débordant.
   2. **Générer le composite natif une seule fois** (⚠️ `-strip` obligatoire : sans lui, la sortie fait
      >140 Mo à cause des métadonnées/miniatures embarquées) :
      ```bash
      magick "PRM_XXX.psd[0]" -flatten -strip -depth 8 full_native.png
      ```
   3. **Découper en INSETANT de 2–3 px** par rapport à la géométrie du calque (`-crop LxH+X+Y +repage`).
      ⚠️ **Le bord du cadre est anti-aliasé et fond vers le blanc** du composite → un crop pile sur la
      géométrie laisse un liseré clair de 1 px. On rentre donc de 2–3 px de chaque côté (perte invisible) :
      ```bash
      # calque hero 646x250+77+238  -> inset 3px
      magick full_native.png -crop 640x244+80+241 +repage -quality 92 img_banner.jpg
      # calque carte 292x170+93+1009 -> inset 3px
      magick full_native.png -crop 286x164+96+1012 +repage -quality 92 img_en_boutique.jpg
      ```
   4. **Contrôle qualité** : poser chaque crop sur fond rouge zoomé ET vérifier la couleur des bords
      (doit refléter la photo, PAS ~95–99 % de blanc) :
      ```bash
      magick img.jpg -bordercolor red -border 6 -filter point -resize 200% check.png
      magick img.jpg -crop %[fx:w]x1+0+0 +repage -resize 1x1! -format '%[pixel:u]' info:   # couleur bord haut
      ```

   #### Retina

   > **[Fait]** Le PSD de campagne est une planche **aplatie à ~800 px de large** : la source est donc **~1x**,
   > il n'y a pas de vraie donnée 2x à l'intérieur (les calques « photo » ne dépassent que de peu le cadre).
   >
   > **[Préco] Livrable « format retina » (dimensions ×2)** : ré-échantillonner chaque crop à **2× la largeur
   > d'affichage** (hero 640→**1280**, cartes 260→**520**), en **conservant le `width` d'affichage** dans le HTML
   > (`width="640"`, `width="260"`) :
   > ```bash
   > magick crop.jpg -filter Lanczos -resize 1280x -quality 88 img_banner.jpg
   > ```
   > ⚠️ **NE PAS ajouter `-unsharp`** : le masque de netteté crée un **halo clair sur le pourtour**
   > (liseré blanc) — c'est du reste pour ça qu'il faut aussi inséter le crop (étape 3). Lanczos seul suffit.
   > ⚠️ L'upscale ne crée pas de détail : la netteté reste limitée par la source 1x. **Pour un vrai retina,
   > réclamer les fichiers photos d'origine** (ou les smart objects haute résolution) au studio de création.
6. **[Préco] Fonds des blocs — attention.** Le beige `#f3eee6` ne s'applique **qu'aux blocs/cartes**
   concernés, **jamais aux titres de section** ni aux espaceurs. Sur les cartes produit (moitié photo /
   moitié texte), mettre `bgcolor="#f3eee6"` **sur la cellule texte uniquement** ; photo et beige
   doivent avoir **la même hauteur**, sans débord beige au-dessus/en dessous. (Erreur classique :
   wrapper beige englobant titre + spacers.)
   - **Tags « # XXX »** (ex. « # À LA UNE », « # BARISTA », « # MASTERCLASS BOUTIQUE ») : encart
     **fond blanc**, texte taupe `#8e8373`, **collé en haut à droite** du bloc (flush bord supérieur
     et droit, sans padding), comme le « # À LA UNE » de `guide_2`. Jamais du texte posé directement sur le fond.
7. **[Préco] Couleurs de CTA — relever par email.** Ne pas présumer le brun : la couleur du bouton
   varie selon l'email (brun `#aa896a`, **noir `#000000`**, ou contour). Toujours vérifier sur la maquette.
8. **[Préco] Retours à la ligne fidèles à la maquette.** Reproduire les coupures de lignes des textes
   telles qu'elles apparaissent sur la maquette, avec `<br class="dn" />` (saut desktop, masqué en mobile).
   Respecter aussi les **paragraphes** (sauts de paragraphe via `<p>` espacés, pas `<br>`).
9. **[Préco] Dates : « 1er » en exposant.** Toute occurrence de « 1er » dans une date doit utiliser
    la balise `<sup>` : `1<sup style="line-height: 0; font-size: 8px;">er</sup>` (ex. « hors 1ᵉʳ mai »).
10. **[Préco] Footer variable par email.** Le bas de page change d'un email à l'autre : un email sans
    offre numérotée n'a **que** la note `*` (livraison) ; un email avec offre ajoute la/les note(s) `(1)`,
    `(2)`… **Vérifier le footer mot à mot sur la maquette pour chaque email.**
11. **[Préco] Liens.** `target="_blank"`, URLs `nespresso.com` absolues. Vérifier les liens
   spécifiques par offre (codes promo, pages produit Original/Vertuo/Pro).
12. **[Préco] Responsive.** S'appuyer uniquement sur les classes mobiles existantes
   (`.w100p`, `.dn`, `.db`, `.wid_cen`, `.pt-30m`…). Ne pas introduire de nouvelles conventions.
13. **[Préco] Poids.** Viser < 100 Ko HTML et des images optimisées (Gmail tronque au-delà de ~102 Ko).

---

## 5. Conformité & validation (cadre agence)

- **[Préco]** Tout email destiné à l'envoi passe par une **validation humaine** (relecture client
  Nespresso) avant diffusion — en particulier les emails à **offre commerciale** (#09, #10, #11, #14) :
  vérifier montants, codes promo, dates de validité et **mentions légales** (conditions de livraison,
  réserve « visuels non contractuels »).
- **[Préco]** Caractère **publicitaire** des emails : s'assurer de la présence des mentions
  obligatoires et d'un lien de désabonnement conforme (à confirmer dans la chaîne d'envoi).

---

## 6. Workflow de production recommandé

1. Dupliquer `guide_2/` → `guide_N/` (avec `fontAbsolute/` + `fontLocale/`).
2. Mettre à jour : `<title>`, objet/pré-header, badge `#NN`, bannière hero.
3. Assembler les **modules** depuis la bibliothèque selon la maquette de l'email.
4. Adapter textes (entités HTML) et liens/CTA.
5. Exporter et nommer les images dans `guide_N/.../images/`.
6. Prévisualiser en local (WAMP) :
   `http://localhost/PRM_journees_Nespresso_mars/guide_N/fontLocale/guide_N.html`
7. Synchroniser `fontAbsolute` (= idem + URLs CDN police).
8. QA (§7) puis validation humaine.

---

## 7. Checklist QA avant envoi

- [ ] `fontAbsolute` et `fontLocale` strictement identiques **hors** URL `@font-face`.
- [ ] Encodage `iso-8859-1` conservé, **zéro caractère cassé** (`�`), accents en entités.
- [ ] `<title>`, objet et pré-header corrects et cohérents avec la maquette.
- [ ] Badge `#NN` correct.
- [ ] Tous les `alt` renseignés ; toutes les images se chargent (local + CDN).
- [ ] Tous les liens testés (`target="_blank"`, bonnes pages, codes promo).
- [ ] Rendu OK : Outlook ancien + nouveau, Gmail, Apple Mail, mobile (≤ 480 px).
- [ ] Tailles d'images conformes à `guide_2` (photos ~1x, logo/icônes 2x).
- [ ] Fonds : titres de section sur blanc, beige limité aux cartes (pas de débord).
- [ ] Offres : montants / codes / dates / mentions légales vérifiés.
- [ ] Poids HTML maîtrisé, images optimisées.
- [ ] Validation humaine obtenue avant diffusion.
