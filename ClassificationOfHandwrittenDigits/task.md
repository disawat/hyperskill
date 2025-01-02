# Project: Classification of Handwritten Digits

## Description
We start by feeding data to our program. We will use the MNIST digits dataset from Keras.
To proceed, we need to figure out how a machine sees pictures. A computer senses an image as a 2D array of pixels. Each pixel has coordinates (x, y) and a value — from 0 (the darkest) to 255 (the brightest).
In machine learning, we need to flatten (convert) an image into one dimension array. This means that a 28x28 pixels image, which is initially a 2D array, transforms into a 1D array with 28x28 = 784 elements in it.

## Stage 1/5: The Keras dataset
1. Import tensorflow and numpy to your program. The first one loads the data, the second one transforms it;
2. Load the data in your program. You need x_train and y_train only. Skip x_test and y_test in return of load_data(), we will create them ourselves in the next stage.
Sometimes x_train or x_test will be called the features array (because they contain brightnesses of the pixels, which are the images' features). y_train or y_test will be called the target array (because they contain classes, digits which we are going to predict);
3. Reshape the features array to the 2D array with n rows (n = number of images in the dataset) and m columns (m = number of pixels in each image);
4. Print information about the dataset: target classes' names; the shape of the features array; the shape of the target array; the minimum and maximum values of the features array.

## Stage 2/5: Split into sets
At this stage, you need to use sklearn to split your data into train and test sets. We will use only a portion of the dataset to process model training faster in the next stage.

It is crucial to ensure a balanced training dataset after splitting, as an insufficient amount of data for training recognition of certain digits can negatively impact the quality of our model. We will check this point as well.

Objectives:
1. Import a necessary tool from sklearn;
2. Use the first 6000 rows of the datasets. Set the test set size as 0.3 and the random seed of 40 to make your output reproducible;
3. Print new datasets' shapes.
4. Let's make sure that our dataset is balanced after splitting. Print the proportions of samples per class in the training set as in the example below. We recommend using pd.Series.value_counts(normalize=True).

## Stage 3/5: Train models with default settings
We are ready to train our models. In this stage, you need to find the best algorithm that can identify handwritten digits. Refer to the following algorithms: K-nearest Neighbors, Decision Tree, Logistic Regression, and Random Forest. In this stage, you need to train these four classifiers with default parameters. In the next stages, we will try to improve their performances. We will use an accuracy metric to evaluate the models.

Objectives:
1. Import sklearn implementations of the classifiers from the description and the accuracy scorer;
2. Since you are going to train a lot of models, implementing the following function will make the process fast and convenient:

# the function
def fit_predict_eval(model, features_train, features_test, target_train, target_test):
    # here you fit the model
    # make a prediction
    # calculate accuracy and save it to score
    print(f'Model: {model}\nAccuracy: {score}\n')


# example
# code
fit_predict_eval(
        model=KNeighborsClassifier(),
        features_train=x_train,
        features_test=x_test,
        target_train=y_train,
        target_test=y_test
    )
# output
# >>> Model: KNeighborsClassifier()
# >>> Accuracy: 0.1234

3. Initialize the models with default parameters. Some of the algorithms have randomness, so you need to set random_state=40 to receive reproducible results;
4. Fit the models;
5. Make predictions and print the accuracies. Make sure that the program prints the models and their results in the following order: K-nearest Neighbors, Decision Tree, Logistic Regression, and Random Forest;
6. Which model performs better? Print the answer, including the model's name without parameters, and its accuracy. Round the result to the third decimal place.

## Stage 4/5: Data preprocessing
At this stage, we will improve model performance by preprocessing the data. We will see how normalization affects the accuracy. Recall that normalization scales values of features from 0 to 1.

Objectives:
1. Import sklearn.preprocessing.Normalizer transformer;
2. Initialize the normalizer, transform the features (x_train and x_test), and then save the output to x_train_norm and x_test_norm;
3. Answer the following questions:
    - Does the normalization have a positive impact in general? (yes/no)
    - Which two models show the best scores? Round the result to the third decimal place and print the accuracy of models in descending order.

## Stage 5/5: Hyperparameter tuning
In the final stage, you need to improve model performance by tuning the hyperparameters. No need to do it manually, as sklearn has convenient tools for this task. We advise using GridSearchCV. It searches through the specified parameter values for an estimator. Basically, it takes estimator, param_grid, and scoring as arguments. As a starting point, you will be provided with a list of parameters to find a better set than the default one.

We urge you to try more parameter values to improve the result. The test system has minimum requirements on the algorithms and their accuracies. It can pass only two algorithms (K-nearest Neighbors and Random Forest) that performed in the best possible way in the previous stage. Concerning the scores, the test system requires values that can be achieved by finding the best set of parameters from the lists below.

Objectives:
1. Choose a data representation that performed the best. You need to choose between the initial dataset and the one with normalized features. You also take only two models with the highest accuracy;
2. Initialize GridSearchCV(estimator=..., param_grid=..., scoring='accuracy', n_jobs=-1) to search over the following parameters:
    - For the K-nearest Neighbors classifier: {'n_neighbors': [3, 4], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'brute']}
    - For the Random Forest classifier: {'n_estimators': [300, 500], 'max_features': ['sqrt', 'log2'], 'class_weight': ['balanced', 'balanced_subsample']}. Don't forget to set random_state=40 in the Random Forest classifier!
    Note that njobs parameter is responsible for the number of jobs that will be run in parallel. Set njobs=-1 to use all processors;
3. Run the fit method for GridSearchCV. Use the train set only. Since a number of models (one of two algorithms with a set of parameter values is one model) must be trained to compare the performances, this step will take about 30 minutes;
4. Print the best sets of parameters for both algorithms. You can get this information in the attribute called best_estimator_ of each algorithm's GridSearchCV instance. Train two best estimators on the test set and print their accuracies.