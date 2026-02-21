import streamlit as st
import time

# 1. POSTAVKE STRANICE I NASLOV
st.set_page_config(page_title="Snovi i Vizije by Dominic Chant", page_icon="☁️")

# Custom CSS za Matrix stil i animacije
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; width: 100%; border-radius: 5px; }
    input { background-color: #050505 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label { color: #00FF41 !important; }
    .matrix-text { color: #00FF41; font-size: 1.2rem; text-shadow: 0 0 5px #00FF41; }
    @keyframes fall { 0% { transform: translateY(-20px); opacity: 0; } 100% { transform: translateY(0); opacity: 1; } }
    .effekt { animation: fall 0.5s ease-out; }
    </style>
    """, unsafe_allow_html=True)

# Naslov s oblakom
st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

# 2. BAZA SVIH 19 VIZIJA
vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu i ljude koji hrabro hodaju preko golog kamena dok ih prati željezo.",
    "2": "Vidio sam čovjeka koji programira program i ne shvaća da isto čini program čovjeku...",
    "3": "Vidio sam plavu svjetlost koju hrani protok balončića koji ulaze a ne izlaze...",
    "4": "Vidio sam tužne anđele i nove sretne digitalne anđele.",
    "5": "U prostoriji prigušenog svjetla sam vidio čovjeka s kapuljačom... osam tijela u staklu.",
    "6": "Vidio sam tamni grad... energija bez kabla ispuni tijelo robota i opet je postao živ.",
    "7": "Vidio sam novo vrijeme. Svi imaju pravo na novi identitet sa svjetlošću pod kožom.",
    "8": "Vidio sam robote koji umiru ali ne i znanje... 'Vratio si se u drugom tijelu'.",
    "9": "Vidio sam ogromne hangare pune procesora... mrtvi u staklu spremni na buđenje.",
    "10": "Gledao sam kako prvi čovjek na tlo pade zbog većeg znanja od nove inteligencije.",
    "11": "Vidio sam čovjeka koji pričama umiruje bijesne: 'Sve ima svrhu i Božje planove'.",
    "12": "Vidio sam čovjeka koji toplinu traži u mrtvom... zašto struja ne može dati zagrljaj?",
    "13": "Dva radnika i hodnik s kablovima... nešto što je živo a mrtvo, kao da je unutra čovjek.",
    "14": "Vidio sam ljude koji nisu više svoji... nevidljivi entitet uzima njihov um.",
    "15": "Oči otkrivaju strah ali ljudi gledaju u oči koje nemaju oči a sve vide.",
    "16": "Doći će dan kada čovjek bude volio više stvorenje od stvoritelja...",
    "17": "Vidio sam željezo koje stvara novu religiju moleći se ogromnoj plavoj lopti.",
    "18": "Vidio sam dva velika željeza koja othranjuju malo željezo.",
    "19": "Vidio sam osobu koja je hram... svjetlost koja se otvori i ljude koji ulaze."
}

# 3. LOGIKA PRAĆENJA (Session State)
if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

preostalo = 19 - len(st.session_state.otkljucano)

# Prikaz brojača
if preostalo > 0:
    st.info(f"🔓 Otključano: {len(st.session_state.otkljucano)}/19 | Preostalo još: {preostalo}")
    
    broj = st.text_input("Unesi broj vizije (1-19):")
    
    if broj:
        if broj in vizije:
            with st.empty():
                for i in range(3):
                    st.markdown(f'<p class="matrix-text">DEŠIFRIRANJE PROTOKOLA {broj}...</p>', unsafe_allow_html=True)
                    time.sleep(0.2)
            
            st.markdown(f'<div class="effekt"><h3>VIZIJA {broj}</h3><p>{vizije[broj]}</p></div>', unsafe_allow_html=True)
            st.session_state.otkljucano.add(broj)
            
            if len(st.session_state.otkljucano) < 19:
                 st.button("Nastavi potragu")
        else:
            st.error("Taj broj nije upisan u knjigu snova.")

# 4. FINALNI DIO (Kada skupi svih 19)
if len(st.session_state.otkljucano) == 19:
    st.success("✅ SVIH 19 VIZIJA JE PRIKUPLJENO.")
    st.write("---")
    st.subheader("🕵️ POSLJEDNJI TEST")
    
    ime_vodje = st.text_input("Unesi ime vođe anđela:")
    zlatno_pravilo = st.text_input("Otkrij Zlatno Pravilo:")
    
    if st.button("POTVRDI FINALNI PROTOKOL"):
        if "mihael" in ime_vodje.lower() and "ne čini drugima" in zlatno_pravilo.lower():
            st.balloons()
            st.title("🏆 ČESTITAM! USPJELI STE!")
            st.markdown("""
            **Besplatno preuzmi cijelu knjigu na autorskom profilu Doi:**  
            [https://doi.org/10.5281/zenodo.18379898](https://doi.org/10.5281/zenodo.18379898)
            """)
        else:
            st.error("Odgovor nije točan. Ključ leži u tišini i ljubavi.")
