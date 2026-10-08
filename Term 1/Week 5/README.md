# Term 1 - Week 5: Machine Learning Basics

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

The workshop introduced the basic steps of a machine-learning classification project: preparing data, checking the target distribution, making a train/test split, and using a Pipeline to avoid data leakage.

**What did I hand in?**

The completed work for this week is in the hackathon notebook and presentation. I did not make a separate workshop submission.

**What did I find difficult, and how did I solve it?**

At first, I found class imbalance and the train/test split confusing. I learned that a model can appear accurate by predicting only the largest class, so we used balanced accuracy and a stratified split instead.

### Checklist

- [ ] No separate workshop file was submitted this week.
- [x] The hackathon notebook runs from the raw data through to a prediction.

---

## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:**

Income classification with the UCI Adult dataset

**My pair partner:**

Iqbal

**Tool we had to use:**

Python, scikit-learn, and Jupyter Notebook

**SDG we had to address:**

SDG 8: Decent Work and Economic Growth

**What problem does it solve, and for whom?**

The project studies income patterns in U.S. Census data from 1994. It predicts whether an adult belongs to the `<=50K` or `>50K` income class using education and employment information. Our intended users are labour-market researchers who want to study broad patterns and evaluate training or employment policy. They are not individual caseworkers or organisations deciding whether one person receives support. As context, the U.S. Census Bureau reported that 38.1 million people, or 14.5% of the population, were below the official poverty level in 1994. This poverty figure gives context for economic security, but it is not the target our model predicts. [U.S. Census Bureau](https://www.census.gov/library/publications/1996/demo/p60-189.html)

**What did you build?**

We built a scikit-learn notebook that starts with the raw UCI Adult files and ends with a prediction for a fictional person. The notebook cleans the data, makes a stratified train/test split, and uses a Pipeline to fill missing values, scale numerical data, and encode categories. We compared a Dummy baseline, KNN, Logistic Regression, and Random Forest. Random Forest performed best on balanced accuracy and on F1 score for the smaller `>50K` class.

**How did we evaluate it?**

The income classes are imbalanced: 76.1% of records are `<=50K` and 23.9% are `>50K`. For that reason, we tuned all three models with 3-fold cross-validation using balanced accuracy rather than ordinary accuracy. We kept 20% of the data separate for final testing. The Dummy baseline achieved a balanced accuracy of 0.50, while the selected Random Forest achieved 0.757 in cross-validation and 0.766 on the final test set.

**Link to the live thing (if any):**

There is no separate website. The working prototype is the Google Colab notebook. Its final cell makes a prediction for a fictional person and shows the predicted income class and probability.

**How do I run it?**

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload or open `Adult_Income_Classification.ipynb`.
3. Connect to a runtime, then choose **Runtime > Run all**.
4. Wait for the training cells to finish. The notebook downloads the UCI Adult data automatically, so no manual data upload is needed.
5. In the final cell, view the prediction for the fictional person.

Tested in Google Colab with Python, pandas, scikit-learn, and matplotlib.

**Who did what?**

- **Max Lopez:** Defined the research question, user, and SDG 8 link. Loaded, combined, and cleaned the data; performed exploratory analysis; created the stratified train/test split; and prepared the presentation.
- **Iqbal:** Built the preprocessing Pipeline, trained and tuned the models, evaluated the results, and made the fictional-person prediction cell.
- **Together:** We ran the completed notebook in Google Colab and checked that it works from the raw data through to the final prediction.

**Ethical reflection - what are the risks of your tool? Who could it harm?**

The main risk is that the model can copy patterns and inequalities from historical data. The dataset is from the United States in 1994, and it includes sensitive characteristics such as race and sex. A prediction of `>50K` for someone who actually belongs in the `<=50K` class could be harmful if a real organisation used it to withhold support. We reduced one technical risk by using a Pipeline, so missing-value handling and encoding are fitted only on training data. We also used balanced accuracy because the `>50K` class is much smaller. The notebook and presentation clearly state that this model is for research and education only, not automatic decisions. Before any real-world use, we would also need to compare errors across groups such as sex.

### Dataset Card / Paragraph

- **Source & Link:** [UCI Machine Learning Repository, Adult dataset](https://archive.ics.uci.edu/dataset/2/adult).
- **Who collected it:** Extracted by Barry Becker from the 1994 U.S. Census database.
- **When and how:** Collected in 1994 through U.S. Census data.
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Number of rows and columns:** 48,842 rows and 15 columns before cleaning. After removing 52 exact duplicates and dropping two columns, the analysis used 48,790 rows and 13 columns.
- **Target & class balance:** The target is `income` (`<=50K` or `>50K`). 76.1% of records are `<=50K` and 23.9% are `>50K`.
- **Known limitations:** The data is from 1994, covers only the U.S. context, and may reflect historical bias related to race and sex.

### Checklist

- [x] Add `Adult_Income_Classification.ipynb` to `hackathon/` before submitting to GitHub.
- [x] Add the PowerPoint file to `hackathon/` before submitting to GitHub.
- [x] The prototype runs, and the run instructions are written above.
- [x] Ethical reflection written above.

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in if our group is selected to present.*

- [ ] My group presented in this week.
- [ ] Slides are in `presentation/`.
- [ ] Proof of the live demo is in `presentation/`.

**How did it go? What would I do differently next time?**

Not presented yet.

---

## 4. Reflection

**What is the most important thing I learned this week?**

I learned how to turn raw data into a usable dataset for machine learning. I loaded and combined the two Adult dataset files, standardised the income labels, removed exact duplicate rows, and checked missing values. I also explored the data to understand the income-class imbalance and created a reproducible stratified train/test split. This showed me why data preparation and checking the data are necessary before building a model.

**Where does this connect to "AI for Good"?**

My work connects to AI for Good because it investigates patterns related to income and economic security, which fits SDG 8: Decent Work and Economic Growth. The project can help labour-market researchers study broad patterns, but it should not make decisions about individual people. Because the data is from the United States in 1994 and includes sensitive characteristics, we must be careful not to reproduce historical inequalities or treat the prediction as fact.
