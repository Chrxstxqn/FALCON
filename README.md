# FALCON - Flexible Authentication Login Cracking & Optimized Node

```
    ███████╗ █████╗ ██╗      ██████╗ ██████╗ ███╗   ██╗
    ██╔════╝██╔══██╗██║     ██╔════╝██╔═══██╗████╗  ██║
    █████╗  ███████║██║     ██║     ██║   ██║██╔██╗ ██║
    ██╔══╝  ██╔══██║██║     ██║     ██║   ██║██║╚██╗██║
    ██║     ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                    by Chrxstxqn
    Flexible Authentication Login Cracking & Optimized Node
    v1.0 - Terminal User Interface (TUI) for Hashcat
```

## 📋 Overview

**FALCON** è un'interfaccia grafica intuitiva per il terminale che semplifica l'utilizzo di **hashcat**, il più potente password cracking engine disponibile. Fornisce un'interfaccia user-friendly basata su menu per configurare e lanciare attacchi di cracking in modo facile e veloce.

Non ricrea hashcat, ma lo avvolge in un'interfaccia professionale che rende il processo meno complicato e riduce gli errori di sintassi.

## ✨ Features

### 🎨 Interfaccia Intuitiva
- Menu principale ben organizzato e colorato
- Configurazione guidata passo dopo passo
- Barra di progresso animata durante il caricamento
- Output colorato e facile da leggere
- Due loghi ASCII art distinti (caricamento + menu principale)

### 🚀 Funzionalità Complete
- **5 Modalità di Attacco**: Dictionary, Combination, Brute-force, Hybrid Wordlist+Mask, Hybrid Mask+Wordlist
- **10+ Tipi di Hash Supportati**: MD5, SHA1, SHA256, SHA512, bcrypt, NTLM, NetNTLMv2, WPA/WPA2, Kerberos
- **Configurazione GPU**: Abilita/disabilita accelerazione GPU
- **Livelli di Workload**: 4 livelli selezionabili (Low, Default, High, Nightmare)
- **Regole Custom**: Supporto per file di regole personalizzate
- **Opzioni Extra**: Aggiungi parametri extra di hashcat direttamente

### 🎯 Preset Pre-configurati
Inizi velocemente con preset per:
- MD5 Dictionary Attack
- SHA1 Dictionary Attack
- 8 Character Brute-force
- 6 Digit PIN
- bcrypt Dictionary Attack

### 📊 Anteprima Comando
- Visualizza il comando completo prima di eseguirlo
- Verifica parametri configurati
- Conferma prima del lancio

### 📚 Documentazione Integrata
- Esempi di attacchi comuni
- Guida ai pattern MASK (?l, ?u, ?d, ?s, ?a, ?b)
- Help contestuale

## 🔧 Installation

### Prerequisiti
- Python 3.7 o superiore
- Debian/Ubuntu o qualsiasi distro basata su Debian
- hashcat installato nel sistema

### Step-by-Step

1. **Installa hashcat**:
```bash
sudo apt update
sudo apt install hashcat
```

2. **Scarica FALCON**:
```bash
git clone https://github.com/Chrxstxqn/FALCON
cd FALCON
```

3. **Rendi eseguibile**:
```bash
chmod +x falcon.py
```

4. **Avvia l'applicazione**:
```bash
python3 falcon.py
# oppure
./falcon.py
```

## 🎮 Quick Start

### Attacco Dizionario MD5
1. Seleziona "1. Configura Attacco"
2. Imposta il file con gli hash MD5
3. Hash Type → 0 (MD5)
4. Attack Mode → 0 (Dictionary)
5. Carica una wordlist
6. Seleziona "3. Esegui Attacco"

### Brute-force 6 Cifre
1. Vai a "2. Visualizza Preset"
2. Seleziona "4 - 6 Digit PIN"
3. Imposta il file con gli hash
4. Esegui l'attacco

### Ibrido (Wordlist + Mask)
1. Configura Attack Mode → 6 (Hybrid)
2. Carica wordlist
3. Imposta Mask (es: ?d?d per aggiungere 2 cifre)
4. Esegui

## 📖 Menu Principale

```
FALCON - Menu Principale
============================================================

1. Configura Attacco      - Imposta tutti i parametri
2. Visualizza Preset      - Carica configurazioni salvate
3. Esegui Attacco         - Lancia il cracking
4. Mostra Esempi          - Guida ai pattern MASK
5. Anteprima Comando      - Visualizza il comando
0. Esci                   - Chiudi FALCON
```

