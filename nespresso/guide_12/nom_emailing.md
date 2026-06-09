# Nom de l'emailing — guide_12

| Champ | Valeur |
|---|---|
| **Nom de routage (prm_)** | `prm_journees_nespresso_une_offre_pour_vous` |
| **Guide** | guide_12 |
| **N° email** | #12 |
| **Objet** | Une offre pour vous |
| **Titre / pré-header** | Une offre pour vous – Le Guide Nespresso |
| **Campagne** | PRM_journees_Nespresso_mars |

## Détail

- **Sujet de l'email** : offre découverte gamme Original
- **Offre** : 20 % de remise immédiate dès 5 étuis de café gamme Original ; code privilège communiqué dans l'email de confirmation d'inscription
- **CTA principal** : JE COMMANDE → https://www.nespresso.com/fr/fr/order/capsules/original

> ⚠️ Objet identique à `guide_13` (« Une offre pour vous »). Les deux sont distingués par leur slug de routage : voir `guide_13` → `prm_journees_nespresso_une_offre_exclusive`.

## Fichiers du guide

- `fontAbsolute/guide_12.html` — variante production (CDN @font-face)
- `fontLocale/guide_12.html` — variante prévisualisation locale
- `guide_12.txt` — version texte / référence de contenu ✅ intégré
- `guide_12.oft` — template Outlook (ancien) ✅ généré (images embarquées cid:)
- `guide_12_new_outlook.oft` — template nouvel Outlook ✅ généré

> Toute diffusion relève d'une validation humaine (relecture client Nespresso).

> ⚠️ **À faire valider (Nespresso) avant diffusion** — email à offre commerciale :
> code promo affiché `P.SV.QMPL.L2.WQQ` (à confronter à « code communiqué dans
> l'email de confirmation d'inscription »), montant **20 %**, dates
> **30/09/2026 → 31/12/2026** (jour de début ambigu sur la maquette : 30/08 ou
> 30/09), exclusions (Special Reserve / Pierre Hermé / Édition Limitée) et toute
> la mention légale `(1)` — transcrits depuis la planche aplatie (texte ~10 px,
> basse résolution) et donc à recouper avec la source PSD.
