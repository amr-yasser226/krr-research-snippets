## **1. Forward Chaining**  
### **Definition**  
- **Data-driven approach**: Starts with known facts, applies rules to derive new facts until the goal is reached.  
- **Use cases**: Planning, monitoring systems, scenarios with abundant data.  

---

### **Process**  
1. **Match**: Compare IF parts of rules to working memory.  
2. **Conflict Resolution**: Select one rule if multiple match (strategies: rule order, specificity, recency).  
3. **Execute**: Fire the rule, add new facts.  
4. **Repeat** until goal is achieved or no rules apply.  

---

### **Example 1: Proving Z (Rules 1-5)**  
**Initial Facts**: `A, B, C, D, E`  
**Goal**: `Z`  

| Cycle | Working Memory          | Conflict Set | Rule Fired | New Fact |  
|-------|--------------------------|--------------|------------|----------|  
| 1     | `A, B, C, D, E`          | Rules 1,2,3  | Rule 1     | (B exists → no change) |  
| 2     | `A, B, C, D, E`          | Rules 2,3    | Rule 2     | F        |  
| 3     | `A, B, C, D, E, F`       | Rule 3       | Rule 3     | X        |  
| 4     | `A, B, C, D, E, F, X`    | Rule 4       | Rule 4     | Y        |  
| 5     | `A, B, C, D, E, F, X, Y` | Rule 5       | Rule 5     | Z        |  

**Conflict Resolution**: Rule order (Rule 1 first).  

---

### **Example 2: Weather Forecasting (Forward)**  
**Initial Fact**: `arrow is down`  
**Goal**: Predict weather changes.  

| Cycle | Working Memory                          | Rule Fired | New Fact           |  
|-------|-----------------------------------------|------------|--------------------|  
| 0     | `arrow is down`                         | Rule 5     | `pressure is low`  |  
| 1     | `arrow is down, pressure is low`        | Rule 3     | `cyclone`          |  
| 2     | `arrow is down, pressure is low, cyclone` | Rule 1     | `clouds`           |  

**Rules Used**:  
- `Rule 5: arrow is down → pressure is low`  
- `Rule 3: pressure is low → cyclone`  
- `Rule 1: cyclone → clouds`  

---

## **2. Backward Chaining**  
### **Definition**  
- **Goal-driven approach**: Starts with a hypothesis, works backward to prove it using rules/facts.  
- **Use cases**: Diagnosis, troubleshooting, scenarios with limited data.  

---

### **Process**  
1. **Select Rules** with conclusions matching the goal.  
2. **Replace Goal** with the rule’s premises (sub-goals).  
3. **Repeat** until all sub-goals are facts or user-provided.  

---

### **Example 1: Proving Z (Backward)**  
**Goal**: `Z`  
**Steps**:  
1. **Rule 5** (`D & Y → Z`):  
   - Sub-goals: `D` (exists), `Y` (needs proof).  
2. **Rule 4** (`A & B & X → Y`):  
   - Sub-goals: `A` (exists), `B` (exists), `X` (needs proof).  
3. **Rule 3** (`C & D & E → X`):  
   - Sub-goals: `C`, `D`, `E` (all exist).  
4. **Add**: `X → Y → Z` to working memory.  

**Final Working Memory**: `A, B, C, D, E, X, Y, Z`.  

---

### **Example 2: Weather Forecasting (Backward)**  
**Goal**: Prove `clouds` exists.  

| Cycle | Goal            | Rule Used           | Sub-Goals               |  
|-------|-----------------|---------------------|-------------------------|  
| 1     | `clouds`        | Rule 1 (`cyclone`)  | Prove `cyclone`         |  
| 2     | `cyclone`       | Rule 3 (`pressure is low`) | Prove `pressure is low` |  
| 3     | `pressure is low` | Rule 5 (`arrow is down`) | Fact `arrow is down` exists. |  

**Rules Used**:  
- `Rule 1: cyclone → clouds`  
- `Rule 3: pressure is low → cyclone`  
- `Rule 5: arrow is down → pressure is low`  

---

## **3. Key Differences**  
| **Forward Chaining**         | **Backward Chaining**         |  
|-------------------------------|--------------------------------|  
| Data-driven (bottom-up)       | Goal-driven (top-down)         |  
| Generates all possible facts   | Focuses only on goal path      |  
| Example: Weather prediction    | Example: Medical diagnosis     |  

---

## **4. Conflict Resolution Strategies**  
- **Rule Order**: Fire the first applicable rule (e.g., Rule 1 before Rule 3).  
- **Specificity**: Prefer rules with more premises (e.g., `C & D & E → X` over `C & E → F`).  
- **Recency**: Use recently added facts.  

---

## **5. When to Use Which?**  
- **Forward Chaining**:  
  - Most data is available.  
  - Example: Monitoring sensor data in real-time.  
- **Backward Chaining**:  
  - Goal is clear, but data is limited.  
  - Example: Diagnosing a disease from symptoms.  

---

## **6. Summary**  
- **Forward Chaining**:  
  ```  
  Facts → Apply Rules → New Facts → ... → Goal  
  ```  
- **Backward Chaining**:  
  ```  
  Goal ← Sub-Goals ← Rules ← ... ← Facts  
  ```  

---

**Additional Notes**:  
- Discrepancies in rule firing order arise from **conflict resolution strategies**.  
- In backward chaining, missing sub-goals may require user input (e.g., "Is M true?").  
---