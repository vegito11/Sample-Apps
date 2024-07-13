## Basic Pytest Usage

### Basic Usage

1. **Run all tests in the current directory and subdirectories**:
   
   ```bash
   pytest

   # Run tests and show print statements (stdout)
   pytest -s
   ```

2. **Run tests in a specific file**:
   
   ```bash
   pytest path/to/test_file.py
   ```

3. **Run a specific test function**:
   
   ```bash
   pytest path/to/test_file.py::test_function_name
   ```

1. **Run tests matching a specific substring in their name**:

   ```bash
   pytest -k "substring"
   # Run tests that match a given expression
   pytest -k "expression"
   ```

1. **Run tests and stop on the first error or failure**:
   
   ```bash
   pytest -x

   # Run tests and stop after the first N failures
   pytest --maxfail=N
   ```

   --------------------

### Output Options

1. **Show detailed test execution summary**:
   
   ```bash
   pytest -v

   # Show only the summary of test results (quiet mode)
   pytest -q
   ```

1. **Generate JUnit XML report for CI integration**:
  
   ```bash
   pytest --junitxml=path/to/output.xml
   ```

1. **Run tests with coverage report**:
  
   ```bash
   pytest --cov=path/to/module_or_package
   ```

2. **Generate HTML coverage report**:
  
   ```bash
   pytest --cov=path/to/module_or_package --cov-report=html
   ```
   
   --------------------

### Running Tests in Parallel

1. **Run tests in parallel processes**:
   ```bash
   pytest -n auto
   ```

2. **Run tests in parallel on multiple cores (N cores)**:
   ```bash
   pytest -n N
   ```
   --------------------

### Running Tests with Custom Configuration

1. **Use a custom configuration file (pytest.ini)**:
   
   ```bash
   pytest -c path/to/pytest.ini
   ```

2. **Run tests with custom command-line options**:
   
   ```bash
   pytest --options=value
   ```

--------------------