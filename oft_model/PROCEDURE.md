# Créer un modèle Outlook (.oft) à partir d'un fichier HTML d'emailing

Kit pour transformer un emailing HTML (images en chemins relatifs) en modèle
Outlook `.oft` qui s'affiche correctement à l'import dans **« Mes modèles »** :
corps HTML mis en forme, visuels intégrés, **aucune pièce jointe**.

## Contenu du dossier

- `generer_oft.py` — script de génération.
- `modele_reference.oft` — exemple de modèle de référence.
- `PROCEDURE.md` — ce document.

## Méthode retenue (validée)

Le corps est stocké en **HTML** (`PR_HTML`) et chaque image en chemin relatif
(`src="images/..."`) est **intégrée directement dans le HTML en base64**
(`data:image/...`). Conséquences :

- le corps s'affiche mis en forme avec tous les visuels ;
- le fichier ne contient **aucune pièce jointe** (rien à afficher comme tel) ;
- le `.oft` est autonome (aucune dépendance à un dossier d'images).

> Pourquoi pas de RTF ni de pièces jointes `cid:` ? À l'import dans « Mes modèles »,
> l'Outlook actuel n'affiche que le corps HTML ; un corps RTF fabriqué n'est pas
> reconnu (retombe en texte brut) et les images en `cid:` apparaissent comme
> pièces jointes. Le HTML + base64 est la seule combinaison qui rend le résultat
> attendu à l'import.

## Utilisation

### Générer

Depuis ce dossier (`oft_model`), avec Python 3 :

```
python generer_oft.py <chemin_html> <chemin_oft_a_creer>
```

Exemple :

```
python generer_oft.py ..\pmr_brief_rentree\fontLocale\pmr_brief_rentree.html ..\pmr_brief_rentree\fontLocale\pmr_brief_rentree.oft
```

Options :
- `--subject "Objet du mail"` : forcer l'objet (sinon repris du `<title>`).
- `--txt corps.txt` : corps alternatif en texte brut.

Prérequis : Python 3, et le dossier `images/` référencé par le HTML doit être présent.

### Charger dans Outlook

Importer le `.oft` généré dans **« Mes modèles »**.

## Limite importante (envoi réel)

Les images sont intégrées en **base64** dans le HTML : idéal pour l'affichage et la
prévisualisation, mais **à l'envoi réel**, plusieurs clients de messagerie (Gmail,
Outlook classique) **bloquent les images base64** à la réception. Ce `.oft` est donc
un bon modèle de composition/prévisualisation ; pour un **envoi de masse**, la
référence reste la version HTML avec images **hébergées** (via le routeur d'emailing).

Une relecture humaine avant diffusion reste recommandée.
