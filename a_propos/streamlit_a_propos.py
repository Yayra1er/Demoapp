import streamlit as st

def main():
    st.title("À Propos")
    
    st.header("Notre Équipe")
    st.write("Bienvenue sur la page À Propos. Voici notre équipe et nos informations clés.")

    st.subheader("Équipe de K")
    st.write("Nous sommes une équipe passionnée dédiée à fournir des solutions innovantes.")

    # Spécifiez le chemin complet de votre image statique
    image_path = r"E:\Projets\Demoapp\static\images\equip.jpg"

    # Utilisation de st.image pour afficher l'image
    st.image(image_path, caption="Notre Équipe", use_column_width=True)

    st.subheader("Notre Mission")
    st.write("Notre mission est d'améliorer la vie quotidienne grâce à la technologie.")

    st.subheader("Contactez-nous")
    st.write("Pour plus d'informations, n'hésitez pas à nous contacter.")

if __name__ == "__main__":
    main()
