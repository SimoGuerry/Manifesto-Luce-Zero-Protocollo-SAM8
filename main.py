from sam8_cuore_di_luce import CroceDegliInfiniti
import numpy as np

pipeline = CroceDegliInfiniti(snr_soglia=45.0, max_cicli=3)
result   = pipeline.elabora(np.random.randn(256), snr_iniziale=12.0)
print(result.report())
metrics  = result.to_dict()   # → JSON per il tuo sistema
