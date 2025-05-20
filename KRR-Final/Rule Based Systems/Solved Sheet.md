Rule-Based Reasoning Solutions

Example I: Salary Calculation (Forward Chaining)

Rules:

Years of Experience

<2 yrs: base = $30,000

2–5 yrs: base = $40,000



5 yrs: base = $50,000

Education Level

High school ⇒ +$5,000

Bachelor’s ⇒ +$10,000

Master’s+ ⇒ +$15,000

Performance Bonus

Excellent ⇒ +$5,000

Good ⇒ +$3,000

Average ⇒ +$0

Employee 1 (3 yrs, Bachelor’s, Excellent):

Base (3 yrs): $40,000

Education bonus: +$10,000 → $50,000

Performance: +$5,000 → $55,000

Employee 2 (1 yr, High school, Average):

Base (1 yr): $30,000

Education bonus: +$5,000 → $35,000

Performance: +$0 → $35,000

Employee 3 (6 yrs, Master’s, Good):

Base (6 yrs): $50,000

Education bonus: +$15,000 → $65,000

Performance: +$3,000 → $68,000

Example II: Smart Home Automation (Forward Chaining)

Facts:

Sun_set

Movement_detected

Dark_outside (derive from Sun_set)

Rules:

Sun_set ⇒ Turn_on_lights

Movement_detected ∧ Dark_outside ⇒ Turn_on_lights

Cycle

Working Memory

Applicable Rules

Fired

New Fact

1

Sun_set, Movement_detected

R1

R1

Turn_on_lights

—

Goal (lights_on) reached

—

—



(Rule 1 already triggers the action immediately.)

Example III: Medical Diagnosis (Forward Chaining)

Facts:

Fever ∧ Cough

Sore_throat

Rules:

Fever ∧ Cough ⇒ Flu

Sore_throat ∧ Swollen_glands ⇒ Strep_throat

Runny_nose ∧ Sneezing ⇒ Allergies

Cycle

Working Memory

Applicable Rules

Fired

New Fact

1

Fever, Cough, Sore_throat

R1

R1

Flu

2

Fever, Cough, Sore_throat, Flu

—

—

Stop

(Only R1 applies; Strep and Allergies remain untriggered.)

Example IV: Email Filtering (Forward Chaining)

Facts:

Contains(discount)

Unknown_sender ∧ Suspicious_attachment

Rules:

Contains(spam_keyword) ⇒ Spam

Unknown_sender ∧ Suspicious_attachment ⇒ Spam

Cycle

Working Memory

Applicable Rules

Fired

New Fact

1

Contains(discount), Unknown_sender, Suspicious_attachment

R1, R2

R1

Spam

—

Goal (Spam) reached

—

—



(Rule 1 already marks as spam.)

Example V: Fuel Pump Diagnosis (Backward Chaining)

Goal: Is Fuel_pump_faulty?

Facts:

Car_starts ∧ Stalls_frequently

Rules:

¬Car_starts ⇒ Check_battery

Car_starts ∧ Stalls_frequently ⇒ Check_fuel_pump

Strange_noises ⇒ Check_engine

Backward Steps:

Goal: Fuel_pump_faulty

Match conclusion: Rule 2 ⇒ need Car_starts ∧ Stalls_frequently

Both premises are in facts, so infer Check_fuel_pump ⇒ Fuel_pump_faulty

Example VI: Course Advice (Backward Chaining)

Goal: Should student take Calculus?

Facts:

Major = Mathematics

Rules:

Major = CS ⇒ Take(Intro_to_Programming)

Major = Biology ⇒ Take(Intro_to_Biology)

Major = Mathematics ⇒ Take(Calculus)

Backward Steps:

Goal: Take(Calculus)

Match conclusion: Rule 3 requires Major = Mathematics

Major = Mathematics is in facts ⇒ infer Take(Calculus)

