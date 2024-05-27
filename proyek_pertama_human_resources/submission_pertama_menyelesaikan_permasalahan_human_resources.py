# -*- coding: utf-8 -*-
"""Submission_Pertama_ Menyelesaikan_Permasalahan_Human_Resources.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OYX_nLs0djfIzwKIFIR-lUYEUHUVXIqR

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

- Nama: Aqilah Nurfaidah Ammardinah
- Email: aqilahnfard@gmail.com
- Id Dicoding: @nuffavoy

## Persiapan

### Menyiapkan library yang dibutuhkan
"""

!pip install pandas sqlalchemy
!pip install scikit-learn==1.2.2
!pip install joblib==1.3.1
import numpy as np
import pandas as pd
import datetime
import tensorflow as tf
import matplotlib.pyplot as plt
import scipy
import matplotlib
import seaborn as sns
import jupyter
import sqlalchemy
import joblib

from sklearn.cluster import KMeans
from sqlalchemy import create_engine
from sklearn.metrics import silhouette_score
from sqlalchemy import create_engine
from sklearn.preprocessing import PowerTransformer
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score

! pip freeze > requirements.txt

"""### Menyiapkan data yang akan digunakan

## Data Understanding

**Gathering Data**

Ambil data
"""

employees_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv")

employees_df.head()

"""**Informasi terkait data karyawan dimuat dalam 34 feature**

- EmployeeId - Employee Identifier
- Attrition - Did the employee attrition? (0=no, 1=yes)
- Age - Age of the employee
- BusinessTravel - Travel commitments for the job
- DailyRate - Daily salary
- Department - Employee Department
- DistanceFromHome - Distance from work to home (in km)
- Education - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
- EducationField - Field of Education
- EnvironmentSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- Gender - Employee's gender
- HourlyRate - Hourly salary
- JobInvolvement - 1-Low, 2-Medium, 3-High, 4-Very High
- JobLevel - Level of job (1 to 5)
- JobRole - Job Roles
- JobSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- MaritalStatus - Marital Status
- MonthlyIncome - Monthly salary
- MonthlyRate - Mounthly rate
- NumCompaniesWorked - Number of companies worked at
- Over18 - Over 18 years of age?
- OverTime - Overtime?
- PercentSalaryHike - The percentage increase in salary last year
- PerformanceRating - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
- RelationshipSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- StandardHours - Standard Hours
-tockOptionLevel - Stock Option Level
- TotalWorkingYears - Total years worked
- TrainingTimesLastYear - Number of training attended last year
- WorkLifeBalance - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
- YearsAtCompany - Years at Company
- YearsInCurrentRole - Years in the current role
- YearsSinceLastPromotion - Years since the last promotion
- YearsWithCurrManager - Years with the current manager

## Data Preparation / Preprocessing

Menghubungkan database menggunakan library pandas
"""

URL = "postgresql://postgres.dctrjwkgkadbbtfpdteg:admin.supa02@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

"""**Data Cleansing**

Cek informasi dataframe
"""

employees_df.info()

"""Cek jumlah missing value pada dataset"""

employees_df.isna().sum()

"""Drop missing value"""

df = employees_df.dropna()

"""Membuat Dataframe baru"""

main_df = df[["EmployeeId", "Age", "Attrition", "BusinessTravel", "DailyRate", "Department", "DistanceFromHome", "Education", "EducationField", "EmployeeCount", "Gender", "JobInvolvement", "JobLevel", "JobRole", "JobSatisfaction", "MaritalStatus", "MonthlyIncome", "NumCompaniesWorked", "OverTime", "PerformanceRating", "TotalWorkingYears", "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager"]]
main_df['status'] = df['Attrition'].apply(lambda x: 'left' if x == 1 else 'stayed')

main_df.columns = ["employee_id", "age", "attrition", "business_travel", "daily_rate", "department", "distance_from_home", "education", "education_field", "employee_count", "gender", "job_involvement", "job_level", "job_role", "job_satisfaction", "marital_status", "monthly_income", "num_companies_worked", "over_time", "performance_rating", "total_working_years", "training_time_years", "work_life_balance", "years_at_company", "years_in_current_role", "years_since_last_promotion", "years_with_current_manager", "status"]
main_df.head(10)

"""**EDA**

Cek deskripsi dataframe
"""

main_df.describe(include="all")

att_df = main_df.query('attrition == 1.0')

"""Melihat distribusi data dari feature kategorikal"""

categorical = ["department", "education_field", "job_role", "marital_status"]

fig, ax = plt.subplots(len(categorical), 1,figsize=(15,22))
for i, feature in enumerate(categorical):
  sns.countplot(data=att_df, x=feature, hue=feature, ax=ax[i])
plt.show()

