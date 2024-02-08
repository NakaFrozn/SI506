# SI 506: Problem Set 04

## This Week's Problem Set

This week's problem set includes seven (7) problems that focus on loops and conditional statements.


## Background

The UMSI Career Fair happens each Fall and Winter term. You can find more information about employers
of interest through Handshake (https://umich.joinhandshake.com/).

For this problem set, you are provided with a list of data that includes basic information about the
employers who attended the Winter 2023 career fair, including names, locations, the total number of
employees, websites, and their industries, respectively. You are going to use `for` loops, `while`
loops, and conditional statements to complete the problems below.


## 1.0 Problem 01 (20 points)

**Task:** Use a `for` loop and the `range` type to populate a nested list.

1. Create an empty list named `employers`. Then, using a `for` loop with the `range()` type, access
   each string element in `data`. Use the appropriate `str` method and the appropriate delimiter value
   to split each string element into a list and add the new list to `employers` using the appropriate
   list method.

   :exclamation: The value assigned to `employers` _must_ match the list `employers_check` (see Setup
   Code). Uncomment the associated `assert` statement to confirm the variable matches the expected
   value.

2. Extract the first element from the `employers` list using list indexing and assign it to a variable
   named `headers`.

   :exclamation: The value assigned to `headers` _must_ match the list `headers_check` (see Setup
   Code). Uncomment the associated `assert` statement to confirm the variable matches the expected
   value.



## 2.0 Problem 02 (20 points)

**Task:** Implement the accumulator pattern using a `for` loop and conditional
statements to separate the employers into two groups. The `universities_innovation` list if it is
a university _and_ contains the term 'innovation' in its name; otherwise, add it to the
`other_companies` list.

1. Create an empty list and assign it to a variable named `universities_innovation`.

2. Create another empty list and assign it to a variable named `other_companies`.

3. Using a `for` loop, iterate over each element in the list `employers` excluding the headers row.
   Within the loop block, extract the first element in the `employers` list and assign a variable
   name of your choice to the new string. Utilize str method chaining (for case-insensitive comparison)
   with leading and trailing spaces removed. In the loop block, write an `if` statement that evaluates
   whether or not the new variable includes the words "university" _and_ "innovation". If the
   conditional statement evaluates to `True` add the employer list to the `universities_innovation`
   list. Otherwise, if the conditional statement evaluates to `False` add a second conditional
   statement that adds the employer list to the `other_companies` list.

   :exclamation: Since Python is a case-sensitive programming language, you may want to ensure at
   this step that you perform a **case-insensitive** comparison with the industry variable.

   :exclamation: Make sure that you extract the employer variable and perform str method chaining
   (for case-insensitive comparison) in a single line of code.

   :exclamation: The value assigned to `universities_innovation` list _must_ match the list
   `universities_innovation_check` (see Setup Code). Uncomment the associated `assert` statement to
   confirm the variable matches the expected value.

   :exclamation: The value assigned to `other_companies` list _must_ match the list
   `other_companies_check` (see Setup Code). Uncomment the associated `assert` statement to confirm
   the variable matches the expected value.



## 3.0 Problem 03 (20 points)

**Task:** Implement the accumulator pattern using a `for` loop and conditional statements in
order to "bin" the employers into different lists.

1. Assign an empty list to each of the following five (5) variables: `consulting`, `education`,
   `healthcare`, `software` and `other_industry`.

2. Using a standard `for` loop, iterate over each element in `other_companies`.

3. In the loop block, extract the industry information from each company and assign
   it to a variable named `industry`.

   :exclamation: Since Python is a case-sensitive programming language, you may want to ensure at
   this step that you perform a **case-insensitive** comparison with the industry variable.

   :exclamation: Note that the industry value may be spelled variously.

   :exclamation: Make sure that you extract the industry variable and perform str method chaining
   (for case-insensitive comparison) in a single line of code.

4. Next, check the value of the variable `industry`. If the value equals "consulting",
   "education", "healthcare" or "software", add _**only**_ the names of the associated companies to
   the corresponding lists you initialized earlier. Otherwise, add the names of the companies to
   the `other_industry` list.

   :exclamation: The five lists _must_ match their corresponding list variables provided in the
   Setup Code. Uncomment the associated `assert` statements to confirm the variables match the
   expected values.



## 4.0 Problem 04 (25 points)

**Task:** Using a `for` loop, conditional statements, and comparison operators such as `==`, `>` or
`<`, find the companies that have the largest number of employees _and_ are based in Michigan.

1. Create an empty list named `largest_michigan_companies`.

2. Create a variable named `max_num_employees` and assign it the value -1.

   :bulb: The value of this variable will be used as a reference while comparing the number of
   employees in `other_companies`.

3. Using a standard `for` loop, iterate over each element in `other_companies`.

   :exclamation: Do not use the `range()` type for this problem.

4. In the loop block, extract the _number of employees_ from each company within the `other_companies`
   list. Convert the _number of employees_ element to an integer and assign it to a variable named
   `num_employees`. Then assign the associated _location_ element of that company to a variable named
   `location`. Utilize str method chaining (for case-insensitive comparison) with leading and
   trailing spaces removed.

5. Next, implement a conditional statement to check if the company is located in Michigan. If
   `True`, compare the value of `num_employees` to the value of `max_num_employees`.

    1. If the (current) company's employee count is greater than `max_num_employees`, update the
       value of `max_num_employees` with the employee count of the (current) company. Then mutate
       the `largest_michigan_companies` list so that it includes only the (current) company's **name**.

       :exclamation: Make sure you clear/empty the `largest_michigan_companies` list before adding
       the (current) company's name using the appropriate list method.

    2. However, if the (current) company's employee count is **equal** to `max_num_employees`, simply
       add the (current) company's **name** to `largest_michigan_companies` using the appropriate list
       method.

       :exclamation: The value assigned to `largest_michigan_companies` list _must_ match the list
       `largest_michigan_companies_check` (see Setup Code). Uncomment the associated `assert`
       statement to confirm the variable matches the expected value.



## 5.0 Problem 05 (20 points)

**Task:** We have provided a multiline string named `salaries` (see Setup Code). Each line contains
a company name, a job title, and an average salary for the job. You will be asked to convert the
multiline string to a list and extract salary information in the following problems.

1. Utilize an appropriate string method to split the multiline string `salaries`
   into a list of strings, and assign it to a variable called `salary_list`.

2. Create a `for` loop using the `range()` type. Then access each element in `salary_list` using
   indexing.

   :exclamation: You must use a single argument within the `range()` type (_Hint_: use a built-in
   function).

3. In the loop block, split each string element into a list and assign the new nested
   list to `salary_list` in the same position as the string from which it was
   constructed.

   :exclamation: Make sure this step is executed with a single line of code.

   :exclamation: The value assigned to `salary_list` _must_ match the list `salary_list_check`
   (see Setup Code). Uncomment the associated `assert` statement to confirm the variable matches
   the expected value.



## 6.0 Problem 06 (25 points)

**Task:** In this problem, you will implement a `while` loop (a.k.a. an indefinite loop).

:exclamation: Beware of getting stuck in an infinite loop (mistakes do happen). If you need to exit
the infinite loop, type `CTRL + C` or `command + C` in the terminal.

1. Assign an empty list to a variable named `consult_manager_salary`.

2. Assign a sensible start value to a variable named `i`.

3. Utilize a `while` loop to iterate over the list `salary_list`.

   :bulb: Utilize `i` in your `while` statement.

4. In the `while` loop block, extract the _job title_ for each job, and  assign this value to a
variable named `job_title`. Utilize str method chaining (for case-insensitive comparison) with
leading and trailing spaces removed.
   Then, extract the _salary_ for each job, and assign it to a variable named `job_salary`. Next,
   implement a conditional statement that employs the appropriate membership operator to select jobs
   that are titled for either a **Consultant** or **Manager**. Inside the conditional statement,
   populate `consult_manager_salary` with the **salaries** for that job from `salary_list`.

   :bulb: Remember to increment the value of the variable `i` by one (1) in each iteration.

   :exclamation: Make sure to use the appropriate logical operator to ensure
   the salaries of _both_ consultants and managers are added to `consult_manager_salary`.

   :exclamation: Make sure to convert the salary value from type `str` to type `int` before adding
   it to `consult_manager_salary`.

   :exclamation: The value assigned to `consult_manager_salary` _must_ match the list
   `consult_manager_salary_check` (see Setup Code). Uncomment the associated `assert` statement to
   confirm the variable matches the expected value.

5. Write an expression that computes average salary for the salaries contained in
   `consult_manager_salary`. Assign this value to the variable `avg_consult_manager_salary`.
   Utilize two built-in functions to calculate the average salary in the `consult_manager_salary`
   list, then use another built-in function to _round_ the average salary to _two (2) decimal_
   places.

   :exclamation: The built-in `sum()` function _must_ be used to calculate the sum of all items in
   the `consult_manager_salary` list. The built-in `len()` function _must_ be used to calculate the
   number of items in the `consult_manager_salary` list. Another built-in function must be used to
   _round_ the average salary value.

   :exclamation: The variable assignment _must_ be written using a single line of code.



## 7.0 Problem 07 (20 points)

**Task:** You will implement a `while` loop with an `if` and `elif` statement and the `break`
statement to solve the following problem.

1. Assign a sensible start value to a variable named `i`.

2. Create an empty list and assign it to a variable named `company_salary_one`.

3. Utilize a `while` loop to iterate over `salary_list`.

4. In the loop, check each job's salary. If the salary is between one hundred thousand (100000) and
   one hundred and fifty thousand (150000), both inclusive, append the company name to a list named
   `company_salary_one`. If a job salary is over one hundred and seventy five thousand (175000),
   create a tuple with the first element being the company's name and second element being the
   salary, then assign the tuple to a variable named named `company_salary_two` and _**EXIT**_ the
   while loop completely. You _must_ increment the value of the variable `i` by one (1) in each
   iteration of the loop.

   :exclamation: The value assigned to `company_salary_one` _must_ match the list
   `company_salary_one_check` (see Setup Code). Uncomment the associated `assert` statement to
   confirm the variable matches the expected value.

   :exclamation: The value assigned to `company_salary_two` _must_ match the tuple
   `company_salary_two_check` (see Setup Code). Uncomment the associated `assert` statement to
   confirm the variable matches the expected value.