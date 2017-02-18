import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from ClassifierWrapper import ClassifierWrapper
import tempfile

# Get data fetched from UI
formatData = tempfile.gettempdir() + "\\ba_data.txt"
with open(formatData) as f:
    content = f.readlines()

# Below the Data Set is being read
# Alternatively, use content[0]
trainFileName = tempfile.gettempdir() + "\\ba_query.csv"
Data = pd.read_csv(trainFileName)

# Selecting the Columns of OBJECT type
olist = list(Data.select_dtypes(['object']))

# Converting the OBJECT type to INTEGER type
for col in olist:
    Data[col] = Data[col].astype('category').cat.codes

# Loading the ATTRIBUTE columns
X = Data.drop(content[1], axis=1)

# Loading the TARGET column
Y = Data[content[1]].astype('category')

# Splitting the DATA
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=3)

# Instantiating KN NEIGHBOURS Class
kn = KNeighborsClassifier(n_neighbors=1)

# Calling the Wrapper Class
cw = ClassifierWrapper(kn, X_train, X_test, Y_train, Y_test)

# Print all values from the KNN classifier
# Printed values will be used by the UI to display to user
print(cw.values())

# Now predict
# Alternatively, use content[2]
queryFileName = tempfile.gettempdir() + "\\ba_query.csv"

# TODO: Now do the same thing for the query file, and call cw.predict
