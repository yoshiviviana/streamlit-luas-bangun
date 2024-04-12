import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Hitung Luas Bangun Datar & Ruang',
    ['Hitung Luas Persegi Panjang',
    'Hitung Luas Segitiga',
    'Hitung Luas Persegi',
    'Hitung Luas Jajar Genjang',
    'Hitung Luas Trapesium',
    'Hitung Luas Layang Layang',
    'Hitung Luas Belah Ketupat',
    'Hitung Luas Lingkaran',
    'Hitung Luas Kubus',
    'Hitung Luas Balok',
    'Hitung Luas Limas Segiempat',
    'Hitung Luas Tabung',
    'Hitung Luas Kerucut',
    'Hitung Luas Bola'],                           
    default_index=0)

# halaman hitung luas persegi panjang
if (selected == 'Hitung Luas Persegi Panjang') :
    st.title('Hitung Luas Persegi Panjang')

    panjang = st.number_input ("Masukkaan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.write ("Luas Persegi Panjang Adalah = ", luas)
        st.success (f"Luas Persegi Panjang Adalah = {luas}")

if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')

    alas = st.slider ("Masukkan Nilai Alas", 0, 200)
    tinggi = st.slider ("Masukkan Nilai Tinggi", 0, 200)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 0.5 * alas * tinggi
        st.write ("Luas Segitiga Adalah = ", luas)
        st.success (f"Luas Segitiga Adalah = {luas}")

if (selected == 'Hitung Luas Persegi') :
    st.title('Hitung Luas Persegi')

    sisi = st.number_input ("Masukkan Nilai Sisi", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = sisi * sisi
        st.write ("Luas Persegi Adalah = ", luas)
        st.success (f"Luas Persegi Adalah = {luas}")

if (selected == 'Hitung Luas Jajar Genjang') :
    st.title('Hitung Luas Jajar Genjang')

    alas = st.slider ("Masukkan Nilai Alas", 0, 200)
    tinggi = st.slider ("Masukkan Nilai Tinggi", 0, 200)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = alas * tinggi
        st.write ("Luas Jajar Genjang Adalah = ", luas)
        st.success (f"Luas Jajar Genjang Adalah = {luas}")

if (selected == 'Hitung Luas Trapesium') :
    st.title('Hitung Luas Trapesium')

    a = st.number_input ("Masukkan Nilai Sisi Sejajar 1", 0)
    b = st.number_input ("Masukkan Nilai Sisi Sejajar 2", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 0.5 * ( a + b ) * tinggi
        st.write ("Luas Trapesium Adalah = ", luas)
        st.success (f"Luas Trapesium Adalah = {luas}")

if (selected == 'Hitung Luas Layang Layang') :
    st.title('Hitung Luas Layang Layang')

    D1 = st.number_input ("Masukkan Nilai Diagonal 1", 0)
    D2 = st.number_input ("Masukkan Nilai Diagonal 2", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 0.5 * D1 * D2
        st.write ("Luas Layang Layang Adalah = ", luas)
        st.success (f"Luas Layang Layang Adalah = {luas}")

if (selected == 'Hitung Luas Belah Ketupat') :
    st.title('Hitung Luas Belah Ketupat')

    D1 = st.number_input ("Masukkan Nilai Diagonal 1", 0)
    D2 = st.number_input ("Masukkan Nilai Diagonal 2", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 0.5 * D1 * D2
        st.write ("Luas Belah Ketupat Adalah = ", luas)
        st.success (f"Luas Belah Ketupat Adalah = {luas}")

if (selected == 'Hitung Luas Lingkaran') :
    st.title('Hitung Luas Lingkaran')

    r1 = st.number_input ("Masukkan Nilai Jari-Jari 1", 0)
    r2 = st.number_input ("Masukkan Nilai Jari-Jari 2", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 3.14 * r1 * r2
        st.write ("Luas Lingkaran Adalah = ", luas)
        st.success (f"Luas Lingkaran Adalah = {luas}")

if (selected == 'Hitung Luas Kubus') :
    st.title('Hitung Luas Kubus')

    rusuk = st.number_input ("Masukkaan Nilai Rusuk", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 6 * rusuk * rusuk
        st.write ("Luas Kubus Adalah = ", luas)
        st.success (f"Luas Kubus Adalah = {luas}")   

if (selected == 'Hitung Luas Balok') :
    st.title('Hitung Luas Balok')

    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = ( 2 * panjang * lebar ) + ( 2 * panjang * tinggi ) + ( 2 * lebar * tinggi )
        st.write ("Luas Balok Adalah = ", luas)
        st.success (f"Luas Balok Adalah = {luas}")

if (selected == 'Hitung Luas Limas Segiempat') :
    st.title('Hitung Luas Limas Segiempat')

    alas = st.number_input ("Masukkan nilai Alas", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = ( alas * alas ) + ( 4 * 0.5 * alas * tinggi )
        st.write ("Luas Limas Segiempat Adalah", luas)
        st.success (f"Luas Limas Segiempat Adalah = {luas}")

if (selected == 'Hitung Luas Tabung') :
    st.title('Hitung Luas Tabung')

    jarijari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 2 * 3.14 * jarijari * ( jarijari + tinggi )
        st.write ("Luas Tabung Adalah", luas)
        st.success (f"Luas Tabung Adalah = {luas}")

if (selected == 'Hitung Luas Kerucut') :
    st.title('Hitung Luas Kerucut')

    jarijari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    garisP = st.number_input ("Masukkan Nilai Garis Pelukis", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 3.14 * jarijari * ( jarijari + garisP )
        st.write ("Luas Kerucut Adalah", luas)
        st.success (f"Luas Kerucut Adalah = {luas}")

if (selected == 'Hitung Luas Bola') :
    st.title('Hitung Luas Bola')

    jarijari = st.number_input ("Masukkan Nilai Jari-Jari", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 4 * 3.14 * ( jarijari * jarijari )
        st.write ("Luas Bola Adalah", luas)
        st.success (f"Luas Bola Adalah = {luas}")
         