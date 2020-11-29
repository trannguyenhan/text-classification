# classify-labels-for-articles
Classify labels for news with k-nearest-neighbor algorithms <br />
The data set in the project has been pre-processed :
<ol>
<li>Delete HTML code in the data</li>
<li>Standardization of Vietnamese Unicode</li>
<li>Standardized typing method</li>
<li>Separated Vietnamese words</li>
<li>Lowercase</li>
<li>Delete unnecessary characters</li>
<li>Eliminate Vietnamese stopword</li>
</ol>

<p>Name and number of label write in file path_file_dataset.txt <br/></p>
<p>Since the data is too large so I would represent 10 documents per label to train and test. The results were not very satisfactory because the data collected for training was not much. <br />
Result : <br />
type 1 : 36.36363636363637% <br />
type 2 : 27.27272727272727% <br />
type 3 : 27.27272727272727% <br />
type 4 : 9.090909090909092% <br />
type 5 : 45.45454545454545% <br />
type 6 : 9.090909090909092% <br />
type 7 : 36.36363636363637% <br />
type 8 : 45.45454545454545% <br />
type 9 : 54.54545454545454% <br />
type 10 : 9.090909090909092% <br />
</p>