import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Identifikasi Bahaya Bahan Kimia",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Aplikasi Identifikasi Bahaya Bahan Kimia")
st.write("Aplikasi ini digunakan untuk mengetahui bahaya, APD, dan penanganan awal beberapa bahan kimia di laboratorium.")

data = {
    "Nama Bahan": [
        "Asam Klorida (HCl)",
        "Natrium Hidroksida (NaOH)",
        "Asam Sulfat (H2SO4)",
        "Amonia (NH3)",
        "Etanol (C2H5OH)",
        "Aseton (C3H6O)"
    ],
    "Jenis Bahaya": [
        "Korosif, iritasi saluran pernapasan",
        "Korosif, menyebabkan luka bakar pada kulit",
        "Sangat korosif, bereaksi hebat dengan air",
        "Iritan, beracun jika terhirup dalam konsentrasi tinggi",
        "Mudah terbakar",
        "Mudah terbakar dan menyebabkan iritasi"
    ],
    "Simbol GHS": [
        "Korosif",
        "Korosif",
        "Korosif",
        "Iritan / Toksik",
        "Flammable",
        "Flammable / Iritan"
    ],
    "APD yang Digunakan": [
        "Jas lab, sarung tangan, kacamata safety, masker",
        "Jas lab, sarung tangan, kacamata safety",
        "Jas lab, sarung tangan tahan kimia, face shield",
        "Jas lab, sarung tangan, masker, bekerja di lemari asam",
        "Jas lab, sarung tangan, jauhkan dari api",
        "Jas lab, sarung tangan, kacamata safety, jauhkan dari api"
    ],
    "Penanganan Awal": [
        "Jika terkena kulit, bilas dengan air mengalir minimal 15 menit.",
        "Jika terkena kulit, bilas dengan air mengalir dan lepaskan pakaian terkontaminasi.",
        "Jika terkena kulit, bilas dengan air banyak. Jangan menambahkan air ke asam pekat.",
        "Jika terhirup, pindahkan korban ke tempat dengan udara segar.",
        "Jauhkan dari sumber api. Jika terkena kulit, bilas dengan air.",
        "Jauhkan dari sumber api. Jika terhirup, pindahkan ke tempat terbuka."
    ]
}

df = pd.DataFrame(data)

st.subheader("📋 Daftar Bahan Kimia")
st.dataframe(df, use_container_width=True)

st.subheader("🔍 Pilih Bahan Kimia")

pilihan = st.selectbox("Pilih nama bahan kimia:", df["Nama Bahan"])

hasil = df[df["Nama Bahan"] == pilihan].iloc[0]

st.success(f"Data bahaya untuk {pilihan}")

col1, col2 = st.columns(2)

with col1:
    st.write("### 🧪 Nama Bahan")
    st.write(hasil["Nama Bahan"])

    st.write("### ⚠️ Jenis Bahaya")
    st.write(hasil["Jenis Bahaya"])

    st.write("### 🏷️ Simbol GHS")
    st.write(hasil["Simbol GHS"])

with col2:
    st.write("### 🥽 APD yang Digunakan")
    st.write(hasil["APD yang Digunakan"])

    st.write("### 🚑 Penanganan Awal")
    st.write(hasil["Penanganan Awal"])

st.warning("Catatan: Data ini hanya contoh pembelajaran. Untuk penggunaan resmi, tetap harus merujuk pada SDS/MSDS bahan kimia.")
