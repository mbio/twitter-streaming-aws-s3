# Data pipeline Twitter - AWS S3 

Exemple de data pipeline pour extraire des tweets et les enregistrer dans AWS S3 avec Kinesis Data Firehose.

![Twitter AWS S3 data pipeline](data-pipeline-01.png?raw=true "Twitter AWS S3 data pipeline")

## Pré-requis

- Créer un compte Amazon Web Services et configurer un utilisateur IAM avec accès par programmation.
- Créer un bucket S3 où écrire les données.
- Créer un flux AWS Kinesis Data Firehose pour écrire dans S3.
- Créer un compte développeur Twitter et une application.
- Renommer le ficher `app/config.ini-template` en `app/config.ini` et inscrire:
    - les informations de connexion aux comptes AWS et Twitter;
    - les mots-clés à suivre sur Twitter, séparés par des virgules.
- Cloner/télécharger ce projet sur votre poste.

## Exécution

1. Installer les librairies requises. Pour les **utilisateurs Vagrant**, lancer `vagrant up`. Sinon, exécuter

    ```
    pip3 install --no-cache-dir -r requirements.txt
    ```
   
2. Démarrer le streaming (taper **Ctrl+C** pour arrêter l'exécution) :
    
    ```
    cd app
    python3 twitter-stream.py
    ```
3. Vérifier que les données sont écrites dans votre bucket S3.