"""Dapat dilihat bahwa departemen Research & Development memiliki lebih dari 50% pengurangan karyawan dibandingkan dua Departemen lainnya,
kita juga dapat melihat pada background pendidikan, karyawan dengan background medical dan life sciences cenderung memutuskan untuk keluar dari perusahaan. Selain itu ada 3 Role pekerjaan yang memiliki tingkat atrisi paling tinggi yaitu Research scientist, Labroratory technician dan Sales executive, kemudian untuk status pernikahan, atrisi karyawan lebih didominasi oleh karyawan dengan status single

Membuat helper function bernama categorical_plot
"""

def categorical_plot(features, df, segment_feature=None):
    fig, ax = plt.subplots(len(features), 1,figsize=(8,18))
    for i, feature in enumerate(features):
        if segment_feature:
            sns.countplot(data=df, x=segment_feature, hue=feature, ax=ax[i])
        else:
            sns.countplot(data=df, x=feature, ax=ax[i])
    plt.tight_layout()
plt.show()

"""Melihat distribusi data numerik"""

numerical = ["age", "daily_rate", "monthly_income"]
att_df[numerical].hist(bins=25, grid=True)

"""Membuat helper function untuk feature numerik"""

def numerical_dis_plot(features, df, segment_feature=None, showfliers=True):
    fig, ax = plt.subplots(len(features), 1,figsize=(6,12))
    for i, feature in enumerate(features):
        if segment_feature:
            sns.boxplot(y=segment_feature, x=feature, data=df, ax=ax[i], showfliers=showfliers)
            ax[i].set_ylabel(None)
        else:
            sns.boxplot(x=feature, data=df, ax=ax[i], showfliers=showfliers)
    plt.tight_layout()
    plt.show()

def numerical_dis_plot_2(features, df, segment_feature=None, showfliers=True):
    fig, ax = plt.subplots(len(features), 1,figsize=(12,20))
    for i, feature in enumerate(features):
        if segment_feature:
            sns.boxplot(y=segment_feature, x=feature, data=df, ax=ax[i], showfliers=showfliers)
            ax[i].set_ylabel(None)
        else:
            sns.boxplot(x=feature, data=df, ax=ax[i], showfliers=showfliers)
    plt.tight_layout()
    plt.show()

"""Membuat grafik box plot"""

numerical_dis_plot(
    features=["age", "years_with_current_manager", "education", "job_satisfaction", "monthly_income", "job_involvement"],
    df=att_df,
    segment_feature="status"
)

"""Terlihat bahwa karyawan dengan rentang usia sekitar 25 sampai dengan pertengahan 30 an memiliki peluang tingkat atrisi yang lebih tinggi dibandingkan usia lainnya,

Dalam atrisi karyawan berdasarkan beberapa tahun dibawah bimbingan manager, atrisi karyawan didominasi oleh hubungan dengan tahun pertama hingga kelima,

Kemudian kita juga dapat melihat pada level pendidikan karyawan dengan tingkat pendidikan yang setara dengan s1 sampai dengan s2 cenderung memutuskan untuk keluar dari perusahaan,

Kemudian pada atrisi berdasarkan kepuasan pekerja, atrisi didominasi oleh karyawan dengan level kepuasan 3 kebawah,

Selanjutnya penghasilan perbulan juga memperlihatkan bahwa para karyawan berpotensi lebih besar untuk mengundurkan diri pada rentang pendapatan dibawah 6000,

Pada level keterlibatan dalam pekerjaan, atrisi didominasi oleh level pertengahan antara level 2 hingga level 3,

## Modeling

Membuat dataframe baru dengan feature numerik
"""

kmeans_df = att_df[["employee_id", "age", "education", "distance_from_home", "job_level", "daily_rate", "total_working_years", "performance_rating", "job_involvement", "job_satisfaction", "years_with_current_manager", "monthly_income", "attrition"]]
kmeans_df.head(10)

"""Mengatasi skewness menggunakan metode power transform dan menyimpan object transformer ke dalam berkas .joblib"""

def power_transforms(features, df):
  df = df[features]
  for feature in features:
    transformer = PowerTransformer(standardize=True)
    y = np.asanyarray(df[feature])
    y = y.reshape(-1,1)
    transformer.fit(y)
    df["transform_{}".format(feature)] = transformer.transform(y)
    df.drop([feature], axis=1, inplace=True)
    joblib.dump(transformer, "transformer_{}.joblib".format(feature))
  return df

"""Menggunakan helper function power_transforms"""

transformed_kmeans_df = power_transforms(
    features=["employee_id", "age", "education", "distance_from_home", "daily_rate", "job_level",
              "job_involvement", "job_satisfaction", "years_with_current_manager", "monthly_income", "total_working_years"],
    df=kmeans_df
)
transformed_kmeans_df.head()

"""Cek distribusi dataframe"""

numerical_dis_plot(
    features=["transform_employee_id", "transform_age", "transform_education", "transform_distance_from_home", "transform_job_level",
              "transform_job_involvement", "transform_job_satisfaction", "transform_years_with_current_manager", "transform_monthly_income", "transform_total_working_years"],
    df=transformed_kmeans_df,
)

"""Membuat model K-means Clustering"""

inertia = {}
silhouette = {}

