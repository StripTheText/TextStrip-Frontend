# Imports for the Streamlit app

import streamlit as st


# Definition of the Layout of the Streamlit app
def app():
    st.set_page_config(
        page_title="Strip The Text App",
        page_icon="🧊",
        initial_sidebar_state="expanded")

    st.title('Strip the Text')

    st.markdown("""

    ## Ein Universitätsprojekt von Studierenden der Dualen Hochschule Baden-Württemberg Mannheim

    ### Projektteam:
    - [Tobias Kister - 9416513](https://github.com/tkister)
    - [Daniel Schmitz - 6695185](https://github.com/dschmtz)
    - [Jan Neifeld - 8722662](https://github.com/JanDN312)
    - [Michel Medved - 9303634](https://github.com/mimed100)

    ### Projektbeschreibung: 

    Bei den Projekt handelt es sich um die Realisierung eines Web-Tools, welches es ermöglicht, Texte von unnötigen 
    Informationen zu befreien und die zentralen Punkte der Englischsprachigen Texte zu erfassen. Des Weiteren bildet 
    das nachfolgende Projekt die Möglichkeit die vorliegenden Texte anhand ihres Inhaltes zu einer bestimmten 
    Kategorie von Dokumenten zu klassifizieren.

    """)


app()
