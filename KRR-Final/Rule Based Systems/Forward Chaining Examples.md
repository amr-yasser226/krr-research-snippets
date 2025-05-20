## Example 1: Power Out Scenario

**Knowledge Base:**

1. **Rule 1:** If the power is out, then the lights are off.
    
2. **Rule 2:** If the lights are off, then the room is dark.
    
3. **Rule 3:** If the room is dark, then turn on the flashlight.
    
4. **Rule 4:** If the flashlight’s battery is dead, then replace the battery.
    

**Initial Facts:**

- The power is out.
    
- The flashlight’s battery is dead.
    

---

### Step-by-Step Forward Chaining

1. **Initialize Facts**
    
    - Facts: { power is out; flashlight’s battery is dead }
        
2. **Apply Rule 1** (power is out → lights are off)
    
    - Premise met: “power is out”
        
    - **Infer:** “lights are off”
        
    - Facts now: { power is out; flashlight’s battery is dead; lights are off }
        
3. **Apply Rule 2** (lights are off → room is dark)
    
    - Premise met: “lights are off”
        
    - **Infer:** “room is dark”
        
    - Facts now: { power is out; flashlight’s battery is dead; lights are off; room is dark }
        
4. **Apply Rule 3** (room is dark → turn on the flashlight)
    
    - Premise met: “room is dark”
        
    - **Infer:** “turn on the flashlight”
        
    - Facts now: { power is out; flashlight’s battery is dead; lights are off; room is dark; turn on the flashlight }
        
5. **Apply Rule 4** (flashlight’s battery is dead → replace the battery)
    
    - Premise met: “flashlight’s battery is dead”
        
    - **Infer:** “replace the battery”
        
    - Facts now: { power is out; flashlight’s battery is dead; lights are off; room is dark; turn on the flashlight; replace the battery }
        
6. **Termination**
    
    - No further rules apply.
        

**Final Conclusions:**

- The power is out.
    
- The flashlight’s battery is dead.
    
- The lights are off.
    
- The room is dark.
    
- Turn on the flashlight.
    
- Replace the battery.
    

---

## Example 2: Doorbell Scenario

**Knowledge Base:**

1. **Rule 1:** If the doorbell rings, then someone is at the door.
    
2. **Rule 2:** If someone is at the door **and** I’m not wearing shoes, then put on shoes.
    
3. **Rule 3:** If someone is at the door **and** I’m wearing shoes, then open the door.
    
4. **Rule 4:** If I open the door **and** there is a package, then sign for the package.
    

**Initial Facts:**

- The doorbell rings.
    
- I’m not wearing shoes.
    
- There is a package.
    

---

### Step-by-Step Forward Chaining

1. **Initialize Facts**
    
    - Facts: { doorbell rings; not wearing shoes; package present }
        
2. **Apply Rule 1** (doorbell rings → someone is at the door)
    
    - Premise met: “doorbell rings”
        
    - **Infer:** “someone is at the door”
        
    - Facts now: { doorbell rings; not wearing shoes; package present; someone is at the door }
        
3. **Apply Rule 2** (someone is at the door **and** not wearing shoes → put on shoes)
    
    - Premises met: “someone is at the door” **and** “not wearing shoes”
        
    - **Infer:** “put on shoes”
        
    - Facts now: { doorbell rings; not wearing shoes; package present; someone is at the door; put on shoes }
        
4. **Apply Rule 3** (someone is at the door **and** wearing shoes → open the door)
    
    - “Wearing shoes” is not (yet) in facts, so this rule does **not** apply under positive‐only chaining.
        
5. **Apply Rule 4** (open the door **and** package present → sign for the package)
    
    - “Open the door” is not in facts, so this rule does **not** apply.
        
6. **Termination**
    
    - No further positive inferences are possible.
        

**Final Conclusions (strict chaining):**

- The doorbell rings.
    
- I’m not wearing shoes.
    
- There is a package.
    
- Someone is at the door.
    
- Put on shoes.
    

---

## Example 3: Employee Salary Determination 

**Problem Definition:** A company determines final salary by three sequential rule sets:

1. **Years of Experience** ⇒ base salary
    
2. **Education Level** ⇒ add-on
    
3. **Performance Bonus** ⇒ add-on
    

**Employee Data:**

- **Employee 1:** 3 years, Bachelor’s, Excellent
    
- **Employee 2:** 1 year, High school, Average
    
- **Employee 3:** 6 years, Master’s, Good
    

**Forward Chaining Solution:**

| Employee | Step                   | Calculation           | Result  |
| -------- | ---------------------- | --------------------- | ------- |
| **1**    | Apply Experience rule  | 3 yrs ⇒ $40,000       | $40,000 |
|          | Apply Education rule   | +$10,000 (Bachelor’s) | $50,000 |
|          | Apply Performance rule | +$5,000 (Excellent)   | $55,000 |
| **2**    | Apply Experience rule  | 1 yr ⇒ $30,000        | $30,000 |
|          | Apply Education rule   | +$5,000 (High school) | $35,000 |
|          | Apply Performance rule | +$0 (Average)         | $35,000 |
| **3**    | Apply Experience rule  | 6 yrs ⇒ $50,000       | $50,000 |
|          | Apply Education rule   | +$15,000 (Master’s)   | $65,000 |
|          | Apply Performance rule | +$3,000 (Good)        | $68,000 |

**Final Salaries:**

- Employee 1: **$55,000**
    
- Employee 2: **$35,000**
    
- Employee 3: **$68,000**
    

---

## Example 4: Smart Home Automation 

**Problem Definition:** Rules:

1. IF SunSet ⇒ LightsOn
    
2. IF MovementDetected ∧ DarkOutside ⇒ LightsOn
    

Facts:

- SunSet (✓)
    
- MovementDetected (✓)
    

**Forward Chaining Steps:**

1. **Applicable Rule:** Rule 1 (SunSet ⇒ LightsOn) ⇒ add **LightsOn**
    
2. Lights are now on; goal reached.
    

**Conclusion:** LightsOn is derived.

---

## Example 5: Medical Diagnosis 

**Problem Definition:** Rules:

1. IF Fever ∧ Cough ⇒ Flu
    
2. IF SoreThroat ∧ SwollenGlands ⇒ StrepThroat
    
3. IF RunnyNose ∧ Sneezing ⇒ Allergies
    

Facts:

- Fever (✓), Cough (✓)
    
- SoreThroat (✓)
    

**Forward Chaining Steps:**

1. **Rule 1** matches Fever ∧ Cough ⇒ add **Flu**
    
2. No rule for combining Flu with other facts; stop.
    

**Conclusion:** Patient might have **Flu**.

---

## Example 6: Email Filtering 

**Problem Definition:** Rules:

1. IF contains(“free”|“discount”|“promotion”) ⇒ Spam
    
2. IF UnknownSender ∧ SuspiciousAttachment ⇒ Spam
    

Facts:

- contains(“discount”) (✓)
    
- UnknownSender ∧ SuspiciousAttachment (✓)
    

**Forward Chaining Steps:**

1. **Rule 1** matches ⇒ add **Spam**
    
2. Spam already marked; Rule 2 also matches but no new fact.
    

**Conclusion:** Email is classified as **Spam**.