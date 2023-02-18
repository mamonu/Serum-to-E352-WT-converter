import streamlit as st
import os
import glob
from WTconvert import *


def main():
    st.title("Serum to WaveEdit Converter")

    input_dir = st.text_input("Input Directory", "./serum")
    output_dir = st.text_input("Output Directory", "./converted")

    if st.button("Convert"):
        input_files = glob.glob(os.path.join(input_dir, "**", "*.wav"), recursive=True)
        for file in input_files:
            rel_file = file.replace(os.path.join(input_dir, ""), "")
            output_file = os.path.join(output_dir, rel_file)
            st.write("Converting " + rel_file)
            convert_serum_to_waveedit(file, output_file)
        st.write("Conversion complete.")


if __name__ == "__main__":
    main()