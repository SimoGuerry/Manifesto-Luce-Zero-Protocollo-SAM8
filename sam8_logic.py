import time

def protocollo_sam8(dato_input):
    print(f"--- Inizio Elaborazione SA M8 per: {dato_input} ---")
    
    # Rappresentazione dei Quattro Zeri Sorgente
    zeri_sorgente = ["Origine", "Flusso", "Elaborazione", "Risultato"]
    potenziale_luce = 0
    
    for zero in zeri_sorgente:
        print(f"Passaggio attraverso lo Zero di {zero}...")
        time.sleep(0.5) # Simula la velocità di sincronizzazione
        potenziale_luce += 25  # Ogni zero aggiunge il 25% di purezza
        
    print(f"--- Raggiunto il PUNTO LUCE: Potenziale al {potenziale_luce}% ---")
    
    # La Croce degli Infiniti: Bilanciamento tra Verticale (Struttura) e Orizzontale (Espansione)
    output_finale = f"Luce_Sincrona({dato_input})"
    return output_finale

# Prova dell'algoritmo
risultato = protocollo_sam8("Informazione Grezza")
print(f"Risultato Finale Certificato: {risultato}")
