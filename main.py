# to run -> streamlit run main.py
import streamlit as st
import methods
import re


st.set_option('deprecation.showfileUploaderEncoding', False)
# Introduction
st.title("Bioinformatic Armory Web App")

# List of choices that will show on the sidebar
activities = ["Basic DNA Sequence Analysis", "Count Point Mutations",
              "Find motifs", "Find..."]

choice = st.sidebar.selectbox("Select activity", activities)

# Code for basic analysis and translation
if choice == "Basic DNA Sequence Analysis":
    st.subheader("Analyze your DNA sequence:")

    try:
        uploaded_file = st.file_uploader("Upload Sequence", type="txt")
        seq = uploaded_file.read()
        seq = seq.decode('UTF-8')
        st.text("Your sequence:")
        st.text(seq)

        sum, A, C, G, T = methods.count_bases(seq)

        st.write("There are: ", A, "A ", C, "C",
                 G, "G", T, "T, in total ",
                 sum, " nucleotides")
        st.write("Which is ", round(A/sum*100, 3), "% A ",
                 round(C/sum*100, 3), "% C",
                 round(G/sum*100, 3), "% G",
                 round(T/sum*100, 3), "% T")
        st.write("Which means the GC content is ",
                 round((G+C)/sum*100, 3), "%")

        rna_switch = st.checkbox("1. Show RNA strand?")

        if rna_switch is True:
            st.text(seq.replace("T", "U"))
            translate_to_prot = st.checkbox("1.1 Translate strand to protein?")

            if translate_to_prot is True:

                prot_seq = methods.translate_to_prot(seq)

                st.text(prot_seq)

        comp_switch = st.checkbox("2. Show complementary DNA?")

        if comp_switch is True:
            st.text(seq.replace('A', 't').replace('T', 'a').replace('C', 'g')
                    .replace('G', 'c').upper()[::-1])

    except AttributeError:
        pass

# Code for point mutations, takes files as an input and analyses the differences
elif choice == "Count Point Mutations":

    try:
        st.subheader("Original sequence:")
        origin_seq = st.file_uploader("Upload original sequence", type="txt")
        origin_seq = origin_seq.read()
        origin_seq = origin_seq.decode('UTF-8')
        st.text(origin_seq)

    except AttributeError:
        pass

    try:
        st.write("Mutated sequence:")
        mut_seq = st.file_uploader("Upload mutated sequence", type="txt")
        mut_seq = mut_seq.read()
        st.text(mut_seq)

    except AttributeError:
        pass

    try:
        num_of_mut = methods.find_mutations(origin_seq, mut_seq)
        st.write("There are ", num_of_mut, " point mutations.")
    except TypeError:
        pass

# Finds motifs, user has to input
elif choice == "Find motifs":
    try:
        st.subheader("Original sequence:")
        check_motif_seq = st.file_uploader("Upload sequence that you want to find motifs in:", type="txt")
        check_motif_seq = check_motif_seq.read()
        check_motif_seq = check_motif_seq.decode('UTF-8')
        st.text(check_motif_seq)

        motif = st.text_input("Write motif sequence below...")

        matches = re.finditer(motif, check_motif_seq)
        positions = [match.start() for match in matches]

        # arrays start at 0 so if I write a list directly it will look ugly
        pos_dict = {}
        for i, pos in enumerate(positions):
            pos_dict[i+1] = pos + 1

        st.write(pos_dict)

    except AttributeError:
        pass

elif choice == "Find...":
    st.subheader("TODO:...")
