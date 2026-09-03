import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """
    Inyecta CSS global garantizando la separación de responsabilidades.
    Ajusta el color del panel lateral a la imagen de referencia y 
    aplica bordes Cyan a todas las cajas de entrada.
    """
    css = """
    <style>
        /* --- FONDO PRINCIPAL Y TIPOGRAFÍA --- */
        .stApp { background-color: #060B15 !important; }
        
        .texto-principal { font-size: 1.125rem !important; color: #F8FAFC; line-height: 1.6; text-align: justify; }
        h1 { color: #00E5FF !important; font-size: 2.5rem !important; font-weight: 800; text-align: center; text-shadow: 0 0 10px rgba(0, 229, 255, 0.3); }
        h2, h3 { color: #F8FAFC !important; font-size: 1.75rem !important; text-align: center; margin-bottom: 0.5rem; }
        
        .metadato-home { color: #8B9BB4 !important; font-size: 1.1rem !important; text-transform: uppercase; text-align: center; display: block; margin-bottom: 2.5rem; font-weight: bold; }
        .metadato { color: #8B9BB4 !important; font-size: 0.875rem !important; text-transform: uppercase; font-weight: 600; }
        
        /* --- NAVEGACIÓN LATERAL (SIDEBAR) --- */
        [data-testid="stSidebar"] { 
            background-color: #0127C0 !important; /* Panel lateral ajustado al color de la imagen */
            border-right: 1px solid #2A3F5F; 
        }
        
        /* --- CORRECCIÓN DE CAJAS DE ENTRADA (INPUTS) --- */
        div[data-baseweb="input"] { 
            background-color: #111A2C !important; 
            border: 2px solid #00E5FF !important; /* Borde Cyan #00E5FF aplicado a todas las cajas */
            border-radius: 6px !important; 
        }
        div[data-baseweb="input"]:focus-within { 
            border-color: #00E5FF !important; 
            box-shadow: 0 0 8px rgba(0, 229, 255, 0.6) !important; /* Resplandor más fuerte al hacer clic */
        }
        div[data-baseweb="input"] input { 
            color: #00E5FF !important; 
            -webkit-text-fill-color: #00E5FF !important; 
            font-weight: bold !important; 
            font-size: 1.1rem !important; 
        }
        
        /* --- OPCIONES DEL MENÚ COMO BOTONES RESALTADOS (Home y Ejercicios) --- */
        [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label {
            background-color: #3282B8 !important; 
            padding: 12px 15px !important;
            border-radius: 8px !important;
            margin-bottom: 12px !important;
            border: 1px solid #00E5FF !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
        }
        [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:hover {
            background-color: #00E5FF !important; 
            border-color: #F8FAFC !important;
            transform: translateX(4px); 
        }
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div { 
            font-size: 1.25rem !important; 
            font-weight: 700 !important; 
            color: #F8FAFC !important; 
            padding: 0 !important; 
            margin: 0 !important;
            transition: color 0.3s ease !important;
        }
        [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:hover p {
            color: #060B15 !important; 
        }
        
        /* --- TABS (PRODUCCIÓN, PERFORACIÓN, RESERVORIOS) --- */
        [data-testid="stTabs"] button[data-baseweb="tab"] p,
        [data-testid="stTabs"] button[data-baseweb="tab"] div { font-size: 1.3rem !important; font-weight: bold !important; color: #8B9BB4 !important; }
        [data-testid="stTabs"] button[aria-selected="true"] p { color: #00E5FF !important; text-shadow: 0 0 8px rgba(0, 229, 255, 0.5); }
        
        /* --- TARJETA INFO HOME --- */
        .tarjeta-info {
            background-color: #111A2C; padding: 35px; border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.5); border-top: 4px solid #00E5FF;
            margin: 0 auto; max-width: 850px; border: 1px solid #1A273D;
        }

        /* --- TAB PRODUCCIÓN: TARJETAS Y BOTONES --- */
        .tarjeta-produccion {
            background-color: #111A2C; padding: 20px; border-radius: 8px;
            border-left: 4px solid #FF7A00; margin-bottom: 1rem; border: 1px solid #1A273D;
        }
        .valor-destacado-prod { font-size: 1.85rem !important; font-weight: 900; color: #F8FAFC; margin-top: 5px; text-shadow: 0 0 10px rgba(255, 122, 0, 0.2); }
        
        .stButton>button { 
            background: #111A2C !important; color: #F8FAFC !important; 
            border: 1px solid #2A3F5F !important; border-radius: 6px !important; width: 100%; 
            position: relative; overflow: hidden; transition: all 0.3s ease !important;
        }
        .stButton>button:hover { border-color: #FF7A00 !important; box-shadow: 0 0 15px rgba(255, 122, 0, 0.4) !important; color: #FF7A00 !important; }
        
        .ripple-fluido {
            position: absolute; background: radial-gradient(circle, rgba(255, 122, 0, 0.8) 0%, rgba(255, 122, 0, 0) 70%);
            border-radius: 50%; transform: scale(0); animation: animacionRippleLiq 0.8s cubic-bezier(0.1, 0.7, 0.3, 1);
            pointer-events: none; width: 300px; height: 300px; margin-top: -150px; margin-left: -150px;
        }
        @keyframes animacionRippleLiq { to { transform: scale(3); opacity: 0; } }

        /* --- TAB PERFORACIÓN: TARJETAS MAGNÉTICAS 3D --- */
        .tarjeta-magnetica {
            background-color: #111A2C; padding: 20px; border-radius: 8px;
            border-left: 4px solid #B026FF; margin-bottom: 1rem; border: 1px solid #1A273D;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
            transform: perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1);
        }
        .tarjeta-magnetica:hover { 
            transform: perspective(1000px) rotateX(5deg) rotateY(-5deg) scale3d(1.05, 1.05, 1.05);
            box-shadow: -8px 12px 20px rgba(176, 38, 255, 0.3); border-color: #B026FF;
        }
        .valor-destacado-perf { font-size: 1.85rem !important; font-weight: 900; color: #F8FAFC; margin-top: 5px; text-shadow: 0 0 10px rgba(176, 38, 255, 0.2); }

        /* --- TAB RESERVORIOS: POP-IN CASCADA --- */
        .tarjeta-reservorio {
            background-color: #111A2C; padding: 20px; border-radius: 8px;
            border-left: 4px solid #00B4D8; margin-bottom: 1rem; border: 1px solid #1A273D;
            opacity: 0; animation: popIn 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
        }
        .delay-1 { animation-delay: 0.1s; }
        .delay-2 { animation-delay: 0.3s; }
        .delay-3 { animation-delay: 0.5s; }
        @keyframes popIn { 0% { opacity: 0; transform: scale(0.8) translateY(20px); } 100% { opacity: 1; transform: scale(1) translateY(0); } }
        .valor-destacado-res { font-size: 1.85rem !important; font-weight: 900; color: #F8FAFC; margin-top: 5px; text-shadow: 0 0 10px rgba(0, 180, 216, 0.2); }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- FUNCIONES DE RENDERIZADO HTML ---
def renderizar_tarjeta_info(texto):
    html = f"""<div class="tarjeta-info"><p class="texto-principal">{texto}</p></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_produccion(titulo, valor, unidad=""):
    html = f"""<div class="tarjeta-produccion"><div class="metadato">{titulo}</div><div class="valor-destacado-prod">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_magnetica(titulo, valor, unidad=""):
    html = f"""<div class="tarjeta-magnetica"><div class="metadato">{titulo}</div><div class="valor-destacado-perf">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

