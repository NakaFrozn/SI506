# SI 506 Week 09 Bonus Challenge

__Background__: For this exercise the code you write will group UNESCO Heritage Sites by region and
store the regional counts in a dictionary. The data is sourced from the file `data-sites.csv`.

__Tasks__: Complete the following tasks:

1. Implement the function `get_sites_by_key()`. The goal is to accumulate site counts grouped by a
   particular headers column name (e.g., `region_en`, `undp_code`). Review the function's docstring
   regarding its expected behavior, parameters, and return value.

   In the function block leverage the accumulation pattern to populate the dictionary. Employ a `for`
   loop that iterates over the passed in `sites` list, accumulating counts of UNESCO Heritage Sites
   grouped on the values associated with the passed in `key` (a column header string).

   :exclamation: Inside the loop block check for the absence of a key in `counts` before attempting
   to accumulate counts.

   Passing "region_en" as the `key` should result in a dictionary of regional site counts:

   ```python
   {
      "Africa": < count >,
      ...
      "Latin America and the Caribbean": < count >
   }
   ```

   Once the loop terminates return `counts` to the caller.

2. After implementing the function move the `main()` function. You will encounter two (`2`) variable
   assignments currently assigned `None`. Replace `None` with the appropriate function calls (i.e., `read_csv_to_dicts()`, `get_sites_by_key()`), passing the minimum number of arguments required by
   each.

   ```python
   ...

   sites = None

   region_counts = None

   ...
   ```

3. Uncomment the `region_counts_sorted` variable assignment. A new, re-ordered
   dictionary is created by passing the `region_counts` key-value pairs (items) along with an
   anonymous __lambda__ function to the built-in `sorted()` function which is then passed to the
   built-in `dict` function.

   ```python
   counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
   ```

   :bulb: The preferred approach is to employ a dictionary comprehension rather than the built-in
   `dict()` function to create a reordered dictionary because it's easier to read and the
   comprehension is more performant (it avoids the lookup costs associated with built-in functions).

4. When running your code, consider uncommenting the `print()` and `pp.pprint()` calls in
   order to check your work. Also uncomment the `assert` statements as needed to test the return
   values of your function calls.

   :exclamation: If either or both of the `assert` statements fail while you work on the challenge
   be sure to __comment out__ the `assert` statement(s) before submitting the bonus challenge to
   Gradescope in order to avoid triggering a runtime `AssertionError` (which results in a score of
   zero (`0`)).

5. Upload your code to Gradescope to earn bonus points. You can resubmit your solution
   as many times as needed until the submission period expires.

   :exclamation: The autograder assumes that you have formatted your code using VS Code's Black
   formatter extension and that you have set the maximum line length to 100 characters
   (default = 88). See the VS Code [install guides](https://si506.org/guides/) or the Slack
   `# general` channel.
