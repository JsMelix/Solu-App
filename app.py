# Metaverse AI App en Python 🚀

Esta app está creada con **Python + CustomTkinter** y tiene una interfaz moderna estilo metaverso con:

* Fondo oscuro futurista
* Colores neón
* Paneles glassmorphism
* Chat estilo IA
* Diseño minimalista y moderno

---

# 📦 Instalación

Primero instala las dependencias:

```bash
pip install customtkinter pillow
```

---

# 🧠 Código Completo

Guarda este archivo como:

```bash
app.py
```

```python
import customtkinter as ctk
from PIL import Image

# Configuración inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.geometry("1400x850")
app.title("Metaverse AI")
app.configure(fg_color="#050816")

# =========================
# HEADER
# =========================
header = ctk.CTkFrame(
    app,
    fg_color="#0b1120",
    corner_radius=0,
    height=80
)
header.pack(fill="x")

logo = ctk.CTkLabel(
    header,
    text="◉ METAVERSE AI",
    font=("Orbitron", 30, "bold"),
    text_color="#00F5FF"
)
logo.pack(side="left", padx=30, pady=20)

status = ctk.CTkLabel(
    header,
    text="SYSTEM ONLINE",
    font=("Arial", 16),
    text_color="#00FF99"
)
status.pack(side="right", padx=30)

# =========================
# SIDEBAR
# =========================
sidebar = ctk.CTkFrame(
    app,
    width=260,
    fg_color="#09101d",
    corner_radius=0
)
sidebar.pack(side="left", fill="y")

menu_title = ctk.CTkLabel(
    sidebar,
    text="NAVIGATION",
    font=("Orbitron", 20, "bold"),
    text_color="#7DF9FF"
)
menu_title.pack(pady=(30,20))

buttons = [
    "Dashboard",
    "AI Assistant",
    "Hackathons",
    "Metaverse",
    "Settings"
]

for item in buttons:
    btn = ctk.CTkButton(
        sidebar,
        text=item,
        fg_color="#111827",
        hover_color="#00F5FF",
        text_color="white",
        corner_radius=15,
        height=50,
        font=("Arial", 16, "bold")
    )
    btn.pack(padx=20, pady=10, fill="x")

# =========================
# MAIN CONTENT
# =========================
main = ctk.CTkFrame(
    app,
    fg_color="#050816"
)
main.pack(expand=True, fill="both")

hero = ctk.CTkFrame(
    main,
    fg_color="#0b1120",
    corner_radius=25,
    border_width=1,
    border_color="#00F5FF"
)
hero.pack(padx=30, pady=30, fill="x")

hero_title = ctk.CTkLabel(
    hero,
    text="WELCOME TO THE FUTURE",
    font=("Orbitron", 42, "bold"),
    text_color="#00F5FF"
)
hero_title.pack(pady=(30,10))

hero_subtitle = ctk.CTkLabel(
    hero,
    text="Build AI agents, metaverse experiences and hackathon projects.",
    font=("Arial", 18),
    text_color="#cbd5e1"
)
hero_subtitle.pack(pady=(0,30))

# =========================
# CHAT SECTION
# =========================
chat_frame = ctk.CTkFrame(
    main,
    fg_color="#0f172a",
    corner_radius=25,
    border_width=1,
    border_color="#8B5CF6"
)
chat_frame.pack(padx=30, pady=10, fill="both", expand=True)

chat_title = ctk.CTkLabel(
    chat_frame,
    text="AI CHAT",
    font=("Orbitron", 28, "bold"),
    text_color="#8B5CF6"
)
chat_title.pack(pady=20)

chat_box = ctk.CTkTextbox(
    chat_frame,
    height=400,
    fg_color="#111827",
    text_color="#E2E8F0",
    corner_radius=20,
    border_width=1,
    border_color="#00F5FF",
    font=("Consolas", 15)
)
chat_box.pack(padx=20, pady=10, fill="both", expand=True)

chat_box.insert("end", "🤖 AI SYSTEM READY...\n")
chat_box.insert("end", "🌌 Welcome to the Metaverse Interface\n\n")

# =========================
# INPUT AREA
# =========================
input_frame = ctk.CTkFrame(
    chat_frame,
    fg_color="transparent"
)
input_frame.pack(fill="x", padx=20, pady=20)

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Ask the AI something...",
    height=55,
    corner_radius=20,
    border_color="#00F5FF",
    fg_color="#111827",
    text_color="white",
    font=("Arial", 15)
)
entry.pack(side="left", fill="x", expand=True, padx=(0,15))

# Función para enviar mensajes

def send_message():
    user_message = entry.get()

    if user_message.strip() != "":
        chat_box.insert("end", f"🧑 You: {user_message}\n")
        chat_box.insert("end", f"🤖 AI: Processing request in the metaverse...\n\n")
        entry.delete(0, "end")

send_btn = ctk.CTkButton(
    input_frame,
    text="SEND",
    width=140,
    height=55,
    corner_radius=20,
    fg_color="#8B5CF6",
    hover_color="#00F5FF",
    text_color="white",
    font=("Orbitron", 16, "bold"),
    command=send_message
)
send_btn.pack(side="right")

# =========================
# FOOTER
# =========================
footer = ctk.CTkLabel(
    app,
    text="Powered by Python • AI • Metaverse UI",
    font=("Arial", 14),
    text_color="#64748B"
)
footer.pack(pady=10)

# Ejecutar aplicación
app.mainloop()
```

