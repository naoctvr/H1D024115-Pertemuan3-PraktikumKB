import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
 
# 1. Definisi Antecedent (Input) dan Consequent (Output)
# Range ditentukan berdasarkan semesta pembicaraan pada soal
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpas = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpas')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')
 
# 2. Membership Functions (Menggunakan fungsi segitiga/trimf sebagai standar)
# Kejelasan Informasi [0 - 100]
kejelasan_informasi['tidak'] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi['cukup'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100])
 
# Kejelasan Persyaratan [0 - 100]
kejelasan_persyaratan['tidak'] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan['cukup'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])

# Kemampuan Petugas [0 - 100]
kemampuan_petugas['tidak'] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas['cukup'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])

# Ketersediaan Sarpas [0 - 100]
ketersediaan_sarpas['tidak'] = fuzz.trapmf(ketersediaan_sarpas.universe, [0, 0, 60, 75])
ketersediaan_sarpas['cukup'] = fuzz.trimf(ketersediaan_sarpas.universe, [60, 75, 90])
ketersediaan_sarpas['memuaskan'] = fuzz.trapmf(ketersediaan_sarpas.universe, [75, 90, 100, 100])
 
# Kepuasan Pelayanan [0 - 400]
kepuasan_pelayanan['tidak'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan['kurang'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['cukup'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['sangat'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])
 

# 3. Definisi Aturan Fuzzy (Rules)
rule1 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['kurang'])
rule2 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule3 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['cukup'])
rule4 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule5 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule6 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['cukup'])
rule7 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule8 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule9 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule10 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule11 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule12 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['cukup'])
rule13 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule14 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule15 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule16 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule17 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule18 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule19 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule20 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule21 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule22 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule23 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule24 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule25 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule26 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule27 = ctrl.Rule(kejelasan_informasi['tidak'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule28 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule29 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule30 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['cukup'])
rule31 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule32 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule33 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule34 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule35 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule36 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule37 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule38 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule39 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule40 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule41 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule42 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule43 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule44 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule45 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule46 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule47 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule48 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule49 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule50 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule51 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule52 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule53 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['sangat'])
rule54 = ctrl.Rule(kejelasan_informasi['cukup'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule55 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule56 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['cukup'])
rule57 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule58 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule59 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule60 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule61 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule62 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule63 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule64 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['cukup'])
rule65 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule66 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule67 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule68 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule69 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule70 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule71 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['sangat'])
rule72 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule73 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule74 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['memuaskan'])
rule75 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule76 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['memuaskan'])
rule77 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['sangat'])
rule78 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])
rule79 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['tidak'], kepuasan_pelayanan['sangat'])
rule80 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['cukup'], kepuasan_pelayanan['sangat'])
rule81 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpas['memuaskan'], kepuasan_pelayanan['sangat'])

# 4. Sistem Kontrol dan Simulasi
kepuasan_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, 
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, 
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, 
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, 
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, 
    rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, 
    rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, 
    rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81  
])
kepuasan = ctrl.ControlSystemSimulation(kepuasan_ctrl)
 
# 5. Memasukkan Nilai Input Sesuai Soal
# kejelasan informasi = 80, kejelasan_persyaratan = 60, kemampuan petugas = 50, dan ketersediaan sarpas = 90
kepuasan.input['kejelasan_informasi'] = 80
kepuasan.input['kejelasan_persyaratan'] = 60
kepuasan.input['kemampuan_petugas'] = 50
kepuasan.input['ketersediaan_sarpas'] = 90
 
# 6. Melakukan Perhitungan (Crushing/Compute)
kepuasan.compute()
 
# 7. Output Hasil
hasil_kepuasan = kepuasan.output['kepuasan_pelayanan']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Kejelasan Informasi       : 80")
print(f"Kejelasan Persyaratan     : 60")
print(f"Kemampuan Petugas         : 50")
print(f"Ketesediaan Sarpas        : 90")
print("--------------------------------------")
print(f"Hasil Kepuasan Masyarakat : {hasil_kepuasan:.2f}")
 
# Visualisasi (Opsional, butuh matplotlib)
kejelasan_informasi.view()
kejelasan_persyaratan.view()
kemampuan_petugas.view()
ketersediaan_sarpas.view()
kepuasan_pelayanan.view()
kepuasan_pelayanan.view(sim=kepuasan)

plt.show()