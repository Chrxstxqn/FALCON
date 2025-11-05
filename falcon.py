"""
FALCON - Flexible Authentication Login Cracking & Optimized Node
Terminal User Interface (TUI) Wrapper for Hashcat.
Created by Christian Schito - Chrxstxqn (https://github.com/Chrxstxqn/FALCON)
"""

import subprocess
import os
import sys
import time
from pathlib import Path
from typing import Optional, Dict, List
import shutil
import shlex  # usato per splittare le extra options in argomenti separati


class Colors:
    """Codici colore ANSI per il terminale"""
    # Colori principali
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    
    # Background
    BG_BLUE = "\033[44m"
    BG_RED = "\033[41m"
    
    # Style
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    
    # Bright colors
    BRIGHT_CYAN = "\033[36;1m"
    BRIGHT_GREEN = "\033[32;1m"
    BRIGHT_RED = "\033[31;1m"
    BRIGHT_YELLOW = "\033[33;1m"
    BRIGHT_MAGENTA = "\033[35;1m"


class FALCONLoader:
    """Schermata di caricamento animata per FALCON"""

    def display_loading_logo(self):
        """Logo ASCII art per la schermata principale"""
        logo = f"""
{Colors.BRIGHT_MAGENTA}{Colors.BOLD}


░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
        Flexible Authentication Login Cracking & Optimized Node
                        v1.0 - by Chrxstxqn
        Official Repository: https://github.com/Chrxstxqn/FALCON
{Colors.RESET}
        """
        return logo

    @staticmethod
    def display_loading_screen():
        loader = FALCONLoader()
        os.system("clear" if os.name == "posix" else "cls")

        print(loader.display_loading_logo())
        print()

        # Animazione di caricamento
        loading_steps = [
            ("🔧", "Inizializzando FALCON..."),
            ("🧩", "Caricando moduli di attacco..."),
            ("⚙️", "Configurando engine hashcat..."),
            ("🗄️", "Preparando database hash..."),
            ("💻", "Ottimizzando parametri GPU..."),
            ("🖥️", "Inizializzando interfaccia TUI..."),
            ("✅", "FALCON pronto all'utilizzo!"),
        ]

        for i, (emoji, step) in enumerate(loading_steps, 1):
            os.system("clear" if os.name == "posix" else "cls")
            print(loader.display_loading_logo())
            print()

            # Barra di progresso
            progress = int((i / len(loading_steps)) * 100)
            filled = int((progress / 100) * 40)
            bar = f"{Colors.BRIGHT_GREEN}{'█' * filled}{Colors.RESET}{Colors.DIM}{'░' * (40 - filled)}{Colors.RESET}"

            print(f"  ┌{'─' * 42}┐")
            print(f"  │ {bar} │")
            print(f"  └{'─' * 42}┘")
            print(f"  {Colors.BRIGHT_CYAN}{progress}%{Colors.RESET} - {Colors.BRIGHT_YELLOW}{emoji} {step}{Colors.RESET}")
            print()

            # Effetto terminale stile hacking
            hacking_chars = ["█", "▓", "▒", "░", "▯"]
            for j in range(2):
                chars = ''.join(chr(33 + (k + j) % 94) for k in range(15))
                print(f"  {Colors.DIM}$ {chars}{Colors.RESET}")

            time.sleep(0.35)  # Velocizzato da 0.6 a 0.35

        # Schermata finale
        os.system("clear" if os.name == "posix" else "cls")
        print(loader.display_loading_logo())
        print()
        print(f"  {Colors.BRIGHT_GREEN}┌────────────────────────────────────────────┐{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}│{Colors.RESET}     ✓ FALCON CARICATO CORRETTAMENTE        {Colors.BRIGHT_GREEN}│{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}│{Colors.RESET}     Ready for Cracking Operations...       {Colors.BRIGHT_GREEN}│{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}└────────────────────────────────────────────┘{Colors.RESET}")
        print()
        time.sleep(1)


