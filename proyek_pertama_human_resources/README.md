# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Perusahaan Jaya Jaya maju adalah perusahaan yang bergerak dibidang multinasional, telah berdiri sejak tahun 2000 dan memiliki lebih dari seribu karyawan yang tersebar di seluruh penjuru negeri

### Permasalahan Bisnis

- Tingkat atrisi yang mencapai lebih dari 10% dapat berpotensi menurunkan produktivitas dan kepuasan pekerja karyawan yang tersisa, menyebabkan kekurangan tenaga kerja yang terampil dan ahli dibidangnya, dan juga dapat menghambat inovasi dan pengembangan perusahaan

### Cakupan Proyek

Berdasarkan permasalahan bisnis yang telah disebutkan, kita akan mencari faktor meningkatnya atrisi karyawan seperti :
1. Bagaimana penghasilan karyawan mempengaruhi berpengaruh atrisi
2. Apa dampak dari kepuasan pekerja terhadap tingkat atrisi?
3. Apakah usia karyawan juga mempengaruhi tingkat atrisi?
4. Seberapa besar pengaruh keterlibatan karyawan berdampak pada atrisi?
5. Bagaimana hubungan antara karyawan dan manajer dapat mempengaruhi atrisi karyawan
6. Seberapa besar efek dari tingkat pendidikan karyawan dalam atrisi?
     
 * Membuat Business Dashboard untuk memantau informasi dan mengatasi faktor faktor atrisi karyawan
 * Membuat model prediksi untuk mengidentifikasi faktor yang paling berpengaruh

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv

Setup environment:

* Dashboard:
  - Instal Docker dengan mengunduh Docker Desktop Installer
  - Silakan mengikuti seluruh proses instalasi yang ada
  - Pada bagian akhir proses instalasi, tekan tombol Close untuk mengakhiri seluruh proses instalasi
  - Untuk menjalankan Docker, bukalah Docker Desktop
  - Jalankan perintah pada terminal untuk memanggil Docker image
    -     `Docker pull metabase/metabase:v0.46.4`
  - Setelah proses docker image selesai, jalankan image dengan perintah berikut
    -     `docker run -p 3000:3000 --name metabase2 metabase/metabase`
  - Buka metabase pada port *http://localhost:3000/setup*
  - Selesaikan proses registrasi

* Notebook:
  - Buka Terminal atau Powershell
  - Jalankan perintah
    -     `mkdir proyek_pertama`
  - Pindah ke folder terbaru tersebut menggunakan perintah berikut
    -     `cd proyek_pertama`
  - Buat sebuah virtual environment dengan menjalankan perintah berikut
    -     `pipenv install`
  - Aktifkan virtual environment dengan menjalankan perintah berikut
    -     `pipenv shell`
  - Instal semua library yang dibutuhkan dari file requirements.txt menggunakan perintah berikut
    -     `pip install -r requirements.txt`
  - Buka jupyter-notebook dengan menjalankan perintah berikut
    -     `jupyter-notebook`
       
## Business Dashboard

Business Dashboard ini bertujuan memberikan gambaran tentang faktor faktor atrisi karyawan dalam perusahaan, dashboard ini dapat membantu HR untuk memantau karyawan, memperbaiki faktor atrisi dan juga meningkatkan strategi retensi karyawan

* Informasi Umum : Menampilkan data pengunduran karyawan, jumlah role pekerjaan, rata rata gaji dan usia
* Analisis Departemen : Berfokus pada pola atrisi di berbagai departemen
* Analisis Tingkat pendidikan : Meneliti hubungan antara tingkat pendidikan dan tingkat atrisi
* Analisis Gaji : Mencari dampak penghasilan terhadap pengunduran diri
* Analisis Hubungan manajerial : Mencari korelasi antara atrisi karyawan dan durasi hubungan mereka dengan manajer
* Analisis Peran pekerjaan : Meneliti tingkat atrisi dengan tingkat keterlibatan para karyawan
* Analisis Usia : Mencari hubungan antara tingkat atrisi dan juga usia karyawan

