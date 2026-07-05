# Register statistics: manuscript vs exemplars

Prose-only lines; inline math -> MATH token; naive sentence splitter with abbreviation guards. Books include example/
exercise text, so treat their rows as indicative.

| corpus | sents | mean w/s | med | sd | >35w | <10w | FK | commas/s | ;/1000w | (/1000w | we/1000w | subord/s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MANUSCRIPT | 623 | 17.1 | 14 | 11.1 | 7% | 28% | 12.4 | 0.87 | 3.2 | 3.3 | 3.7 | 0.39 |
| EXEMPLARS (pooled) | 5363 | 25.1 | 20 | 101.0 | 18% | 22% | 16.2 | 2.10 | 3.1 | 40.4 | 5.1 | 0.57 |

## Per-exemplar

| corpus | sents | mean w/s | med | sd | >35w | <10w | FK | commas/s | ;/1000w | (/1000w | we/1000w | subord/s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rubinInferenceMissingData1976b | 244 | 22.0 | 19 | 15.8 | 17% | 23% | 12.5 | 1.26 | 5.8 | 16.9 | 4.5 | 1.07 |
| rubinMultipleImputationNonresponse1987 | 1122 | 26.1 | 16 | 146.9 | 17% | 31% | 17.8 | 2.80 | 3.1 | 37.2 | 2.3 | 0.41 |
| Meng01121991 | 281 | 25.8 | 24 | 14.1 | 23% | 12% | 14.7 | 1.76 | 2.3 | 20.5 | 10.1 | 0.72 |
| mengPerformingLikelihoodRatio1992b | 130 | 24.0 | 22 | 16.9 | 23% | 23% | 14.6 | 1.75 | 2.2 | 16.0 | 8.0 | 0.48 |
| barnardMiscellaneaSmallsampleDegrees1999 | 98 | 26.4 | 23 | 22.9 | 32% | 30% | 15.2 | 2.12 | 5.4 | 31.3 | 13.1 | 0.64 |
| dempsterMaximumLikelihoodIncomplete1977a | 500 | 20.4 | 19 | 14.0 | 13% | 25% | 12.6 | 1.11 | 0.8 | 19.1 | 12.6 | 0.53 |
| littleStatisticalAnalysisMissing2019 | 1071 | 33.1 | 24 | 166.2 | 22% | 9% | 21.0 | 3.39 | 2.9 | 80.3 | 2.6 | 0.70 |
| mengMultipleImputationInferencesUncongenial1994a | 665 | 21.6 | 20 | 15.2 | 16% | 28% | 14.8 | 1.56 | 3.1 | 23.4 | 1.3 | 0.54 |
| kenwardLikelihoodBasedFrequentist1998 | 322 | 19.8 | 18 | 13.9 | 9% | 26% | 12.8 | 0.99 | 2.7 | 19.5 | 9.6 | 0.50 |
| coxGeneralDefinitionResiduals1968 | 466 | 23.6 | 22 | 15.6 | 19% | 20% | 13.5 | 1.21 | 4.6 | 18.5 | 10.3 | 0.63 |
| firthBiasReductionMaximum1993 | 225 | 17.4 | 16 | 13.0 | 10% | 35% | 11.2 | 1.22 | 4.9 | 12.5 | 2.3 | 0.43 |
| efronBootstrapMethodsAnother1979 | 239 | 25.0 | 22 | 18.7 | 19% | 13% | 14.6 | 2.08 | 2.0 | 40.3 | 7.9 | 0.45 |

## Sentence-opener profile (% of sentences)

| corpus | The | This | That | It | We | A | In | For |
|---|---|---|---|---|---|---|---|---|
| MANUSCRIPT | 37.2 | 5.9 | 2.9 | 1.1 | 2.1 | 2.4 | 1.8 | 1.8 |
| EXEMPLARS (pooled) | 14.4 | 3.1 | 0.4 | 1.8 | 2.6 | 2.7 | 6.5 | 3.2 |