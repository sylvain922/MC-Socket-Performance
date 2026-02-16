#!/bin/bash
# Script pour lancer automatiquement N workers

NUM_WORKERS=${1:-8}  # Par défaut 8 workers
BASE_PORT=25545

echo "Lancement de $NUM_WORKERS workers..."

for i in $(seq 0 $((NUM_WORKERS-1))); do
    PORT=$((BASE_PORT + i))
    java -cp ../src WorkerSocket $PORT > /dev/null 2>&1 &
    echo "Worker lancé sur port $PORT (PID: $!)"
done

echo "Tous les workers sont prêts. Vous pouvez lancer le Master."
