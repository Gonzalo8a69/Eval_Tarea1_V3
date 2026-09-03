import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

def aplicar_estilos():
    """
    Inyecta CSS global. Transforma la app a un Dark Theme corporativo.
    Soluciona el conflicto de legibilidad de inputs entre Modo Claro/Oscuro de Streamlit.
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
        
        /* --- CORRECCIÓN DEFINITIVA DE CAJAS DE ENTRADA (INPUTS) --- */
        div[data-baseweb="input"] { 
            background-color: #111A2C !important; 
            border: 1px solid #2A3F5F !important; 
            border-radius: 6px !important; 
        }
        div[data-baseweb="input"]:focus-within { 
            border-color: #00E5FF !important; 
            box-shadow: 0 0 8px rgba(0, 229, 255, 0.4) !important; 
        }
        /* El -webkit-text-fill-color evita que el Modo Claro de Streamlit vuelva invisible el texto */
        div[data-baseweb="input"] input { 
            color: #00E5FF !important; 
            -webkit-text-fill-color: #00E5FF !important; 
            font-weight: bold !important; 
            font-size: 1.1rem !important; 
        }
        
        /* --- NAVEGACIÓN Y TABS --- */
        [data-testid="stSidebar"] { background-color: #0B1221 !important; border-right: 1px solid #1A273D; }
        [data-testid="stSidebar"] .stRadio label p,
        [data-testid="stSidebar"] .stRadio label div { font-size: 1.3rem !important; font-weight: 600 !important; color: #8B9BB4 !important; padding: 10px 0; }
        
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
            border-left: 4px solid #FF7A00; margin-bottom: 1rem; border-right: 1px solid #1A273D; border-top: 1px solid #1A273D; border-bottom: 1px solid #1A273D;
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
            border-left: 4px solid #B026FF; margin-bottom: 1rem; border-right: 1px solid #1A273D; border-top: 1px solid #1A273D; border-bottom: 1px solid #1A273D;
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
            border-left: 4px solid #00B4D8; margin-bottom: 1rem; border-right: 1px solid #1A273D; border-top: 1px solid #1A273D; border-bottom: 1px solid #1A273D;
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

# ... (El resto de funciones renderizar_tarjeta_info, renderizar_tarjeta_produccion, inyectar_js_animacion, etc., se mantienen exactamente igual que en tu versión funcional)
