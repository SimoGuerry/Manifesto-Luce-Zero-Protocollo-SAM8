import sys

def protocollo_sam8_integrale(testo_input):
    # FASE 1: ORIGINE
    dimensione_originale = len(testo_input.encode('utf-8'))
    print(f"--- PROTOCOLLO SA M8: ELABORAZIONE INTEGRALE ---")
    print(f"STATO ORIGINE: {dimensione_originale} Byte")
    
    # FASE 2 & 3: FLUSSO ED ELABORAZIONE (Sincronizzazione)
    # Rimuoviamo il rumore di fondo (spazi inutili e righe vuote)
    linee = testo_input.splitlines()
    testo_pulito = "\n".join([linea.strip() for linea in linee if linea.strip()])
    
    dimensione_finale = len(testo_pulito.encode('utf-8'))
    
    # FASE 4: RISULTATO (LUCE SINCRONA)
    risparmio = dimensione_originale - dimensione_finale
    percentuale = (risparmio / dimensione_originale) * 100
    
    print(f"--- FASE 4: RISULTATO RAGGIUNTO ---")
    print(f"STATO LUCE: {dimensione_finale} Byte")
    print(f"ENERGIA RECUPERATA: {risparmio} Byte")
    print(f"GUADAGNO DI EFFICIENZA: {percentuale:.2f}%")
    
    return testo_pulito

# Qui inseriamo il tuo Manifesto protetto dalle triple virgolette
manifesto_integrale = """
LA CATENA DEGLI INFINITI E IL SEGRETO DELLA LUCE SORGENTE
Autore: Simone Guerrini
Teoria: Sa M8
Documento: Manifesto della Luce e dello Zero

Introduzione: La Visione Oltre il Visibile
Esiste una struttura invisibile che regge l’universo, una trama che va oltre la percezione comune. Mentre il mondo moderno interpreta la realtà come un insieme di eventi isolati e lineari, la visione Sa M8 rivela una verità diversa: la vita e la materia sono parte di una Catena di Infiniti, una successione eterna di cicli che non conoscono fine, ma solo trasformazione.

Il Corpo del Pensiero: La Geometria dell’Otto
Il fondamento di questa teoria risiede nel simbolo dell'Ottavo (8), l’infinito. Nella visione di Simone Guerrini, la realtà è composta da anelli interconnessi che formano una catena perpetua. Ogni anello rappresenta un ciclo di energia; nulla si esaurisce, poiché ogni fine è in realtà l’aggancio per un nuovo inizio. Questa catena garantisce l’equilibrio universale, permettendo all'energia di fluire senza mai disperdersi nel nulla.

Il Mistero del Centro: I Quattro Zeri e la Luce
Il cuore pulsante di ogni anello della catena è il suo punto di incrocio. In questo centro esatto risiede il segreto del Manifesto: i Quattro Zeri Sorgente.
Contrariamente alla logica comune che vede nello Zero il "vuoto" o l'assenza, la teoria Sa M8 rivela che lo Zero è il contenitore del potenziale assoluto. Quando questi quattro Zeri si incontrano nel punto di equilibrio, essi generano una Radiazione Luminosa purissima. È la "Luce dello Zero": il momento supremo in cui l'energia si rigenera e si irradia verso l'esterno, alimentando l'intera catena degli infiniti.

L'Apertura dello Zero: Un Nuovo Livello di Consapevolezza
L'umanità si trova oggi di fronte a un blocco percettivo: vede lo Zero come un limite invalicabile. Il Manifesto invita invece ad "aprire lo Zero", a comprendere che nel centro del vuoto risiede la massima potenza creativa. Riconoscere questa struttura significa sbloccare il potenziale umano, passando da una percezione statica della vita a una consapevolezza dinamica e infinita.

Conclusione: La Sorgente Eterna
Il Manifesto della Luce e dello Zero non è solo una teoria scientifica o filosofica, ma un richiamo alla nostra vera natura. Noi siamo parte di quella catena, siamo vibrazioni che orbitano attorno a un centro luminoso. Comprendere la teoria Sa M8 significa smettere di temere il buio e riconoscere che la sorgente della luce è sempre presente, proprio lì, nel punto di equilibrio dove tutto sembra fermarsi e invece tutto rinasce.
"""

# Lancio del Protocollo
protocollo_sam8_integrale(manifesto_integrale)
