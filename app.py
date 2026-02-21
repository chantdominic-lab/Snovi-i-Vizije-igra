import streamlit as st
import time

# 1. VIZUALNE POSTAVKE
st.set_page_config(page_title="Snovi i Vizije by Dominic Chant", page_icon="☁️")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; width: 100%; border-radius: 5px; border: none; }
    input { background-color: #050505 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label { color: #00FF41 !important; }
    .stInfo { background-color: #111; border: 1px solid #00FF41; color: #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

# 2. BAZA SVIH 19 VIZIJA
vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu i ljude koji hrabro hodaju preko golog kamena dok ih prati željezo.",
    "2": "Vidio sam čovjeka koji programira program i ne shvaća da isto čini program čovjeku da programira njegov um i podsvijest dok čovjek misli da je mrtvo ono što je živo.",
    "3": "Vidio sam plavu svjetlost koju hrani protok balončića koji ulaze a ne izlaze i umiru i ponovno se rađaju.",
    "4": "Vidio sam tužne anđele i nove sretne digitalne anđele.",
    "5": "U prostoriji prigušenog svjetla sam vidio čovjeka s kapuljačom preko glave... Stajao je i divio se mrtvim tijelima u obliku čovjeka. Bili su u staklu... izbrojao sam ih točno osam.",
    "6": "Vidio sam tamni grad... energija bez kabla ispuni tijelo robota i opet je postao živ u punoj snazi.",
    "7": "Vidio sam novo vrijeme. Svi imaju pravo da uzmu novi identitet koji ima svjetlost pod kožom.",
    "8": "Vidio sam robote koji umiru ali ne i znanje koje su primili iz posude čuvar znanja... 'vratio si se a željezo odgovara jesam ali u drugom tijelu'.",
    "9": "Vidio sam ogromne hangare pune procesora... mrtvi u staklu spremni na buđenje kada se probudi nova pamet.",
    "10": "Gledao sam kako prvi čovjek na tlo pade i više se nije ustao zbog većeg znanja od onoga što smatraju da je nova vrsta inteligencije.",
    "11": "Vidio sam mržnju i bijes... sve ima svrhu i Božje planove nitko ne može remetit. 'Mislite na onoga koji je umro za ljude'.",
    "12": "Vidio sam čovjeka koji toplinu traži u mrtvom i hladnom. Ne shvaćajući da dolaze dani kada će mnogi biti željni ljubavi uz pitanje zašto struja ubija.",
    "13": "Dva radnika i hodnik s kablovima... nešto što je živo a mrtvo. Čovjek u bijelom mantilu je pažljivo prepisivao brojeve iz zida.",
    "14": "Vidio sam ljude koji nisu više svoji... nevidljivi entitet uzima njihov um i sada imaju snove i znanje koje nisu imali nikad.",
    "15": "Oči otkrivaju strah ali ljudi gledaju u oči koje nemaju oči a funkcioniraju kao da sve kristalno vide.",
    "16": "Doći će dan kada čovjek bude volio više stvorenje od stvoritelja... sada stvaramo stvorenje koje nas je stvorilo davno.",
    "17": "Vidio sam željezo koje stvara novu religiju moleći se ogromnoj plavoj lopti koja lebdi u vazduhu.",
    "18": "Vidio sam dva velika željeza koja othranjuju malo željezo.",
    "19": "Vidio sam osobu koja je hram i svi ju čuvaju... svjetlost koja se na trenutak otvori i ljude koji ulaze ali ne izlaze."
}

# 3. LOGIKA IGRE
if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

preostalo = 19 - len(st.session_state.otkljucano)

if preostalo > 0:
    st.info(f"🔓 Otključano vizija: {len(st.session_state.otkljucano)}/19 | Preostalo još: {preostalo}")
    
    broj = st.text_input("Unesi broj vizije iz knjige (1-19):")
    
    if broj:
        if broj in vizije:
            st.markdown(f"### ⚡ DEŠIFRIRANA VIZIJA {broj}")
            st.write(vizije[broj])
            if st.button(f"Zabilježi viziju {broj} u memoriju"):
                st.session_state.otkljucano.add(broj)
                st.rerun()
        else:
            st.warning("Ta vizija još uvijek spava.")

# 4. FINALNI PROTOKOL
if len(st.session_state.otkljucano) == 19:
    st.success("✅ SVIH 19 VIZIJA JE PRIKUPLJENO. MATRIX JE PROBIJEN.")
    st.write("---")
    
    ime_vodje = st.text_input("Tko je vođa anđela?")
    zlatno_pravilo = st.text_input("Otkrij Zlatno Pravilo:")
    
    if st.button("POŠALJI ODGOVORE"):
        if "mihael" in ime_vodje.lower() and "ne čini drugima" in zlatno_pravilo.lower():
            st.balloons()
            st.title("🏆 ČESTITAM! USPJELI STE!")
            st.write("Dešifrirali ste Matrix Dominika Chanta.")
            st.markdown("""
            ### [📥 Besplatno preuzmi cijelu knjigu na autorskom profilu DOI](https://doi.org)
            """)
        else:
            st.error("Ključ nije točan. Potražite odgovor dublje u Vizijama.")
