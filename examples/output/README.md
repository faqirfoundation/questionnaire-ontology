## Answer-EQ_5D_5L_EQ_VAS-a01
### Input
```yaml
answerId: https://pods.faqir.org/questionnaire/answer_EQ_5D_5L_EQ_VAS_a01
answerInQuestionnaireResponse: https://pods.faqir.org/questionnaire/response_EQ_5D_5L_01
answerIsEmpty: false
answerTimeStamp: '2025-07-11T10:35:11Z'
answerToQuestion: https://pods.faqir.org/questionnaire/question_EQ_5D_5L_EQ_VAS
answerValueNumerical:
  numericalValue: 83
questionType: numberInterval

```
## Question-EQ_5D_5L_02
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionCodingParams:
- code: '1'
  display: I have no problems washing or dressing myself
- code: '2'
  display: I have slight problems washing or dressing myself
- code: '3'
  display: I have moderate problems washing or dressing myself
- code: '4'
  display: I have severe problems washing or dressing myself
- code: '5'
  display: I am unable to wash or dress myself
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_02_a01
- https://pods.faqir.org/answer_06_EQ_5D_5L_02_01
- https://pods.faqir.org/answer_06_EQ_5D_5L_02_02
- https://pods.faqir.org/answer_06_EQ_5D_5L_02_03
questionId: https://pods.faqir.org/question_EQ_5D_5L_02
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_02
- https://pods.faqir.org/orderedquestion_06_EQ_5D_5L_02_s01
- https://pods.faqir.org/orderedquestion_06_EQ_5D_5L_02_s02
questionLabel: SELF-CARE. Please tick the ONE box that best describes your health
  TODAY.
questionRequired: false
questionTag: q_EQ_5D_5L_02
questionType: choice

```
## Answer-EQ_5D_5L_03-a01
### Input
```yaml
answerId: https://pods.faqir.org/answer_EQ_5D_5L_03_a01
answerInQuestionnaireResponse: https://pods.faqir.org/response_EQ_5D_5L_01
answerIsEmpty: false
answerTimeStamp: '2025-07-11T10:35:05Z'
answerToQuestion: https://pods.faqir.org/question_EQ_5D_5L_03
answerValueString:
- stringValue: '3'
questionType: choice

```
## Answer-EQ_5D_5L_02-a01
### Input
```yaml
answerId: https://pods.faqir.org/answer_EQ_5D_5L_02_a01
answerInQuestionnaireResponse: https://pods.faqir.org/response_EQ_5D_5L_01
answerIsEmpty: true
answerTimeStamp: '2025-07-11T10:35:08Z'
answerToQuestion: https://pods.faqir.org/question_EQ_5D_5L_02
answerValueString: []
questionType: choice

```
## ScoreValue-EQ_5D_5L_EQ_VAS_01
### Input
```yaml
scoreDefinitionType: numerical_integer
scoreValueBasedOnScoreDefinition: https://pods.faqir.org/sdEQ_5D_5L
scoreValueDerivedFromQuestionnaireResponse:
- https://pods.faqir.org/response_EQ_5D_5L_01
scoreValueId: https://pods.faqir.org/svEQ_5D_5L_01
scoreValueNumerical:
  numericalValue: 12345
scoreValueStatus: valid
scoreValueTimeStamp: '2025-07-11T10:55:00Z'

