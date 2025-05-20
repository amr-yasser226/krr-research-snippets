## Example 1: Diagnosing a Network Connection

**Knowledge Base**

1. **Rule 1:** If the router is working **and** DNS is resolving, then the Internet is reachable.
    
2. **Rule 2:** If the modem’s link light is on, then the router is working.
    
3. **Rule 3:** If the DNS server’s address is correctly configured, then DNS is resolving.
    

**Facts**

- The modem’s link light is on.
    
- The DNS server’s address is correctly configured.
    

**Goal**

- Prove: **Internet is reachable**
    

### Step-by-Step Backward Chaining

1. **Start with the Goal**: Internet is reachable.
    
2. **Find Matching Rule**: Rule 1 concludes “Internet is reachable.”
    
    - Sub-goals:  
        a. Router is working  
        b. DNS is resolving
        
3. **Solve Sub-goal “Router is working”**
    
    - Rule 2 concludes “Router is working.”
        
        - Sub-goal: Modem’s link light is on (true by fact).
            
    - Therefore, Router is working.
        
4. **Solve Sub-goal “DNS is resolving”**
    
    - Rule 3 concludes “DNS is resolving.”
        
        - Sub-goal: DNS server’s address is correctly configured (true by fact).
            
    - Therefore, DNS is resolving.
        
5. **Apply Rule 1**
    
    - Both sub-goals are satisfied ⇒ Internet is reachable.
        

**Conclusion**: By backward chaining, we infer that the Internet is reachable.

---

## Example 2: Deciding Whether to Bring an Umbrella

**Knowledge Base**

1. **Rule 1:** If the forecast predicts rain, then I will bring an umbrella.
    
2. **Rule 2:** If the sky is cloudy **and** the humidity is high, then the forecast predicts rain.
    
3. **Rule 3:** If the weather app shows humidity above 80%, then humidity is high.
    

**Facts**

- The sky is cloudy.
    
- The weather app shows humidity = 85%.
    

**Goal**

- Prove: **Bring an umbrella**
    

### Step-by-Step Backward Chaining

1. **Start with the Goal**: Bring an umbrella.
    
2. **Find Matching Rule**: Rule 1 concludes “Bring an umbrella.”
    
    - Sub-goal: Forecast predicts rain
        
3. **Solve Sub-goal “Forecast predicts rain”**
    
    - Rule 2 concludes this.
        
        - Sub-goals:  
            a. Sky is cloudy (true)  
            b. Humidity is high
            
4. **Solve Sub-goal “Humidity is high”**
    
    - Rule 3 concludes this.
        
        - Sub-goal: Weather app shows humidity > 80% (true by fact).
            
    - Therefore, humidity is high.
        
5. **Apply Rule 2**
    
    - Sky is cloudy and humidity is high ⇒ Forecast predicts rain.
        
6. **Apply Rule 1**
    
    - Forecast predicts rain ⇒ Bring an umbrella.
        

**Conclusion**: Backward chaining confirms that you should bring an umbrella.

---

## Example 3: Employee 2 Salary Calculation

**Knowledge Base**

1. **Rule: Years of Experience**
    
    - If experience < 2 years ⇒ base salary = $30,000
        
    - If 2 ≤ experience ≤ 5 years ⇒ base salary = $40,000
        
    - If experience > 5 years ⇒ base salary = $50,000
        
2. **Rule: Education Level**
    
    - High school diploma ⇒ +$5,000
        
    - Bachelor’s degree ⇒ +$10,000
        
    - Master’s degree or higher ⇒ +$15,000
        
3. **Rule: Performance Bonus**
    
    - Rating “excellent” ⇒ +$5,000
        
    - Rating “good” ⇒ +$3,000
        
    - Rating “average” ⇒ +$0
        

**Facts for Employee 2**

- Years of Experience = 1
    
- Education Level = High school diploma
    
- Performance Rating = Average
    

**Goal**  
Determine Employee 2’s final salary.

### Step-by-Step Backward Chaining

1. **Start with the Goal**: Final salary of Employee 2.
    
2. **Identify Base Salary** (Rule: Years of Experience)
    
    - Sub-goal: Match experience bracket.
        
    - Experience = 1 ⇒ < 2 years ⇒ base salary = $30,000.
        
3. **Apply Education Increase** (Rule: Education Level)
    
    - Sub-goal: Match education level.
        
    - High school diploma ⇒ increase = $5,000.
        
    - Salary after education = $30,000 + $5,000 = $35,000.
        