## ⚙️ Configurazione Dettagliata

### Hash Types Supportati
| Codice | Tipo | Uso |
|--------|------|-----|
| 0 | MD5 | Web, Database |
| 100 | SHA1 | Legacy Systems |
| 1400 | SHA2-256 | Moderno, Sicuro |
| 1700 | SHA2-512 | Moderno, Highly Secure |
| 3200 | bcrypt | Password Hashing |
| 1000 | NTLM | Windows |
| 2500 | WPA/WPA2 | WiFi |

### Attack Modes
| Modalità | Descrizione | Uso |
|----------|-------------|-----|
| 0 | Dictionary | Wordlist attack |
| 1 | Combination | Combina wordlist |
| 3 | Brute-force | Prova tutte combinazioni |
| 6 | Hybrid Wordlist+Mask | Wordlist + pattern |
| 7 | Hybrid Mask+Wordlist | Pattern + wordlist |

### Pattern MASK
```
?l = Minuscolo (a-z)
?u = Maiuscolo (A-Z)
?d = Cifra (0-9)
?s = Speciale (!@#$...)
?a = Tutto (?l?u?d?s)
?b = Non-ASCII (0x80-0xff)
?1-?4 = Custom charset

Esempi:
?d?d?d?d         = 4 cifre (0000-9999)
?a?a?a?a         = 4 caratteri qualsiasi
password?d?d     = password + 2 cifre
?u?l?l?l         = Maiuscolo + 3 minuscoli
```

### Workload Levels
```
1 (Low)       - Basso uso risorse, lento
2 (Default)   - Bilanciato
3 (High)      - Alto uso risorse, veloce
4 (Nightmare) - Massimo, può causare lag
```

## 🎨 Colori e Interfaccia

FALCON usa un sistema di colori per una migliore esperienza:
- **Cyan**: Headers e informazioni
- **Green**: Messaggi positivi e prompt
- **Yellow**: Avvertimenti e titoli
- **Red**: Errori
- **Magenta**: Logo principale

## 🐛 Troubleshooting

### "Hashcat non trovato nel PATH"
```bash
sudo apt install hashcat
hashcat --version  # Verifica
```

### GPU non riconosciuta
```bash
# Per NVIDIA
nvidia-smi

# Per AMD
rocm-smi

# Installa driver se necessario
# NVIDIA: sudo apt install nvidia-utils nvidia-driver-XXX
# AMD: sudo apt install rocm-hip
```

### Permessi Negati
```bash
chmod +x falcon.py
python3 falcon.py
```

### FALCON si blocca
Riduci il Workload Level (opzione 8) da 3 a 1 o 2

## 📋 Requisiti di Sistema

- **CPU**: Dual-core o meglio
- **RAM**: 2GB minimo (4GB+ consigliato)
- **Storage**: 1GB per wordlist
- **GPU**: Opzionale (ma molto utile)

## 🚀 Performance Tips

1. **Usa GPU**: Se disponibile, migliore di 10-100x rispetto CPU
2. **Scegli Workload appropriato**: Non sempre il massimo è meglio
3. **Wordlist grande**: Download rockyou.txt o simili
4. **Regole di Transformation**: Aumenta success rate con meno tentativi
5. **Mask intelligenti**: Specializza mask basato su target

## 📝 File di Configurazione

FALCON non salva automaticamente configurazioni (tutto in memoria), ma puoi:
1. Prendere nota dei preset usati
2. Creare script di lancio personalizzati
3. Salvare parametri in file di testo per riferimento

## ⚖️ Legal Notice

FALCON è uno strumento di security testing. Assicurati di:
- Avere permesso di testare gli hash che cracki
- Non usare per scopi illegali
- Testare solo su sistemi autorizzati
- Rispettare leggi locali

## 🤝 Contributing

Contributi sono benvenuti! Per suggerimenti o bug report:
- Apri un issue
- Invia una pull request
- Contatta il team di sviluppo

## 📄 License

FALCON è rilasciato sotto licenza MIT

**Versione**: 1.0  
**Ultimo Aggiornamento**: November 2025  
**Stato**: Demo

Buon cracking con FALCON! 🦅
