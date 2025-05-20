## Example 1: Deriving Z from A, B, C, D, E

**Facts:** A, B, C, D, E  
**Rules:**

1. IF A ∧ C ⇒ B
    
2. IF C ∧ D ⇒ F
    
3. IF C ∧ D ∧ E ⇒ X
    
4. IF A ∧ B ∧ X ⇒ Y
    
5. IF D ∧ Y ⇒ Z
    

### Forward Chaining

|Cycle|Working Memory|Applicable Rules|Fired Rule|New Fact|
|:-:|:--|:--|:--|:--|
|1|A, B, C, D, E|1, 2, 3|1|— (B exists)|
|2|A, B, C, D, E|2, 3|2|F|
|3|A, B, C, D, E, F|3|3|X|
|4|A, B, C, D, E, F, X|4|4|Y|
|5|A, B, C, D, E, F, X, Y|5|5|Z|

**Conclusion:** Z is derived in Cycle 5.

### Backward Chaining

1. **Goal:** Z
    
    - Rule 5 ⇒ sub‐goals: D (✓), Y (unknown)
        
2. **Sub‐goal:** Y
    
    - Rule 4 ⇒ sub‐goals: A (✓), B (✓), X (unknown)
        
3. **Sub‐goal:** X
    
    - Rule 3 ⇒ sub‐goals: C (✓), D (✓), E (✓) ⇒ X proven
        
4. **Roll up:** Y proven (via Rule 4)
    
5. **Finally:** Z proven (via Rule 5)
    

---

## Example 2: Proving Z via Intermediate Y and X

**Facts:** A, B, C, D, E  
**Rules:**

1. IF Y ∧ D ⇒ Z
    
2. IF X ∧ B ∧ E ⇒ Y
    
3. IF A ⇒ X
    
4. IF C ⇒ L
    
5. IF L ∧ M ⇒ N
    

### Forward Chaining

|Cycle|Working Memory|Applicable Rules|Fired Rule|New Fact|
|:-:|:--|:--|:--|:--|
|1|A, B, C, D, E|3, 4|3|X|
|2|A, B, C, D, E, X|4, 2|4|L|
|3|A, B, C, D, E, X, L|2|2|Y|
|4|A, B, C, D, E, X, L, Y|1|1|Z|

**Conclusion:** Z is derived in Cycle 4.

### Backward Chaining

1. **Goal:** Z
    
    - Rule 1 ⇒ sub‐goals: Y (unknown), D (✓)
        
2. **Sub‐goal:** Y
    
    - Rule 2 ⇒ sub‐goals: X (unknown), B (✓), E (✓)
        
3. **Sub‐goal:** X
    
    - Rule 3 ⇒ sub‐goal: A (✓) ⇒ X proven
        
4. **Roll up:** Y proven (via Rule 2)
    
5. **Finally:** Z proven (via Rule 1)
    

---

## Example 3: Triggering an Alarm

**Facts:** MotionDetected, TimeNight, DoorOpen, WindowClosed, TemperatureHigh, SmokeDetected  
**Rules:**

1. IF MotionDetected ∧ TimeNight ⇒ IntruderAlert
    
2. IF DoorOpen ∧ WindowClosed ⇒ ForcedEntry
    
3. IF IntruderAlert ∧ ForcedEntry ⇒ AlarmSound
    
4. IF TemperatureHigh ∧ WindowClosed ⇒ FireRisk
    
5. IF FireRisk ∧ SmokeDetected ⇒ AlarmSound
    

### Forward Chaining

|Cycle|Working Memory|Applicable Rules|Fired Rule|New Fact|
|:-:|:--|:--|:--|:--|
|1|MotionDetected, TimeNight, DoorOpen, WindowClosed, TemperatureHigh, SmokeDetected|1, 2, 4|1|IntruderAlert|
|2|..., IntruderAlert|2, 4|2|ForcedEntry|
|3|..., IntruderAlert, ForcedEntry|4|4|FireRisk|
|4|..., FireRisk|3, 5|3|AlarmSound|

_Stop: AlarmSound derived in Cycle 4._

### Backward Chaining

1. **Goal:** AlarmSound
    
    - Rule 3 ⇒ sub‐goals: IntruderAlert (unknown), ForcedEntry (unknown)
        
2. **Sub‐goal:** IntruderAlert
    
    - Rule 1 ⇒ sub‐goals: MotionDetected (✓), TimeNight (✓) ⇒ IntruderAlert proven
        
3. **Sub‐goal:** ForcedEntry
    
    - Rule 2 ⇒ sub‐goals: DoorOpen (✓), WindowClosed (✓) ⇒ ForcedEntry proven
        
4. **Roll up:** AlarmSound proven via Rule 3
    

---

## Example 4: Loan Disbursement

**Facts:** CreditScoreHigh, IncomeAbove50k, CollateralProvided, DebtRatioLow, DocumentationComplete  
**Rules:**

1. IF CreditScoreHigh ∧ IncomeAbove50k ⇒ Prequalified
    
2. IF Prequalified ∧ CollateralProvided ⇒ LoanApproved
    
3. IF DebtRatioLow ∧ IncomeAbove50k ⇒ Prequalified
    
4. IF LoanApproved ∧ DocumentationComplete ⇒ LoanDisbursed
    
5. IF LoanApproved ∧ HighRisk ⇒ ManualReview
    

### Forward Chaining

|Cycle|Working Memory|Applicable Rules|Fired Rule|New Fact|
|:-:|:--|:--|:--|:--|
|1|CreditScoreHigh, IncomeAbove50k, CollateralProvided, DebtRatioLow, DocumentationComplete|1, 3|1|Prequalified|
|2|..., Prequalified|2|2|LoanApproved|
|3|..., LoanApproved|4, 5|4|LoanDisbursed|

_Stop: LoanDisbursed derived in Cycle 3._

### Backward Chaining

1. **Goal:** LoanDisbursed
    
    - Rule 4 ⇒ sub‐goals: LoanApproved (unknown), DocumentationComplete (✓)
        
2. **Sub‐goal:** LoanApproved
    
    - Rule 2 ⇒ sub‐goals: Prequalified (unknown), CollateralProvided (✓)
        
3. **Sub‐goal:** Prequalified
    
    - Rule 1 ⇒ sub‐goals: CreditScoreHigh (✓), IncomeAbove50k (✓) ⇒ Prequalified proven
        
4. **Roll up:** LoanApproved proven ⇒ LoanDisbursed proven