```
## Question-EQ_5D_5L_03
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionCodingParams:
- code: '1'
  display: I have no problems doing my usual activities
- code: '2'
  display: I have slight problems doing my usual activities
- code: '3'
  display: I have moderate problems doing my usual activities
- code: '4'
  display: I have severe problems doing my usual activities
- code: '5'
  display: I am unable to do my usual activities
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_03_a01
questionId: https://pods.faqir.org/question_EQ_5D_5L_03
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_03
questionLabel: USUAL ACTIVITIES (e.g. work, study, housework, family or leisure activities).
  Please tick the ONE box that best describes your health TODAY.
questionRequired: false
questionTag: q_EQ_5D_5L_03
questionType: choice

```
## QuestionnaireResponse-EQ_5D_5L-01
### Input
```yaml
questionnaireResponseBySubject: https://pods.faqir.org/123
questionnaireResponseHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_01_a01
- https://pods.faqir.org/answer_EQ_5D_5L_02_a01
- https://pods.faqir.org/answer_EQ_5D_5L_03_a01
- https://pods.faqir.org/answer_EQ_5D_5L_04_a01
- https://pods.faqir.org/answer_EQ_5D_5L_05_a01
- https://pods.faqir.org/answer_EQ_5D_5L_EQ_VAS_a01
questionnaireResponseId: https://pods.faqir.org/response_EQ_5D_5L_01
questionnaireResponseLastUpdated: '2025-07-11T10:35:00Z'
questionnaireResponseStatus: completed
questionnaireResponseTimeStamp: '2025-07-11T10:35:00Z'
questionnaireResponseToQuestionnaire: https://pods.faqir.org/questionnaire_EQ_5D_5L

```
## ScoreValue-EQ_5D_5L_01
### Input
```yaml
scoreDefinitionType: numerical_integer
scoreValueBasedOnScoreDefinition: https://pods.faqir.org/sdEQ_5D_5L_EQ_VAS
scoreValueDerivedFromQuestionnaireResponse:
- https://pods.faqir.org/response_EQ_5D_5L_01
scoreValueId: https://pods.faqir.org/sdEQ_5D_5L_EQ_VAS_01
scoreValueNumerical:
  numericalValue: 77
scoreValueStatus: valid
scoreValueTimeStamp: '2025-07-11T10:55:00Z'

```
## Question-EQ_5D_5L_04
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionCodingParams:
- code: '1'
  display: I have no pain or discomfort
- code: '2'
  display: I have slight pain or discomfort
- code: '3'
  display: I have moderate pain or discomfort
- code: '4'
  display: I have severe pain or discomfort
- code: '5'
  display: I have extreme pain or discomfort
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_04_a01
questionId: https://pods.faqir.org/question_EQ_5D_5L_04
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_04
questionLabel: PAIN / DISCOMFORT. Please tick the ONE box that best describes your
  health TODAY.
questionRequired: false
questionTag: q_EQ_5D_5L_04
questionType: choice

```
## Questionnaire-EQ-5D-5L
### Input
```yaml
questionnaireHasOrderedQuestion:
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_01
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_01
  questionOrder: 1
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_02
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_02
  questionOrder: 2
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_03
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_03
  questionOrder: 3
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_04
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_04
  questionOrder: 4
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_05
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_05
  questionOrder: 5
- orderedQuestionHasQuestion: https://pods.faqir.org/question_EQ_5D_5L_EQ_VAS
  orderedQuestionId: https://pods.faqir.org/orderedquestion_EQ_5D_5L_EQ_VAS
  questionOrder: 6
questionnaireHasQuestionnaireResponse:
- https://pods.faqir.org/response_EQ_5D_5L_01
questionnaireId: https://pods.faqir.org/questionnaire_EQ_5D_5L
questionnaireLabel: EQ-5D-5L
questionnaireLastUpdated: '2025-09-09T11:52:00Z'
questionnaireStatus: active
questionnaireUsesScoreDefinition:
- https://pods.faqir.org/sdEQ_5D_5L
- https://pods.faqir.org/sdEQ_5D_5L_EQ_VAS
questionnaireVersion: 1.0.0

```
## Answer-EQ_5D_5L_04-a01
### Input
```yaml
answerId: https://pods.faqir.org/answer_EQ_5D_5L_04_a01
answerInQuestionnaireResponse: https://pods.faqir.org/response_EQ_5D_5L_01
answerIsEmpty: false
answerTimeStamp: '2025-07-11T10:35:05Z'
answerToQuestion: https://pods.faqir.org/question_EQ_5D_5L_04
answerValueString:
- stringValue: '2'
questionType: choice

