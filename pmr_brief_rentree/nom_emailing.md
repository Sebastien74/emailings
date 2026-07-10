# Nom de l'emailing — PMR Brief rentrée 0,31

| Champ | Valeur |
|---|---|
| **Campagne** | EMAIL COLLECTE PRM — offre de recrutement rentrée |
| **Template** | PRM Collecte |
| **Objet** | Bénéficiez de votre offre de rentrée sur les cafés Nespresso |
| **Pré-header** | Livraison offerte où que vous soyez |
| **Période** | Septembre 2026 |
| **Type** | Clic to Lead (Oui) + Code promo (Oui) — collecte de prospects PRM |

## Détail

- **Sujet** : offre de rentrée sur la gamme Original — 0,31 € la capsule (soit 31 € les 100 capsules), dès 50 capsules commandées parmi la sélection.
- **Mécanique** : le prospect confirme son email pour recevoir son code privilège (collecte de lead).
- **CTA principal** : JE DÉCOUVRE → https://www.nespresso.com/fr/fr/order/capsules/original
- **Base d'intégration** : structure et modules repris de `nespresso/guide_1` (en-tête, app, 4 icônes services, social, B Corp, footer).

## Fichiers du dossier

- `fontAbsolute/pmr_brief_rentree.html` — variante production (CDN @font-face)
- `fontLocale/pmr_brief_rentree.html` — variante prévisualisation locale (police embarquée)
- `pmr_brief_rentree.txt` — version texte / référence de contenu (UTF-8)
- `images/` — visuels (hero + 4 cartes extraits du PSD ; icônes/logo/social mutualisés depuis guide_1)

## Prévisualisation locale (WAMP)

`http://localhost/pmr_brief_rentree/fontLocale/pmr_brief_rentree.html`

## ⚠️ Points à faire valider (relecture client Nespresso)

- **Incohérence d'offre à arbitrer** : le corps annonce « 0,31 € la capsule », mais la **mention légale (1)** (reprise de la maquette) parle d'une « remise immédiate de **5 €** ». À confirmer / réécrire par le client.
- **Liens des blocs récurrents** (RENDEZ-NOUS VISITE, footer, app, jeu-concours) repris de `guide_1` / du PSD : à vérifier (notamment l'URL du règlement du jeu `jeu-concours-summer`).
- **Visuels extraits du PSD aplati en ~1x** (source 800 px de large). Pour un rendu retina, ré-exporter les photos depuis les calques du PSD.
- Email à **caractère publicitaire** + **jeu-concours** : vérifier mentions obligatoires, lien de désabonnement et règlement dans la chaîne d'envoi (escalade humaine).
