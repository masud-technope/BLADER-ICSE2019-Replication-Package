
# Improving IR-Based Bug Localization with Effective Reformulation of Query using Crowdsourced Data Analytics


Abstract
------------------------------------------------------
```
Recent findings suggest that IR-based bug localization techniques do not perform well with low quality bug reports. Low quality bug reports do not contain any program entity names that could help find the encountered bugs or defects in the source code of a software system.
Only a few studies attempt to address this issue using query reformulation. Unfortunately, they might fail for low quality bug reports (the poor queries) due to their high reliance on the report texts.
In this paper, we propose a novel technique--BLADER--that localizes buggy entities from a software project using appropriate query reformulation and effective information retrieval. 
First, we build a multi-dimensional semantic space with a vocabulary of about 660K words extracted from Stack Overflow using a popular unsupervised machine learning algorithm (e.g., FastText). 
Second, we improve a poor query by choosing appropriate keywords from the source code that have high clustering tendency with this query within the semantic space above.
Third, we then use the improved query for bug localization with Information Retrieval. 
Experiments with 1,546 queries from six subject systems report that our approach can localize bugs with 17% higher MAP@10 and 21% higher MRR@10 than the baseline. 
Comparisons with ten existing approaches including the state-of-the-art show that our technique achieves 11% higher MAP@10, 15% higher MRR@10, and improves 23% more of the baseline queries.
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

- Baseline/query: Baseline queries
- Baseline/rank: Query Effectiveness of baseline queries.


**BLADER: The proposed technique**

- BLADER/query: Reformulated queries by our technique. The tool will store queries in this folder.
- BLADER/rank: Query Effectiveness of our queries. The tool will store the QE of the queries in this folder.
- BLADER-Reported/query: Reformulated queries by our technique (reported in the paper)
- BLADER-Reported/rank: Query Effectiveness of our queries (reported in the paper)


**Bug Report & Goldsets**

- BugReport: Raw content from 1,546 bug reports from six systems
- Goldset: Change set for 1,546 reported bugs
- SelectedBug: Bug IDs of the bug reports under experiment.


**System Corpora & Lucene Indices**

- Corpus: Source code corpus for six subject systems where original file names are replaced with indices.
- Lucene-Index: Lucene index for code search


**BLADER Prototype & External Dependencies**

- blader-runner.jar: Our proposed tool.
- stopword: The folder contains stop word and keyword list.
- Candidate: The folder contains the candidate source terms for each of the queries. 
- Candidate-Base: The candidate terms from the baseline queries, i.e., bug report texts.
- Model: The machine learning model and resampled training sets.
- Model-Reported: The machine learning model and resampled training sets (reported in the paper).
- Python-Module: Python scripts for learning and loading the word embeddings.
- Word2Vec-Data: Cached word embeddings for the bug reports and candidate terms.


**Installing, Building and Execution**

README: Prototype overview, artifact details and required commands for the tool's execution.
INSTALL: System requirements and installation details


**Licensing & Others**

LICENSE: Our artifacts are under MIT license
Screenshots: It contains the screenshots of the available operations.


Available Operations
------------------------------------------------------------

- reformulateQuery: Create reformulated query.
- getBLResult: Collect/evaluate bug localization results of BLADER
- getQEPerformance: Evaluate query effectiveness of BLADER
- getBaselineBLPerformance: Evaluate bug localization results of Baseline queries.
- getReportedBLPerformance: Show replicated bug localization performances for the reported queries.
- getReportedQEPerformance: Show replicated query effectiveness performances for the reported queries.

**Required parameters for the operations**

-task : expects a task to be performed
-queryFileKey: a random alpha-numeric key to be used for storing queries and results.
-topk : expects the number of results to be analyzed.


Q.1: How to install the BLADER tool?
------------------------------------------------------

- Download all items from GitHub using git clone command, and keep in /home folder. *The exact URL will be provided later*.
- Unzip all zip files, and make sure that they are in the home directory. For example, ecf in Corpus/class.zip should be /home/Corpus/class
- Download the FastText models from Google Drive (Optional)
- Run the tool from within the home directory.


Q.2: How to reformulate the poor queries from the subject systems?
------------------------------------------------------

java -jar blader-runner.jar -task reformulateQuery -queryFileKey blader-replication-test

Currently, the tool extracts raw bug reports from "BugReport" folder using the Bug IDs from "SelectedBug", and then reformulates the reports.

**Query File format:**

BugID1	Reformulated-query

BugID2	Reformulated-query

BugID3	Reformulated-query

..........................................................

Q.3: How to collect Top-K bug localization results?
----------------------------------------------------------------

java -jar blader-runner.jar -task getBLResult -topk 10 -queryFileKey blader-replication-test

The above command collects Top-10 results and reports Hit@10, MRR@10, MAP@10 for the queries. *Results from Table III and IV can be found using the command above.*
If you want to extract all the results rather than Top-K only, you can set -topk to a big number, 100000 to get all the results. This provides the ranking of all source code files for each given query.


Q.4: How to determine Query Effectiveness (QE) performances?
-----------------------------------------------------------------

java -jar blader-runner.jar -task getQEPerformance -queryFileKey blader-replication-test


Q.5: How to replicate the bug localization performances reported in the paper?
-------------------------------------------------------------------------------------

java -jar blader-runner.jar -task getReportedBLPerformance  -topk 10 -reportKey ST

This command shows Hit@10, MRR@10, MAP@10 for all 6 subject systems, and their mean measures (as shown in Table 5)


Q.6: How to replicate the Query Effectiveness performances reported in the paper?
-------------------------------------------------------------------------------------
java -jar blader-runner.jar -task getReportedQEPerformance  -reportKey ST
This commands shows query improvement, query worsening and query preserving statistics across all 6 subject systems (as shown in Table 9).
