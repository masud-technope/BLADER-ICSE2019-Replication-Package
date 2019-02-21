
# Improving IR-Based Bug Localization with Data Analytics-Driven Query Reformulation


Abstract
------------------------------------------------------
```
Recent findings suggest that IR-based bug localization techniques do not perform well with low quality bug reports 
since they do not contain any program entity names. 
Such entities could help find the encountered bugs or defects in the source code of a software system.
While there are a few studies that attempted to address this issue with query reformulation (i.e., improving the query texts), 
they often fail because of their high reliance on the report texts.   
In this paper, we propose a novel technique--BLADER--that localizes buggy entities from a software project using appropriate 
query reformulation and effective information retrieval. 
First, we build a multi-dimensional semantic space and a large vocabulary of ~660K words by employing a popular text mining algorithm (FastText) on 1.40 million Q&A 
threads of Stack Overflow. Second, we improve a poor query by choosing appropriate keywords 
from the source code that have high clustering tendency with the query within the semantic space above.
Third, we use the improved query for bug localization with Information Retrieval. 
Experiments with 1,546 queries from six subject systems report that our approach can localize bugs with 17% higher MAP and 21% higher MRR 
than the baseline. Comparisons with eleven existing approaches including the state-of-the-art show 
that our technique achieves 11% higher MAP, 15% higher MRR, and 
improves 23% more of the poor queries
intended for the bug localization.
```

Subject Systems (6):
-------------------------------------------------------
- ecf (163)
- eclipse.jdt.core (132)
- eclipse.jdt.debug (229)
- eclipse.jdt.ui (407)
- eclipse.pde.ui (510)
- tomcat70 (105)

**Total Bugs: 1,546**

Materials Included
-------------------------------------------------------
**Baseline Method**

- ```Baseline/query```: Baseline queries.
- ```Baseline/rank```: Query Effectiveness of the baseline queries.


**BLADER: The proposed technique**

- ```BLADER/query```: Reformulated queries by our technique. The tool will store queries in this folder.
- ```BLADER/rank```: Query Effectiveness(QE) of our queries. The tool will store the QE of the queries in this folder.
- ```BLADER-Reported/query```: Reformulated queries by our technique (as reported in the paper).
- ```BLADER-Reported/rank```: Query Effectiveness of our queries (as reported in the paper).


**Bug Report & Goldsets**

- ```BugReport```: Raw contents from 1,546 bug reports from six subject systems.
- ```Goldset```: Change set of 1,546 reported bugs
- ```SelectedBug```: Bug IDs of the bug reports used in our experiments.


**System Corpora & Lucene Indices**

- ```Corpus```: Source code corpus for six subject systems where original file names are replaced with indices.
- ```Lucene-Index```: Lucene index for code search

**BLADER Prototype & External Dependencies**

- ```blader-runner.jar```: Our proposed prototype.
- ```stopword```: Stop word and keyword list.
- ```Candidate```: Candidate source terms for each of the queries. 
- ```Candidate-Base```: Candidate terms from the baseline queries, i.e., bug report texts.
- ```Model```: Machine learning model and resampled training sets.
- ```Model-Reported```: Machine learning model and resampled training sets (as reported in the paper).
- ```Python-Module```: Python scripts for learning and loading the word embeddings using FastText.
- ```Word2Vec-Data```: Cached word embeddings for baseline keywords and candidate terms.

**Installing, Building and Execution**

- ```README```: Prototype overview, artifact details and required commands for the prototype's execution.
- ```INSTALL```: System requirements and installation details

**Licensing & Others**

- ```LICENSE```: Our artifacts are under MIT license
- ```Screenshots```: Screenshots of the available operations.

Available Operations
------------------------------------------------------------

- ```reformulateQuery```: Create reformulated query.
- ```getBLResult```: Collect/evaluate bug localization results of BLADER
- ```getQEPerformance```: Evaluate Query Effectiveness of BLADER
- ```getBaselineBLPerformance```: Evaluate bug localization results of Baseline queries.
- ```getReportedBLPerformance```: Show replicated bug localization performances for the reported queries.
- ```getReportedQEPerformance```: Show replicated Query Effectiveness performances for the reported queries.

**Required parameters for the operations**

- ```task```: expects a task to be performed
- ```queryFileKey```: a random alpha-numeric key to be used for storing queries and results.
- ```topk```: expects the number of top results to be analyzed.
- ```filterKey```: expects a filter key (e.g., TG, HQ) to be applied to the dataset.


Q.1: How to install the BLADER tool?
------------------------------------------------------

- Download all items from GitHub using git clone command, and keep in ```/home``` folder. **The exact URL will be provided later if accepted**.
- Unzip all zip files, and make sure that they are in the home directory. For example, ecf in ```Corpus/class.zip``` should be ```/home/Corpus/class```.
- Download the *FastText* models from [**Google Drive**](https://goo.gl/unZG9K) (Optional). It will be needed if you are testing with the bug reports beyond these six systems.
- Run the tool from within the home directory.


Q.2: How to reformulate the poor queries from the subject systems?
------------------------------------------------------
```
java -jar blader-runner.jar -task reformulateQuery -queryFileKey blader-replication-test
```

Currently, the tool extracts raw bug reports from ```BugReport``` folder using the Bug IDs from ```SelectedBug```, and then reformulates the poor queries.

**Query File format:**

- BugID1	Reformulated-query
- BugID2	Reformulated-query
- BugID3	Reformulated-query

......................................................................................................................

Q.3: How to get Top-K bug localization performances?
----------------------------------------------------------------
```
java -jar blader-runner.jar -task getBLResult -topk 10 -queryFileKey blader-replication-test
```

The above command collects Top-10 results, and calculates **Hit@10, MRR@10, MAP@10** for the queries. 
If you want to extract all the results rather than Top-K only, you can set ```-topk``` to a big number, 100000 to get all the results. 
This provides the ranking of all source code files for each given query.


Q.4: How to determine Query Effectiveness (QE) performances?
-----------------------------------------------------------------
```
java -jar blader-runner.jar -task getQEPerformance -queryFileKey blader-replication-test
```
This shows the statistics on improvement, worsening and preserving of the baseline queries.


Q.5: How to replicate the bug localization performances of Baseline reported in the paper?
--------------------------------------------------------------------------------------------
```
java -jar blader-runner.jar -task getBaselineBLPerformance  -topk 10 
```
This shows the Top-10 performance measures for the baseline

Q.6: How to replicate the bug localization performances of BLADER reported in the paper?
-------------------------------------------------------------------------------------
```
java -jar blader-runner.jar -task getReportedBLPerformance  -topk 10 -queryFileKey BLADER-best
```
**Without the Tangled commits**
```
java -jar blader-runner.jar -task getReportedBLPerformance  -topk 10 -queryFileKey BLADER-best -filterKey TG
```
Results from Table III and V can be replicated using the command above.

Q.7: How to replicate the Query Effectiveness performances of BLADER reported in the paper?
-------------------------------------------------------------------------------------
```
java -jar blader-runner.jar -task getReportedQEPerformance  -queryFileKey BLADER-best
```
**Without the Tangled commits**
```
java -jar blader-runner.jar -task getReportedQEPerformance  -queryFileKey BLADER-best -filterKey TG
```
**With only low quality baseline queries**
```
java -jar blader-runner.jar -task getReportedQEPerformance  -queryFileKey BLADER-best -filterKey HQ
```
This commands shows query improvement, query worsening and query preserving statistics across all 6 subject systems (as shown in Tables IV and VI).


-------------------------------------------------------------------------------------
