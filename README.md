# Évaluation de Performances - Monte Carlo Master-Worker Socket

## Description
Implémentation parallèle de l'algorithme Monte Carlo pour le calcul de π 
utilisant une architecture Master-Worker basée sur des sockets TCP/IP Java.

## Auteur
Sylvain COUTURIER - BUT Informatique 3ème année

## Structure du Projet
- `src/` : Code source Java (Master et Worker)
- `scripts/` : Scripts d'automatisation des tests
- `data/` : Résultats expérimentaux bruts (CSV)
- `results/` : Graphiques et analyses
- `rapport/` : Rapport d'évaluation PDF

## Compilation

```bash
cd src/
javac MasterSocket.java WorkerSocket.java