def renderizar_tarjeta_reservorio(titulo, valor, unidad, delay_class):
    html = f"""<div class="tarjeta-reservorio {delay_class}"><div class="metadato">{titulo}</div><div class="valor-destacado-res">{valor:,.2f} {unidad}</div></div>"""
    st.markdown(html, unsafe_allow_html=True)

# --- INTERACTIVIDAD JS ---
def inyectar_js_animacion():
    js = """<script>
        document.addEventListener("DOMContentLoaded", function() {
            const doc = window.parent.document;
            
            function iniciarCyberText() {
                const titulos = doc.querySelectorAll('h1');
                titulos.forEach(element => {
                    if (element.dataset.cyberDone) return;
                    const originalText = element.innerText;
                    const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*<>";
                    let iteraciones = 0;
                    element.dataset.cyberDone = "true";
                    
                    const intervalo = setInterval(() => {
                        element.innerText = originalText.split("").map((letra, index) => {
                            if (index < iteraciones || letra === " ") return originalText[index];
                            return caracteres[Math.floor(Math.random() * caracteres.length)];
                        }).join("");
                        if (iteraciones >= originalText.length) clearInterval(intervalo);
                        iteraciones += 0.5;
                    }, 30);
                });
            }

            function configurarRipples() {
                const botones = doc.querySelectorAll('.stButton > button');
                botones.forEach(btn => {
                    if (!btn.dataset.rippleActivo) {
                        btn.dataset.rippleActivo = "true";
                        btn.addEventListener('mousedown', function(e) {
                            const rect = btn.getBoundingClientRect();
                            const x = e.clientX - rect.left;
                            const y = e.clientY - rect.top;
                            const ripple = doc.createElement('span');
                            ripple.classList.add('ripple-fluido');
                            ripple.style.left = x + 'px';
                            ripple.style.top = y + 'px';
                            btn.appendChild(ripple);
                            setTimeout(() => ripple.remove(), 600);
                        });
                    }
                });
            }

            const observer = new MutationObserver(() => {
                iniciarCyberText();
                configurarRipples();
            });
            observer.observe(doc.body, { childList: true, subtree: true });
            
            setTimeout(() => { iniciarCyberText(); configurarRipples(); }, 500);
        });
    </script>"""
    components.html(js, height=0)

