import time
import hashlib

class MyGuardianCore:
    """
    Guardian Biometric Protocol (GBP)
    Sistema de monitoramento e resposta adaptativa.
    """
    def __init__(self, user="Monarca"):
        self.user = user
        self.baseline_hr = 70
        self.battery_level = 100
        self.history_hr = []
        self.mesh_buffer = []
        self.is_emergency = False
        print(f"[{self.user}] My Guardian Core vFinal: Sistema Nervoso Integrado Ativo.")

    def monitor_vitals(self, hr, mov):
        """MOTOR 1: EUFORIA - Análise de Tendências."""
        self.history_hr.append(hr)
        if len(self.history_hr) > 10:
            self.history_hr.pop(0)

        if len(self.history_hr) >= 3:
            trend = self.history_hr[-1] - self.history_hr[-3]
            if trend > 40 and mov < 20:
                print(f"[!] TREND: Subida abrupta (+{trend} BPM) com baixa mobilidade.")
                self.trigger_rescue(hr, "ANOMALIA_TENDENCIA")
                return

        if hr - self.baseline_hr > 45 and mov < 20:
            print("[!] DESVIO: Batimento crítico detectado.")
            self.trigger_rescue(hr, "ANOMALIA_BASELINE")

    def trigger_rescue(self, hr, cause):
        """MOTOR 2: NEMO & MESH - Localização e Redundância."""
        self.is_emergency = True
        # Coordenadas genéricas (Praça da Sé, SP) para preservação de privacidade
        location = {"lat": -23.5505, "long": -46.6333}
        print(f"[NEMO] Protocolo de Resgate Ativado por {cause}. Fixando: {location}")
        self.battery_policy()
        self.scan_and_relay(location)
        self.seal_event(hr, location, cause)

    def battery_policy(self):
        """Gestão Inteligente de Energia."""
        if self.battery_level < 30:
            print("[ENERGIA] Modo Sobrevivência: Reduzindo pulso para 60min.")
        else:
            print("[ENERGIA] Bateria Estável: Pulso de 20min.")

    def scan_and_relay(self, my_loc):
        """MOTOR MESH: Caridade Digital e Redundância."""
        print("[MESH] Varredura LoRa/Bluetooth ativa. Buscando vizinhos...")
        self.mesh_buffer.append({"peer": "VULNERAVEL_02", "status": "Retransmitindo"})
        print(f"[MESH] Rede estabelecida. Retransmitindo alertas via {self.user}.")

    def seal_event(self, hr, loc, cause):
        """MOTOR 3: BLACKBOX - Criptografia de Registro Inviolável."""
        raw_data = f"{hr}{loc}{cause}{time.time()}"
        hash_seal = hashlib.sha256(raw_data.encode()).hexdigest()
        print(f"[BLACKBOX] Evento Selado. Hash: {hash_seal}")

if __name__ == "__main__":
    # Prova de Conceito
    guardian = MyGuardianCore("Tiago")
    print("\n--- TESTE DE CAMADA DE PROTEÇÃO ---")
    guardian.monitor_vitals(hr=72, mov=10)
    guardian.monitor_vitals(hr=115, mov=5)
    guardian.monitor_vitals(hr=145, mov=8)