4. **Apply Performance Bonus** (Rule: Performance Bonus)
    
    - Sub-goal: Match performance rating.
        
    - Average ⇒ bonus = $0.
        
    - Final salary = $35,000 + $0 = $35,000.
        

**Conclusion**: Employee 2’s final salary is **$35,000**.

---

## Example 4: Employee 3 Salary Calculation

**Knowledge Base**

_(Same as Example 1 above)_

**Facts for Employee 3**

- Years of Experience = 6
    
- Education Level = Master’s degree
    
- Performance Rating = Good
    

**Goal**  
Determine Employee 3’s final salary.

### Step-by-Step Backward Chaining

1. **Start with the Goal**: Final salary of Employee 3.
    
2. **Identify Base Salary** (Rule: Years of Experience)
    
    - Experience = 6 ⇒ > 5 years ⇒ base salary = $50,000.
        
3. **Apply Education Increase** (Rule: Education Level)
    
    - Master’s degree ⇒ increase = $15,000.
        
    - Salary after education = $50,000 + $15,000 = $65,000.
        
4. **Apply Performance Bonus** (Rule: Performance Bonus)
    
    - Good ⇒ bonus = $3,000.
        
    - Final salary = $65,000 + $3,000 = $68,000.
        

**Conclusion**: Employee 3’s final salary is **$68,000**.

---

## Example 5: Car Engine Diagnosis (Backward Chaining)

**Problem Definition:** Rules:

1. IF Won’tStart ⇒ CheckBattery
    
2. IF Starts ∧ StallsFrequently ⇒ CheckFuelPump
    
3. IF StrangeNoises ⇒ CheckEngine
    

Fact:

- Starts ∧ StallsFrequently (✓)
    

**Backward Chaining Steps:**

1. **Goal:** CheckFuelPump
    
    - Rule 2 matches ⇒ sub‐goal: (Starts ∧ StallsFrequently)
        
2. Both facts are in working memory ⇒ CheckFuelPump proven.
    

**Conclusion:** Fuel pump should be checked.

---

## Example 6: Course Advising (Backward Chaining)

**Problem Definition:** Rules:

1. IF Major=CS ⇒ Take(IntroProgramming)
    
2. IF Major=Biology ⇒ Take(IntroBiology)
    
3. IF Major=Mathematics ⇒ Take(Calculus)
    

Fact:

- Major=Mathematics (✓)
    

**Backward Chaining Steps:**

1. **Goal:** Take(Calculus)
    
    - Rule 3 matches ⇒ sub‐goal: Major=Mathematics
        
2. Fact Major=Mathematics is present ⇒ Take(Calculus) proven.
    

**Conclusion:** Student should take **Calculus**.

---

## Example 7: Medical Expert System (Backward Chaining)

**Problem Definition:** Potential diagnoses: Hemochromatosis, Hepatitis C, Hepatitis B, Hepatitis A, Jaundice, Flu.

Symptom sets:

- Hemochromatosis: {StomachPain, JointPain, Weakness, DarkUrine, Jaundice}
    
- Hepatitis C: {JointPain, Fever, Fatigue, Vomiting, PaleStools}
    
- Hepatitis B: {PaleStools, DarkUrine, Jaundice}
    
- Hepatitis A: {FluSymptoms, Jaundice}
    
- Jaundice: {Jaundice}
    
- Flu: {FluSymptoms}
    

Facts: StomachPain, JointPain, Weakness, DarkUrine, Jaundice (✓ all)

**Backward Chaining Steps:**

1. **Goal:** Hemochromatosis?
    
    - Checks all five symptoms ⇒ all present ⇒ diagnosis: **Hemochromatosis**.
        
2. No need to test further diseases.
    

**Conclusion:** Patient has **Hemochromatosis**.

---

## Example 8: Plant Disease Diagnosis (Backward Chaining)

**Problem Definition:** Diseases & symptom patterns:

- BlackHeart: {HighTemp, NormalHumidity, ReddishBrownTuber, Spots}
    
- LateBlight: {LowTemp, HighHumidity, NormalTuber, Spots}
    
- DryRoot: {HighTemp, NormalHumidity, DryTuber, Circles}
    
- EarlyBlight: {NormalTemp, NormalHumidity, BrownTuber, Wrinkles}
    

Facts: HighTemp, NormalHumidity, ReddishBrownTuber, Spots (✓ all)

**Backward Chaining Steps:**

1. **Goal:** BlackHeart?
    
    - Symptoms match exactly ⇒ **BlackHeart**.
        
2. No further checks needed.
    

**Conclusion:** Plant is diagnosed with **Black Heart** disease.