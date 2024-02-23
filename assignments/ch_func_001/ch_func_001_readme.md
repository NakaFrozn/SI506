# SI 506 Week 06 Bonus Challenge (20 points)

__Task__: Insert missing function calls in certain variable assignments, passing relevant arguments
as necessary to return the appropriate values.

__Function Behavior__:

   :bulb: The function `get_lowest_sugar_content()` is designed to iterate over a list of cereals
   and return a list of one or more cereals (__brand name only__) containing the __lowest__ sugar
   content. Inside the loop block the function delegates to other functions the task of retrieving
   cereal information in its quest to locate the cereal or cereals containing the lowest sugar
   content per serving size.

1. __Replace__: Inside `get_lowest_sugar_content()` loop block are four (4) variable
   assignments currently assigned `None`.

   ```python
   ...

   for cereal in cereals:
        brand = None
        serving_size_gm = None
        sugar_gm = None
        sugar_content = None

        ...
   ```

   Replace `None` with the appropriate function call in order to access or compute the following
   cereal information by calling either `calculate_sugar_content()` or `get_cereal_attribute()`:

   1. `brand` (`str`): brand name
   2. `serving_size_gm` (`int`): Serving size (grams)
   3. `sugar_gm` (`float`): Sugar content (grams)
   4. `sugar_content` (`float`): Sugar content per serving size (grams)

   __Restrictions__:

   :exclamation: Do not pass keyword arguments to either `calculate_sugar_content()` or
   `get_cereal_attribute()`. Pass arguments __by position only__.

2. __Replace__: After inserting the relevant function calls in `get_lowest_sugar_content()` proceed
   to the function named `main()`. Locate the following variable assignment:

   ```python
   min_sugar_cereals = None
   ```

   Replace `None` with a call to the function `get_lowest_sugar_content()`, passing to it the
   following arguments in __reverse order__ employing __keyword arguments__:

   __Parameters (by position)__

   * `cereals` (`list`): nested lists in `data` that represent cereals
   * `headers` (`list`): the nested list element in `data` that represents the column "headers".

   __Restrictions__:

   :exclamation: You _must_ employ __indexing__ and __slicing__ to access the lists that you need
   from `data` to pass to the function as arguments. Do so without assigning the element(s) accessed
   to variables.

   :exclamation: As noted above, do not pass arguments to `get_lowest_sugar_content()` by position.
   Pass arguments in __reverse order__ employing __keyword arguments__.

3. __Submit__: Upload your code to Gradescope to earn bonus points. You can resubmit your solution as
   many times as needed until the submission period expires.

   __Restrictions__:

   :exclamation: The auto grader assumes that you have formatted your code using VS Code's Black
   formatter extension and that you have set the maximum line length to 100 characters
   (default = 88). See the VS Code [install guides](https://si506.org/guides/) or the Slack
   `# general` channel.

   __Debugging__:

   :bulb: When running your code, consider uncommenting the `assert` statement and the built-in
   function `print()` call in order to check your work. If you trigger a runtime `AssertionError`
   use the debugger to check the function `get_lowest_sugar_content()` and the variable assignment
   changes you made per step 1. If you have yet to configure the debugger utilize `print()` to
   inspect the return values of the function calls that you added to `get_lowest_sugar_content()`.
