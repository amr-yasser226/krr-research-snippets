# krr-research-snippets

A curated collection of Python‑based Knowledge Representation & Reasoning (KRR) exercises, including an interactive Jupyter notebook and two standalone logic mini‑projects.

## Table of Contents
- [About](#about)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Lab 7 Notebook](#lab-7-notebook)
  - [Mini Projects](#mini-projects)
- [Author’s Expertise](#authors-expertise)
- [Concepts and Ideas](#concepts-and-ideas)
- [Contributing](#contributing)
- [License](#license)

## About
This repository showcases core AI techniques for modeling and automated reasoning, demonstrating how real‑world problems and classic puzzles can be encoded, solved, and explored in Python.

## Repository Structure
```
krr-research-snippets/
├── Labs/
│   └── lab 7.ipynb                # Jupyter notebook: employee salary calculation exercise
├── mini-projects/
│   ├── Mini Project 1.py          # Logic puzzle solver (truth-tellers & liars)
│   └── Mini_Project 2.py          # English ↔ predicate-logic translator
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## Prerequisites
- Python 3.7 or higher  
- (Optional) Jupyter Notebook for interactive execution  

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/amr-yasser226/krr-research-snippets.git
   cd krr-research-snippets
   ```  
2. (Optional) Install Jupyter:  
   ```bash
   pip install jupyter
   ```

## Usage

### Lab 7 Notebook
Launch the notebook to explore conditional business‑rule encoding and salary computations:
```bash
jupyter notebook Labs/lab\ 7.ipynb
```

### Mini Projects
- **Mini Project 1**: Solve classic “truth‑tellers vs. liars” puzzles by brute‑force enumeration  
  ```bash
  python "mini-projects/Mini Project 1.py"
  ```
- **Mini Project 2**: Translate simple English quantifier sentences to first‑order logic and back  
  ```bash
  python "mini-projects/Mini_Project 2.py"
  ```

## Author’s Expertise
- **Python Programming**: clear, idiomatic implementations  
- **Interactive Data Science**: Jupyter notebooks for narrative‑driven code  
- **Logic & Automated Reasoning**: puzzle solving via search and formal logic  

## Concepts and Ideas
- **Knowledge Representation & Reasoning**: structuring information so machines can infer and decide  
- **Automated Search**: exhaustive truth‑value enumeration for Knights & Knaves puzzles  
- **Predicate Logic Translation**: mapping between natural language and formal quantifier syntax  

## Contributing
Contributions, new snippets, and improvements are welcome! Please open an issue or submit a pull request.

## License
This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
```