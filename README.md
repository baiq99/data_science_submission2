# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
**Jaya Jaya Institut** adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan dengan reputasi yang sangat baik di berbagai bidang. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut juga menghadapi tantangan yang signifikan terkait dengan tingginya tingkat siswa yang tidak menyelesaikan pendidikannya alias dropout.

**Masalah dropout** ini merupakan masalah yang serius bagi institusi pendidikan, karena dropout yang tinggi dapat mempengaruhi citra institusi, mengurangi tingkat kelulusan, dan pada akhirnya berdampak pada daya tarik institusi bagi calon siswa di masa mendatang. Tingkat dropout yang tinggi juga bisa menjadi indikasi bahwa ada masalah mendasar dalam proses penerimaan siswa, pembelajaran, atau dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis
Berikut adalah beberapa pertanyaan yang menggambarkan permasalahan bisnis yang akan diselesaikan oleh Jaya Jaya Institut:

1. Bagaimana cara mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini?
2. Faktor-faktor apa saja yang paling berpengaruh terhadap keputusan siswa untuk dropout?
3. Apa yang dapat dilakukan untuk meningkatkan tingkat retensi siswa dan memastikan lebih banyak siswa menyelesaikan pendidikan mereka?

### Cakupan Proyek
* Analisis Data: Menggunakan data yang ada untuk mengidentifikasi faktor-faktor utama yang mempengaruhi dropout.
* Visualisasi & Pelaporan: Mengembangkan dashboard yang dapat digunakan untuk memonitor dan menganalisis faktor-faktor tersebut secara visual.
* Rekomendasi & Intervensi: Berdasarkan hasil analisis, memberikan rekomendasi untuk intervensi yang dapat dilakukan untuk mengurangi droput.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset Jaya Jaya Institut
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

* Setup Environment - Anaconda
   conda create --name base python=3.12
   conda activate base
   pip install -r requirements.txt

* Setup Environment - Shell/Terminal
   mkdir Submission 1-Proyek Data Science-Baiq Ega Aulia
   cd Submission 1-Proyek Data Science-Baiq Ega Aulia
   pipenv install
   pipenv shell
   pip install -r requirements.txt

* Run predict_attrition_app
   python predict_attrition_app.py

* Menyiapkan Metabase:
    ```bash
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses melalui browser di: [http://localhost:3000/setup](http://localhost:3000/setup)

    username: root@mail.com
    password: root123

* Setup database (Supabase):
    - Daftar di: https://supabase.com/dashboard/sign-in
    - Buat proyek baru, salin `DATABASE_URL` dari pengaturan
    - Kirim data menggunakan SQLAlchemy:
    ```python
    from sqlalchemy import create_engine
    engine = create_engine("DATABASE_URL")
    df.to_sql('dataset_edutech', engine)
    ```
* Menjalankan Sistem Machine Learning
   


## Business Dashboard
Dashboard ini dirancang untuk memberikan wawasan komprehensif kepada institut terhadap faktor-faktor yang berkontribusi dengan `Status` baik dropout, enrolled, ataupun graduated. Dengan dashboard ini tim institut dapat :
1. Memantau Tingkat Dropout Secara Proaktif:
    - Melalui visualisasi persentase siswa yang dropout, enrolled, dan graduate, tim dapat memantau tren dropout secara real-time. Ini memungkinkan institusi untuk segera mengambil tindakan jika terlihat ada peningkatan signifikan dalam tingkat dropout.

2. Menganalisis Faktor-Faktor yang Mempengaruhi Dropout:
    - Dengan analisis mendalam tentang bagaimana faktor-faktor seperti nilai akademik, beasiswa, biaya pendidikan, dan kualifikasi orang tua mempengaruhi status siswa, tim dapat mengidentifikasi elemen-elemen yang paling berisiko bagi siswa. Ini memungkinkan penyesuaian kebijakan dan intervensi yang lebih tepat sasaran.

Akses Dashboard: http://localhost:3000/public/dashboard/0c596eac-0e72-4165-af73-4ff1c5539f07

## Conclusion
Proyek ini dirancang untuk membantu Jaya Jaya Institut memahami dan menanggulangi permasalahan tingginya angka mahasiswa yang dropout. Berikut adalah ringkasan dari temuan utama:
1. **Identifikasi Dini Mahasiswa Berisiko Dropout**
   Dengan menerapkan model prediksi berbasis Random Forest, institusi kini dapat mengenali mahasiswa yang berpotensi mengalami dropout sejak dini. Model ini bekerja berdasarkan data historis serta faktor akademik, demografis, dan ekonomi, memberikan hasil yang cukup akurat untuk mendukung pengambilan keputusan.
2. **Faktor-Faktor Utama yang Mempengaruhi Dropout**
   Berdasarkan analisis korelasi dan feature importance, ditemukan bahwa performa akademik (nilai dan jumlah mata kuliah yang diambil) serta kondisi keuangan (seperti beasiswa dan status pemukiman) merupakan faktor paling dominan. Mahasiswa dengan performa akademik rendah di awal masa studi cenderung lebih berisiko untuk keluar.
3. **Strategi untuk Meningkatkan Retensi Mahasiswa**
   Untuk meningkatkan tingkat kelulusan, institusi disarankan untuk melakukan intervensi berbasis data secara dini, seperti menyediakan dukungan akademik tambahan, menyesuaikan beban studi, dan memperluas bantuan keuangan bagi mahasiswa yang membutuhkan.

## Rekomendasi Tindakan
Berikut beberapa langkah strategis yang dapat diambil oleh Jaya Jaya Institut guna menekan angka dropout dan meningkatkan keberhasilan studi mahasiswa:
1. **Penerapan Sistem Pemantauan Berbasis Prediksi**
   Implementasikan model prediktif dalam sistem monitoring rutin guna mengidentifikasi mahasiswa berisiko tinggi dan memberikan intervensi yang tepat waktu.
2. **Penguatan Layanan Akademik dan Psikologis**
   Perluasan akses terhadap bimbingan belajar, konseling, dan dukungan kesehatan mental sangat penting untuk membantu mahasiswa yang menghadapi kesulitan secara akademik maupun personal.
3. **Reformasi Kurikulum dan Evaluasi Program Studi**
   Tinjau ulang program studi dengan angka dropout tinggi dan sesuaikan kurikulum atau metode pengajaran. Penambahan fleksibilitas jadwal dan materi pembelajaran yang mendukung dapat membantu mengurangi tekanan akademik.
