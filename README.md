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
<p>Since the data is too large so I would represent 100 documents per label to train and test (view branch V3, this branch is use 10 document per label to train and test). The results were not very satisfactory because the data collected for training was not much. <br />
Result : <br />
type 1 : 35.64356435643564% <br />
type 2 : 51.48514851485149% <br />
type 3 : 27.722772277227726% <br />
type 4 : 43.56435643564357% <br />
type 5 : 58.415841584158414% <br />
type 6 : 49.504950495049506% <br />
type 7 : 57.42574257425742% <br />
type 8 : 41.584158415841586% <br />
type 9 : 69.3069306930693% <br />
type 10 : 37.62376237623762% <br />
</p>