```
## Answer-EQ_5D_5L_05-a01
### Input
```yaml
answerId: https://pods.faqir.org/answer_EQ_5D_5L_05_a01
answerInQuestionnaireResponse: https://pods.faqir.org/response_EQ_5D_5L_01
answerIsEmpty: false
answerTimeStamp: '2025-07-11T10:35:05Z'
answerToQuestion: https://pods.faqir.org/question_EQ_5D_5L_05
answerValueString:
- stringValue: '1'
questionType: choice

```
## Question-EQ_5D_5L_05
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionCodingParams:
- code: '1'
  display: I am not anxious or depressed
- code: '2'
  display: I am slightly anxious or depressed
- code: '3'
  display: I am moderately anxious or depressed
- code: '4'
  display: I am severely anxious or depressed
- code: '5'
  display: I am extremely anxious or depressed
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_05_a01
questionId: https://pods.faqir.org/question_EQ_5D_5L_05
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_05
questionLabel: ANXIETY / DEPRESSION. Please tick the ONE box that best describes your
  health TODAY.
questionRequired: false
questionTag: q_EQ_5D_5L_05
questionType: choice

```
## ScoreDefinition-EQ_5D_5L_EQ_VAS
### Input
```yaml
scoreDefinitionAuthoredByOrg:
- https://euroqol.org/
scoreDefinitionFormula: 'Simply the numerical answer of the EQ-VAS question.

  - Missing values are preferably coded as 999.

  '
scoreDefinitionHasScoreValue:
- https://pods.faqir.org/svEQ_5D_5L_EQ_VAS_01
scoreDefinitionId: https://pods.faqir.org/sdEQ_5D_5L_EQ_VAS
scoreDefinitionInterpretationGuide: 'User''s own perceived health on the day of the
  questionnaire completion.

  This scale is numbered from 0 to 100.

  100 means the *best* health you can imagine.

  0 means the *worst* health you can imagine.

  If there is a discrepancy between where the respondent has placed the X and the
  number

  he/she has written in the box, administrators should use the number in the box (this
  is

  only relevant for the Paper Self-Complete version).

  '
scoreDefinitionIntervalParams:
  maxValue: 999
  minValue: 0
scoreDefinitionLabel: EQ-5D-5L EQ-VAS score
scoreDefinitionType: numerical_integer
scoreDefinitionUsedByQuestionnare:
- https://pods.faqir.org/questionnaire_EQ_5D_5L
scoreDefinitionUsesQuestion:
- https://pods.faqir.org/q_EQ_5D_5L_EQ_VAS

```
## Answer-EQ_5D_5L_01-a01
### Input
```yaml
answerId: https://pods.faqir.org/answer_EQ_5D_5L_01_a01
answerInQuestionnaireResponse: https://pods.faqir.org/c
answerIsEmpty: false
answerTimeStamp: '2025-07-11T10:35:05Z'
answerToQuestion: https://pods.faqir.org/question_EQ_5D_5L_01
answerValueString:
- stringValue: '1'
questionType: choice

```
## ScoreDefinition-EQ_5D_5L
### Input
```yaml
scoreDefinitionAuthoredByOrg:
- https://euroqol.org/
scoreDefinitionFormula: "Each state is referred to by a 5-digit code: each digit representing\
  \ the answer to each question or dimension (e.g. 12345).\nThe first digit represents\
  \ the level selected for mobility, the second for self-care, the third for usual\
  \ activities, the fourth for pain/discomfort and the fifth for anxiety/depression.\n\
  - Missing values are preferably coded as \u20189\u2019.\n- Ambiguous values (e.g.\
  \ two boxes are ticked for a single dimension) should\nbe treated as missing values.\n"
scoreDefinitionHasScoreValue:
- https://pods.faqir.org/svEQ_5D_5L_01
scoreDefinitionId: https://pods.faqir.org/sdEQ_5D_5L
scoreDefinitionInterpretationGuide: "A total of 3125 possible health states are defined\
  \ in this way. \nLEVEL 1: indicating no problem\nLEVEL 2: indicating slight problems\n\
  LEVEL 3: indicating moderate problems\nLEVEL 4: indicating severe problems\nLEVEL\
  \ 5: indicating unable to/extreme problems\n"
scoreDefinitionIntervalParams:
  maxValue: 99999
  minValue: 11111
scoreDefinitionLabel: EQ-5D-5L score
scoreDefinitionType: numerical_integer
scoreDefinitionUsedByQuestionnare:
- https://pods.faqir.org/questionnaire_EQ_5D_5L
scoreDefinitionUsesQuestion:
- https://pods.faqir.org/question_EQ_5D_5L_01
- https://pods.faqir.org/question_EQ_5D_5L_02
- https://pods.faqir.org/question_EQ_5D_5L_03
- https://pods.faqir.org/question_EQ_5D_5L_04
- https://pods.faqir.org/question_EQ_5D_5L_05

```
## Question-EQ_5D_5L_VAS
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_EQ_VAS_a01
questionId: https://pods.faqir.org/question_EQ_5D_5L_EQ_VAS
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_EQ_VAS
questionIntervalParams:
  maxLabel: The best health you can imagine
  maxValue: 100
  minLabel: The worst health you can imagine
  minValue: 0