# --- CONTROLADORES GRÁFICOS MATPLOTLIB ---
def configurar_grafico_oscuro(ax, color_acento):
    ax.set_facecolor('#111A2C')
    ax.tick_params(colors='#8B9BB4')
    for spine in ax.spines.values():
        spine.set_color('#2A3F5F')
    ax.grid(True, linestyle='--', alpha=0.3, color='#8B9BB4')
    ax.xaxis.label.set_color(color_acento)
    ax.yaxis.label.set_color(color_acento)

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_produccion("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta_produccion("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta_produccion("Caudal Máximo", qmax, "STB/d")
    
    _, col_graf, _ = st.columns([1, 3, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#060B15') 
        configurar_grafico_oscuro(ax, '#FF7A00')
        ax.plot(q_arr, p_arr, color='#FF7A00', linewidth=2.5, label='Curva IPR')
        ax.scatter(qo, pwf, color='#00E5FF', s=100, zorder=5, label='Punto Operativo')
        ax.set_xlabel('Caudal (STB/d)', fontweight='bold')
        ax.set_ylabel('Pwf (psi)', fontweight='bold')
        legend = ax.legend(facecolor='#111A2C', edgecolor='#2A3F5F')
        for text in legend.get_texts(): text.set_color('#F8FAFC')
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_perforacion(gh, ph, dp, tvd, pform):
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_magnetica("Gradiente", gh, "psi/ft")
    with c2: renderizar_tarjeta_magnetica("P. Hidrostática", ph, "psi")
    with c3: renderizar_tarjeta_magnetica("Diferencial (\u0394P)", dp, "psi")
    
    _, col_graf, _ = st.columns([1, 1, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(3.5, 5))
        fig.patch.set_facecolor('#060B15')
        configurar_grafico_oscuro(ax, '#B026FF')
        ax.plot([0, ph], [0, tvd], color='#B026FF', linewidth=2.5, label='P. Hidrostática')
        ax.scatter(pform, tvd, color='#00E5FF', s=100, label='P. Formación')
        ax.invert_yaxis()
        ax.set_xlabel('Presión (psi)', fontweight='bold')
        ax.set_ylabel('Profundidad TVD (ft)', fontweight='bold')
        legend = ax.legend(facecolor='#111A2C', edgecolor='#2A3F5F')
        for text in legend.get_texts(): text.set_color('#F8FAFC')
        st.pyplot(fig, use_container_width=True)

def mostrar_panel_reservorios(hn, p_mmstb, r_mmstb):
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_reservorio("Espesor Neto", hn, "ft", "delay-1")
    with c2: renderizar_tarjeta_reservorio("POES", p_mmstb, "MMSTB", "delay-2")
    with c3: renderizar_tarjeta_reservorio("Reservas Rec.", r_mmstb, "MMSTB", "delay-3")
    
    _, col_graf, _ = st.columns([1, 2, 1])
    with col_graf:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        fig.patch.set_facecolor('#060B15')
        configurar_grafico_oscuro(ax, '#00B4D8')
        ax.bar(['POES Original', 'Recuperable'], [p_mmstb, r_mmstb], color=['#00B4D8', '#00E5FF'], width=0.5)
        ax.set_ylabel('Volumen (MMSTB)', fontweight='bold')
        st.pyplot(fig, use_container_width=True)
