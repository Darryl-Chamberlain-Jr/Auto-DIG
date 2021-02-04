# General Form
generalForm = {
    "Code Name": "",
    "Folder": "", # Core, Limits, or Modeling
    "Subfolder": "",
    "Topic": "",
    "Topic Number": "",
    "Objective Number": "", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "",
    "Long Description": "",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

## CORE MODULES ###
# Module 1 - Real and Complex Numbers
divideComplex = {
    "Code Name": "divideComplex",
    "Folder": "Core",
    "Subfolder": "01realComplex",
    "Topic": "Real and Complex Numbers",
    "Topic Number": "1",
    "Objective Number": "C.01.04",
    "Short Description": "Divide two complex numbers.",
    "Long Description": "Given two complex numbers written as a fraction, convert the complex number to the form a+bi.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 4 - Quadratic Functions
quadraticEquationToGraph = {
    "Code Name": "quadraticEquationToGraph",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "04quadratic",
    "Topic": "Quadratic Functions",
    "Topic Number": "4",
    "Objective Number": "C.04.02",
    "Short Description": "Use a quadratic function to identify its graph.",
    "Long Description": "Given a quadratic function in vertex form, identify the graph of the function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 6 - Polynomial Functions
polyEndBehavior = {
    "Code Name": "polyEndBehavior",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "06polynomial",
    "Topic": "Polynomial Functions",
    "Topic Number": "6",
    "Objective Number": "C.06.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the end behavior of the polynomial.",
    "Long Description": "Given a polynomial of the form f(x) = a(x-z_1)^[even/odd](x+z_1)^[odd/even](x-z_2)^[even/odd](x+z_2)^[odd/even], identify the end behavior.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

### MODELING MODULES ###
# Module 9M - Modeling w/ Linear Functions
identifyModelPopulationLinear = {
    "Code Name": "identifyModelPopulationLinear",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "09modelingLinear",
    "Topic": "Modeling with Linear Functions",
    "Topic Number": "9M",
    "Objective Number": "M.09.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify whether the population can be modeled by a linear equation.",
    "Long Description": "Given a table of population values, determine whether a linear model is appropriate.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 10M - Modeling w/ Power Functions
constructDirectModel = {
    "Code Name": "constructDirectModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "10modelingPower",
    "Topic": "Modeling with Power Functions",
    "Topic Number": "10M",
    "Objective Number": "M.10.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a direct model for the real-world problem.",
    "Long Description": "Direct model under the context of Kepler's Third Law.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 12L - Graphing Rational Functions with Limits
identifyGraphOfRationalFunction = {
    "Code Name": "identifyGraphOfRationalFunction",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "12graphingRationalFunctions",
    "Topic": "Graphing Rational Functions with Limits",
    "Topic Number": "12L",
    "Objective Number": "L.12.05", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the graph of a rational function in general form using asymptotes and/or roots.",
    "Long Description": "Given a graph of a rational function, use limits and asymptotes to determine the equation.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# LISTS OF QUESTIONS
masterQuestionList = [
    # Core questions
    divideComplex, quadraticEquationToGraph, polyEndBehavior, identifyModelPopulationLinear,
    constructDirectModel, identifyGraphOfRationalFunction
]
