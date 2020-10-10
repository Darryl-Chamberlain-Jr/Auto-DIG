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
multiplyComplex = {
    "Code Name": "multiplyComplex",
    "Folder": "Core",
    "Subfolder": "01realComplex",
    "Topic": "Real and Complex Numbers",
    "Topic Number": "1",
    "Objective Number": "C.01.04",
    "Short Description": "Multiply two complex numbers.",
    "Long Description": "Given two complex numbers, multiply and reduce to the form a+bi.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
orderOfOperations = {
    "Code Name": "orderOfOperations",
    "Folder": "Core",
    "Subfolder": "01realComplex",
    "Topic": "Real and Complex Numbers",
    "Topic Number": "1",
    "Objective Number": "C.01.03",
    "Short Description": "Simplify the expression using the order of operations.",
    "Long Description": "Currently tests one of three different structures, which focuses on probing a linear view of PEMDAS or understanding M/D A/S are the same.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
subgroupComplex = {
    "Code Name": "subgroupComplex",
    "Folder": "Core",
    "Subfolder": "01realComplex",
    "Topic": "Real and Complex Numbers",
    "Topic Number": "1",
    "Objective Number": "C.01.02",
    "Short Description": "Identify the smallest subgroup an unsimplified number belongs to.",
    "Long Description": "Probes recognition of Complex subgroups based on superficial properties: presence of i, presence of sqrt, presence of fraction, etc.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
subgroupReal = {
    "Code Name": "subgroupReal",
    "Folder": "Core",
    "Subfolder": "01realComplex",
    "Topic": "Real and Complex Numbers",
    "Topic Number": "1",
    "Objective Number": "C.01.01",
    "Short Description": "Identify the smallest subgroup an unsimplified number belongs to.",
    "Long Description": "Probes recognition of Real subgroups based on superficial properties: presence of i, presence of sqrt, presence of fraction, etc.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 2 - Linear Functions
linearGraphToStandard = {
    "Code Name": "linearGraphToStandard",
    "Folder": "Core",
    "Subfolder": "02linear",
    "Topic": "Linear Functions",
    "Topic Number": "2",
    "Objective Number": "C.02.03",
    "Short Description": "Convert from graph to standard form.",
    "Long Description": "Provides a graph with two integer points identified and asks for the coefficients of the function in Standard Form.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
linearParOrPer = {
    "Code Name": "linearParOrPer",
    "Folder": "Core",
    "Subfolder": "02linear",
    "Topic": "Linear Functions",
    "Topic Number": "2",
    "Objective Number": "C.02.03",
    "Short Description": "Use a point and a description of another line to construct a line.",
    "Long Description": "Provides a line in Standard form, a relation (parallel or perpendicular) and a point for students to construct the associated function in slope-intercept form.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
linearTwoPoints = {
    "Code Name": "linearTwoPoints",
    "Folder": "Core",
    "Subfolder": "02linear",
    "Topic": "Linear Functions",
    "Topic Number": "2",
    "Objective Number": "C.02.01",
    "Short Description": "Use two points to construct a line.",
    "Long Description": "Provides two integer points and asks students to construct the corresponding linear function in slope-intercept form.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveIntegerLinear = {
    "Code Name": "solveIntegerLinear",
    "Folder": "Core",
    "Subfolder": "02linear",
    "Topic": "Linear Functions",
    "Topic Number": "2",
    "Objective Number": "C.02.04",
    "Short Description": "Solve a linear function with integer coefficients.",
    "Long Description": "Given the form a_1(b_1x+c_1) = a_2(b_2x+c_2), solve the linear function for x. There exists a single x that satisifes this equation.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveLinearRational = {
    "Code Name": "solveLinearRational",
    "Folder": "Core",
    "Subfolder": "02linear",
    "Topic": "Linear Functions",
    "Topic Number": "2",
    "Objective Number": "C.02.04",
    "Short Description": "Solve a linear function with rational coefficients.",
    "Long Description": "Given the form (a_1x+b_1)/c_1 - (a_2x+b_2)/c_2 = (a_3x+b_3)/c_3, solve the linear function for x. There exists a unique solution to the equation.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 3 - Linear Inequalities
describeSet = {
    "Code Name": "describeSet",
    "Folder": "Core",
    "Subfolder": "03inequality",
    "Topic": "Linear Inequalities",
    "Topic Number": "3",
    "Objective Number": "C.03.01",
    "Short Description": "Translate a description of numbers to interval notation.",
    "Long Description": "Given a description such as 'No more than [blank] from [blank]', identify the corresponding inteval notation.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveCompoundAND = {
    "Code Name": "solveCompoundAND",
    "Folder": "Core",
    "Subfolder": "03inequality",
    "Topic": "Linear Inequalities",
    "Topic Number": "3",
    "Objective Number": "C.03.03",
    "Short Description": "Solve an 'and' inequality.",
    "Long Description": "Given a linear inequality of the form a_1x+b_1 leq (a_2x+b_2)c/ < a_3x+b_3, solve for the interval of solutions. Solution set is a non-empty, proper subset of the real numbers.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveCompoundOR = {
    "Code Name": "solveCompoundOR",
    "Folder": "Core",
    "Subfolder": "03inequality",
    "Topic": "Linear Inequalities",
    "Topic Number": "3",
    "Objective Number": "C.03.03",
    "Short Description": "Solve an 'or' inequality.",
    "Long Description": "Given the inequalities a_1x + b_1 > c_1x or a_2x+b_2 < c_2x, solve for the interval of solutions. Solution set is a non-empty, proper subset of the real numbers.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveIntegerInequality = {
    "Code Name": "solveIntegerInequality",
    "Folder": "Core",
    "Subfolder": "03inequality",
    "Topic": "Linear Inequalities",
    "Topic Number": "3",
    "Objective Number": "C.03.03",
    "Short Description": "Solve a linear inequality with integer coefficients.",
    "Long Description": "Given the inequality a_1x+b_1 'less/leq/greater/geq' a_2x+b_2, solve for the interval of solutions. Solution set is a non-empty, proper subset of the real numbers.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveRationalInequality = {
    "Code Name": "solveRationalInequality",
    "Folder": "Core",
    "Subfolder": "03inequality",
    "Topic": "Linear Inequalities",
    "Topic Number": "3",
    "Objective Number": "C.03.03",
    "Short Description": "Solve a linear inequality with rational coefficients.",
    "Long Description": "Given the inequality (a_1/b_1)x + (a_2/b_2) 'less/leq/greater/geq' (a_3/b_3)x + (a_4/b_4), solve for the interval of solutions. Solution set is a non-empty, proper subset of the real numbers.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 4 - Quadratic Functions
factorLeadingOver1Composite = {
    "Code Name": "factorLeadingOver1Composite",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "04quadratic",
    "Topic": "Quadratic Functions",
    "Topic Number": "4",
    "Objective Number": "C.04.03",
    "Short Description": "Factor a quadratic with leading coefficients greater than 1.",
    "Long Description": "Factor a quadratic of the form ax^2+bx+c, where a is a composite with at least two primes.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
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
quadraticFormula = {
    "Code Name": "quadraticFormula",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "04quadratic",
    "Topic": "Quadratic Functions",
    "Topic Number": "4",
    "Objective Number": "C.04.04",
    "Short Description": "Solve a quadratic equation using the Quadratic Formula.",
    "Long Description": "Solve a quadratic equation that leads to exactly two irrational roots.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
quadraticGraphToEquation = {
    "Code Name": "quadraticGraphToEquation",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "04quadratic",
    "Topic": "Quadratic Functions",
    "Topic Number": "4",
    "Objective Number": "C.04.03",
    "Short Description": "Use a quadratic graph to construct its equation.",
    "Long Description": "Using the displayed graph of a quadratic and assuming a is either 1 or -1, construct the standard form quadratic function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveQuadraticFactorComposites = {
    "Code Name": "solveQuadraticFactorComposites",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "04quadratic",
    "Topic": "Quadratic Functions",
    "Topic Number": "4",
    "Objective Number": "C.04.04",
    "Short Description": "Solve a quadratic equation that can be factored.",
    "Long Description": "Solve a quadratic equation that leads to exactly two rational roots.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 5 - Radical Functions
domainRadical = {
    "Code Name": "domainRadical",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "05radical",
    "Topic": "Radical Functions",
    "Topic Number": "5",
    "Objective Number": "C.05.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Determine the domain of a radical function.",
    "Long Description": "Given a radical function of the form f(x) = a(h_0x-h_1)^(1/m)+k, determine its domain.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
radicalEquationToGraph = {
    "Code Name": "radicalEquationToGraph",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "05radical",
    "Topic": "Radical Functions",
    "Topic Number": "5",
    "Objective Number": "C.05.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use the equation of a radical function to identify its graph.",
    "Long Description": "Given a radical function of the form f(x) = a(x-h)^(1/m)+k, identify its graph.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
radicalGraphToEquation = {
    "Code Name": "radicalGraphToEquation",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "05radical",
    "Topic": "Radical Functions",
    "Topic Number": "5",
    "Objective Number": "C.05.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use the graph of a radical function to construct its equation.",
    "Long Description": "Given a graph of a radical function with integer inflection point*, identify the equation of the radical function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveRadicalLinear = {
    "Code Name": "solveRadicalLinear",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "05radical",
    "Topic": "Radical Functions",
    "Topic Number": "5",
    "Objective Number": "C.05.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a radical equation that leads to a linear equation.",
    "Long Description": "Solve a radical equation of the form sqrt(a_1x-b_1) - sqrt(a_2x-b_2) = 0. May lead to 0 or 1 real solutions.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveRadicalQuadratic = {
    "Code Name": "solveRadicalQuadratic",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "05radical",
    "Topic": "Radical Functions",
    "Topic Number": "5",
    "Objective Number": "C.05.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a radical equation that leads to a quadratic equation.",
    "Long Description": "Solve a radical equation of the form sqrt(a_1x^2+b_1) - sqrt(a_2x) = 0. May lead to 0, 1, or 2 real solutions.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 6 - Polynomial Functions
constructPolyComplex = {
    "Code Name": "constructPolyComplex",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "06polynomial",
    "Topic": "Polynomial Functions",
    "Topic Number": "6",
    "Objective Number": "C.06.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct the lowest-degree polynomial given at least one complex root.",
    "Long Description": "Assuming a is 1, construct a third-degree polynomial with one displayed complex root and one rational root.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructPolyRationals = {
    "Code Name": "constructPolyRationals",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "06polynomial",
    "Topic": "Polynomial Functions",
    "Topic Number": "6",
    "Objective Number": "C.06.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct the lowest-degree polynomial given at least one rational root.",
    "Long Description": "Assuming a is 1, construct a third-degree polynomial with rational roots.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
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
polyGraphToFunction = {
    "Code Name": "polyGraphToFunction",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "06polynomial",
    "Topic": "Polynomial Functions",
    "Topic Number": "6",
    "Objective Number": "C.06.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use a graph of a polynomial to identify its equation.",
    "Long Description": "Identify a possible equation of the polynomial using the end and zero behavior of the graphed polynomial.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
polyZeroBehavior = {
    "Code Name": "polyZeroBehavior",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "06polynomial",
    "Topic": "Polynomial Functions",
    "Topic Number": "6",
    "Objective Number": "C.06.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the zero behavior of a particular root for a polynomial.",
    "Long Description": "Given a polynomial of the form f(x) = a(x-z_1)^[even/odd](x+z_1)^[odd/even](x-z_2)^[even/odd](x+z_2)^[odd/even], identify the zero behavior of a given zero.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 7 - Rational Functions
domainRational = {
    "Code Name": "domainRational",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "07rational",
    "Topic": "Rational Functions",
    "Topic Number": "7",
    "Objective Number": "C.07.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the domain of a rational function.",
    "Long Description": "Given a rational function of the form f(x)= n/(ax^2+bx+c) where the denominator has two rational roots, determine the domain of the function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
rationalEquationToGraph = {
    "Code Name": "rationalEquationToGraph",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "07rational",
    "Topic": "Rational Functions",
    "Topic Number": "7",
    "Objective Number": "C.07.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use a rational equation to identify its graph.",
    "Long Description": "Given a rational function of the form f(x) = a/(x-h)^n + k, identify its corresponding graph.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
rationalGraphToEquation = {
    "Code Name": "rationalGraphToEquation",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "07rational",
    "Topic": "Rational Functions",
    "Topic Number": "7",
    "Objective Number": "C.07.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use a graph of a rational function to identify its equation.",
    "Long Description": "Given the graph of a rational function with a single vertial asymptote, identify the equation of the form f(x) = 1/(x-h)^n + k.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveRationalLinear = {
    "Code Name": "solveRationalLinear",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "07rational",
    "Topic": "Rational Functions",
    "Topic Number": "7",
    "Objective Number": "C.07.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a rational equation that leads to a linear equation.",
    "Long Description": "Solve a rational equation of the form (a/bx+c) - d = e/f(bx+c), solve for x. There can be 0 or 1 real solutions.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveRationalQuadratic = {
    "Code Name": "solveRationalQuadratic",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "07rational",
    "Topic": "Rational Functions",
    "Topic Number": "7",
    "Objective Number": "C.07.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a rational equation that leads to a quadratic equation.",
    "Long Description": "Solve the rational equation of the form (a*x)/(b*x+c) + (d*x**2)/(b*f*x**2 + (b*g+c*f)*x+c*g) = e/(f*x+g). This can lead to 0, 1, or 2 real solutions. 0 real solution case avoids 0 real but 2 complex solutions.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 8 - Logarithmic and Exponential Functions
domainRangeExp = {
    "Code Name": "domainRangeExp",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "08logExp",
    "Topic": "Logarithmic and Exponential Functions",
    "Topic Number": "8",
    "Objective Number": "C.08.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the domain or range of an exponential function.",
    "Long Description": "Given an exponential function of the form f(x) = a*e^{x-h}+k, identify its domain or range.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
domainRangeLog = {
    "Code Name": "domainRangeLog",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "08logExp",
    "Topic": "Logarithmic and Exponential Functions",
    "Topic Number": "8",
    "Objective Number": "C.08.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the domain or range of a logarithmic function.",
    "Long Description": "Given a logarithmic function of the form f(x) = a*log(x-h)+k, identify its domain or range.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveByConverting = {
    "Code Name": "solveByConverting",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "08logExp",
    "Topic": "Logarithmic and Exponential Functions",
    "Topic Number": "8",
    "Objective Number": "C.08.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a logarithmic equation by converting to exponential form.",
    "Long Description": "Given a logarithmic equation of the form log_b(a_0*x+a_1)+k = c, solve for x by converting to the form b^(c-k) = a_0x+a_1.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveByLogProperties = {
    "Code Name": "solveByLogProperties",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "08logExp",
    "Topic": "Logarithmic and Exponential Functions",
    "Topic Number": "8",
    "Objective Number": "C.08.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve a logarithmic equation by using log properties.",
    "Long Description": r"Given a logarithmic equation of the form a = ln(sqrt[rootDegree]{\frac{ numerator }{ e^{coefficient}x } } ) where root degree can be 2 or larger and the ln may or may not be there, use log properties to solve for x.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveExpDifferentBases = {
    "Code Name": "solveExpDifferentBases",
    "Folder": "Core", # Core, Limits, or Modeling
    "Subfolder": "08logExp",
    "Topic": "Logarithmic and Exponential Functions",
    "Topic Number": "8",
    "Objective Number": "C.08.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve an exponential equation with different bases.",
    "Long Description": "Given an exponential equation of the form b_1^(a_1x+c_1) = b_2^(a_2x+c_2) where gcd(b_1, b_2)=1, solve for x.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

### MODELING MODULES ###
# Module 9M - Modeling w/ Linear Functions
domainLinearModel = {
    "Code Name": "domainLinearModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "09modelingLinear",
    "Topic": "Modeling with Linear Functions",
    "Topic Number": "9M",
    "Objective Number": "M.09.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Determine the domain of the linear model.",
    "Long Description": "Given a word description of a real-world problem, determine the restricted domain of the model.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructLinearModelMixture = {
    "Code Name": "constructLinearModelMixture",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "09modelingLinear",
    "Topic": "Modeling with Linear Functions",
    "Topic Number": "9M",
    "Objective Number": "M.09.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a linear model for a mixture-type real-world problem.",
    "Long Description": "Mixture-type linear model that requires rational coefficients.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructLinearModelCostsProfitsRevenue = {
    "Code Name": "constructLinearModelCostsProfitsRevenue",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "09modelingLinear",
    "Topic": "Modeling with Linear Functions",
    "Topic Number": "9M",
    "Objective Number": "M.09.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a linear model for a costs-profits-revenue real-world problem.",
    "Long Description": "Costs-profits-revenue problem in the context of student costs in a semester.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructLinearModelDistanceAndRate = {
    "Code Name": "constructLinearModelDistanceAndRate",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "09modelingLinear",
    "Topic": "Modeling with Linear Functions",
    "Topic Number": "9M",
    "Objective Number": "M.09.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a linear model for a distance-rate-time real-world problem.",
    "Long Description": "Distance-rate-time problem in the context of a bike path with different speeds going up, flat, and down.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
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
constructIndirectModel = {
    "Code Name": "constructIndirectModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "10modelingPower",
    "Topic": "Modeling with Power Functions",
    "Topic Number": "10M",
    "Objective Number": "M.10.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct an indirect model for the real-world problem.",
    "Long Description": "Indirect model under the context of physics - rate of vibration of a string under constant tension.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructJointModel = {
    "Code Name": "constructJointModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "10modelingPower",
    "Topic": "Modeling with Power Functions",
    "Topic Number": "10M",
    "Objective Number": "M.10.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a joint model for the real-world problem.",
    "Long Description": "Using the given joint model for the volume of a cylinder, identify how increasing/reducing the radius and height would change the constant coefficient.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyModelPopulationPower = {
    "Code Name": "identifyModelPopulationPower",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "10modelingPower",
    "Topic": "Modeling with Power Functions",
    "Topic Number": "10M",
    "Objective Number": "M.10.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify whether the population can be modeled by a power equation.",
    "Long Description": "Given a table of population values, determine whether a power model is appropriate.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyModelVariation = {
    "Code Name": "identifyModelVariation",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "10modelingPower",
    "Topic": "Modeling with Power Functions",
    "Topic Number": "10M",
    "Objective Number": "M.10.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify whether the word description can be modeled by a power equation.",
    "Long Description": "Given a word description of either a direct, indirect, joint, or non-power model, determine the most appropriate model.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 11M - Modeling w/ Log and Exp Functions
constructBacteriaGrowth = {
    "Code Name": "constructBacteriaGrowth",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "11modelingLogExp",
    "Topic": "Modeling with Log and Exp Functions",
    "Topic Number": "11M",
    "Objective Number": "M.11.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a model for a bacteria growth real-world problem.",
    "Long Description": "Bacteria double, triple, or quadruple. Students given an initial amount and amount after some number of hours. Asks students to determine the replication rate in terms of minutes.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructHalfLifeModel = {
    "Code Name": "constructHalfLifeModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "11modelingLogExp",
    "Topic": "Modeling with Log and Exp Functions",
    "Topic Number": "11M",
    "Objective Number": "M.11.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct a model for a half-life real-world problem.",
    "Long Description": "Determine the half-life  of an element given an initial amount and amount after X years.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
constructTemperatureModel = {
    "Code Name": "constructTemperatureModel",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "11modelingLogExp",
    "Topic": "Modeling with Log and Exp Functions",
    "Topic Number": "11M",
    "Objective Number": "M.11.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Given an exponential model for temperature, determine all coefficients.",
    "Long Description": "Given the temperature equation T(t) = Ae^{kt} + T_s, initial values, and values after X amount of minutes, determine the constant k.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyModelGraph11 = {
    "Code Name": "identifyModelGraph11",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "11modelingLogExp",
    "Topic": "Modeling with Log and Exp Functions",
    "Topic Number": "11M",
    "Objective Number": "M.11.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the type of model best used for the graph provided.",
    "Long Description": "Given a collection of data points along a linear, power, log, exp, or random model, determine the correct model.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyModelPopulationLogExp = {
    "Code Name": "identifyModelPopulationLogExp",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "11modelingLogExp",
    "Topic": "Modeling with Log and Exp Functions",
    "Topic Number": "11M",
    "Objective Number": "M.11.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the type of model best used for the table provided.",
    "Long Description": "Given a table of population values, determine the appropriate model.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 12M - Solve Real-World Problems
constructModelMixed = {
    "Code Name": "constructModelMixed",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "12solvingWordProblems",
    "Topic": "Solving Real-World Word Problems with Modeling",
    "Topic Number": "12M",
    "Objective Number": "M.12.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Construct the linear, power, logarithmic, or exponential model needed for the situation.",
    "Long Description": "Randomly chooses a construct problem from linear, power, or log/exp modules.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyModelGraph12 = {
    "Code Name": "identifyModelGraph12",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "12solvingWordProblems",
    "Topic": "Solving Real-World Word Problems with Modeling",
    "Topic Number": "12M",
    "Objective Number": "M.12.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the type of model best used for the graph provided.",
    "Long Description": "Given a collection of data points along a linear, power, log, exp, or random model, determine the correct model.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveModelExp = {
    "Code Name": "solveModelExp",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "12solvingWordProblems",
    "Topic": "Solving Real-World Word Problems with Modeling",
    "Topic Number": "12M",
    "Objective Number": "M.12.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve the real-world problem using an exponential model.",
    "Long Description": "Solve the following problem: A new virus is spreading throughout the world. There were initially X many cases reported, but the number of confirmed cases has [doubled/tripled/quadrupled] every X days. How long will it be until there are at least X confirmed cases?",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveModelLinear = {
    "Code Name": "solveModelLinear",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "12solvingWordProblems",
    "Topic": "Solving Real-World Word Problems with Modeling",
    "Topic Number": "12M",
    "Objective Number": "M.12.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve the real-world problem using a linear model.",
    "Long Description": "Solve the following problem: In CHM2045L, Brittany created a X liter X percent solution of chemical chi using two different solution percentages of chemical chi. When she went to write her lab report, she realized she forgot to write the amount of each solution she used! If she remembers she used X percent and %d percent solutions, what was the amount she used of the X percent solution?",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
solveModelPower = {
    "Code Name": "solveModelPower",
    "Folder": "Modeling", # Core, Limits, or Modeling
    "Subfolder": "12solvingWordProblems",
    "Topic": "Solving Real-World Word Problems with Modeling",
    "Topic Number": "12M",
    "Objective Number": "M.12.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Solve the real-world problem using a power model.",
    "Long Description": "Solve the following problem: Pringles wants to add X percent more chips to their cylinder cans and minimize the design change of their cans. They've decided that the best way to minimize the design change is to increase the radius and height by the same percentage. What should this increase be?",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
### LIMITS MODULES ###
# Module 9L - Operating on Functions
determine1to1 = {
    "Code Name": "determine1to1",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "09operationsOnFunctions",
    "Topic": "Operating on Functions",
    "Topic Number": "9L",
    "Objective Number": "L.09.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Determine whether the equation is 1-1.",
    "Long Description": "Four types of functions: radical function, even polynomial with a single unique zero, odd polynomial with a single unique zero, and polynomial with more than one unique zero.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
domainAfterOperating = {
    "Code Name": "domainAfterOperating",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "09operationsOnFunctions",
    "Topic": "Operating on Functions",
    "Topic Number": "9L",
    "Objective Number": "L.09.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Determine the domain after operating on two functions.",
    "Long Description": "After adding, subtracting, or multiplying a rational, polynomial, or radical functions, determine the domains.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
findInverseLogOrExp = {
    "Code Name": "findInverseLogOrExp",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "09operationsOnFunctions",
    "Topic": "Operating on Functions",
    "Topic Number": "9L",
    "Objective Number": "L.09.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the inverse of a logarithmic or exponential function at a point.",
    "Long Description": "Given a logarithmic or exponential function, determine its inverse function and then evaluate that inverse function at a point.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
findInversePolyOrRadical = {
    "Code Name": "findInversePolyOrRadical",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "09operationsOnFunctions",
    "Topic": "Operating on Functions",
    "Topic Number": "9L",
    "Objective Number": "L.09.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the inverse of a polynomial or radical function at a point.",
    "Long Description": "Given a polynomial or radical function, determine whether the function has an inverse. If it does, evaluate the inverse at a point.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
functionComposition = {
    "Code Name": "functionComposition",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "09operationsOnFunctions",
    "Topic": "Operating on Functions",
    "Topic Number": "9L",
    "Objective Number": "L.09.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the composition of two functions at a point.",
    "Long Description": "Given two functions an a point to compose them at, evaluate the composition of the two functions at the point.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 10L - Synthetic Division
factorUsingSynthetic2Integers = {
    "Code Name": "factorUsingSynthetic2Integers",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "10syntheticDivision",
    "Topic": "Synthetic Division",
    "Topic Number": "10L",
    "Objective Number": "L.10.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Factor the polynomial using synthetic division with integer roots.",
    "Long Description": "Third degree polynomial with at least one integer root. Students can use synthetic division once then quadratic formula for the others.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
factorUsingSynthetic2Rationals = {
    "Code Name": "factorUsingSynthetic2Rationals",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "10syntheticDivision",
    "Topic": "Synthetic Division",
    "Topic Number": "10L",
    "Objective Number": "L.10.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Factor the polynomial using synthetic division with rational roots.",
    "Long Description": "Fourth degree polynomial where all zeros are between -5 and 5.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
possibleRoots = {
    "Code Name": "possibleRoots",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "10syntheticDivision",
    "Topic": "Synthetic Division",
    "Topic Number": "10L",
    "Objective Number": "L.10.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Determine the possible (rational or integer) roots of the polynomial.",
    "Long Description": "Testing on the Rational Root Theorem.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
syntheticDivision = {
    "Code Name": "syntheticDivision",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "10syntheticDivision",
    "Topic": "Synthetic Division",
    "Topic Number": "10L",
    "Objective Number": "L.10.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Synthetically divide the polynomial without missing terms.",
    "Long Description": "Divide fourth-degree polynomial with a linear function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
syntheticDivisionMissingTerms = {
    "Code Name": "syntheticDivisionMissingTerms",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "10syntheticDivision",
    "Topic": "Synthetic Division",
    "Topic Number": "10L",
    "Objective Number": "L.10.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Synthetically divide the polynomial with missing terms.",
    "Long Description": "Divide fourth-degree polynomial with a linear function.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# Module 11L - Introduction to Limits
evaluateLimitAnalyticalEasy = {
    "Code Name": "evaluateLimitAnalyticalEasy",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "11introToLimits",
    "Topic": "Introduction to Limits",
    "Topic Number": "11L",
    "Objective Number": "L.11.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the limit analytically, where the limit is a real number.",
    "Long Description": "Evaluate a one-sided limit that is easy to graph: f(x)= a(1/x-h)^n + k",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
evaluateLimitAnalyticalHard = {
    "Code Name": "evaluateLimitAnalyticalHard",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "11introToLimits",
    "Topic": "Introduction to Limits",
    "Topic Number": "11L",
    "Objective Number": "L.11.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the limit analytically, where the limit may not be defined on one side.",
    "Long Description": r"Evaluate the indeterminate limit: lim_{x rightarrow %d} frac{sqrt{%dx - %d} - %d}{%dx - %d}.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
evaluateLimitGraphically = {
    "Code Name": "evaluateLimitGraphically",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "11introToLimits",
    "Topic": "Introduction to Limits",
    "Topic Number": "11L",
    "Objective Number": "L.11.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the limit graphically.",
    "Long Description": "Given a graph of a function, determine the values that make the displayed limit true.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
interpretLimit = {
    "Code Name": "interpretLimit",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "11introToLimits",
    "Topic": "Introduction to Limits",
    "Topic Number": "11L",
    "Objective Number": "L.11.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Use the interpretation of the limit to choose the corresponding limit notation.",
    "Long Description": "Asks students to interpret the meaning of a limit.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
oneSidedLimits = {
    "Code Name": "oneSidedLimits",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "11introToLimits",
    "Topic": "Introduction to Limits",
    "Topic Number": "11L",
    "Objective Number": "L.11.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Evaluate the one-sided limit analytically or graphically.",
    "Long Description": "Provides a limit and asks what set of values should be used to evaluate the one-sided limit.",
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
identifyHAs = {
    "Code Name": "identifyHAs",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "12graphingRationalFunctions",
    "Topic": "Graphing Rational Functions with Limits",
    "Topic Number": "12L",
    "Objective Number": "L.12.03", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the horizontal asymptotes of a rational function, if any exist.",
    "Long Description": "May or may not include a horizontal asymptote.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyHoles = {
    "Code Name": "identifyHoles",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "12graphingRationalFunctions",
    "Topic": "Graphing Rational Functions with Limits",
    "Topic Number": "12L",
    "Objective Number": "L.12.01", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the holes of a rational function, if any exist.",
    "Long Description": "May or may not include a hole.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyOAs = {
    "Code Name": "identifyOAs",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "12graphingRationalFunctions",
    "Topic": "Graphing Rational Functions with Limits",
    "Topic Number": "12L",
    "Objective Number": "L.12.04", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the oblique asymptotes of a rational function, if any exist.",
    "Long Description": "May or may not include a oblique asymptote.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}
identifyVAs = {
    "Code Name": "identifyVAs",
    "Folder": "Limits", # Core, Limits, or Modeling
    "Subfolder": "12graphingRationalFunctions",
    "Topic": "Graphing Rational Functions with Limits",
    "Topic Number": "12L",
    "Objective Number": "L.12.02", # format: X.0X.0X, where the first entry is C for Core, M for Modeling, or L for Limits
    "Short Description": "Identify the vertical asymptotes of a rational function, if any exist.",
    "Long Description": "May or may not include a vertical asymptote.",
    "Notes": "Revised in 2020 to accommodate Auto-DIG v0.2.",
    "Author": "Darryl Chamberlain Jr.",
    "Date": "August 2020"
}

# LISTS OF QUESTIONS
masterQuestionList = [
    # Core questions
    divideComplex, multiplyComplex, orderOfOperations, subgroupComplex, subgroupReal, # M1
    linearGraphToStandard, linearParOrPer, linearTwoPoints, solveIntegerLinear, solveLinearRational, # M2
    describeSet, solveCompoundAND, solveCompoundOR, solveIntegerInequality, solveRationalInequality, # M3
    factorLeadingOver1Composite, quadraticEquationToGraph, quadraticFormula, quadraticGraphToEquation, solveQuadraticFactorComposites, # M4
    domainRadical, radicalEquationToGraph, radicalGraphToEquation, solveRadicalLinear, solveRadicalQuadratic, # M5
    constructPolyComplex, constructPolyRationals, polyEndBehavior, polyGraphToFunction, polyZeroBehavior, # M6
    domainRational, rationalEquationToGraph, rationalGraphToEquation, solveRationalLinear, solveRationalQuadratic, # M7
    domainRangeExp, domainRangeLog, solveByConverting, solveByLogProperties, solveExpDifferentBases, # M8
    # Modeling questions
    domainLinearModel, constructLinearModelMixture, constructLinearModelCostsProfitsRevenue,
    constructLinearModelDistanceAndRate, identifyModelPopulationLinear, # M9
    constructDirectModel, constructIndirectModel, constructJointModel, identifyModelPopulationPower, identifyModelVariation, # M10
    constructBacteriaGrowth, constructHalfLifeModel, constructTemperatureModel, identifyModelGraph11, identifyModelPopulationLogExp, # M11
    constructModelMixed, identifyModelGraph12, solveModelExp, solveModelLinear, solveModelPower, # M12
    # Limits questions
    determine1to1, domainAfterOperating, findInverseLogOrExp, findInversePolyOrRadical, functionComposition, # M9
    factorUsingSynthetic2Integers, factorUsingSynthetic2Rationals, possibleRoots, syntheticDivision, syntheticDivisionMissingTerms, # M10
    evaluateLimitAnalyticalEasy, evaluateLimitAnalyticalHard, evaluateLimitGraphically, interpretLimit, oneSidedLimits, # M11
    identifyGraphOfRationalFunction, identifyHAs, identifyHoles, identifyOAs, identifyVAs # M12
]
MAC1105ExamQuestions=[
# M1
subgroupReal, divideComplex, orderOfOperations,
# M2
linearTwoPoints, linearParOrPer, solveLinearRational,
# M3
solveIntegerInequality, solveRationalInequality, solveCompoundAND,
# M4
quadraticEquationToGraph, quadraticGraphToEquation, quadraticFormula,
# M5
domainRadical, radicalEquationToGraph, solveRadicalLinear,
# M6
polyGraphToFunction, polyZeroBehavior, constructPolyRationals,
# M7
solveRationalQuadratic, rationalGraphToEquation, solveRationalLinear,
# M8
domainRangeExp, domainRangeLog, solveExpDifferentBases
]
