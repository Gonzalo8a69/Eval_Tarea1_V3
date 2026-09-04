import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def aplicar_estilos():
    """
    Inyecta CSS global garantizando la separación de responsabilidades visuales y lógicas.
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
        section[data-testid="stSidebar"], 
        section[data-testid="stSidebar"] > div:first-child,
        section[data-testid="stSidebar"] > div:first-child > div { 
            background-color: #1A56B6 !important; 
        }
        section[data-testid="stSidebar"] {
            border-right: 1px solid #2A3F5F !important; 
        }
        
        /* --- CAJAS DE ENTRADA (INPUTS) --- */
        div[data-baseweb="input"] { 
            background-color: #111A2C !important; 
            border: 2px solid #00E5FF !important; 
            border-radius: 6px !important; 
        }
        div[data-baseweb="input"]:focus-within { 
            border-color: #00E5FF !important; 
            box-shadow: 0 0 8px rgba(0, 229, 255, 0.6) !important; 
        }
        div[data-baseweb="input"] input { 
            color: #00E5FF !important; 
            -webkit-text-fill-color: #00E5FF !important; 
            font-weight: bold !important; 
            font-size: 1.1rem !important; 
        }
        
        /* --- OPCIONES DEL MENÚ (Home y Ejercicios) --- */
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
        
        /* --- TABS --- */
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
            transition: all 0.3s ease;
        }
        .tarjeta-produccion:hover {
            border-color: #FF7A00;
            box-shadow: 0 6px 15px rgba(255, 122, 0, 0.3);
            transform: translateY(-3px);
        }
        .valor-destacado-prod { font-size: 1.85rem !important; font-weight: 900; color: #F8FAFC; margin-top: 5px; text-shadow: 0 0 10px rgba(255, 122, 0, 0.2); }
        
        .stButton>button { 
            background: #111A2C !important; color: #F8FAFC !important; 
            border: 1px solid #2A3F5F !important; border-radius: 6px !important; width: 100%; 
            position: relative; overflow: hidden; transition: all 0.3s ease !important;
        }
        .stButton>button:hover { border-color: #FF7A00 !important; box-shadow: 0 0 15px rgba(255, 122, 0, 0.4) !important; color: #FF7A00 !important; }
        
        /* Ripple JavaScript */
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

        /* --- TAB RESERVORIOS: POP-IN CASCADA Y HOVER --- */
        .tarjeta-reservorio {
            background-color: #111A2C; padding: 20px; border-radius: 8px;
            border-left: 4px solid #00B4D8; margin-bottom: 1rem; border: 1px solid #1A273D;
            opacity: 0; animation: popIn 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
            transition: all 0.3s ease; 
        }
        .tarjeta-reservorio:hover {
            border-color: #00B4D8;
            box-shadow: 0 6px 15px rgba(0, 180, 216, 0.4);
            transform: translateY(-3px) scale(1.02);
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

# --- CONTROLADORES GRÁFICOS ---
def configurar_grafico_oscuro(ax, color_acento):
    """Configuración residual para las gráficas que aún utilicen Matplotlib."""
    pass

def mostrar_panel_ipr(qo, qb, qmax, pwf, q_arr, p_arr):
    """PANEL PRODUCCIÓN"""
    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_produccion("Caudal Actual", qo, "STB/d")
    with c2: renderizar_tarjeta_produccion("Caudal a Burbuja", qb, "STB/d")
    with c3: renderizar_tarjeta_produccion("Caudal Máximo", qmax, "STB/d")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    _, col_graf, _ = st.columns([0.2, 8, 0.2])
    with col_graf:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=q_arr, y=p_arr,
            mode='lines',
            name='Curva IPR',
            line=dict(color='#FF7A00', width=4),
            hovertemplate='Caudal: %{x:.1f} STB/d<br>Pwf: %{y:.1f} psi<extra></extra>'
        ))

        fig.add_trace(go.Scatter(
            x=[qo], y=[pwf],
            mode='markers',
            name='Punto Operativo',
            marker=dict(color='#00E5FF', size=16, line=dict(color='#060B15', width=2)),
            hovertemplate='<b>Punto Actual</b><br>Caudal: %{x:.1f} STB/d<br>Pwf: %{y:.1f} psi<extra></extra>'
        ))

        fig.update_layout(
            title=dict(
                text='Análisis de Desempeño de Afluencia (Curva IPR)',
                font=dict(size=22, color='#060B15', weight='bold'),
                x=0.5,
                y=0.95
            ),
            height=550, 
            plot_bgcolor='#F4F6F9', 
            paper_bgcolor='#F4F6F9', 
            xaxis_title=dict(text='Caudal (STB/d)', font=dict(size=18, color='#060B15', weight='bold')),
            yaxis_title=dict(text='Presión de Fondo Pwf (psi)', font=dict(size=18, color='#060B15', weight='bold')),
            xaxis=dict(
                showgrid=True, gridcolor='#D1D5DB', zeroline=False, 
                tickfont=dict(size=14, color='#060B15', weight='bold')
            ),
            yaxis=dict(
                showgrid=True, gridcolor='#D1D5DB', zeroline=False, 
                tickfont=dict(size=14, color='#060B15', weight='bold')
            ),
            legend=dict(
                yanchor="top", y=0.85, xanchor="right", x=0.98, 
                bgcolor="rgba(255,255,255,0.9)", 
                bordercolor="#060B15", borderwidth=1,
                font=dict(size=14, color='#060B15', weight='bold')
            ),
            margin=dict(l=20, r=20, t=60, b=20), 
            hovermode="closest"
        )

        st.plotly_chart(fig, use_container_width=True)

def mostrar_panel_perforacion(gh, ph, dp, tvd, pform):
    """PANEL PERFORACIÓN"""
    if dp > 50:
        estado = "SOBREBALANCE (ΔP > 0)"
        color_borde = "#00B4D8" 
        mensaje = "La presión hidrostática supera a la de formación. El pozo está bajo control."
    elif abs(dp) <= 50:
        estado = "BALANCE APROXIMADO (ΔP ≈ 0)"
        color_borde = "#FF7A00" 
        mensaje = "La presión hidrostática está en equilibrio con la formación."
    else:
        estado = "BAJO BALANCE (ΔP < 0) - ¡ALERTA!"
        color_borde = "#FF2A2A" 
        mensaje = "La presión de formación supera a la hidrostática. Riesgo inminente de influjo (Kick)."

    html_estado = f"""
    <div style="background-color: #111A2C; border: 1px solid #1A273D; border-left: 6px solid {color_borde}; padding: 15px 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.4);">
        <h3 style="color: {color_borde}; margin-top: 0; margin-bottom: 5px; font-size: 1.5rem; text-shadow: 0 0 8px {color_borde}60;">ESTADO OPERATIVO: {estado}</h3>
        <p style="color: #F8FAFC; margin: 0; font-size: 1.1rem;">{mensaje}</p>
    </div>
    """
    st.markdown(html_estado, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_magnetica("Gradiente", gh, "psi/ft")
    with c2: renderizar_tarjeta_magnetica("P. Hidrostática", ph, "psi")
    with c3: renderizar_tarjeta_magnetica("Diferencial (\u0394P)", dp, "psi")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    _, col_graf, _ = st.columns([0.2, 8, 0.2])
    with col_graf:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=[0, ph], y=[0, tvd],
            mode='lines',
            name='P. Hidrostática',
            line=dict(color='#B026FF', width=4),
            hovertemplate='Presión: %{x:.1f} psi<br>Profundidad: %{y:.1f} ft<extra></extra>'
        ))

        fig.add_trace(go.Scatter(
            x=[pform], y=[tvd],
            mode='markers',
            name='P. Formación',
            marker=dict(color='#00E5FF', size=16, line=dict(color='#060B15', width=2)), 
            hovertemplate='<b>Formación</b><br>Presión: %{x:.1f} psi<br>Profundidad: %{y:.1f} ft<extra></extra>'
        ))

        fig.update_layout(
            title=dict(
                text='Perfil de Presión Hidrostática vs TVD',
                font=dict(size=22, color='#060B15', weight='bold'),
                x=0.5,
                y=0.95
            ),
            height=550, 
            plot_bgcolor='#F4F6F9', 
            paper_bgcolor='#F4F6F9', 
            xaxis_title=dict(text='Presión (psi)', font=dict(size=18, color='#060B15', weight='bold')),
            yaxis_title=dict(text='Profundidad TVD (ft)', font=dict(size=18, color='#060B15', weight='bold')),
            xaxis=dict(
                showgrid=True, gridcolor='#D1D5DB', zeroline=False, 
                tickfont=dict(size=14, color='#060B15', weight='bold')
            ),
            yaxis=dict(
                showgrid=True, gridcolor='#D1D5DB', zeroline=False, 
                autorange='reversed', 
                tickfont=dict(size=14, color='#060B15', weight='bold')
            ),
            legend=dict(
                yanchor="top", y=0.85, xanchor="right", x=0.98, 
                bgcolor="rgba(255,255,255,0.9)", 
                bordercolor="#060B15", borderwidth=1,
                font=dict(size=14, color='#060B15', weight='bold')
            ),
            margin=dict(l=20, r=20, t=60, b=20),
            hovermode="closest"
        )

        st.plotly_chart(fig, use_container_width=True)

def mostrar_panel_reservorios(hn, p_mmstb, r_mmstb):
    """
    PANEL RESERVORIOS:
    Se generan gráficas de barras comparativas utilizando Plotly para cumplir
    con los requisitos visuales de la rúbrica, garantizando colores llamativos.
    """
    # Cálculo para visualización en STB y cumplir con mostrar ambas unidades sin alterar parámetros de app.py
    p_stb = p_mmstb * 1_000_000
    r_stb = r_mmstb * 1_000_000

    c1, c2, c3 = st.columns(3)
    with c1: renderizar_tarjeta_reservorio("Espesor Neto", hn, "ft", "delay-1")
    with c2: renderizar_tarjeta_reservorio("POES", p_mmstb, "MMSTB", "delay-2")
    with c3: renderizar_tarjeta_reservorio("Reservas Rec.", r_mmstb, "MMSTB", "delay-3")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    _, col_graf, _ = st.columns([0.2, 8, 0.2])
    with col_graf:
        fig = go.Figure()

        # Gráfico de barras combinando colores que contrastan (Azul Verdoso y Naranja Radiante)
        fig.add_trace(go.Bar(
            x=['POES Original', 'Reservas Recuperables'],
            y=[p_mmstb, r_mmstb],
            marker_color=['#00B4D8', '#FF7A00'], 
            text=[f"{p_mmstb:,.2f} MMSTB<br>({p_stb:,.0f} STB)", f"{r_mmstb:,.2f} MMSTB<br>({r_stb:,.0f} STB)"],
            textposition='auto',
            textfont=dict(size=15, color='#060B15', weight='bold'),
            hovertemplate='<b>%{x}</b><br>Volumen: %{y:.2f} MMSTB<extra></extra>'
        ))

        fig.update_layout(
            title=dict(
                text='Comparativa Volumétrica: POES vs Reservas Recuperables',
                font=dict(size=22, color='#060B15', weight='bold'),
                x=0.5,
                y=0.95
            ),
            height=550,
            plot_bgcolor='#F4F6F9', 
            paper_bgcolor='#F4F6F9',
            xaxis_title=dict(text='Categoría', font=dict(size=18, color='#060B15', weight='bold')),
            yaxis_title=dict(text='Volumen (MMSTB)', font=dict(size=18, color='#060B15', weight='bold')),
            xaxis=dict(
                showgrid=False, 
                tickfont=dict(size=16, color='#060B15', weight='bold')
            ),
            yaxis=dict(
                showgrid=True, gridcolor='#D1D5DB', zeroline=False, 
                tickfont=dict(size=14, color='#060B15', weight='bold')
            ),
            margin=dict(l=20, r=20, t=60, b=20),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
