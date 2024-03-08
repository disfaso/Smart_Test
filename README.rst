------------------------------
Smart Test
------------------------------
============
INTRODUZIONE
============
Smart_Test è un'applicazione Python progettata per la creazione e la gestione 
di verifiche e esercizi per l'insegnamento e l'apprendimento in ambito scolastico. 
Questo strumento fornisce un'interfaccia intuitiva e semplice da utilizzare per docenti e 
formatori che desiderano creare e personalizzare verifiche su varie materie e argomenti.

Con Smart_Test, è possibile:

- Generare verifiche personalizzate con una varietà di tipologie di esercizi in formato .docx per poter essere modificate al bisogno.
- Salvare le verifiche generate per la gestione a lungo termine.
- Aggiungere nuovi esercizi e argomenti al database per ampliare la varietà di contenuti disponibili.
- Un alto livello di classificazione degli esercizi caricati, che permetta di selezionare in base a tipologia di esercizio e livello stimato

Questo progetto è stato sviluppato con l'obiettivo di semplificare il processo di creazione 
di verifiche, permettendo il salvataggio di esercizi ritenuti interessanti e permettendo di 
creare una prima verifica con le caratteristiche desiderate da cui partire

Per iniziare ad utilizzare Smart_Test, segui le istruzioni di installazione e configurazione riportate di seguito. Per eventuali problemi o domande, consulta la sezione di risoluzione dei problemi o contatta il team di sviluppo.

========================
Istruzioni di Installazione
========================
1. Assicurati di avere Python installato sul tuo sistema. Smart_Test è compatibile con Python 3.6 e versioni successive.

2. Scarica il repository Smart_Test sul tuo computer. Puoi farlo clonando il repository da GitHub utilizzando il comando git clone::
    git clone https://github.com/disfaso/Smart_Test

  Oppure puoi scaricare il repository come file ZIP e estrarlo sul tuo computer.

3. Installa le dipendenze del progetto eseguendo il comando::
    pip install -r requirements.txt

4. Avvia Smart_Test eseguendo il comando::
    python Smart_Test



Se si vogliono fare dei tentativi di generazione di verifica, 
si può utilizzare la materia "Falsa",
che prenderà esercizi da Falsa_Esercizi.json

Questi esercizi sono per lo più inizializzati con parametri
    tipologia: esercizio
    livello: basilare
    tematica: tematica_0
    sottotematica: sottotematica_0