*Link Dashboard :*
- *username/email: root@gmail.com*
- *password: root123*
- localhost:3000/setup

## Conclusion

Berdasarkan analisis data yang telah dilakukan, dapat disimpulkan bahwa faktor faktor seputar penghasilan, keterlibatan para pekerja dan juga kepuasan para pekerja sangat berpengaruh atas naiknya tingkat _atrisi_ karyawan,

- _Atrisi berdasarkan penghasilan per bulan_: Penghasilan per bulan memiliki pengaruh signifikan terhadap tingkat atrisi karyawan. Hal ini menunjukan bahwa penghasilan karyawan yang berada dibawah empat ribu dolar memiliki potensi lebih tinggi untuk mengundundurkan diri
  
- _Atrisi berdasarkan kepuasan pekerja dan hubungan dengan manajer_: Hubungan antara kepuasan kerja dan tingkat atrisi menunjukkan pola yang menarik,
     - **Kurang dari 1 tahun** : Karyawan yang bekerja kurang dari 1 tahun dengan manajer mereka memiliki tingkat atrisi tertinggi. Hal ini menunjukkan kurangnya masa onboarding dan membangun hubungan yang kuat antara karyawan dan manager di awal karir
     - **2 hingga 4 tahun** : Pada rentang waktu ini, karyawan memiliki tingkat kepuasan kerja yang relatif rendah
     - **6 hingga 8 tahun** : Dengan tingkat kepuasan kerja yang relatif tinggi, karyawan di rentang waktu ini mungkin merasa stagnan dan membutuhkan peningkatan pada karir mereka
         
- _Atrisi berdasarkan usia_:
       - Data menunjukan bahwa karyawan dengan rentang usia sekitar 25 sampai dengan 30 an memiliki peluang tingkat atrisi yang lebih tinggi dibandingkan usia lainnya. Hal ini terjadi karena mereka masih mencari karir yang tepat dan belum sepenuhnya berkomitmen pada satu perusahaan
      - Pada usia mendekati 40 para karyawan cenderung memilih untuk menjalani karir yang stabil dan lebih royal terhadap perusahaan

- _Atrisi berdasarkan role pekerjaan dan keterlibatan pekerja_: Nilai atrisi ini juga meningkat pada sebagian role pekerjaan yang disebabkan oleh tingkat keterlibatan dalam pekerjaan yang lumayan rendah dibandingkan role pekerjaan lain. Hal ini menyebabkan para karyawan cenderung memilih untuk mencari peningkatan juga pengalaman baru dan memutuskan untuk mengundurkan diri

- _Atrisi berdasarkan tingkat pendidikan_: Pada informasi tingkat atrisi karyawan berdasarkan level pendidikan, karyawan dengan tingkat pendidikan yang setara dengan s1 sampai dengan s2 cenderung memutuskan untuk keluar dari perusahaan. Hal ini terjadi karena pada tahap sarjana sampai pascasarjana, karyawan memiliki harapan terhadap karir yang tinggi dan menginginkan kesempatan untuk mengembangkan pengalaman yang lebih besar, para karyawan mungkin merasa stagnan dan kemudian mencari kesempatan dan peluang yang sejalan dengan ambisi mereka.


  
### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- *Menerapkan program insentif berdasarkan kinerja*, monthly income sangat berpengaruh pada attrition, maka dari itu memberikan insentif yang tinggi dan relevan pada departemen atau individu, akan berpengaruh terhadap loyalitas para karyawan, selain itu memberikan insentif berdasarkan kinerja juga dapat memberikan motivasi kepada para karyawan dan juga mengurangi para karyawan yang merasa stagnan pada karir mereka
  
- *Memberikan program konseling, mentorship dan juga pengembangan keterampilan kepada para karyawan*, job satisfaction dan job involvement juga memiliki pengaruh terhadap atrisi karyawan, memberikan akses karyawan kepada program konseling, mentorship atau pengembangan keterampilan dapat memberikan dukungan personal dan juga membantu para karyawan untuk menyelaraskan aspirasi dan ambisi mereka dengan tujuan perusahaan
