# Stima del Valore di una Fiat 500 Usata 🚗

Questo progetto propone un'implementazione di un sistema di stima del valore di mercato per veicoli usati, specificamente per il modello Fiat 500, mediante un'applicazione web basata su Flask. L'applicazione permette l'inserimento interattivo di parametri descrittivi del veicolo e impiega un modello di regressione lineare, sviluppato con Scikit-Learn, per generare previsioni di prezzo basate su dati storici.

## 📌 Caratteristiche principali
- Interfaccia web interattiva per l'inserimento dei parametri del veicolo.
- Modello di regressione lineare per la stima del valore di mercato.
- API Flask per la gestione delle richieste e l'elaborazione delle previsioni in tempo reale.
- UI ottimizzata con **Tailwind CSS** per garantire un'esperienza utente intuitiva e reattiva.

## 🛠️ Tecnologie adottate
- **Python** per lo sviluppo backend e la gestione del modello predittivo.
- **Flask** come framework per la creazione e gestione dell'interfaccia web.
- **Scikit-Learn** per la definizione, l'addestramento e la validazione del modello di regressione.
- **Tailwind CSS** per un design modulare e adattabile.

## 📊 Dataset e Modello Predittivo
Il modello di regressione lineare è stato addestrato su un dataset contenente osservazioni relative a Fiat 500 usate. Le feature selezionate per la previsione includono:
- **model**: specifica del modello del veicolo.
- **engine_power**: potenza del motore (in cavalli vapore).
- **transmission**: tipologia di trasmissione (manuale, automatica, ecc.).
- **age_in_days**: anzianità del veicolo espressa in giorni.
- **km**: chilometraggio totale registrato.
- **previous_owners**: numero di proprietari precedenti.
- **price**: valore di mercato stimato (variabile target).

L'algoritmo è stato ottimizzato per minimizzare l'errore quadratico medio (MSE), assicurando un'elevata capacità predittiva. Future iterazioni del modello potrebbero includere tecniche di regressione più avanzate, come modelli basati su gradient boosting o reti neurali.

## 🔧 Prospettive di sviluppo
Il progetto è aperto a contributi per il miglioramento delle capacità predittive e dell'architettura software. Tra le possibili evoluzioni:
- Implementazione di modelli di machine learning più complessi (Random Forest, XGBoost, deep learning).
- Integrazione con database per una gestione più strutturata e scalabile dei dati.
- Espansione delle feature analizzate per includere ulteriori parametri economici e ambientali.

## 📜 Licenza
Il progetto è distribuito sotto licenza **MIT**.

---
✉️ Per domande o suggerimenti, contattami su GitHub: [@ITISlucaT](https://github.com/ITISlucaT)

