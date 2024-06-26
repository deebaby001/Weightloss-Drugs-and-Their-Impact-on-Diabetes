
![weightloss drugs multiple types](https://github.com/deebaby001/Weightloss-Drugs-and-Their-Impact-on-Diabetes/assets/14750340/36ea2eb4-258b-4a62-8406-8b5747e25997)


# Weightloss-Drugs-and-Their-Impact-on-Diabetes

In this study we will take a look a the impact of four of the top selling injectable, prescriptiongm drugs for weight loss currently available: Wegovy, Ozempic, Semaglutide and Zepbound. I will review of their differences and similarities and the effects these types of therapies cause. Finally, in consideration of ith the the overall impact these are having in combating the epidemic of Diabetes in the United States.

Sprint Deliverables

Sprint 0 Deliverables ( See Google Drive)
https://docs.google.com/document/d/1Qq7B4UZuYO--Y4lo7M5itMpAUHcQjah2tZRD1FOx5Q8/edit?usp=sharing

Sprint 1: Deliverables ( See Google Drive)
https://docs.google.com/document/d/1qbFLLd-yNodoMxrycrm29KxqD2oDXEzEa2yswZDDFw4/edit

Sprint 2: Deliverable (See Google Drive)
https://docs.google.com/document/d/1uHtWrQUwLL61G3zWSVwopTAL_J_QkDWGv13rA4EK07E/edit?usp=sharing

Sprint 3: Deliverable (See Google Drive)
https://docs.google.com/document/d/1mKDWEXSCXRVxumQzdJLAExe-s6d9t1o1KepQ5tshqtE/edit
=============================
Overall Purpose of this Study
In this study, I am investigating the relationship between the curent sales and projected sales of several types of injectable weghtloss drugs and their relationship to comorbid factors effecting the disease, diabetes. 

Introductory Overview

Diabetes 

The disease symptomology, Diabetes, also known as Diabetes Mellitus, is a chronic disease that occurs when your blood glucose, also called blood sugar, is too high. Glucose is your body’s main source of energy, which comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose get into your cells to be used for energy. In diabetes, your body doesn’t make enough—or any—insulin, or doesn’t use insulin properly. As a result, glucose stays in your blood and doesn’t reach your cells, leading to various health problems.

Forms / Types of Diabetes

Type 1 Diabetes: This is an autoimmune condition where your body's immune system attacks and destroys the cells in your pancreas that make insulin. People with type 1 diabetes need to take insulin every day to stay alive.

Type 2 Diabetes: In this type, your body doesn’t use insulin well and can’t keep blood sugar at normal levels. It is the most common type of diabetes.

Gestational Diabetes: This type develops in some people during pregnancy. Most of the time, this type of diabetes goes away after the baby is born.

Prediabetes: People with prediabetes have blood glucose levels that are higher than normal but not high enough to be diagnosed with type 2 diabetes.

Comorbidity Factors of Diabetes
Obesity: This is termed as any person having a BMI over 28%
Dysilpidema: This refers to a symptomology where there is an instability of hormones. Specifically, these that most effect weight: 
Hypertension: The term, hypertension, is just another word for, High Blood Pressure.

Comorbidity Factors and Diabetes

In 2015, the Centers for Disease Control, piloted a study on 33 factors that were labeled the Behavioral Risk Factor Surveillance System (BRFSS). For the purposes of this study, I will be utilizing a subset of this originally documented dataset. The original study conducted in 2015 (CDC) called the Behavioral Risk Factor Surveillance System (BRFSS), a telephone survey that begun in 1984 and is conducted annually by the CDC. Each year, over 400,000 people in the United States are surveyed concerning health-related behaviors, chronic health conditions and the use of preventative services.
https://www.medicalnewstoday.com/articles/321844

Treatments for Diabetes

In the past decade, the treatment of diabetes has seen significant advancements. The growing availability of different drug classes and agents, rising use of combination therapy, and evolving clinical guidance have fundamentally improved the outlook for people with this condition. However, there is still no cure for diabetes, but losing weight, eating healthy food, and being active can really help. Other things you can do to help include taking medicine as prescribed, getting diabetes self-management education and support, and making and keeping healthcare appointments.

Here are the injectable drugs: Wegovy, Ozempic, Semaglutide and Zepbound that we will evaluate in this study.

- Wegovy: Wegovy is a prescription medication used for weight loss in adults with obesity or overweight and weight-related medical problems. It is an injectable form of semaglutide, a glucagon-like peptide-1 (GLP-1) receptor agonist, that works by reducing appetite and slowing the rate of food passing through the body.

- Ozempic: Ozempic, also known as semaglutide, is an injectable medication used to treat type 2 diabetes. It belongs to a class of drugs known as glucagon-like peptide-1 (GLP-1) receptor agonists and helps manage blood sugar levels in adults with type 2 diabetes, along with exercise and a healthy diet.

- Semaglutide: Semaglutide is an antidiabetic medication used for the treatment of type 2 diabetes and an anti-obesity medication used for long-term weight management. It is a peptide similar to the hormone glucagon-like peptide-1 (GLP-1), modified with a side chain, and can be administered by subcutaneous injection or taken orally.

- Zepbound: Zepbound, also known as tirzepatide, is a prescription drug used for weight loss in certain adults. It is a glucose-dependent insulinotropic polypeptide (GIP) receptor and glucagon-like peptide-1 (GLP-1) receptor agonist, which works by decreasing appetite and slowing the movement of food from the stomach into the small intestine.



EDA

Diabetes Early-Onset dataset
Summary Statistics

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>520.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>48.028846</td>
    </tr>
    <tr>
      <th>std</th>
      <td>12.151466</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>39.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>47.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>57.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>90.000000</td>
    </tr>
  </tbody>
</table>
</div>

by Age (histogram)

![image](https://github.com/deebaby001/Weightloss-Drugs-and-Their-Impact-on-Diabetes/assets/14750340/b0fabe26-9002-442d-89be-7fdc903a0393)


by Gender (bar)

![image](https://github.com/deebaby001/Weightloss-Drugs-and-Their-Impact-on-Diabetes/assets/14750340/d9a6f2bb-d76e-4892-b311-1e1541bfc30d)


by Age + Gender (boxplot)

![image](https://github.com/deebaby001/Weightloss-Drugs-and-Their-Impact-on-Diabetes/assets/14750340/33aff619-c067-4679-a22a-59ceedde566c)


Data Transformations

Null values

Age                   0
Gender                0
Polyuria              0
Polydipsia            0
sudden weight loss    0
weakness              0
Polyphagia            0
Genital thrush        0
visual blurring       0
Itching               0
Irritability          0
delayed healing       0
partial paresis       0
muscle stiffness      0
Alopecia              0
Obesity               0
class                 0
dtype: int64



Risks
Inaccessibility of datasets: This is due to HIPPA and other medically related requirements as mandated by the holding companies of much of the research data that exists. 

Resources
How to cite a source: Author, A. (Year). Title of the data set (Version number) [Data set]. Publisher Name.
1. Kumar, A. (2020). https://www.kaggle.com/datasets/singhakash/early-stage-diabetes-risk-prediction-datasets?resource=download&select=diabetes_data_upload.csv. Kaggle.
   