for k in range(2,10):
    model = KMeans(n_clusters = k, random_state=75)
    model.fit_predict(transformed_kmeans_df)
    inertia[k]= model.inertia_
    silhouette[k]= silhouette_score(transformed_kmeans_df, model.labels_)

fig, axs = plt.subplots(1,2, figsize = (11,4))
axs[0].plot(inertia.keys(), inertia.values(), marker = 'o', lw = 3)
axs[0].set_xlabel('Number of Clusters', fontsize = 12)
axs[0].set_ylabel('Inertia')
axs[0].set_title('The Elbow Method', fontsize = 15)

axs[1].plot(inertia.keys(), silhouette.values(), marker = '*' , lw = 3)
axs[1].set_xlabel('Number of Clusters', fontsize = 12)
axs[1].set_ylabel('Silhouette Coefficient')
axs[1].set_title('The Silhouette Method', fontsize = 15)
plt.show()

"""Membuat dan melatih model K-means dengan jumlah klaster 4, kemudian menyimpan model ke dalam berkas kmeans_clustering_model.joblib"""

K = 4

model = KMeans(n_clusters=K, random_state=75)
model.fit(transformed_kmeans_df)

joblib.dump(model, "kmeans_clustering_model.joblib")

"""Menggunakan model untuk mengelompokkan karyawan ke dalam empat klaster"""

clusters = model.predict(transformed_kmeans_df)

kmeans_df["employee_status"] = clusters.astype(str)
kmeans_df.sample(5)

"""Menggabungkan data Kmeans_df dengan att_df"""

result_kmeans_df = pd.merge(
    left=att_df,
    right=kmeans_df[["employee_id", "employee_status"]],
    on="employee_id",
    how="inner"
)

result_kmeans_df.head()

"""**Menganalisis dan menginterpretasi hasil dari model k-means clustering**

Menentukan urutan nilai kategorikal pada kolom employee_status
"""

result_kmeans_df['employee_status'] = pd.Categorical(result_kmeans_df['employee_status'], [
    "0", "1", "2", "3"
])

"""Melihat distribusi pelanggan pada setiap kelompok atau klaster"""

sns.countplot(data=result_kmeans_df, y='employee_status')

"""Karyawan dalam atrisi kita didominasi oleh klaster 0, 2 dan 3

Melihat karakteristik setiap klaster berdasarkan feature numerik
"""

numerical_dis_plot_2(
    features=["age", "education", "distance_from_home", "job_involvement", "job_satisfaction",
              "years_with_current_manager", "years_since_last_promotion", "monthly_income"],
    df=result_kmeans_df,
    segment_feature="employee_status"
)

"""*   Klaster 2 dan 3 merupakan kelompok karyawan yang melakukan atrisi paling banyak, pada rentang usia diatas 25 hingga mendekati 50
*   klaster 2 dan 3 merupakan kelompok karyawan yang melakukan atrisi pada rentang pendidikan level 2 hingga 3
*   klaster 2 adalah karyawan yang melakukan atrisi paling banyak dalam rentang jarak atara rumah dan kantor sekitar 4 sampai 20 kilometer
*   klaster 0, 1, 2 dan 3 adalah karyawan yang sama sama melakukan atrisi pada level keterlibatan pekerja sekitar level 2 hingga level 3
*   klaster 0 dan 2 adalah karyawan yang melakukan atrisi pada level kepuasan pekerja sekitar level 2 hingga level 4, sedangkan klaster 1 dan 3 adalah karyawan yang melakukan atrisi pada level 1 hingga level 3
*   klaster 2 adalah karyawan yang melakukan atrisi paling banyak pada tahun ke 3 hingga 7 bersama dengan manajer mereka
*   klaster 2 adalah karyawan yang melakukan atrisi paling banyak pada sekitar 0 sampai 7 tahun terakhir sejak mendapat promosi
*   klaster 2 adalah karyawan yang melakukan atrisi paling banyak pada rentang pendapatan 5000 hingga 10000 perbulan

Berikut beberapa poin yang dapat disimpulkan dari grafik di atas

* Kluster 2 merupakan kelompok karyawan dengan atrisi tinggi yang memiliki tingkat kepuasan yang tinggi

* Kluster 3 merupakan kelompok karyawan dengan atrisi tinggi yang memiliki tingkat kepuasan yang rendah

* Kluster 1 merupakan kelompok karyawan dengan atrisi rendah yang memiliki tingkat kepuasan yang rendah

* Kluster 0 merupakan kelompok karyawan dengan atrisi rendah yang memiliki tingkat kepuasan yang tinggi

## Evaluation
"""

le = LabelEncoder()

for col in ['business_travel', 'education_field', 'department', 'gender', 'education', 'job_role', "over_time", 'marital_status', 'years_with_current_manager', 'status']:
    result_kmeans_df[col] = le.fit_transform(result_kmeans_df[col])

X = result_kmeans_df.drop('employee_status', axis=1)
y = result_kmeans_df['employee_status']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("---------------------------")
print("Random Forest")
print(f"Accuracy: {accuracy}")
print("---------------------------")