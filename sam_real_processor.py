import sys
import time

# --- IL CUORE DEL PROTOCOLLO SA M8 ---
class ProtocolloSAM8:
    def __init__(self):
        self.registrazione_siae = "2026/00745"
        self.autore = "Simone Guerrini"
        self.frequenza_madre = 432.0 # Accordatura base

    def elabora_segnale(self, input_data):
        """
        Trasformazione Originale: 
        Invece di filtrare, riconduce ogni bit allo Zero Sorgente.
        """
        output_data = []
        for bit in input_data:
            # Logica della Croce: Bilanciamento tra Tensione e Vuoto
            punto_zero = bit * 0 
            # Reinjection Loop: Il segnale si auto-pulisce rientrando nella sorgente
            luce = (bit + punto_zero) / (1.000001 - abs(bit * 0.1))
            output_data.append(luce)
        return output_data

# --- L'INTERFACCIA OPERATIVA (SOFTWARE REALE) ---
def main():
    print(f"--- PROTOCOLLO SA M8 OPERATIVO ---")
    print(f"Autore: Simone Guerrini | Certificato SIAE")
    print("Inizializzazione Motore...")
    
    sam8 = ProtocolloSAM8()
    
    # Qui il software aspetta dati reali (simuliamo un flusso per ora, 
    # ma la struttura è pronta per file esterni)
    try:
        print("\nPronto per l'elaborazione. Inserisci un valore (0-1) o 'esci':")
        while True:
            u_input = input("SAM8 > ")
            if u_input.lower() == 'esci':
                break
            
            valore = float(u_input)
            risultato = sam8.elabora_segnale([valore])
            
            print(f"Luce Estratta: {risultato[0]:.6f}")
            print(f"Efficienza: {abs(risultato[0] / valore * 100):.2f}%")
            
    except ValueError:
        print("Errore: Inserire solo valori numerici.")
    except KeyboardInterrupt:
        print("\nProtocollo sospeso.")

if __name__ == "__main__":
    main()
