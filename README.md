# Data pipeline Twitter - AWS S3 

Exemple de data pipeline pour extraire des tweets et les enregistrer dans AWS S3.

![Twitter AWS S3 data pipeline](data-pipeline-01.png?raw=true "Twitter AWS S3 data pipeline")

## Pré-requis

- Créer un compte Amazon Web Services et configurer un utilisateur IAM avec accès par programmation.
- Créer un bucket S3 où écrire les données.
- Créer un flux AWS Kinesis Data Firehose avec enregistrement dans S3.
- Créer un compte développeur Twitter et une application.
- Renommer le ficher `app/config.ini-template` en `config.ini` et inscrire les informations de connexion de vos comptes AWS et Twitter.

## Librairies

Pour les **utilisateurs Vagrant**:

```
vagrant up
```

Pour les **utilisateurs Docker**:

```
docker-compose up
```

Pour les autres, installer les librairies requises:

```
pip3 install --no-cache-dir -r requirements.txt
```

## Exécution

Vous pouvez indiquer des mots-clés à suivre, séparés par des virgules, dans le fichier `app/config.ini`. Pour lancer le streaming :

```
cd app
python3 stream.py
```

Taper **Ctrl+C** pour arrêter l'exécution. Vérifier que les données sont écrites dans votre bucket S3.