questionLabel: '"We would like to know how good or bad your health is TODAY.

  This scale is numbered from 0 to 100.

  100 means the *best* health you can imagine.

  0 means the *worst* health you can imagine.

  Mark an X on the scale to indicate how your health is TODAY.

  Now, please write the number you marked on the scale."

  '
questionNumericalParams:
  numericalPrecision: 0
questionRequired: false
questionTag: q_EQ_5D_5L_EQ_VAS
questionType: numberInterval

```
## Question-EQ_5D_5L_01
### Input
```yaml
questionAuthoredByOrg:
- https://euroqol.org/
questionCodingParams:
- code: '1'
  display: I have no problems in walking about
- code: '2'
  display: I have slight problems in walking about
- code: '3'
  display: I have moderate problems in walking about
- code: '4'
  display: I have severe problems in walking about
- code: '5'
  display: I am unable to walking about
questionHasAnswer:
- https://pods.faqir.org/answer_EQ_5D_5L_01_a01
- https://pods.faqir.org/answer_05_EQ_5D_5L_01_01
- https://pods.faqir.org/answer_05_EQ_5D_5L_01_02
- https://pods.faqir.org/answer_05_EQ_5D_5L_01_03
questionId: https://pods.faqir.org/question_EQ_5D_5L_01
questionInOrderedQuestion:
- https://pods.faqir.org/orderedquestion_EQ_5D_5L_01
- https://pods.faqir.org/orderedquestion_05_EQ_5D_5L_01_s01
- https://pods.faqir.org/orderedquestion_05_EQ_5D_5L_01_s02
- https://pods.faqir.org/orderedquestion_06_EQ_5D_5L_01_q01
questionLabel: MOBILITY. Please tick the ONE box that best describes your health TODAY.
questionRequired: false
questionTag: q_EQ_5D_5L_01
questionType: choice

```
## ScoreDefinition-01
### Input
```yaml
scoreDefinitionAuthoredByOrg:
- https://www.moveup.care/
scoreDefinitionFormula: Unknown
scoreDefinitionHasScoreValue:
- https://pods.faqir.org/svTFJSK
scoreDefinitionId: https://pods.faqir.org/TFJSK
scoreDefinitionIntervalParams:
- maxValue: 100
  minValue: 0
scoreDefinitionLabel: "Total Forgotten Joint Score Knee (/100) (een hoge score geeft\
  \ een hogere mate van \u201Cvergeten\u201D weer, dat wil zeggen een lager bewustzijn\
  \ van het kunstgewricht) score"
scoreDefinitionType: numerical_integer
scoreDefinitionUsedBySection:
- https://pods.faqir.org/7eTPK5NLGTv8jeTW5
scoreDefinitionUsesQuestion: https://pods.faqir.org/FoIn0

```
