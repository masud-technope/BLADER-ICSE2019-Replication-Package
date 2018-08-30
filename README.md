
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