class FALCON:

    # Modalità di attacco di hashcat
    ATTACK_MODES = {
        "0": "Straight (Dictionary Attack)",
        "1": "Combination",
        "3": "Brute-force",
        "6": "Hybrid Wordlist + Mask",
        "7": "Hybrid Mask + Wordlist",
    }

    # Tipi di hash comuni
    HASH_TYPES = {
        "0": "MD5",
        "100": "SHA1",
        "1400": "SHA2-256",
        "1700": "SHA2-512",
        "3200": "bcrypt",
        "5500": "NetNTLMv2",
        "5600": "NetNTLMv2",
        "1000": "NTLM",
        "2500": "WPA/WPA2",
        "13100": "Kerberos 5 TGS-REP etype 23",
    }

    def __init__(self):
        self.config: Dict = {
            "hash_file": None,
            "hash_type": None,
            "attack_mode": None,
            "wordlist": None,
            "mask": None,
            "rules": None,
            "gpu": True,
            "workload": "3",
            "extra_options": "",
        }
        self.check_hashcat()

    def check_hashcat(self):
        """Verifica se hashcat è installato"""
        if not shutil.which("hashcat"):
            self.print_error("Hashcat non trovato nel PATH")
            self.print_info("Installa hashcat con: sudo apt install hashcat")
            sys.exit(1)

    def clear_screen(self):
        """Pulisce lo schermo"""
        os.system("clear" if os.name == "posix" else "cls")

    @staticmethod
    def display_main_logo():
        """Logo ASCII art per la schermata di caricamento"""
        logo = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}
    ███████╗ █████╗ ██╗      ██████╗ ██████╗ ███╗   ██╗
    ██╔════╝██╔══██╗██║     ██╔════╝██╔═══██╗████╗  ██║
    █████╗  ███████║██║     ██║     ██║   ██║██╔██╗ ██║
    ██╔══╝  ██╔══██║██║     ██║     ██║   ██║██║╚██╗██║
    ██║     ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
{Colors.RESET}
{Colors.BRIGHT_GREEN}
    ╔══════════════════════════════════════════════════════════════╗
    ║   Flexible Authentication Login Cracking & Optimized Node    ║
    ║                     v1.0 - by Chrxstxqn                      ║
    ║   Official Repository: https://github.com/Chrxstxqn/FALCON   ║
    ╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}
        """
        return logo

    def print_header(self, text: str):
        """Stampa un header colorato"""
        print()
        print(f"{Colors.BRIGHT_CYAN}{'=' * 60}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}  {text}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}{'=' * 60}{Colors.RESET}")
        print()

    def print_success(self, text: str):
        """Stampa messaggio di successo"""
        print(f"{Colors.BRIGHT_GREEN}✓ {text}{Colors.RESET}")

    def print_error(self, text: str):
        """Stampa messaggio di errore"""
        print(f"{Colors.BRIGHT_RED}✗ {text}{Colors.RESET}")

    def print_info(self, text: str):
        """Stampa messaggio informativo"""
        print(f"{Colors.BRIGHT_CYAN}ℹ {text}{Colors.RESET}")

    def print_warning(self, text: str):
        """Stampa messaggio di avvertimento"""
        print(f"{Colors.BRIGHT_YELLOW}⚠ {text}{Colors.RESET}")

    def show_menu(self, title: str, options: Dict[str, str]) -> str:
        """Mostra un menu colorato e ritorna la scelta dell'utente"""
        self.clear_screen()
        print(self.display_main_logo())
        self.print_header(title)

        for key, value in options.items():
            print(f"  {Colors.BRIGHT_CYAN}{key}{Colors.RESET}. {value}")

        print()
        choice = input(f"{Colors.BRIGHT_GREEN}> {Colors.RESET}").strip()

        if choice not in options:
            self.print_error("Opzione non valida!")
            input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            return self.show_menu(title, options)

        return choice

    def get_file_path(self, prompt: str) -> Optional[str]:
        """Chiede il percorso di un file e verifica che esista"""
        print()
        path_input = input(f"{Colors.BRIGHT_CYAN}{prompt}{Colors.RESET}: ").strip()

        if not path_input:
            return None

        path = Path(path_input).expanduser()

        if not path.exists():
            self.print_error(f"File non trovato: {path}")
            return self.get_file_path(prompt)

        return str(path)

    def select_hash_type(self) -> str:
        """Seleziona il tipo di hash"""
        self.clear_screen()
        print(self.display_main_logo())
        self.print_header("Seleziona Tipo di Hash")

        for code, name in self.HASH_TYPES.items():
            print(f"  {Colors.BRIGHT_YELLOW}{code:5}{Colors.RESET} - {name}")

        print()
        hash_type = input(f"{Colors.BRIGHT_GREEN}> {Colors.RESET}").strip()

        if hash_type not in self.HASH_TYPES:
            self.print_error("Tipo di hash non valido!")
            input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            return self.select_hash_type()

        self.print_success(f"Selezionato: {self.HASH_TYPES[hash_type]}")
        input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
        return hash_type

    def select_attack_mode(self) -> str:
        """Seleziona la modalità di attacco"""
        choice = self.show_menu("Seleziona Modalità di Attacco", self.ATTACK_MODES)
        self.print_success(f"Selezionato: {self.ATTACK_MODES[choice]}")
        input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
        return choice

    def configure_attack(self):
        """Configura i parametri dell'attacco"""
        while True:
            self.clear_screen()
            print(self.display_main_logo())
            self.print_header("Configurazione Attacco")

            print(f"{Colors.BRIGHT_YELLOW}Parametri Attuali:{Colors.RESET}")
            print(f"  1. Hash File:      {Colors.BRIGHT_CYAN}{self.config['hash_file'] or '(non impostato)'}{Colors.RESET}")
            print(f"  2. Hash Type:      {Colors.BRIGHT_CYAN}{self.HASH_TYPES.get(self.config['hash_type'], '(non impostato)')}{Colors.RESET}")
            print(f"  3. Attack Mode:    {Colors.BRIGHT_CYAN}{self.ATTACK_MODES.get(self.config['attack_mode'], '(non impostato)')}{Colors.RESET}")
            print(f"  4. Wordlist:       {Colors.BRIGHT_CYAN}{self.config['wordlist'] or '(non impostato)'}{Colors.RESET}")
            print(f"  5. Mask:           {Colors.BRIGHT_CYAN}{self.config['mask'] or '(non impostato)'}{Colors.RESET}")
            print(f"  6. Rules:          {Colors.BRIGHT_CYAN}{self.config['rules'] or '(non impostato)'}{Colors.RESET}")
            print(f"  7. GPU:            {Colors.BRIGHT_GREEN if self.config['gpu'] else Colors.BRIGHT_RED}{'Abilitata' if self.config['gpu'] else 'Disabilitata'}{Colors.RESET}")
            print(f"  8. Workload:       {Colors.BRIGHT_CYAN}{self.config['workload']}{Colors.RESET}")
            print(f"  9. Extra Options:  {Colors.BRIGHT_CYAN}{self.config['extra_options'] or '(nessuno)'}{Colors.RESET}")
            print(f"  0. Indietro")

            print()
            choice = input(f"{Colors.BRIGHT_GREEN}> {Colors.RESET}").strip()

            if choice == "0":
                break
            elif choice == "1":
                self.config["hash_file"] = self.get_file_path("Percorso file con hash")
            elif choice == "2":
                self.config["hash_type"] = self.select_hash_type()
            elif choice == "3":
                self.config["attack_mode"] = self.select_attack_mode()
            elif choice == "4":
                wordlist = self.get_file_path("Percorso wordlist")
                if wordlist:
                    self.config["wordlist"] = wordlist
            elif choice == "5":
                mask = input(f"{Colors.BRIGHT_CYAN}Inserisci mask pattern (es: ?a?a?a?a){Colors.RESET}: ").strip()
                if mask:
                    self.config["mask"] = mask
            elif choice == "6":
                rules = self.get_file_path("Percorso file regole")
                if rules:
                    self.config["rules"] = rules
            elif choice == "7":
                self.config["gpu"] = not self.config["gpu"]
                status = "abilitata" if self.config["gpu"] else "disabilitata"
                self.print_success(f"GPU {status}")
                input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            elif choice == "8":
                print()
                print(f"  {Colors.BRIGHT_YELLOW}1. 1 (Low){Colors.RESET}")
                print(f"  {Colors.BRIGHT_YELLOW}2. 2 (Default){Colors.RESET}")
                print(f"  {Colors.BRIGHT_YELLOW}3. 3 (High){Colors.RESET}")
                print(f"  {Colors.BRIGHT_YELLOW}4. 4 (Nightmare){Colors.RESET}")
                workload = input(f"{Colors.BRIGHT_GREEN}> {Colors.RESET}").strip()
                if workload in ["1", "2", "3", "4"]:
                    self.config["workload"] = workload
                    self.print_success("Workload aggiornato")
                    input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            elif choice == "9":
                extra = input(f"{Colors.BRIGHT_CYAN}Inserisci opzioni extra (es: --show --username){Colors.RESET}: ").strip()
                if extra is not None:
                    self.config["extra_options"] = extra
                    self.print_success("Opzioni aggiornate")
                    input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")

    def validate_config(self) -> bool:
        """Valida la configurazione prima di lanciare l'attacco"""
        if not self.config["hash_file"]:
            self.print_error("File con hash non impostato!")
            return False

        if not self.config["hash_type"]:
            self.print_error("Tipo di hash non impostato!")
            return False

        if not self.config["attack_mode"]:
            self.print_error("Modalità di attacco non impostata!")
            return False

        # Wordlist richiesta per alcune modalità (0 = straight, 1 = combination, 6 = hybrid wordlist+mask)
        if self.config["attack_mode"] in ["0", "1", "6"]:
            if not self.config["wordlist"]:
                self.print_error("Wordlist non impostata per questa modalità di attacco!")
                return False

        # Mask richiesta per modalità brute-force e hybrid
        if self.config["attack_mode"] in ["3", "6", "7"]:
            if not self.config["mask"]:
                self.print_error("Mask non impostata per questa modalità di attacco!")
                return False

        return True

    def build_command(self) -> List[str]:
        """Costruisce il comando hashcat"""
        cmd: List[str] = ["hashcat"]

        # Attack mode
        cmd.extend(["-a", str(self.config["attack_mode"])])

        # Hash type
        cmd.extend(["-m", str(self.config["hash_type"])])

        # Workload
        cmd.extend(["-w", str(self.config["workload"])])

        # GPU flag -> meglio passare come due argomenti separati
        if self.config["gpu"]:
            # -d indica device, 1 è un esempio; puoi cambiare/gestire device in seguito
            cmd.extend(["-d", "1"])

        # Rules
        if self.config["rules"]:
            cmd.extend(["-r", str(self.config["rules"])])

        # Hash file (obbligatorio)
        cmd.append(str(self.config["hash_file"]))

        # Wordlist (per modalità che lo supportano)
        if self.config["attack_mode"] in ["0", "1", "6"]:
            if self.config["wordlist"]:
                cmd.append(str(self.config["wordlist"]))

        # Mask (per modalità che lo supportano)
        if self.config["attack_mode"] in ["3", "6", "7"]:
            if self.config["mask"]:
                cmd.append(str(self.config["mask"]))

        # Extra options: splittiamo la stringa in argomenti reali
        if self.config["extra_options"]:
            try:
                extra_args = shlex.split(self.config["extra_options"])
                cmd.extend(extra_args)
            except Exception:
                # fallback: aggiungi la stringa così com'è
                cmd.append(self.config["extra_options"])

        return cmd

    def show_command_preview(self, cmd: List[str]):
        """Mostra un'anteprima del comando"""
        self.clear_screen()
        print(self.display_main_logo())
        self.print_header("Anteprima Comando")

        command_str = " ".join(shlex.quote(c) for c in cmd)
        print(f"Comando che sarà eseguito:\n")
        print(f"{Colors.BRIGHT_CYAN}{command_str}{Colors.RESET}\n")

        print(f"{Colors.BRIGHT_YELLOW}Parametri Configurati:{Colors.RESET}")
        print(f"  Attack Mode:  {Colors.GREEN}{self.ATTACK_MODES.get(self.config.get('attack_mode',''))}{Colors.RESET}")
        print(f"  Hash Type:    {Colors.GREEN}{self.HASH_TYPES.get(self.config.get('hash_type',''))}{Colors.RESET}")
        print(f"  Hash File:    {Colors.GREEN}{self.config.get('hash_file')}{Colors.RESET}")
        print(f"  Wordlist:     {Colors.GREEN}{self.config.get('wordlist')}{Colors.RESET}")
        print(f"  Mask:         {Colors.GREEN}{self.config.get('mask')}{Colors.RESET}")
        print(f"  Rules:        {Colors.GREEN}{self.config.get('rules')}{Colors.RESET}")
        print(f"  GPU:          {Colors.GREEN}{'Abilitata' if self.config['gpu'] else 'Disabilitata'}{Colors.RESET}")
        print()

        choice = input(f"{Colors.BRIGHT_CYAN}Vuoi continuare? (s/n){Colors.RESET}: ").strip().lower()
        return choice == "s"

    def run_attack(self):
        """Esegue l'attacco hashcat"""
        if not self.validate_config():
            input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            return

        cmd = self.build_command()

        if not self.show_command_preview(cmd):
            self.print_info("Attacco annullato")
            input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")
            return

        self.clear_screen()
        print(self.display_main_logo())
        self.print_header("Esecuzione Attacco")
        print(f"{Colors.BRIGHT_YELLOW}L'attacco è in corso...{Colors.RESET}\n")

        try:
            # Esegui il comando (cmd è una lista di argomenti)
            result = subprocess.run(cmd, check=False)
            if result.returncode == 0:
                self.print_success("Attacco completato con successo!")
            elif result.returncode == 1:
                self.print_warning("Attacco completato: nessuna password trovata")
            else:
                self.print_error(f"Errore durante l'esecuzione (codice: {result.returncode})")
        except Exception as e:
            self.print_error(f"Errore: {str(e)}")

        print()
        input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")

    def show_examples(self):
        """Mostra esempi di utilizzo"""
        self.clear_screen()
        print(self.display_main_logo())
        self.print_header("Esempi di Utilizzo")

        examples = f"""
{Colors.BRIGHT_YELLOW}ATTACCO DIZIONARIO (MD5):{Colors.RESET}
  - Attack Mode: Straight (0)
  - Hash Type: MD5 (0)
  - Wordlist: /path/to/wordlist.txt

{Colors.BRIGHT_YELLOW}ATTACCO BRUTE-FORCE (8 caratteri alfanumerici):{Colors.RESET}
  - Attack Mode: Brute-force (3)
  - Hash Type: MD5 (0)
  - Mask: ?a?a?a?a?a?a?a?a

{Colors.BRIGHT_YELLOW}ATTACCO IBRIDO (Wordlist + Mask):{Colors.RESET}
  - Attack Mode: Hybrid Wordlist + Mask (6)
  - Hash Type: bcrypt (3200)
  - Wordlist: /path/to/wordlist.txt
  - Mask: ?d?d

{Colors.BRIGHT_YELLOW}ATTACCO CON REGOLE:{Colors.RESET}
  - Attack Mode: Straight (0)
  - Hash Type: SHA1 (100)
  - Wordlist: /path/to/wordlist.txt
  - Rules: /path/to/rules.txt

{Colors.BRIGHT_CYAN}PATTERN MASK:{Colors.RESET}
  ?l = carattere minuscolo (a-z)
  ?u = carattere maiuscolo (A-Z)
  ?d = cifra (0-9)
  ?s = carattere speciale
  ?a = tutto (?l?u?d?s)
  ?b = non-ASCII (0x80-0xff)
  ?1-?4 = charset custom
        """

        print(examples)
        input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")

    def show_presets(self):
        """Mostra preset configurati"""
        presets = {
            "1": ("MD5 Dictionary", {
                "hash_type": "0",
                "attack_mode": "0",
            }),
            "2": ("SHA1 Dictionary", {
                "hash_type": "100",
                "attack_mode": "0",
            }),
            "3": ("8 Char Brute-force", {
                "hash_type": "0",
                "attack_mode": "3",
                "mask": "?a?a?a?a?a?a?a?a",
            }),
            "4": ("6 Digit PIN", {
                "hash_type": "0",
                "attack_mode": "3",
                "mask": "?d?d?d?d?d?d",
            }),
            "5": ("bcrypt Dictionary", {
                "hash_type": "3200",
                "attack_mode": "0",
            }),
        }

        choice = self.show_menu("Seleziona Preset", {
            k: f"{v[0]}" for k, v in presets.items()
        })

        if choice in presets:
            preset_config = presets[choice][1]
            for key, value in preset_config.items():
                self.config[key] = value

            self.print_success(f"Preset '{presets[choice][0]}' applicato!")
            input(f"{Colors.DIM}Premi Enter per continuare...{Colors.RESET}")

    def main_menu(self):
        """Menu principale"""
        while True:
            menu_options = {
                "1": "Configura Attacco",
                "2": "Visualizza Preset",
                "3": "Esegui Attacco",
                "4": "Mostra Esempi",
                "5": "Anteprima Comando",
                "0": "Esci",
            }

            choice = self.show_menu("FALCON - Menu Principale", menu_options)

            if choice == "1":
                self.configure_attack()
            elif choice == "2":
                self.show_presets()
            elif choice == "3":
                self.run_attack()
            elif choice == "4":
                self.show_examples()
            elif choice == "5":
                if self.validate_config():
                    cmd = self.build_command()
                    self.show_command_preview(cmd)
            elif choice == "0":
                self.clear_screen()
                print(f"\n  {Colors.BRIGHT_MAGENTA}{'█' * 40}{Colors.RESET}")
                print(f"  {Colors.BRIGHT_MAGENTA}║ {Colors.RESET}Grazie per aver usato FALCON!{Colors.BRIGHT_MAGENTA} ║{Colors.RESET}")
                print(f"  {Colors.BRIGHT_MAGENTA}{'█' * 40}{Colors.RESET}\n")
                sys.exit(0)

    def run(self):
        """Avvia l'applicazione"""
        try:
            FALCONLoader.display_loading_screen()
            self.main_menu()
        except KeyboardInterrupt:
            self.clear_screen()
            print(f"\n{Colors.BRIGHT_RED}Interrotto dall'utente. Arrivederci!{Colors.RESET}\n")
            sys.exit(0)


if __name__ == "__main__":
    app = FALCON()
    app.run()