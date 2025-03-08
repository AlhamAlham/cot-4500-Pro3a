# cot-4500-Pro3a

## Overview
This project implements 2 numerical methods for solving ODE's
1. **Euler Method**
2. **Runge-Kutta Method**

Each algorithm follows the specifications given in Chapter 5 of the course material.
Test_assignment_3 runs the methods for several functions, while assignment_3 runs the functions given in the assignment.

## Repository Structure
cot-4500-Pro3a/
\│-- src/ \
│ │-- main/ \
│ │ │-- init.py \
│ │ │-- assignment_3.py \
│ │-- test/ \
│ │ │-- init.py \
│ │ │-- test_assignment_3.py \
│-- requirements.txt \
│-- README.md\


## Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/AlhamAlham/cot-4500-Pro3a
cd cot-4500-Pro3a
```
### **2. Install Dependencies**
This project requires Python and the necessary dependencies (only numpy), which are listed in the requirements.txt file. Install them if you haven't using pip:
```bash
pip install -r requirements.txt
```
### **3. Run the Code**
Once the dependencies are installed, you can run the main script:
```bash
python src/main/assignment_3.py
```
### **4. Running Tests**
To run the unit tests, use the following command:
```bash
python -m unittest discover src/test
```
